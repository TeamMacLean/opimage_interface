#!/usr/bin/env python

import time
import json
import os
import sys
import picamera
import collections
import subprocess
def get_camera_settings():
    '''sets the camera up for consistent picture.
    Fixes Resolution 1280 x 1280
    Fixes ISO 200
    Fixes White Balance to best value according to internal camera algorithm
    Fixes Exposure to setting needed
    '''
    camera = picamera.PiCamera()
    camera.resolution = (1280, 1280)
    camera.iso = 200
    time.sleep(2) # wait for camera to settle
    # Now fix the values

    g = camera.awb_gains
    camsettings = {}
    camsettings['resolution'] = (1280,1280)
    camsettings['iso'] = 200
    camsettings['led'] = False
    camsettings['shutter_speed'] = camera.exposure_speed
    camsettings['exposure_mode'] = 'off'
    camsettings['awb_mode'] = 'off'
    camsettings['awb_gains'] = g

    camera.close()
    return camsettings

def get_plots(racks):
    rack_lengths = []
    for i in range(1, racks + 1):
        print "How many plots in rack {0} ?\n".format(i)
        rack_lengths.append(int(raw_input()))
    return rack_lengths

def ask_for_layout():
    racks = 9
    plots = 20
    rows = 6
    print "How many racks (default = 9, press enter for default...)\n"
    keypress = raw_input()
    if keypress:
        racks = int(keypress)
    print "How many plots in each rack (default = 20, press enter for default... this will put 20 plots in each rack. Otherwise type x and you will be asked to define plots on a per rack basis )\n"
    rack_plots = [20 for i in range(racks)]
    keypress = raw_input()
    if keypress:
        rack_plots = get_plots(racks)
    field = {}
    for i in range(1,racks + 1):
        field[i] = rack_plots[i - 1]
    return json.dumps(field)

def write_layout_file(layout_string):
    f = open('layout.json', 'w')
    f.write(layout_string)
    f.close
    return layout_string
    
def write_done_file(done_string):
    f = open('done.json', 'w')
    f.write(done_string)
    f.close
    return done_string

def test_ask_for_layout():
    print "Testing the layout function - will require user input... input 1 rack, 1 plot to test\n"
    json_data = ask_for_layout()
    assert json_data, '{"1":1}'  

def shoot(camsettings, filename):
    try:
	with picamera.PiCamera() as camera:
            camera.resolution = camsettings['resolution']
            camera.iso = camsettings['iso']
            #camera.led = camsettings['led']
            camera.shutter_speed = camsettings['shutter_speed']
            #camera.exposure_mode = camsettings['exposure_mode']
            camera.awb_mode = camsettings['awb_mode']
            camera.awb_gains = camsettings['awb_gains']
	    camera.start_preview()
            time.sleep(2)
            keypress = raw_input()
    	    camera.capture(os.path.join(sys.argv[1], filename))
            camera.close()
            return True
    except:
        return False
    

def step_through_plots(layout,camerasettings):
    done = None
    if os.path.exists('done.json'):
        print "Detected existing run -- continuing from where left off..\n\n"
        with open('done.json','r') as d:
	    s = d.readlines()    
            done = json.loads(s[0])
    else:
        done = collections.defaultdict(dict)
        for rack in sorted(layout):
            for plot in range(1, layout[rack] + 1):
                done[rack][str(plot)] = False
        write_done_file(json.dumps(done))
    for rack in sorted(layout):
        for plot in range(1, layout[rack] + 1):
            if done[rack][str(plot)] == False:
                filename = 'rack_0{0}_plot_0{1}.jpg'.format(rack,plot)
                print "Working on rack {0}, plot {1}:\n will use filename {2}\nHIT ENTER TO PREVIEW IMAGE\nHIT S to skip this plot\n".format(rack,plot,filename)
                keypress = raw_input()
                if not keypress:
                    shoot(camerasettings,filename)
                    done[rack][str(plot)] = filename
                    write_done_file(json.dumps(done))
            else:
                print "Skipping rack {0}, plot {1} - looks like it's done".format(rack,plot)

def main():
    ## get the working dir from the command line
    assert len(sys.argv) == 2, "You must provide a save folder on the command line when running this program"
    save_dir = sys.argv[1]
    assert os.path.isdir(save_dir), "Can't find save folder.. quitting in a panic\n"
    ## get the field layout from the user or the file
    layout = None
    if os.path.exists('layout.json'):
        print "Detected existing field layout file, using that\n"
        with open('layout.json', 'r') as d:
	    s = d.readlines()    
            layout = json.loads(s[0])
    else:
        layout = json.loads(write_layout_file(ask_for_layout()))
    camerasettings = get_camera_settings()
    step_through_plots(layout, camerasettings)

main()

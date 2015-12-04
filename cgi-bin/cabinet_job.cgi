#!/usr/bin/env python

import schedule
import os, sys
import datetime
import time
from opimage_things import cameras
from gpiozero import LED

'''Really simple cabinet control script

Runs a light bed turning it on and off fo the specified times. Does nothing if a file called '.lock_light' exists. 

Goes until the script is killed

'''

LOG_FILENAME = sys.argv[1]
DARK_INTERVAL_H = int(sys.argv[2])
DARK_INTERVAL_M = int(sys.argv[3])
LIGHT_INTERVAL_H = int(sys.argv[4])
LIGHT_INTERVAL_M = int(sys.argv[5])

def get_seconds(dh, dm, lh, lm):
    return [( (lh * 60.0) + lm) * 60, ( (dh * 60.0) + dm) * 60 ]

def append_to_logfile(fname, text):
    with open(fname, 'a') as f:
        text = "toggled_at: " + text + "\n"
        f.write(text)


times = get_seconds(DARK_INTERVAL_H, DARK_INTERVAL_M, LIGHT_INTERVAL_H, LIGHT_INTERVAL_M)
states = ['light', 'dark']
cabinet_led = LED(23)
cabinet_led.off()
start_time = time.time()
interval = times.pop(0)
state = states.pop(0) 
cabinet_led_was_on = False
while True:
    if os.path.isfile('.image_in_progress'):
	message = datetime.datetime.now().isoformat() + " detected image acquisition in progress"
	append_to_logfile(LOG_FILENAME, message)
	if cabinet_led.on:
                message = datetime.datetime.now().isoformat() + " detected cabinet led on, switching off"
	        append_to_logfile(LOG_FILENAME, message)
        	cabinet_led.off()
		cabinet_led_was_on = True
        time.sleep(3)
    else:
	if cabinet_led_was_on:
		cabinet_led.on()
                message = datetime.datetime.now().isoformat() + " restoring cabinet led to on"
	        append_to_logfile(LOG_FILENAME, message)
	if (time.time() - start_time) > interval:
            toggled_at = datetime.datetime.now().isoformat() + " changed to " + state
            append_to_logfile(LOG_FILENAME, toggled_at)
            times.append(interval)
            states.append(state)
            interval = times.pop(0)
            state = states.pop(0)
            cabinet_led.toggle()
            start_time = time.time()

#!/usr/bin/env python

import schedule
import os, sys
import datetime
import time
from opimage_things import cameras
from gpiozero import LED

'''Really simple cabinet control script

Runs a light bed turning it on and off fo the specified times.

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
    


times = get_seconds(DARK_INTERVAL_H, DARK_INTERVAL_M, LIGHT_INTERVAL_H, LIGHT_INTERVAL_M)

irled = LED(23)
while True:
    interval = times.pop(0)
    toggled_at = datetime.datetime.now().isoformat()
    append_to_logfile(LOG_FILENAME, toggled_at)
    times.append(interval)
    irled.toggle()
    time.sleep(interval)

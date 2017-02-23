#!/usr/bin/env python

import schedule
import os, sys
import datetime
import time
from opimage_things import snshat

'''Really simple job sensehat script

Runs a job every X minutes from start of the script.

Goes until the script is killed

'''

work_folder = sys.argv[1]
interval = int(sys.argv[2])
base = datetime.datetime.now().isoformat()
fname = os.path.join(work_folder, base + '_readings_.csv')
f = open(fname, "w")
heading = ",".join(["datetime", "humidity", "temp_h", "pressure", "temp_p" ])  + "\n"
f.write(heading)


def job(f):
    readings = snshat.get_readings()
    dt = datetime.datetime.now().isoformat()
    result = ",".join(readings.insert(0,dt)) + "\n"
    f.write(result)



schedule.every(interval).minutes.do( job(f) )
while True:
    schedule.run_pending()
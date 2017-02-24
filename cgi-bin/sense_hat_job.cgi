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
f.close()


def job(file = None):
    readings = [str(r) for r in snshat.get_readings() ]
    dt = datetime.datetime.now().isoformat()
    readings.insert(0,dt)
    result = ",".join(readings) + "\n"
    file = open(file, "a")
    file.write(result)
    file.close()



schedule.every(interval).minutes.do( job, file=fname )
while True:
    schedule.run_pending()
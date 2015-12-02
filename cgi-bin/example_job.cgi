#!/usr/bin/env python

import schedule

'''Really simple job scheduler

Runs a job every X minutes from start of the script.

Goes until the script is killed

'''

def job():
    print "did summat"
    print "more done"

schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()

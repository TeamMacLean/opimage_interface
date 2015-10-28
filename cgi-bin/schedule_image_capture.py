#!/usr/bin/env python

import schedule
import os,sys
from opimage import utils

'''Really simple job scheduler

Runs a job every 20 minutes from start of the script.

Goes until the script is killed

'''


def add_pid_to_joblist(pid, short_name):
    job_info = {'pid' : pid, 'short_name' : short_name, "status" : 'running'}
    jobs = utils.load_from_json('jobs_list.json')
    jobs.append(job_info)
    utils.write_to_json(jobs, 'jobs_list.json')

add_pid_to_joblist(os.getpid(), sys.argv[1])


def job():
    print "did summat"
    print "more done"

schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()

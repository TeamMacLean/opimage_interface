#!/usr/bin/env python


import os,sys
from opimage import utils

def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

jobs = utils.load_from_json('job_list.json')

updated_job_status = []

for j in jobs:
    if check_pid(j['pid']):
        j['status'] = 'live'
    else:
        j['status'] = 'dead'
    updated_job_status.append(j)

utils.write_to_json(updated_job_status, 'job_list.json')

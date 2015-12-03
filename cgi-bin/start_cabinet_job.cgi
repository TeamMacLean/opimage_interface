#!/usr/bin/env python

import os
from opimage import utils
import cgi, cgitb
import subprocess
import datetime


def start_orphan_process(work_folder, dark_interval_hours, dark_interval_m, light_interval_h, light_interval_m):
    '''starts cabinet_job.cgi

    returns integer: pid of cabinet_job.cgi'''

    process = subprocess.Popen(['cgi-bin/cabinet_job.cgi', dark_interval_hours, dark_interval_minutes, light_interval_hours, light_interval_minutes ] shell=False)
    return process.pid

def add_pid_to_joblist(pid, short_name):
    job_info = {'pid' : pid, 'short_name' : short_name, "status" : 'live', "type" : 'cabinet', "start_time" : datetime.datetime.now().isoformat() }
    jobs = utils.load_from_json('job_list.json')
    jobs.append(job_info)
    utils.write_to_json(jobs, 'job_list.json')

def make_cabinet_job_logfile(short_name, dark_interval_hours, dark_interval_m, light_interval_h, light_interval_m):
    log_filename = datetime.datetime.now().isoformat() + '_' + short_name + '.log'
    header = "\t".join(["dark_interval_hours", str(dark_interval_hours)]) +
    "\t".join(["dark_interval_minutes", str(dark_interval_minutes)]) +
    "\t".join(["light_interval_hours", str(light_interval_hours)]) +
    "\t".join(["light_interval_minutes", str(dark_interval_minutes)])
    with open(log_filename, "w") as lfname:
        lfname.write(header)
    
    return log_filename

cgitb.enable()

form = cgi.FieldStorage()
#print form

dark_interval_hours = int(form.getvalue("dark_interval_hours"))
dark_interval_minutes = int(form.getvalue("dark_interval_minutes"))
light_interval_hours = int(form.getvalue("light_interval_hours"))
light_interval_minutes = int(form.getvalue("light_interval_minutes"))
short_name = form.getvalue("short_name").replace(" ", "_")
log_filename = make_cabinet_job_logfile(short_name, dark_interval_hours, dark_interval_m, light_interval_h, light_interval_m)
pid = start_orphan_process()
add_pid_to_joblist(pid, short_name, )

print "Content-Type: text/html"
print
print "<html>"
print "<head>"
print   '<meta http-equiv="refresh" content="0;url=../index.html" />'
print    '<title>You are going to be redirected</title>'
print  '</head>'
print '<body> '
print    'Redirecting...'
print '  </body> '
print '</html>'

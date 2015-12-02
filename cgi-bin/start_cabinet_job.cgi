#!/usr/bin/env python

import os
from opimage import utils
import cgi, cgitb
import subprocess
import datetime


def start_orphan_process():
    '''starts job.cgi

    returns integer: pid of job.cgi'''

    process = subprocess.Popen('cgi-bin/job.cgi', shell=False)
    return process.pid

def make_work_folder(short_name):
    folder_name = datetime.datetime.now().isoformat() + '_' + short_name
    try:
        os.mkdir(folder_name)
    except OSError:
        folder_name = make_work_folder(short_name)
    return folder_name

def add_pid_to_joblist(pid, short_name, work_folder):
    job_info = {'pid' : pid, 'short_name' : short_name, "status" : 'live', "type" : 'cabinet', "start_time" : datetime.datetime.now().isoformat(), 'work_folder' : work_folder }
    jobs = utils.load_from_json('job_list.json')
    jobs.append(job_info)
    utils.write_to_json(jobs, 'job_list.json')

cgitb.enable()

form = cgi.FieldStorage()
#print form

dark_interval_hours = int(form.getvalue("dark_interval_hours"))
dark_interval_minutes = int(form.getvalue("dark_interval_minutes"))
light_interval_hours = int(form.getvalue("light_interval_hours"))
light_interval_minutes = int(form.getvalue("light_interval_minutes"))
short_name = form.getvalue("short_name").replace(" ", "_")
work_folder = make_work_folder(short_name)
pid = start_orphan_process()
add_pid_to_joblist(pid, short_name, work_folder)

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

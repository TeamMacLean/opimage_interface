#!/usr/bin/env python
import os,sys, signal
from opimage import utils
import cgi, cgitb


cgitb.enable()
form = cgi.FieldStorage()
pid = int(form.getfirst("pid"))

jobs = utils.load_from_json('job_list.json')
for j in jobs:
    if j['pid'] == pid:
      os.kill(pid, signal.SIGTERM)


print "Content-Type: text/html"
print
print "<html>"
print "<head>"
print   '<meta http-equiv="refresh" content="0;url=http://localhost:8000/index.html" />'
print pid
print    '<title>You are going to be redirected</title>'
print  '</head>'
print '<body> '
print    'Redirecting...'
print '  </body> '
print '</html>'

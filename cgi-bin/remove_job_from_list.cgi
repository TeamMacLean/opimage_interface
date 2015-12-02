#!/usr/bin/env python
import os,sys, signal
from opimage import utils
import cgi, cgitb


cgitb.enable()
form = cgi.FieldStorage()
pid = int(form.getfirst("pid"))


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def die_cowardly(pid):
  print "Content-Type: text/html"
  print
  print "<html>"
  print "<head>"
  print    '<title>oops...</title>'
  print  '</head>'
  print  '<body>'
  print  '  <div class="container">'
  print '         <div class="header clearfix">'
  print '           <h3 class="text-muted">Open Pi Image</h3>'
  print '         </div>'
  print '       <div class="col-lg-12"><h3> oops..</h3><p>Looks like that job is still going. Cowardly refusing to remove it from the list</p><a href="/index.html">Click to go to the index</a> </div>'
  print '      </div> <!-- /container -->'
  print '    <!-- jQuery (necessary for Bootstraps JavaScript plugins) -->'
  print '    <script src="js/jquery-1.11.3.min.js"></script>'
  print '    <script src="js/bootstrap.min.js"></script>'
  print '  </body>'
  print '</html>'

safe_to_remove = False
jobs = utils.load_from_json('job_list.json')
updated_job_list = []
for j in jobs:
    if j['pid'] == pid and not check_pid(pid):
        safe_to_remove = True
    else:
      updated_job_list.append(j)

utils.write_to_json(updated_job_list, 'job_list.json')

if not safe_to_remove:
  die_cowardly(pid)
else:
  print "Content-Type: text/html"
  print
  print "<html>"
  print "<head>"
  print   '<meta http-equiv="refresh" content="0;url=../index.html" />'
  print pid
  print    '<title>You are going to be redirected</title>'
  print  '</head>'
  print '<body> '
  print    'Redirecting...'
  print '  </body> '
  print '</html>'

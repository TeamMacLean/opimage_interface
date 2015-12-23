#!/usr/bin/env python
import os,sys, signal
import cgi, cgitb
from opimage import utils
cgitb.enable()

form = cgi.FieldStorage()
folder = form.getfirst("path")
print folder
layout = utils.load_from_json(os.path.join(folder, 'layout.json'))
done = utils.load_from_json(os.path.join(folder, 'done.json'))


racks = sorted(layout.keys())


print "Content-Type: text/html"
print
print "<html>"
print "<head>"
print    '<title>You are going to be redirected</title>'
print  '</head>'
print '<body> '
print    racks
print '  </body> '
print '</html>'

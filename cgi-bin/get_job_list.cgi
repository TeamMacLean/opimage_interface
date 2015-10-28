#!/usr/bin/env python

import  cgi
import json

print("Content-Type: text/json\n\n")

with open('job_list.json',"r") as f:
    print f.read()

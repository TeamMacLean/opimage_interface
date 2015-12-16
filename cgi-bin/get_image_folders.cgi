#!/usr/bin/env python

import  cgi
import json

print("Content-Type: text/json\n\n")

with open('image_folders.json',"r") as f:
    print f.read()

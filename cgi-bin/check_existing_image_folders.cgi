#!/usr/bin/env python


import os
from opimage import utils

def check_folder(folder):
    """ Check For the existence of a folder. """
    if os.path.isdir(folder):
        return True
    else:
        return False

image_folders = utils.load_from_json('image_folders.json')

updated_image_status = []

for f in image_folders:
    if check_folder(f['path']):
        f['status'] = 'found'
    else:
        f['status'] = 'not_found'
    updated_image_status.append(f)

utils.write_to_json(updated_image_status, 'image_folders.json')

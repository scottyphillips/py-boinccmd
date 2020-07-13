#!/usr/bin/env python3
import pyboinccmd as pbc
import re


regex_title = r'========\s\w*\s?\w*?\s========'
regex_numeric = r'\d\)\s-----------'
boinccmd = {}
category = 'default'
data = pbc.getState()
for line in data:
#    print lines
    if re.match(regex_title , line) is not None:
        category = line.replace('========','').strip().replace(' ','_')
        boinccmd[category] = []
        continue
    boinccmd[category].append(line)
if "Projects" in boinccmd:
    data = boinccmd["projects"]
    dict = {}
    dict_id = None
    for line in data:
        # if you find a project number create a new dict object
        if re.match(regex_numeric , line) is not None:
            dict_id = line.replace(') -----------','')
        print(dict_id)

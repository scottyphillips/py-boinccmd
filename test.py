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
    data = boinccmd["Projects"]
    dict = {}
    dict_id = None
    gui_id = 0
    for line in data:
        # if you find a project number create a new dict object
        if re.match(regex_numeric , line) is not None:
            dict_id = line.replace(') -----------','')
            dict[dict_id] = {}
            continue
        tuple = line.strip().split(':', 1)
        # print(tuple)
        # need a GUI flag so we can handle it properly
        if len(tuple) == 2:
          if re.match(r'GUI URL',tuple[0]) is not None:
              gui_id++
          if "name" in tuple[0]:
              print("NAME!!!")
          dict[dict_id][tuple[0]] = tuple[1]
    print(dict)

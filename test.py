#!/usr/bin/env python3
import pyboinccmd as pbc
import re
import json


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

        if len(tuple) == 2:
          # identify if GUI URL is matched and do something about it...
          if re.match(r'GUI URL',tuple[0]) is not None:
              if gui_id == 0:
                  dict[dict_id]['gui'] = {}
              gui_id+=1
              dict[dict_id]['gui'][gui_id] = {}
              continue
          test_values = ["name", "description", "URL"]
          if any(n in tuple[0] for n in test_values) and gui_id > 0:
              dict[dict_id]['gui'][gui_id][tuple[0].replace(' ','_'),lower()] = tuple[1].strip()
          else:
              dict[dict_id][tuple[0].replace(' ','_').replace('\'', '').lower()] = tuple[1].strip()
    print(json.dumps(dict))

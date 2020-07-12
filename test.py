#!/usr/bin/env python3
import pyboinccmd as pbc
import re


regex = r'========\s\w*\s?\w*?\s========'

boinccmd = None
category = 'default'
data = pbc.getState()
for line in data:
#    print lines
    if re.match(regex, line) is not None:
        category = line.replace('========','').strip().replace(' ','_')
        boinccmd[category] = []
        continue
    boinccmd[category].append(line)
print boinccmd

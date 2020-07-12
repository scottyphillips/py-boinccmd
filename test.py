#!/usr/bin/env python3
import pyboinccmd as pbc
import re


regex = r'========\s\w*\s========'
data = pbc.getState()
for line in data:
#    print lines
    if re.match(regex, line) is not None:
        print line

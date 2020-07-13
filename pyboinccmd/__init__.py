import subprocess
import re
import json

regex_title = r'========\s\w*\s?\w*?\s========'
regex_numeric = r'\d\)\s-----------'
boinccmd = {}
category = 'default'

def crunchData(array):
    data = array
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
              dict[dict_id]['gui'][gui_id][tuple[0].replace(' ','_').lower()] = tuple[1].strip()
          else:
              dict[dict_id][tuple[0].replace(' ','_').replace('\'','').lower()] = tuple[1].strip()
    return dict

"""
getState is equivalent to running 'boinccmd --get_state'
for now will wrap the 'boinccmd' executable but will eventually reverse
engineer the RPC to the BOINC client

return: an dict containing the properties of the node.
"""
def getState(ip_address="127.0.0.1", password=None):
    raw = subprocess.check_output(["boinccmd","--host","192.168.1.222","--passwd","password","--get_state"]).decode('utf-8')
    data = raw.splitlines()
    for line in data:
    #    print lines
        if re.match(regex_title , line) is not None:
            category = line.replace('========','').strip().replace(' ','_')
            boinccmd[category] = []
            continue
        boinccmd[category].append(line)
    for category in boinccmd.keys():
        crunch = boinccmd[category]
        print(crunch)
        boinccmd[category] = crunchData(crunch)
    return boinccmd

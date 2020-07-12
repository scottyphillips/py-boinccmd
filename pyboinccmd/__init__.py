import subprocess

"""
getState is equivalent to running 'boinccmd --get_state'
for now will wrap the 'boinccmd' executable but will eventually reverse
engineer the RPC to the BOINC client

return: an dict containing the properties of the node.
"""
def getState(ip_address="127.0.0.1", password=None):
    subprocess.run(["boinccmd","--host","192.168.1.222","--password","password","--get_state"])

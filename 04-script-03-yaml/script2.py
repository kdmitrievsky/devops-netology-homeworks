#!/usr/bin/env python3

import socket
import time
import json
import yaml
import os

servers = {'drive.google.com':'0.0.0.0','mail.google.com':'0.0.0.0','google.com':'0.0.0.0'}
cwd = os.getcwd()

print('**************  START SCRIPT ****************')
print(servers)

for i in range(10):
    for host in servers:
        ip_address = socket.gethostbyname(host)
        if ip_address == servers[host]:
            print(host +' '+ servers[host])
        else:
            print('[ERROR] ' + host + ' IP mismatch: ' + servers[host] + ' ' + ip_address)
            servers[host] = ip_address
        # json
        with open(cwd + '/' + host + ".json", 'w') as jsf:
            json_data = json.dumps({host: servers[host]})
            jsf.write(json_data)
        # yaml
        with open(cwd + '/' + host + ".yaml", 'w') as ymf:
            yaml_data = yaml.dump([{host: servers[host]}])
            ymf.write(yaml_data)
    time.sleep(5)

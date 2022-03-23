#!/usr/bin/env python3

import socket
import time


servers = {'drive.google.com':'0.0.0.0','mail.google.com':'0.0.0.0','google.com':'0.0.0.0'}

print('**************  START SCRIPT ****************')
print(servers)

while 1==1:
    for host in servers:
        ip_address = socket.gethostbyname(host)
        if ip_address == servers[host]:
            print(host +' '+ servers[host])
        else:
            print('[ERROR] ' + host + ' IP mismatch: ' + servers[host] + ' ' + ip_address)
            servers[host] = ip_address
    time.sleep(5)

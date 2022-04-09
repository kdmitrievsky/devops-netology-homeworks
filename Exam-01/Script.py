#!/usr/bin/env python3

import os
import json
import datetime

print('******* ' + datetime.datetime.today().strftime("%d-%m-%Y %H.%M.%S") + ' *******\n')

# Check the Environment
cert_string = "vault write -format=json pki/issue/example-dot-com common_name=\"test.example.com\" ttl=\"720h\""

if os.popen("echo $VAULT_ADDR").read():  # Test VAULT settings
    cert_data = json.loads(os.popen(cert_string).read())  # Get new certs
    with open("/etc/nginx/test.example.com.fullchain.pem", 'w') as cert_file:
        cert_pem = cert_data['data']['certificate']+'\n'+cert_data['data']['issuing_ca']
        cert_file.write(cert_pem)  # Save new certs to file
    with open("/etc/nginx/test.example.com.key.pem", 'w') as key_file:
        key_pem = cert_data['data']['private_key']
        key_file.write(key_pem)  # Save new priv key
    if os.popen("nginx -t").read().find('test is successful'):  # Test nginx config
        os.popen("systemctl restart nginx")  # Restart nginx
        print('Certificate was changed!')
    else:
        print("Configuration test failed!!!\n")
else:
    print("Environment variables NOT set!\n")

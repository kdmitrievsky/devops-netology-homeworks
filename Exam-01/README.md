## Exam

```
vagrant@vagrant:~$ sudo ufw allow ssh
Rules updated
Rules updated (v6)
vagrant@vagrant:~$ sudo ufw allow https
Rules updated
Rules updated (v6)
vagrant@vagrant:~$ sudo ufw allow from any to 127.0.0.1
Rule added
vagrant@vagrant:~$

```
vagrant@vagrant:~$ sudo ufw allow ssh
Rules updated
Rules updated (v6)
vagrant@vagrant:~$ sudo ufw allow https
Rules updated
Rules updated (v6)
vagrant@vagrant:~$  

```
vagrant@vagrant:~$ sudo nano /etc/apt/sources.list.d/nginx.list
vagrant@vagrant:~$ wget http://nginx.org/keys/nginx_signing.key
--2022-04-05 08:28:47--  http://nginx.org/keys/nginx_signing.key
Resolving nginx.org (nginx.org)... 3.125.197.172, 52.58.199.22, 2a05:d014:edb:5702::6, ...
Connecting to nginx.org (nginx.org)|3.125.197.172|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1561 (1.5K) [application/octet-stream]
Saving to: ‘nginx_signing.key’

nginx_signing.key                                           100%[========================================================================================================================================>]   1.52K  --.-KB/s    in 0s

2022-04-05 08:28:48 (76.7 MB/s) - ‘nginx_signing.key’ saved [1561/1561]

vagrant@vagrant:~$ sudo apt-key add nginx_signing.key
OK
vagrant@vagrant:~$

vagrant@vagrant:~$ sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring

```
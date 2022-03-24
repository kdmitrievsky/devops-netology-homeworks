## 4.3 Языки разметки JSON и YAML  

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:  
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
Нужно найти и исправить все ошибки, которые допускает наш сервис  
Ответ:  
a. отсутствует запятая м/у элеметами в 6-й строке  
b. не хватает кавычек в 9-й строке
```
  { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : "7175" 
            }, 
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```  
2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.  
Ответ (script2.py):  
```
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

```  
Вывод скрипта:  
```
/usr/bin/python3.9 /home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-03-yaml/script2.py
**************  START SCRIPT ****************
{'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
[ERROR] drive.google.com IP mismatch: 0.0.0.0 74.125.131.194
[ERROR] mail.google.com IP mismatch: 0.0.0.0 108.177.14.19
[ERROR] google.com IP mismatch: 0.0.0.0 64.233.165.139
drive.google.com 74.125.131.194
mail.google.com 108.177.14.19
google.com 64.233.165.139
drive.google.com 74.125.131.194
mail.google.com 108.177.14.19
google.com 64.233.165.139
drive.google.com 74.125.131.194
mail.google.com 108.177.14.19
google.com 64.233.165.139
drive.google.com 74.125.131.194
[ERROR] mail.google.com IP mismatch: 108.177.14.19 74.125.205.17
[ERROR] google.com IP mismatch: 64.233.165.139 64.233.165.100
drive.google.com 74.125.131.194
mail.google.com 74.125.205.17
google.com 64.233.165.100
drive.google.com 74.125.131.194
mail.google.com 74.125.205.17
google.com 64.233.165.100
drive.google.com 74.125.131.194
mail.google.com 74.125.205.17
google.com 64.233.165.100
drive.google.com 74.125.131.194
mail.google.com 74.125.205.17
google.com 64.233.165.100
drive.google.com 74.125.131.194
mail.google.com 74.125.205.17
google.com 64.233.165.100
...
```
JSON-файлы:  
drive.google.com.json  
```
{"drive.google.com": "74.125.131.194"}
```
google.com.json  
```
{"google.com": "64.233.165.100"}
```
mail.google.com.json  
```
{"mail.google.com": "74.125.205.17"}
```

YAML-файлы:  
drive.google.com.yaml  
```
- drive.google.com: 74.125.131.194
```
google.com.yaml  
```
- google.com: 64.233.165.100
```
mail.google.com.yaml  
```
- mail.google.com: 74.125.205.17
```  


## 4.2 Использование Python в DevOps  

1. Есть скрипт:
```
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```  

Вопросы:

Какое значение будет присвоено переменной c?    **Будет ошибка несоответствия типов**  
Как получить для переменной c значение 12?      **c=str(a)+b**  
Как получить для переменной c значение 3?       **c=a+int(b)**  

2. Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?  
```
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```  
Ответ (script2.py):  
```
#!/usr/bin/env python3

import os

cmd_line = "~/PycharmProjects/devops-netology-homeworks" # Путь к репозиторию
bash_command = ["cd "+cmd_line, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False # Лишняя переменная
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(cmd_line+prepare_result)
#        break # Убираем выход после первого совпадения
```  
Вывод скрипта:  
```
/usr/bin/python3.9 /home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-py/script2.py
~/PycharmProjects/devops-netology-homeworks04-script-02-py/README.md
~/PycharmProjects/devops-netology-homeworks04-script-02-py/script2.py
~/PycharmProjects/devops-netology-homeworks04-script-02-yaml/README.md

Process finished with exit code 0
```  

3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.  
Ответ (script3.py):
```
#!/usr/bin/env python3

import os
import sys
if sys.argv[1]:
    cmd_line = sys.argv[1] #Путь из командной строки
else:
    cmd_line = "~/PycharmProjects/devops-netology-homeworks" # Путь к репозиторию
bash_command = ["cd "+cmd_line, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(cmd_line+prepare_result)
```  
Вывод скрипта:  
```
[kdmitrievsky@Irinka 04-script-02-py]$ ./script3.py ~/PycharmProjects/devops-netology-homeworks/
/home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-py/README.md
/home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-py/script2.py
/home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-py/script3.py
/home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-yaml/README.md
[kdmitrievsky@Irinka 04-script-02-py]$ 
```  
4. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.  
Ответ (script4.py):  
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
/usr/bin/python3.9 /home/kdmitrievsky/PycharmProjects/devops-netology-homeworks/04-script-02-py/script4.py
**************  START SCRIPT ****************
{'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
[ERROR] drive.google.com IP mismatch: 0.0.0.0 142.250.150.194
[ERROR] mail.google.com IP mismatch: 0.0.0.0 173.194.221.83
[ERROR] google.com IP mismatch: 0.0.0.0 173.194.73.139
drive.google.com 142.250.150.194
mail.google.com 173.194.221.83
google.com 173.194.73.139
drive.google.com 142.250.150.194
mail.google.com 173.194.221.83
google.com 173.194.73.139
...
```
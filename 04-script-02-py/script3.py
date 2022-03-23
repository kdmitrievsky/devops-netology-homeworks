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

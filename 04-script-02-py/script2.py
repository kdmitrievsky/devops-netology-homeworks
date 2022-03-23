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
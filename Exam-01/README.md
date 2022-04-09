## Exam 01

1. Создать виртуальную машину Linux
Vagrantfile:
```
Vagrant.configure("2") do |config|
 	config.vm.box = "bento/ubuntu-20.04"
	config.vm.network "forwarded_port", guest: 443, host: 443 # Для проверки сервера с host-машины
 end
```

2. Настройка ufw:

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
3. Установка Vault:  
Здесь сложнее т.к. бусурмане банят адреса России и Белоруссии  

Берём любой БЕСПЛАТНЫЙ VPN-сервис. Мне попался ProtonVPN  
Скачиваем ovpn-файл  
Ставим openvpn и resolvconf  
Открываем окно терминала. Вводим: ``sudo openvpn /vagrant/jp-free-01.protonvpn.net.udp.ovpn``  
Получаем тунель и ставим Vault по указанной [инструкции](https://learn.hashicorp.com/tutorials/vault/getting-started-install?in=vault/getting-started#install-vault) (качаем, ставим ключик репозитория; подключаем репозиторий; ставим ПО) как, типа, мы японцы  
Прерываем процесс в открытом окне терминала и тунель пропадает.  
Итог:  
```
vagrant@vagrant:~$ vault
Usage: vault <command> [args]

Common commands:
    read        Read data and retrieves secrets
    write       Write data, configuration, and secrets
    delete      Delete secrets and configuration
    list        List data or secrets
    login       Authenticate locally
    agent       Start a Vault agent
    server      Start a Vault server
    status      Print seal and HA status
    unwrap      Unwrap a wrapped secret

Other commands:
    audit                Interact with audit devices
    auth                 Interact with auth methods
    debug                Runs the debug command
    kv                   Interact with Vault's Key-Value storage
    lease                Interact with leases
    monitor              Stream log messages from a Vault server
    namespace            Interact with namespaces
    operator             Perform operator-specific tasks
    path-help            Retrieve API help for paths
    plugin               Interact with Vault plugins and catalog
    policy               Interact with policies
    print                Prints runtime configurations
    secrets              Interact with secrets engines
    ssh                  Initiate an SSH session
    token                Interact with tokens
    version-history      Prints the version history of the target Vault server
vagrant@vagrant:~$
```  
4. Создаем центр сертификации по [инструкции](https://learn.hashicorp.com/tutorials/vault/pki-engine?in=vault/secrets-management)  

В отдельном окне терминала запускаем Vault сервер  
Определяем переменные среды VAULT_ADDR и VAULT_TOKEN (я их закинул в /etc/environment)  
Включаем механизм (``vault secrets enable pki``), настраиваем (``vault secrets tune-max-lease-ttl=87600h pki``)  
Создаем корневой сертификат (``vault write -field=certificate pki/root/generate/internal common_name="example.com" ttl=87600h > ca_cert.crt``)  
Настраиваем адреса URL (``vault write pki/config/urls issuing_certificates="$VAULT_ADDR/v1/pki/ca" crl_distribution_points="$VAULT_ADDR/v1/pki/crl"``)  
Создаем роль для сертификатов нашего сайта с максимальным ttl=месяц (``vault write pki/roles/example-dot-com allowed_domains=example.com allow_subdomains=true max_ttl=720h``)  
Создаем сертификат для сайта (``vault write pki/issue/example-dot-com common_name=test.example.com``)  
Достаем из возвращенных данных fullchain сертификат и private key в формате pem

5. Устанавливаем корневой сертификат  ca_cert.crt на host систему в корневые доверенные:

    [Результат](https://disk.yandex.ru/i/sLJFYEupHtqRNg)  (дополнительно подправил /etc/hosts чтоб DNS ресолвил test.example.com)

6. В каждом дистрибутиве есть свои пакеты с nginx, но мы будем ставить  по [инструкции](https://nginx.org/ru/linux_packages.html) от авторов, раздел Ubuntu  
Устанавливаем необходимые пакеты: ``vagrant@vagrant:~$ sudo apt install curl gnupg2 ca-certificates lsb-release ubuntu-keyring``  
Импортируем официальный ключ: ``curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null``  
Проверяем ключ  
Подключаем стабильный репозиторий:   
```
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
| sudo tee /etc/apt/sources.list.d/nginx.list
```
Закрепляем, чтоб пакеты брались из него:  
```
echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
```
Ну и ставим:  
```
sudo apt update
sudo apt install nginx
```
7. Настройка nginx по [инструкции](https://nginx.org/en/docs/http/configuring_https_servers.html):   
Копируем сертификат и ключ в /etc/nginx  
Создаем test.example.com.conf в /etc/ngunx/conf.d  
Закидываем туда:  
```
server {
    listen       443 ssl;
    server_name  test.examle.com;

    access_log  /var/log/nginx/test.access.log  main;

    ssl_certificate     test.example.com.fullchain.pem;
    ssl_certificate_key test.example.com.key.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;

    location / {
        root   /usr/share/nginx/test/html; # Copy here standart index page!!!
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

}
```  
Копируем в /usr/share/nginx/test/html стандартную страницу nginx  
Тестируем конфигурацию: ``vagrant@vagrant:~$ sudo nginx -t``  
Запускаем nginx: ``vagrant@vagrant:~$ sudo systemctl start nginx``  
8. Наслаждаемся:  [Ссылка](https://disk.yandex.ru/i/FtPsJy7fpspRAg)  
9. Делаем скрипт cert_script :  
```
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
    else:
        print("Configuration test failed!!!\n")
else:
    print("Environment variables NOT set!\n")
```
10. Сделал через crontab root-a: ``sudo crontab -e``  
Заполняем. Получаем: ``sudo crontab -l``  
```
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
52 6 9 * * /home/vagrant/cert_script >/home/vagrant/nginx_cert.log
```  
Ждем. Проверяем:  
```
vagrant@vagrant:~$ cat ./nginx_cert.log
******* 09-04-2022 06.52.01 *******
vagrant@vagrant:~$ grep CRON /var/log/syslog
Apr  9 04:45:11 vagrant cron[785]: (CRON) INFO (pidfile fd = 3)
Apr  9 04:45:12 vagrant cron[785]: (CRON) INFO (Running @reboot jobs)
Apr  9 06:52:01 vagrant CRON[1808]: (root) CMD (/home/vagrant/cert_script >/home/vagrant/nginx_cert.log)
Apr  9 06:52:01 vagrant CRON[1807]: (CRON) info (No MTA installed, discarding output)
```
Смотрим страницу заново: [Ссылка](https://disk.yandex.ru/i/mWB4VcCcIHOkVQ)
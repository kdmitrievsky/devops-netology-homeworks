## 3.6. Компьютерные сети, лекция 1  
1. С ответом сервера был получен HTTP-код 301 Moved Permanently (перемещено навсегда). Он означает, что рессурс перемещён и доступен по адресу, указанному в параметре location (location: https://stackoverflow.com/questions).  
Втекущей ситуации сайт принудительно переводит нас на протокол HTTPS.  
```  
vagrant@vagrant:~$ telnet stackoverflow.com 80
Trying 151.101.193.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: f928fcd2-3ba0-4275-9583-fa6fd3318827
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Tue, 08 Feb 2022 19:37:21 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-fra19134-FRA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1644349041.244814,VS0,VE85
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=92c8be71-3590-f33a-af2c-1f0a1e0d93f1; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.
vagrant@vagrant:~$
```  

2. С ответом сервера был получен HTTP-код 307 Temporary Redirect (временно перемещено) [Скриншот](https://disk.yandex.ru/i/UTTlw7FkAztnXg)  
Дольше всего обрабатывался запрос GET / (352ms)  
[Скриншот консоли браузера](https://disk.yandex.ru/i/JgA9_47fHCAr7g)


3. Адрес в Интернет: [178.168.193.128](https://disk.yandex.ru/i/Wt66uYJESXLvyw)  


4. Провайдер: Ростелеком    
Автономная система: 25106  
Владелец адресного пространства 178.168.192.0/20 МТС Беларусь !!!!!  
```
vagrant@vagrant:~$ whois -h whois.ripe.net 178.168.193.128
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

% Note: this output has been filtered.
%       To receive output for a database update, use the "-B" flag.

% Information related to '178.168.192.0 - 178.168.255.255'

% Abuse contact for '178.168.192.0 - 178.168.255.255' is 'abuse@mts.by'

inetnum:        178.168.192.0 - 178.168.255.255
netname:        MTSBY
descr:          Mobile TeleSystems JLLC
remarks:        INFRA-AW
country:        BY
admin-c:        MTJA2-RIPE
tech-c:         MTJA2-RIPE
status:         ASSIGNED PA
mnt-by:         MTSBY-MNT
created:        2010-04-26T15:53:57Z
last-modified:  2018-02-16T11:16:11Z
source:         RIPE

role:           Mobile TeleSystems JLLC admin
address:        Belarus, Minsk, Nezavisimosti ave, 95
admin-c:        IS6999-RIPE
admin-c:        AT14522-RIPE
admin-c:        VA34055-RIPE
tech-c:         NP2078-RIPE
nic-hdl:        MTJA2-RIPE
mnt-by:         MTSBY-MNT
created:        2018-02-16T06:48:11Z
last-modified:  2021-07-01T07:02:29Z
source:         RIPE # Filtered

% Information related to '178.168.192.0/20AS25106'

route:          178.168.192.0/20
origin:         AS25106
mnt-by:         MTSBY-MNT
created:        2020-10-23T11:28:41Z
last-modified:  2020-10-23T11:28:41Z
source:         RIPE

% This query was served by the RIPE Database Query Service version 1.102.2 (BLAARKOP)
```
  
5. qqq  
6. 

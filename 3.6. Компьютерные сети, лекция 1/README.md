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
  
5. Traceroute до 8.8.8.8:  
```  
vagrant@vagrant:~$ vagrant@vagrant:~$ sudo traceroute -IAn 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.2.2 [*]  0.557 ms  0.334 ms  0.326 ms
 2  192.168.1.1 [*]  3.466 ms  3.089 ms  2.693 ms
 3  192.168.100.1 [*]  3.085 ms  2.710 ms  3.032 ms
 4  212.48.195.81 [AS12389]  10.871 ms  10.120 ms  9.719 ms
 5  212.48.195.146 [AS12389]  12.210 ms  11.483 ms  11.678 ms
 6  188.254.2.4 [AS12389]  31.866 ms  32.812 ms  32.518 ms
 7  87.226.194.47 [AS12389]  32.522 ms  31.832 ms  32.316 ms
 8  74.125.244.132 [AS15169]  32.954 ms  32.219 ms  31.086 ms
 9  216.239.48.163 [AS15169]  35.929 ms  37.735 ms  36.993 ms
10  216.239.58.53 [AS15169]  42.478 ms  43.916 ms  43.895 ms
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  8.8.8.8 [AS15169]  40.608 ms  38.822 ms  40.257 ms
```

6. Утилита mtr:  
```  
                                                 My traceroute  [v0.93]
vagrant (10.0.2.15)                                                                                                                                                                                                 2022-02-28T14:18:48+0000
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                                                                                                                                                    Packets               Pings
 Host                                                                         Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. AS???    10.0.2.2                                                         0.0%    33    2.2   1.6   1.0   2.4   0.3
 2. AS???    192.168.1.1                                                      0.0%    33    2.8   4.3   2.8   7.5   0.7
 3. AS???    192.168.100.1                                                    0.0%    33    4.3   4.7   3.9   6.5   0.5
 4. AS12389  212.48.195.81                                                    0.0%    33    9.1   8.4   5.7  32.6   5.0
 5. AS12389  212.48.195.146                                                   0.0%    33   12.6  14.3  12.3  20.4   2.4
 6. AS12389  188.254.2.4                                                      0.0%    33   40.4  34.7  32.4  41.3   2.4
 7. AS12389  87.226.194.47                                                    0.0%    33   32.8  33.2  32.4  38.0   1.2
 8. AS15169  74.125.244.132                                                   0.0%    33   33.6  33.5  32.1  39.4   1.3
 9. AS15169  216.239.48.163                                                   0.0%    33   37.7  42.6  36.2 104.9  13.5
10. AS15169  216.239.58.53                                                    0.0%    33   43.2  42.7  41.5  45.0   0.8
11. (waiting for reply)
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. (waiting for reply)
19. (waiting for reply)
20. AS15169  8.8.8.8                                                          21.9%    32   41.0  41.2  40.1  46.9   1.3

```
Наибольшая задержка на 9 этапе:  
` 9. AS15169  216.239.48.163                                                   0.0%    33   37.7  42.6  36.2 104.9  13.5`  

7. `vagrant@vagrant:~$ dig @8.8.8.8 dns.google`  
```
; <<>> DiG 9.16.1-Ubuntu <<>> @8.8.8.8 dns.google
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27714
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;dns.google.                    IN      A

;; ANSWER SECTION:
dns.google.             693     IN      A       8.8.4.4
dns.google.             693     IN      A       8.8.8.8

;; Query time: 44 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Feb 28 15:57:43 UTC 2022
;; MSG SIZE  rcvd: 71
```  

8. `vagrant@vagrant:~$ dig -x 8.8.8.8`  

```
; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 30731
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;8.8.8.8.in-addr.arpa.          IN      PTR

;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.   8142    IN      PTR     dns.google.

;; Query time: 40 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Mon Feb 28 16:08:11 UTC 2022
;; MSG SIZE  rcvd: 73
```  

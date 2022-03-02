## 3.7. Компьютерные сети, лекция 2  

1. В Windows команда: `ipconfig /all`  
В Linux команда: `ip -a link`  
```  
vagrant@vagrant:~$ ip -a link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:73:60:cf brd ff:ff:ff:ff:ff:ff
```  
2. Протокол LLDP (Link Local Discovery Protocol) в пакете **lldpd**  
Команды: lldpcli и lldpctl  
3. VLAN – Virtual Local Area Network. Пакет в Linux - vlan  
Команды:  
```
vagrant@vagrant:~$ sudo ip link add link eth0 name eth0.100 type vlan id 100  
vagrant@vagrant:~$ sudo ip addr add 192.168.1.200/24 brd 192.168.1.255 dev eth0.10
vagrant@vagrant:~$ sudo ip link set dev eth0.10 up  
```  
либо через **vconfig**:  
```  
vagrant@vagrant:~$ sudo vconfig add eth0 200  
```  

Пример конфига:  
```  
## vlan с ID-100 для интерфейса eth0 ##
auto eth0.100
iface eth0.100 inet static
address 192.168.1.200
netmask 255.255.255.0
vlan-raw-device eth0  
```  
4. Есть Etherchannel(проприетарный Cisco) и LACP (802.3ad). В Linux используется модуль **bonding**  
Режимы:  
**mode=0 (balance-rr)**
Последовательно кидает пакеты, с первого по последний интерфейс.  
**mode=1 (active-backup)**
Один из интерфейсов активен. Если активный интерфейс выходит из строя (link down и т.д.), другой интерфейс заменяет активный.  
**mode=2 (balance-xor)**
Передачи распределяются между интерфейсами на основе формулы ((MAC-адрес источника) XOR (MAC-адрес получателя)) % число интерфейсов. Один и тот же интерфейс работает с определённым получателем. Режим даёт балансировку нагрузки и отказоустойчивость.  
**mode=3 (broadcast)**
Все пакеты на все интерфейсы  
**mode=4 (802.3ad)**
Link Agregation — IEEE 802.3ad, требует от коммутатора настройки.  
**mode=5 (balance-tlb)**
Входящие пакеты принимаются только активным сетевым интерфейсом, исходящий распределяется в зависимости от текущей загрузки каждого интерфейса. Не требует настройки коммутатора.  
**mode=6 (balance-alb)**
Тоже самое что 5, только входящий трафик тоже распределяется между интерфейсами.  
  
Пример конфига (через netplan):  
```  
bonds: 
      bond0:
        dhcp4: no
        interfaces: [eth0, eth1]
        parameters:
          mode: 802.3ad
          mii-monitor-interval: 1  
```  
Если агрегация производится на 3-ем уровне, то в bond-ах можно также настраивать ip-адреса, шлюз по умолчанию и маршрутизацию  

5. В сети с маской /29 есть 8 адресов (2^3), при этом 6 можно использовать для хостов (не забываем адрес сети и броадкаст)  
Соответственно таких подсетей в /24 маске 2^5=32 шт. Примеры подсетей:  
10.10.10.248/29  
10.10.10.240/29  
10.10.10.232/29  
10.10.10.224/29  
10.10.10.216/29  
.......  
6. Думаю можно взять адреса из диапазона 100.64/10.  
Ближайшая маска для подсети 40-50 хостов с учетом служебных адресов - (2^6=64) /26 (или 255.255.255.192)  
7. Показать ARP-таблицу в Windows: **arp -a**  
в Linux: **ip neighbour show** или просто **ip neigh**  
Очистка ARP-кэша в Linux: **ip neighbour flush** или **ip neigh flush**  
в Windows: **netsh interface ip delete arpcache**  
Удаление из ARP-таблицы одного элемента в Linux: **ip neighbour delete** или **ip neigh delete**  
в WIndows: **ARP -d inet_addr [if_addr]**  

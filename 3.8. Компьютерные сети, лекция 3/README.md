## 3.8. Компьютерные сети, лекция 3  

1. show ip route 178.168.193.128  
```  
route-views>show ip route 178.168.193.128
Routing entry for 178.168.192.0/20
  Known via "bgp 6447", distance 20, metric 0
  Tag 6939, type external
  Last update from 64.71.137.241 2w1d ago
  Routing Descriptor Blocks:
  * 64.71.137.241, from 64.71.137.241, 2w1d ago
      Route metric is 0, traffic share count is 1
      AS Hops 4
      Route tag 6939
      MPLS label: none  
```  
show bgp 178.168.193.128
```  
route-views>show bgp 178.168.193.128
BGP routing table entry for 178.168.192.0/20, version 307707451
Paths: (23 available, best #22, table default)
  Not advertised to any peer
  ............
  Refresh Epoch 1
  6939 60280 60330 25106
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external, best
      path 7FE1872E1E48 RPKI State valid
      rx pathid: 0, tx pathid: 0x0
  ............
```  
2. Создание dummy интерфейса:  
```  
vagrant@vagrant:~$ sudo ip link add dev dum0 type dummy
```  

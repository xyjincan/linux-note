
### 管理
    vCenter Server (vcsa)
        各个资源、对象管理

    NSX manager
        分布式防火墙的管理平面，控制平面
        与vCenter Server交互，执行其规则
        网络虚拟化和安全性平台

    ESXi主机

    vRealize Automation Center 自动化云平台
    vRealize Operations Manager统一监控 vROPS
        统一监控与报表 超级运维
            vSphere NSX Virtual SAN vRealize Automation Center Horizon Database


### 下载前 先注册试用
    https://my.vmware.com/cn/web/vmware/registration?source=evap&p=vsphere-eval



### 私网：内部网络 公网：外部网络 NAT

    避免地址冲突
    IP地址资源不足
    保护重要数据
    负载均衡部署融合

    数据包的包头不能被加密
    网络调试更加困难
    真实物理IP被屏蔽





### 网络

    分布式网络虚拟化
        流转发
        控制器





## 技术

    Overlay 封装 突破物理网络系统（VLAN、MAC、三层二层）数量容量限制


Overlay: VXLAN 

    虚拟机本身VLAN信息对外不可见
    VLAN添加VNI（VLAN Network Identifer），取代VLAN用来标识VXLAN网段
        VNI：相同才能实现二层通信
        VTEP与物理网络相连，分配的地址为物理网络IP地址。VXLAN报文中源IP地址为本节点的VTEP地址，VXLAN报文中目的IP地址为对端节点的VTEP地址，一对VTEP地址就对应着一个VXLAN隧道。


防火墙：
    软件防火墙: 
    硬件防火墙：串接 旁路
    
    云计算实现物理线路全不算防火墙不现实、经济



    微分段防火墙：基于每个虚拟机的出入栈流量防护，独立于虚拟机网络IP
        


    NSX不同网段之间互相通信：
        Overlay-VXLAN 虚拟网络默认互相隔离
        基于不同网络之间通信部署防火墙

    与物理拓扑无关的安全策略
    
    逻辑交换机
    分布式端口组
    安全组

NSX-V 服务网关
    提供路由、防火墙、负载均衡、二层-三层VPN、NAT、DHCP和DNS
    二层桥接
    三层路由
    
    实现NAT（保护重要数据，负载均衡部署融合）
        扩展为任意两个网络间服务时的地址转换

    




NSX Edge:分布式虚拟防火墙block reject allow（2-4层）（5-7安全集成合作安全方案）
        二层MAC ARP
        三四 IP地址 UDP/TCP

    NSX Edge服务网关
        防火墙、负载均衡
        物理网络和虚拟网络的接口、流量
        保护虚拟机和物理机之间的流量
        2-4层防护，5-7层需要第三方安全

    NSX分布式防火墙处理东西流量
        保护虚拟机
    
NSX Edge的HA
    部署模式： ECMP HA
        南部流量冗余
        等价多路径
    
    分布式逻辑路由器和外部物理网络之间通过部署最多8台NSX Edge


    双台HA，一台处理Active状态，一台Standby状态备用Edge（不承载流量和服务）
        NSX manager负责对其状态进行管理，同步配置和策略
        主备使用内部通信IP做心跳（非服务IP）
        NSX Conteoller不允许失效设备再次切换回主服务（再次中断部分服务）,需要手动重设

    
NSX Edge服务网关部署

    Source NAT
        masquerading(IP伪装)
        192.168.1.0/24 -> 10.20.181.171
            edge会将网段伪装成10.20.181.171，与其它网络通信

    Destination NAT
        发布内网服务
        将内部192.168.1.2转换成10.20.181.170

        负载均衡：将服务分摊到多个操作单元上执行，共同完成工作

            单臂 在线模式 分布式
        
        负载平衡算法（软件、硬件实现）
            依序 比重 流量比例 使用端 应用类别 连接数据 服务类别 自动分配

        
        应用位置： 本地负载均衡 全局负载均衡

        edge支持 TCP UDP 多种负载均衡算法


NSX Edge服务网关实现VPN

    跨数据中心地区进行复制和备份

    公有云-私有云连接


    NSX Edge Manager / NSX Controller
       异地NSX Edge VPN客户端
    
    二层VPN
        迁移，存储跨数据中心
    三层VPN
        远程客户端连接数据中心资源(SSL VPN)



#### 多vCenter环境中的NSX-V

    NSX支持跨多个集群实现统一的逻辑网络


#### 多虚拟环境下 KVM  NSX-MH

    OVS(Open vSwitch)

### NSX OpenStack











    

    






    


SDN:
    应用层
    向北接口
    控制层
    向南接口
    基础设施层

    南北流量
    东西流量

NFV:网络功能虚拟化
SDN：
    
网络带宽

物理机器 现行标准



OpenFlow


java -jar -Xms258m -Xmx258m -XX:PermSize=512M -XX:MaxPermSize=512m back-module.jar --spring.profiles.active=prod --server.port=8004



-vmargs -Xms128M -Xmx512M -XX:PermSize=64M -XX:MaxPermSize=128M 
-vmargs 说明后面是VM的参数，所以后面的其实都是JVM的参数了 
-Xms128m JVM初始分配的堆内存 
-Xmx512m JVM最大允许分配的堆内存，按需分配 
-XX:PermSize=64M JVM初始分配的非堆内存 
-XX:MaxPermSize=128M JVM最大允许分配的非堆内存，按需分

设置JVM内存的参数有四个：
-Xmx Java Heap最大值，默认值为物理内存的1/4，最佳设值应该视物理内存大小及计算机内其他内存开销而定；
-Xms Java Heap初始值，Server端JVM最好将-Xms和-Xmx设为相同值，开发测试机JVM可以保留默认值；
-Xmn Java Heap Young区大小，不熟悉最好保留默认值；
-Xss 每个线程的Stack大小，不熟悉最好保留默认值；




设置JVM内存的参数有四个：
-Xmx   Java Heap最大值，默认值为物理内存的1/4，最佳设值应该视物理内存大小及计算机内其他内存开销而定；
-Xms   Java Heap初始值，Server端JVM最好将-Xms和-Xmx设为相同值，开发测试机JVM可以保留默认值；
-Xmn   Java Heap Young区大小，不熟悉最好保留默认值；
-Xss   每个线程的Stack大小，不熟悉最好保留默认值；
2. 如何设置JVM内存分配：（1）当在命令提示符下启动并使用JVM时（只对当前运行的类Test生效）：java -Xmx128m -Xms64m -Xmn32m -Xss16m Test（2）当在集成开发环境下（如eclipse）启动并使用JVM时：a. 在eclipse根目录下打开eclipse.ini，默认内容为（这里设置的是运行当前开发工具的JVM内存分配）：-vmargs  -Xms40m  -Xmx256m -vmargs表示以下为虚拟机设置参数，可修改其中的参数值，也可添加-Xmn，-Xss，另外，eclipse.ini内还可以设置非堆内存，如：-XX:PermSize=56m，-XX:MaxPermSize=128m。此处设置的参数值可以通过以下配置在开发工具的状态栏显示：在eclipse根目录下创建文件options，文件内容为：org.eclipse.ui/perf/showHeapStatus=true修改eclipse根目录下的eclipse.ini文件，在开头处添加如下内容：-debug  options  -vm  javaw.exe 重新启动eclipse，就可以看到下方状态条多了JVM信息。
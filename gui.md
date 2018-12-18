systemctl --all|grep gdm
     gdm.service - GNOME Display Manager



systemctl list-unit-files








bluetooth graphical










CentOS 7 运行级别的切换

由命令行级别切换到窗口级别的命令未变：init 5或startx

由窗口级别切换到命令行级别的命令未变：init 3

新版本的运行级别都定义在 /lib/systemd/system下:

[root@localhost ~]# ls -ltr /lib/systemd/system/runlevel*.target
lrwxrwxrwx. 1 root root  16 9月  10 20:58 /lib/systemd/system/default.target -> graphical.target
lrwxrwxrwx. 1 root root  13 9月  10 20:58 /lib/systemd/system/runlevel1.target -> rescue.target
lrwxrwxrwx. 1 root root  15 9月  10 20:58 /lib/systemd/system/runlevel0.target -> poweroff.target
lrwxrwxrwx. 1 root root  17 9月  10 20:58 /lib/systemd/system/runlevel4.target -> multi-user.target
lrwxrwxrwx. 1 root root  17 9月  10 20:58 /lib/systemd/system/runlevel3.target -> multi-user.target
lrwxrwxrwx. 1 root root  17 9月  10 20:58 /lib/systemd/system/runlevel2.target -> multi-user.target
lrwxrwxrwx. 1 root root  16 9月  10 20:58 /lib/systemd/system/runlevel5.target -> graphical.target
lrwxrwxrwx. 1 root root  13 9月  10 20:58 /lib/systemd/system/runlevel6.target -> reboot.target

可以针对不同需要设置不同的运行级别:

如设置命令行级别(init 3)方法:
[root@localhost ~]# ln -svf /lib/systemd/system/runlevel3.target /etc/systemd/system/default.target
或
[root@localhost ~]# ln -svf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target
或 
[root@localhost ~]#systemctl set-default multi-user.target

设置窗口级别(init 5)方法:
[root@localhost ~]# ln -svf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target
或
[root@localhost ~]# ln -svf /lib/systemd/system/graphical.target /etc/systemd/system/default.target
或 
[root@localhost ~]#systemctl set-default graphical.target

-----------------------------分割线-----------------------------

修改系统运行级别：
1、systemd使用比sysvinit的运行级更为自由的target替代。第3运行级用multi-user.target替代。第5运行级用graphical.target替代。runlevel3.target和runlevel5.target分别是指向 multi-user.target和graphical.target的符号链接。
可以使用下面的命令切换到“运行级别3 ”：
systemctl isolate multi-user.target或systemctl isolate runlevel3.target

可以使用下面的命令切换到“运行级别5 ”：
systemctl isolate graphical.target或systemctl isolate runlevel5.target
2、如何改变默认运行级别？
systemd使用链接来指向默认的运行级别。在创建新的链接前，可以通过下面命令删除存在的链接： rm /etc/systemd/system/default.target
默认启动运行级别3 ：
ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target

默认启动运行级别5 ：
ln -sf /lib/systemd/system/graphical.target/etc/systemd/system/default.target

systemd不使用/etc/inittab文件。

-----------------------------分割线-----------------------------

如何查看当前运行级别？
旧的runlevel命令在systemd下仍然可以使用。可以继续使用它，尽管systemd使用 ‘target’ 概念(多个的 ‘target’ 可以同时激活)替换了之前系统的runlevel。
等价的systemd命令是systemctl list-units –type=target

all 
    zkServer.sh start


### START

cd /opt/cc/hadoop-2.7.7/sbin
./start-dfs.sh 
./start-yarn.sh


start-hbase.sh


### STOP

stop-hbase.sh

cd /opt/cc/hadoop-2.7.7/sbin/
./stop-dfs.sh
./stop-yarn.sh





### shutdown reboot

zkServer.sh stop

su root
shutdown -h now



all: 
    zkServer.sh start


start-hbase.sh



stop-hbase.sh




cd /opt/cc/hbase-2.1.1/conf


export HBASE_HOME=/opt/cc/hbase-2.1.1
export PATH=$PATH:$HBASE_HOME/bin







## zoo keeper


cd /opt/cc/zookeeper-3.4.12/bin

./zkServer.sh start
./zkServer.sh status


export ZOOKEEPER_HOME=/opt/cc/zookeeper-3.4.12
export PATH=$PATH:$ZOOKEEPER_HOME/bin


server.1=master.cc:2888:3888
server.2=node000.cc:2888:3888
server.3=node001.cc:2888:3888






master.cc,node001.cc,node002.cc


master.cc
node001.cc
node002.cc
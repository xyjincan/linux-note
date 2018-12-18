
##

cd 

export JAVA_HOME=/opt/jdk


/opt/jdk

/opt/cc
    hadoop-2.7.7  hbase-2.1.1  
    spark-2.4.0-bin-hadoop2.7  zookeeper-3.4.12

/opt/cc/hadoop-2.7.7/etc/hadoop


/cc/
    data  hdfs  tmp


## 格式化

hdfs namenode -format


## 启动


cd /opt/cc/hadoop-2.7.7/sbin
./start-dfs.sh 
./start-yarn.sh


cd /opt/cc/hadoop-2.7.7/sbin/
./stop-dfs.sh
./stop-yarn.sh




hadoop jar /opt/cc/hadoop-2.7.7/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.7.jar pi 10 10



## 网络管理

base
    10.10.1.1-10

master
    10.10.1.10-19

node
    10.20.1.20-99

others io 
    10.20.1.100-200



## hosts


10.10.1.10    master.cc

10.10.1.20    node001.cc
10.10.1.22    node002.cc
10.10.1.23    node003.cc
10.10.1.24    node004.cc


10.10.1.169   E460





## ssh 免密登录
    A生成证书公钥私钥
    B(主机@账号)信任该公钥
    A免密登录B

    ssh-keygen -t rsa -P ""
    cat id_rsa.pub >> authorized_keys
    chmod 600 authorized_keys


## 
export HADOOP_HOME=/opt/cc/hadoop-2.7.7
export PATH=/opt/cc/hadoop-2.7.7/bin:$PATH
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop


























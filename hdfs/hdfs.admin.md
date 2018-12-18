

## 启动


cd /opt/cc/hadoop-2.7.7/sbin
./start-dfs.sh 
./start-yarn.sh


cd /opt/cc/hadoop-2.7.7/sbin/
./stop-dfs.sh
./stop-yarn.sh


hdfs dfsadmin -safemode get


# hdfs

hdfs dfs -df -h /


hadoop fs -du -h /
hadoop fs -ls -h /


### yarn

yarn application -list

yarn node -list -all



#启动系统自带的名为“wordcount”的mapreduce程序

hadoop jar /opt/cc/hadoop-2.7.7/share/hadoop/hadoop-mapreduce-examples-2.7.1.jar 
    wordcount /jc/passwd.txt /jc/passout.txt

hadoop jar /opt/cc/hadoop-2.7.7/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.7.jar 
    pi 10 10



###


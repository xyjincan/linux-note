
### 
    EXPLAINANALYZE

    


## 并行处理 速度

    force_parallel_mode: 主要用于测试，on/true表示强制使用并行查询
    max_worker_processes：决定了整个数据库集群允许启动多少个work process（注意如果有standby，standby的参数必须大于等于主库的参数值）。设置为0，表示不允许并行。
    max_parallel_workers_per_gather: 最多会有多少个后台进程来一起完成当前查询，推荐值为1-4。这些workers主要来自max_worker_processes（进程池的大小）。在OLTP业务中，因为每个worker都会消耗同等的work_mem等资源，可能会产生比较严重的争抢。
    min_parallel_relation_size: 启用并行查询的最小数据表的大小，作为是否启用并行计算的条件之一，如果小于它，不启用并行计算。并不是所有小于它的表一定不会启用并行。
    parallel_setup_cost：表示启动woker process的启动成本，因为启动worker进程需要建立共享内存等操作，属于附带的额外成本。其值越小，数据库越有可能使用并行查询。
    parallel_tuple_cost：woker进程处理完后的tuple要传输给上层node，即进程间查询结果的交换成本，即后台进程间传输一个元组的代价。其值越小，数据库越有可能使用并行。
    parallel_workers：设置表级并行度，可在建表时设置，也可后期设置

    max_worker_processes = 128  
    max_parallel_workers_per_gather = 32  
    parallel_leader_participation = on  
    max_parallel_workers = 128  





###
    内存，磁盘，进程，大小，长度








## 
    日志 检查点 超时时间 后台写入器

    会话层 系统层

    集群 数据块 

## 表空间（pg中文件系统的一个链接）

    select tablename,tablespace from pg_tables where tablename
         on ('dept','xxx');

    create tablespace xxx location '/xxxx';

    create table dept(id int,dname text) tablespace xxspace;

    alter database test set default_tablespace='xxspace';

### shared_buffers   保证了不需要在内存中保留数据集的多个副本。

    将用于PostgreSQL的数据缓存。当多个会话从同一个表中请求相同数据时，
    当设定shared_buffers的值时，也需要考虑操作系统和服务器上其他程序对内存的要求。另一方面，推荐的常用做法是设定上限为RAM的40%。
    看下有多少缓存命中了我们想得到的数据


#### effective_cache_size
    并发的查询将共享的可用空间

    值增加，成本数值显著下降。估计出的数据检索成本比之前低很多。

#### checkpoint_segments 

#####
    default_statistics_target
    g_xlog里面：这个目录包含了预写日表（Write Ahead Log，WAL）文件。

    功能进程包括了bgwriter、checkpointer、autovacuum launcher、log Writer、stats collector process等。
    守护进程还监听连接请求

    select pg_relation_filepath('xxx');// /数据库/表/数据块
    show data_directory;
    select * from pg_setting;



    base：这个目录存放默认的表空间pg_default。模板数据库和其他没有显式赋予表空间的数据库都存放在此目录中。

    pg_tblspc：当你创建新的表空间，符号链接会保存在此目录中。
    pg_xlog：用于数据库崩溃恢复的预写式日志存放在此目录中。
    pg_subtrans：存放跟子事务相关的数据。
    pg_multixact：包含多事务状态的数据。用户的应用程序严重依赖共享行锁的情况下，此目录会被经常使用。
    pg_twophase：保存两阶段提交的相关数据。



### psql

    psql --host=localhost --dbname=xxx --port=5432

    # \d  查看数据库
    # \dt 查看表 \ds \dv \df s代表序列、v代表视图、f代表函数



### 索引
    create index bar on foo(a);
    reindex table foo;

    正常构建一个索引时，它会把表锁住以阻塞写操作。

    CREATE INDEX CONCURRENTLY来创建并发索引。
        并发创建索引比起加锁的标准形式效率要低许多。

    “BRIN是一种为加速非常大型的表上的扫描而设计的新型索引访问方法，它没有B-tree或者其他传统索引的维护开销。

    多列索引，索引用于排序
    部分索引 表达式 全文



### MVCC

PostgreSQL使用MVCC为不同的会话提供不同的数据库视图，这种方式是基于隔离级别设置的。借助MVCC，可以实现高级别的并发性，且不需要牺牲性能。关键规则是读取者不应阻碍写入者，而写入者也不应该阻碍读取者。MVCC被许多其他的数据库所使用（例如Oracle与Berkeley DB）。

需要后台清除多版本的数据，并保证磁盘空间可控






























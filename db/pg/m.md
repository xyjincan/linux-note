## postgresql 常见管理笔记


sudo yum install --downloadonly --downloaddir=/tmp postgresql11 postgresql11-server
yum install postgresql11 postgresql11-server



## vim

/usr/pgsql-11/bin/postgresql-11-setup initdb 
systemctl enable postgresql-11
systemctl start postgresql-11


systemctl disable postgresql-11
systemctl stop postgresql-11


 
 
 
### 自定义postgresql 存储位置
	vi /usr/pgsql-11/bin/postgresql-11-setup
	vi /usr/lib/systemd/system/postgresql-10.service 
	# Location of database directory 
	Environment=PGDATA=/var/lib/pgsql/10/data/
	--------------------- 

	vi pg_hba.conf 
	最后添加一行 如果对具体网段有要求，自行修改 
	host all all 0.0.0.0/0 md5

	vi postgresql.conf
	listen_addresses = '0.0.0.0'

	添加防火墙通过

	sudo firewall-cmd --permanent --add-port=5432/tcp
	sudo firewall-cmd --reload
	--------------------- 

## 修改密码
	
	[root@live data]# sudo -u postgres psql
	postgres=# \password postgres
	-- psql#: ALTER USER postgres WITH PASSWORD 'XXXX-XXX'
	
	

# 导出数据

pg_dump -d vsitution  -t alarm_201809 -f /home/data/app/tmp/alarm09.sql

# 导入数据

psql -d vsitution -f alarm09.sql




#  
pg_restore -d vsitution  alarm09.sql
su -u postgres pg_restore -d vsitution  alarm09.sql
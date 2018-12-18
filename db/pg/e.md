### 拓展知识笔记

-- 建表（键，约束，含联合） 索引 注释 触发器 函数 存储过程  记录
--		 




pg11
    增强分区表功能，支持存储过程
    

索引
    Btree：为每一行记录都建立索引
    时序索引
		记录块内最大最小值
        范围索引


    GiST

	CREATE INDEX "report_date_index" ON "public"."report" USING btree (
	  "date" ASC NULLS LAST
	);

数据块


多进程架构

MVCC方案 架构
    元组可见性


表空间







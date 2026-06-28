[ndhsetup_output.md](https://github.com/user-attachments/files/29432820/ndhsetup_output.md)
SPARK_MAJOR_VERSION is set to 2, using Spark2
26/06/26 13:25:49 INFO SparkContext: Running Spark version 2.3.0.2.6.5.0-292
26/06/26 13:25:49 INFO SparkContext: Submitted application: MovieLens100K_Setup
26/06/26 13:25:49 INFO SecurityManager: Changing view acls to: maria_dev
26/06/26 13:25:49 INFO SecurityManager: Changing modify acls to: maria_dev
26/06/26 13:25:49 INFO SecurityManager: Changing view acls groups to: 
26/06/26 13:25:49 INFO SecurityManager: Changing modify acls groups to: 
26/06/26 13:25:49 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(maria_dev); groups with view permissions: Set(); users  with modify permissions: Set(maria_dev); groups with modify permissions: Set()
26/06/26 13:25:50 INFO Utils: Successfully started service 'sparkDriver' on port 38367.
26/06/26 13:25:51 INFO SparkEnv: Registering MapOutputTracker
26/06/26 13:25:51 INFO SparkEnv: Registering BlockManagerMaster
26/06/26 13:25:51 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
26/06/26 13:25:51 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
26/06/26 13:25:51 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-38af648b-8442-4ac9-be5f-6b31cd219adb
26/06/26 13:25:51 INFO MemoryStore: MemoryStore started with capacity 366.3 MB
26/06/26 13:25:51 INFO SparkEnv: Registering OutputCommitCoordinator
26/06/26 13:25:51 INFO log: Logging initialized @16898ms
26/06/26 13:25:51 INFO Server: jetty-9.3.z-SNAPSHOT
26/06/26 13:25:51 INFO Server: Started @17208ms
26/06/26 13:25:51 INFO AbstractConnector: Started ServerConnector@775dd60d{HTTP/1.1,[http/1.1]}{0.0.0.0:4040}
26/06/26 13:25:51 INFO Utils: Successfully started service 'SparkUI' on port 4040.
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@2792ab14{/jobs,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@3b855608{/jobs/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@55cfd8f{/jobs/job,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@50b57b8a{/jobs/job/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@41115282{/stages,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@23437faa{/stages/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@626ad817{/stages/stage,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@6ab0d9c7{/stages/stage/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@5eae1ee6{/stages/pool,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@3bc9496{/stages/pool/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@637ad087{/storage,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@fe853ce{/storage/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@211f25fb{/storage/rdd,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@46e00d6a{/storage/rdd/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@732b13d9{/environment,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@3e104851{/environment/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@66788295{/executors,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@20b5586d{/executors/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@b2b3279{/executors/threadDump,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@37c5a18d{/executors/threadDump/json,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@150bf1ca{/static,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@3aede249{/,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@64a537ca{/api,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@22765e5a{/jobs/job/kill,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@676c089f{/stages/stage/kill,null,AVAILABLE,@Spark}
26/06/26 13:25:52 INFO SparkUI: Bound SparkUI to 0.0.0.0, and started at http://sandbox-hdp.hortonworks.com:4040
26/06/26 13:25:53 INFO SparkContext: Added file file:/home/maria_dev/ndhsetup.py at file:/home/maria_dev/ndhsetup.py with timestamp 1782480353558
26/06/26 13:25:53 INFO Utils: Copying /home/maria_dev/ndhsetup.py to /tmp/spark-622bed24-d735-468b-b7b9-750ec55e59f4/userFiles-57c77220-981a-4fbf-8fcf-ed67a1061b00/ndhsetup.py
26/06/26 13:25:53 INFO Executor: Starting executor ID driver on host localhost
26/06/26 13:25:53 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 33329.
26/06/26 13:25:53 INFO NettyBlockTransferService: Server created on sandbox-hdp.hortonworks.com:33329
26/06/26 13:25:53 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
26/06/26 13:25:54 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, sandbox-hdp.hortonworks.com, 33329, None)
26/06/26 13:25:54 INFO BlockManagerMasterEndpoint: Registering block manager sandbox-hdp.hortonworks.com:33329 with 366.3 MB RAM, BlockManagerId(driver, sandbox-hdp.hortonworks.com, 33329, None)
26/06/26 13:25:54 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, sandbox-hdp.hortonworks.com, 33329, None)
26/06/26 13:25:54 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, sandbox-hdp.hortonworks.com, 33329, None)
26/06/26 13:25:54 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@3c20339{/metrics/json,null,AVAILABLE,@Spark}
26/06/26 13:25:57 INFO EventLoggingListener: Logging events to hdfs:/spark2-history/local-1782480353713
26/06/26 13:25:58 INFO SharedState: loading hive config file: file:/etc/spark2/2.6.5.0-292/0/hive-site.xml
26/06/26 13:25:58 INFO SharedState: Setting hive.metastore.warehouse.dir ('null') to the value of spark.sql.warehouse.dir ('file:/home/maria_dev/spark-warehouse/').
26/06/26 13:25:58 INFO SharedState: Warehouse path is 'file:/home/maria_dev/spark-warehouse/'.
26/06/26 13:25:58 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@75edaa53{/SQL,null,AVAILABLE,@Spark}
26/06/26 13:25:58 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@2c0ec75e{/SQL/json,null,AVAILABLE,@Spark}
26/06/26 13:25:58 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@120ad7f2{/SQL/execution,null,AVAILABLE,@Spark}
26/06/26 13:25:58 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@13feefb8{/SQL/execution/json,null,AVAILABLE,@Spark}
26/06/26 13:25:58 INFO ContextHandler: Started o.s.j.s.ServletContextHandler@483396cb{/static/sql,null,AVAILABLE,@Spark}
26/06/26 13:26:00 INFO StateStoreCoordinatorRef: Registered StateStoreCoordinator endpoint
============================================================
Spark Session Created Successfully
('Spark Version :', u'2.3.0.2.6.5.0-292')
============================================================

Reading files from HDFS...
26/06/26 13:26:02 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 361.1 KB, free 365.9 MB)
26/06/26 13:26:02 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 32.3 KB, free 365.9 MB)
26/06/26 13:26:02 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 32.3 KB, free: 366.3 MB)
26/06/26 13:26:02 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:0
26/06/26 13:26:02 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 361.2 KB, free 365.6 MB)
26/06/26 13:26:02 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 32.3 KB, free 365.5 MB)
26/06/26 13:26:02 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 32.3 KB, free: 366.2 MB)
26/06/26 13:26:03 INFO SparkContext: Created broadcast 1 from textFile at NativeMethodAccessorImpl.java:0
26/06/26 13:26:03 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 361.2 KB, free 365.2 MB)
26/06/26 13:26:03 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 32.3 KB, free 365.1 MB)
26/06/26 13:26:03 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 32.3 KB, free: 366.2 MB)
26/06/26 13:26:03 INFO SparkContext: Created broadcast 2 from textFile at NativeMethodAccessorImpl.java:0
Files loaded successfully.

Sample User Record
26/06/26 13:26:03 INFO FileInputFormat: Total input paths to process : 1
26/06/26 13:26:04 INFO SparkContext: Starting job: runJob at PythonRDD.scala:141
26/06/26 13:26:04 INFO DAGScheduler: Got job 0 (runJob at PythonRDD.scala:141) with 1 output partitions
26/06/26 13:26:04 INFO DAGScheduler: Final stage: ResultStage 0 (runJob at PythonRDD.scala:141)
26/06/26 13:26:04 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:04 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:04 INFO DAGScheduler: Submitting ResultStage 0 (PythonRDD[6] at RDD at PythonRDD.scala:48), which has no missing parents
26/06/26 13:26:04 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 5.5 KB, free 365.1 MB)
26/06/26 13:26:04 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 3.4 KB, free 365.1 MB)
26/06/26 13:26:04 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:04 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:04 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 0 (PythonRDD[6] at RDD at PythonRDD.scala:48) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:04 INFO TaskSchedulerImpl: Adding task set 0.0 with 1 tasks
26/06/26 13:26:04 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:04 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
26/06/26 13:26:04 INFO Executor: Fetching file:/home/maria_dev/ndhsetup.py with timestamp 1782480353558
26/06/26 13:26:04 INFO Utils: /home/maria_dev/ndhsetup.py has been previously copied to /tmp/spark-622bed24-d735-468b-b7b9-750ec55e59f4/userFiles-57c77220-981a-4fbf-8fcf-ed67a1061b00/ndhsetup.py
26/06/26 13:26:04 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:0+11314
26/06/26 13:26:06 INFO PythonRunner: Times: total = 1195, boot = 774, init = 421, finish = 0
26/06/26 13:26:06 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 1424 bytes result sent to driver
26/06/26 13:26:06 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 1605 ms on localhost (executor driver) (1/1)
26/06/26 13:26:06 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
26/06/26 13:26:06 INFO DAGScheduler: ResultStage 0 (runJob at PythonRDD.scala:141) finished in 1.821 s
26/06/26 13:26:06 INFO DAGScheduler: Job 0 finished: runJob at PythonRDD.scala:141, took 2.042672 s
1|24|M|technician|85711

Sample Rating Record
26/06/26 13:26:06 INFO FileInputFormat: Total input paths to process : 1
26/06/26 13:26:06 INFO SparkContext: Starting job: runJob at PythonRDD.scala:141
26/06/26 13:26:06 INFO DAGScheduler: Got job 1 (runJob at PythonRDD.scala:141) with 1 output partitions
26/06/26 13:26:06 INFO DAGScheduler: Final stage: ResultStage 1 (runJob at PythonRDD.scala:141)
26/06/26 13:26:06 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:06 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:06 INFO DAGScheduler: Submitting ResultStage 1 (PythonRDD[7] at RDD at PythonRDD.scala:48), which has no missing parents
26/06/26 13:26:06 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 5.5 KB, free 365.1 MB)
26/06/26 13:26:06 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 3.4 KB, free 365.1 MB)
26/06/26 13:26:06 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:06 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:06 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 1 (PythonRDD[7] at RDD at PythonRDD.scala:48) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:06 INFO TaskSchedulerImpl: Adding task set 1.0 with 1 tasks
26/06/26 13:26:06 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 1, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:06 INFO Executor: Running task 0.0 in stage 1.0 (TID 1)
26/06/26 13:26:06 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:0+989586
26/06/26 13:26:06 INFO PythonRunner: Times: total = 224, boot = 8, init = 215, finish = 1
26/06/26 13:26:06 INFO Executor: Finished task 0.0 in stage 1.0 (TID 1). 1420 bytes result sent to driver
26/06/26 13:26:06 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 1) in 327 ms on localhost (executor driver) (1/1)
26/06/26 13:26:06 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
26/06/26 13:26:06 INFO DAGScheduler: ResultStage 1 (runJob at PythonRDD.scala:141) finished in 0.361 s
26/06/26 13:26:06 INFO DAGScheduler: Job 1 finished: runJob at PythonRDD.scala:141, took 0.398780 s
196	242	3	881250949

Sample Movie Record
26/06/26 13:26:06 INFO FileInputFormat: Total input paths to process : 1
26/06/26 13:26:06 INFO SparkContext: Starting job: runJob at PythonRDD.scala:141
26/06/26 13:26:06 INFO DAGScheduler: Got job 2 (runJob at PythonRDD.scala:141) with 1 output partitions
26/06/26 13:26:06 INFO DAGScheduler: Final stage: ResultStage 2 (runJob at PythonRDD.scala:141)
26/06/26 13:26:06 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:06 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:06 INFO DAGScheduler: Submitting ResultStage 2 (PythonRDD[8] at RDD at PythonRDD.scala:48), which has no missing parents
26/06/26 13:26:06 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 5.5 KB, free 365.1 MB)
26/06/26 13:26:06 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 3.4 KB, free 365.1 MB)
26/06/26 13:26:06 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:06 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:06 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 2 (PythonRDD[8] at RDD at PythonRDD.scala:48) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:06 INFO TaskSchedulerImpl: Adding task set 2.0 with 1 tasks
26/06/26 13:26:06 INFO TaskSetManager: Starting task 0.0 in stage 2.0 (TID 2, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:06 INFO Executor: Running task 0.0 in stage 2.0 (TID 2)
26/06/26 13:26:06 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:0+118172
26/06/26 13:26:07 INFO PythonRunner: Times: total = 56, boot = 6, init = 49, finish = 1
26/06/26 13:26:07 INFO Executor: Finished task 0.0 in stage 2.0 (TID 2). 1481 bytes result sent to driver
26/06/26 13:26:07 INFO TaskSetManager: Finished task 0.0 in stage 2.0 (TID 2) in 121 ms on localhost (executor driver) (1/1)
26/06/26 13:26:07 INFO TaskSchedulerImpl: Removed TaskSet 2.0, whose tasks have all completed, from pool 
26/06/26 13:26:07 INFO DAGScheduler: ResultStage 2 (runJob at PythonRDD.scala:141) finished in 0.162 s
26/06/26 13:26:07 INFO DAGScheduler: Job 2 finished: runJob at PythonRDD.scala:141, took 0.172971 s
1|Toy Story (1995)|01-Jan-1995||http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)|0|0|0|1|1|1|0|0|0|0|0|0|0|0|0|0|0|0|0
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 68
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 50
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 28
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 66
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 32
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 59
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 61
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 16
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 58
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 35
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 74
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 8
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 55
26/06/26 13:26:07 INFO BlockManagerInfo: Removed broadcast_4_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 54
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 67
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 45
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 56
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 43
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 69
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 48
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 40
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 9
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 38
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 65
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 1
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 15
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 24
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 30
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 41
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 47
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 62
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 21
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 5
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 60
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 75
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 34
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 70
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 18
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 29
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 23
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 64
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 52
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 10
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 33
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 63
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 25
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 11
26/06/26 13:26:07 INFO BlockManagerInfo: Removed broadcast_3_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 42
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 2
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 4
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 53
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 31
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 49
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 46
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 22
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 6
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 39
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 7
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 13
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 26
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 57
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 14
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 3
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 19
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 71
26/06/26 13:26:07 INFO BlockManagerInfo: Removed broadcast_5_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.4 KB, free: 366.2 MB)
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 17
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 44
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 27
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 73
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 51
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 36
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 37
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 20
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 72
26/06/26 13:26:07 INFO ContextCleaner: Cleaned accumulator 12

Users Data
26/06/26 13:26:13 INFO CodeGenerator: Code generated in 905.528998 ms
26/06/26 13:26:14 INFO CodeGenerator: Code generated in 76.46661 ms
26/06/26 13:26:14 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:14 INFO DAGScheduler: Got job 3 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:14 INFO DAGScheduler: Final stage: ResultStage 3 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:14 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:14 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:14 INFO DAGScheduler: Submitting ResultStage 3 (MapPartitionsRDD[24] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:14 INFO MemoryStore: Block broadcast_6 stored as values in memory (estimated size 23.1 KB, free 365.1 MB)
26/06/26 13:26:14 INFO MemoryStore: Block broadcast_6_piece0 stored as bytes in memory (estimated size 11.9 KB, free 365.1 MB)
26/06/26 13:26:14 INFO BlockManagerInfo: Added broadcast_6_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 11.9 KB, free: 366.2 MB)
26/06/26 13:26:14 INFO SparkContext: Created broadcast 6 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:14 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 3 (MapPartitionsRDD[24] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:14 INFO TaskSchedulerImpl: Adding task set 3.0 with 1 tasks
26/06/26 13:26:14 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 3, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:14 INFO Executor: Running task 0.0 in stage 3.0 (TID 3)
26/06/26 13:26:14 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:0+11314
26/06/26 13:26:14 INFO CodeGenerator: Code generated in 36.412561 ms
26/06/26 13:26:14 INFO Executor: Finished task 0.0 in stage 3.0 (TID 3). 1886 bytes result sent to driver
26/06/26 13:26:14 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 3) in 196 ms on localhost (executor driver) (1/1)
26/06/26 13:26:14 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
26/06/26 13:26:14 INFO DAGScheduler: ResultStage 3 (showString at NativeMethodAccessorImpl.java:0) finished in 0.271 s
26/06/26 13:26:14 INFO DAGScheduler: Job 3 finished: showString at NativeMethodAccessorImpl.java:0, took 0.276665 s
+-------+---+------+----------+--------+
|user_id|age|gender|occupation|zip_code|
+-------+---+------+----------+--------+
|      1| 24|     M|technician|   85711|
|      2| 53|     F|     other|   94043|
|      3| 23|     M|    writer|   32067|
|      4| 24|     M|technician|   43537|
|      5| 33|     F|     other|   15213|
+-------+---+------+----------+--------+
only showing top 5 rows


Ratings Data
26/06/26 13:26:14 INFO CodeGenerator: Code generated in 39.623615 ms
26/06/26 13:26:14 INFO CodeGenerator: Code generated in 48.259566 ms
26/06/26 13:26:14 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:14 INFO DAGScheduler: Got job 4 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:14 INFO DAGScheduler: Final stage: ResultStage 4 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:14 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:14 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:14 INFO DAGScheduler: Submitting ResultStage 4 (MapPartitionsRDD[28] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:14 INFO MemoryStore: Block broadcast_7 stored as values in memory (estimated size 22.7 KB, free 365.1 MB)
26/06/26 13:26:14 INFO MemoryStore: Block broadcast_7_piece0 stored as bytes in memory (estimated size 11.7 KB, free 365.1 MB)
26/06/26 13:26:14 INFO BlockManagerInfo: Added broadcast_7_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 11.7 KB, free: 366.2 MB)
26/06/26 13:26:14 INFO SparkContext: Created broadcast 7 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:14 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 4 (MapPartitionsRDD[28] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:14 INFO TaskSchedulerImpl: Adding task set 4.0 with 1 tasks
26/06/26 13:26:14 INFO TaskSetManager: Starting task 0.0 in stage 4.0 (TID 4, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:14 INFO Executor: Running task 0.0 in stage 4.0 (TID 4)
26/06/26 13:26:14 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:0+989586
26/06/26 13:26:14 INFO CodeGenerator: Code generated in 13.809802 ms
26/06/26 13:26:15 INFO Executor: Finished task 0.0 in stage 4.0 (TID 4). 1868 bytes result sent to driver
26/06/26 13:26:15 INFO TaskSetManager: Finished task 0.0 in stage 4.0 (TID 4) in 292 ms on localhost (executor driver) (1/1)
26/06/26 13:26:15 INFO TaskSchedulerImpl: Removed TaskSet 4.0, whose tasks have all completed, from pool 
26/06/26 13:26:15 INFO DAGScheduler: ResultStage 4 (showString at NativeMethodAccessorImpl.java:0) finished in 0.321 s
26/06/26 13:26:15 INFO DAGScheduler: Job 4 finished: showString at NativeMethodAccessorImpl.java:0, took 0.348903 s
+-------+--------+------+---------+
|user_id|movie_id|rating|timestamp|
+-------+--------+------+---------+
|    196|     242|     3|881250949|
|    186|     302|     3|891717742|
|     22|     377|     1|878887116|
|    244|      51|     2|880606923|
|    166|     346|     1|886397596|
+-------+--------+------+---------+
only showing top 5 rows


Movies Data
26/06/26 13:26:15 INFO CodeGenerator: Code generated in 83.964077 ms
26/06/26 13:26:15 INFO CodeGenerator: Code generated in 66.682888 ms
26/06/26 13:26:15 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:15 INFO DAGScheduler: Got job 5 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:15 INFO DAGScheduler: Final stage: ResultStage 5 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:15 INFO DAGScheduler: Parents of final stage: List()
26/06/26 13:26:15 INFO DAGScheduler: Missing parents: List()
26/06/26 13:26:15 INFO DAGScheduler: Submitting ResultStage 5 (MapPartitionsRDD[32] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:15 INFO MemoryStore: Block broadcast_8 stored as values in memory (estimated size 41.7 KB, free 365.0 MB)
26/06/26 13:26:15 INFO MemoryStore: Block broadcast_8_piece0 stored as bytes in memory (estimated size 18.4 KB, free 365.0 MB)
26/06/26 13:26:15 INFO BlockManagerInfo: Added broadcast_8_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 18.4 KB, free: 366.2 MB)
26/06/26 13:26:15 INFO SparkContext: Created broadcast 8 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:15 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 5 (MapPartitionsRDD[32] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:15 INFO TaskSchedulerImpl: Adding task set 5.0 with 1 tasks
26/06/26 13:26:15 INFO TaskSetManager: Starting task 0.0 in stage 5.0 (TID 5, localhost, executor driver, partition 0, ANY, 7922 bytes)
26/06/26 13:26:15 INFO Executor: Running task 0.0 in stage 5.0 (TID 5)
26/06/26 13:26:15 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:0+118172
26/06/26 13:26:15 INFO CodeGenerator: Code generated in 40.294501 ms
26/06/26 13:26:15 INFO Executor: Finished task 0.0 in stage 5.0 (TID 5). 2314 bytes result sent to driver
26/06/26 13:26:15 INFO TaskSetManager: Finished task 0.0 in stage 5.0 (TID 5) in 169 ms on localhost (executor driver) (1/1)
26/06/26 13:26:15 INFO TaskSchedulerImpl: Removed TaskSet 5.0, whose tasks have all completed, from pool 
26/06/26 13:26:15 INFO DAGScheduler: ResultStage 5 (showString at NativeMethodAccessorImpl.java:0) finished in 0.199 s
26/06/26 13:26:15 INFO DAGScheduler: Job 5 finished: showString at NativeMethodAccessorImpl.java:0, took 0.213897 s
+--------+-----------------+------------+------------------+--------------------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+
|movie_id|      movie_title|release_date|video_release_date|            imdb_url|unknown|action|adventure|animation|children|comedy|crime|documentary|drama|fantasy|film_noir|horror|musical|mystery|romance|sci_fi|thriller|war|western|
+--------+-----------------+------------+------------------+--------------------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+
|       1| Toy Story (1995)| 01-Jan-1995|                  |http://us.imdb.co...|      0|     0|        0|        1|       1|     1|    0|          0|    0|      0|        0|     0|      0|      0|      0|     0|       0|  0|      0|
|       2| GoldenEye (1995)| 01-Jan-1995|                  |http://us.imdb.co...|      0|     1|        1|        0|       0|     0|    0|          0|    0|      0|        0|     0|      0|      0|      0|     0|       1|  0|      0|
|       3|Four Rooms (1995)| 01-Jan-1995|                  |http://us.imdb.co...|      0|     0|        0|        0|       0|     0|    0|          0|    0|      0|        0|     0|      0|      0|      0|     0|       1|  0|      0|
|       4|Get Shorty (1995)| 01-Jan-1995|                  |http://us.imdb.co...|      0|     1|        0|        0|       0|     1|    0|          0|    1|      0|        0|     0|      0|      0|      0|     0|       0|  0|      0|
|       5|   Copycat (1995)| 01-Jan-1995|                  |http://us.imdb.co...|      0|     0|        0|        0|       0|     0|    1|          0|    1|      0|        0|     0|      0|      0|      0|     0|       1|  0|      0|
+--------+-----------------+------------+------------------+--------------------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+
only showing top 5 rows


Dataset Summary
26/06/26 13:26:16 INFO CodeGenerator: Code generated in 52.009606 ms
26/06/26 13:26:16 INFO CodeGenerator: Code generated in 34.914373 ms
26/06/26 13:26:16 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:16 INFO DAGScheduler: Registering RDD 35 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:16 INFO DAGScheduler: Got job 6 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:16 INFO DAGScheduler: Final stage: ResultStage 7 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:16 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 6)
26/06/26 13:26:16 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 6)
26/06/26 13:26:16 INFO DAGScheduler: Submitting ShuffleMapStage 6 (MapPartitionsRDD[35] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:16 INFO MemoryStore: Block broadcast_9 stored as values in memory (estimated size 22.9 KB, free 365.0 MB)
26/06/26 13:26:16 INFO MemoryStore: Block broadcast_9_piece0 stored as bytes in memory (estimated size 12.4 KB, free 365.0 MB)
26/06/26 13:26:16 INFO BlockManagerInfo: Added broadcast_9_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 12.4 KB, free: 366.2 MB)
26/06/26 13:26:16 INFO SparkContext: Created broadcast 9 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:16 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 6 (MapPartitionsRDD[35] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:16 INFO TaskSchedulerImpl: Adding task set 6.0 with 2 tasks
26/06/26 13:26:16 INFO TaskSetManager: Starting task 0.0 in stage 6.0 (TID 6, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:16 INFO TaskSetManager: Starting task 1.0 in stage 6.0 (TID 7, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:16 INFO Executor: Running task 0.0 in stage 6.0 (TID 6)
26/06/26 13:26:16 INFO Executor: Running task 1.0 in stage 6.0 (TID 7)
26/06/26 13:26:16 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:0+11314
26/06/26 13:26:16 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:11314+11314
26/06/26 13:26:16 INFO PythonRunner: Times: total = 24, boot = 6, init = 9, finish = 9
26/06/26 13:26:16 INFO PythonRunner: Times: total = 30, boot = 3, init = 8, finish = 19
26/06/26 13:26:16 INFO Executor: Finished task 1.0 in stage 6.0 (TID 7). 2173 bytes result sent to driver
26/06/26 13:26:16 INFO Executor: Finished task 0.0 in stage 6.0 (TID 6). 2173 bytes result sent to driver
26/06/26 13:26:16 INFO TaskSetManager: Finished task 0.0 in stage 6.0 (TID 6) in 164 ms on localhost (executor driver) (1/2)
26/06/26 13:26:16 INFO TaskSetManager: Finished task 1.0 in stage 6.0 (TID 7) in 166 ms on localhost (executor driver) (2/2)
26/06/26 13:26:16 INFO TaskSchedulerImpl: Removed TaskSet 6.0, whose tasks have all completed, from pool 
26/06/26 13:26:16 INFO DAGScheduler: ShuffleMapStage 6 (count at NativeMethodAccessorImpl.java:0) finished in 0.201 s
26/06/26 13:26:16 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:16 INFO DAGScheduler: running: Set()
26/06/26 13:26:16 INFO DAGScheduler: waiting: Set(ResultStage 7)
26/06/26 13:26:16 INFO DAGScheduler: failed: Set()
26/06/26 13:26:16 INFO DAGScheduler: Submitting ResultStage 7 (MapPartitionsRDD[38] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:16 INFO MemoryStore: Block broadcast_10 stored as values in memory (estimated size 7.3 KB, free 365.0 MB)
26/06/26 13:26:16 INFO MemoryStore: Block broadcast_10_piece0 stored as bytes in memory (estimated size 3.8 KB, free 365.0 MB)
26/06/26 13:26:16 INFO BlockManagerInfo: Added broadcast_10_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:16 INFO SparkContext: Created broadcast 10 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:16 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 7 (MapPartitionsRDD[38] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:16 INFO TaskSchedulerImpl: Adding task set 7.0 with 1 tasks
26/06/26 13:26:16 INFO TaskSetManager: Starting task 0.0 in stage 7.0 (TID 8, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:16 INFO Executor: Running task 0.0 in stage 7.0 (TID 8)
26/06/26 13:26:16 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:16 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 33 ms
26/06/26 13:26:16 INFO Executor: Finished task 0.0 in stage 7.0 (TID 8). 1825 bytes result sent to driver
26/06/26 13:26:16 INFO TaskSetManager: Finished task 0.0 in stage 7.0 (TID 8) in 165 ms on localhost (executor driver) (1/1)
26/06/26 13:26:16 INFO TaskSchedulerImpl: Removed TaskSet 7.0, whose tasks have all completed, from pool 
26/06/26 13:26:16 INFO DAGScheduler: ResultStage 7 (count at NativeMethodAccessorImpl.java:0) finished in 0.181 s
26/06/26 13:26:16 INFO DAGScheduler: Job 6 finished: count at NativeMethodAccessorImpl.java:0, took 0.440529 s
('Users :', 943)
26/06/26 13:26:16 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:16 INFO DAGScheduler: Registering RDD 41 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:16 INFO DAGScheduler: Got job 7 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:16 INFO DAGScheduler: Final stage: ResultStage 9 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:16 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 8)
26/06/26 13:26:16 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 8)
26/06/26 13:26:16 INFO DAGScheduler: Submitting ShuffleMapStage 8 (MapPartitionsRDD[41] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:17 INFO MemoryStore: Block broadcast_11 stored as values in memory (estimated size 22.7 KB, free 365.0 MB)
26/06/26 13:26:17 INFO MemoryStore: Block broadcast_11_piece0 stored as bytes in memory (estimated size 12.2 KB, free 364.9 MB)
26/06/26 13:26:17 INFO BlockManagerInfo: Added broadcast_11_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 12.2 KB, free: 366.1 MB)
26/06/26 13:26:17 INFO SparkContext: Created broadcast 11 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:17 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 8 (MapPartitionsRDD[41] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:17 INFO TaskSchedulerImpl: Adding task set 8.0 with 2 tasks
26/06/26 13:26:17 INFO TaskSetManager: Starting task 0.0 in stage 8.0 (TID 9, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:17 INFO TaskSetManager: Starting task 1.0 in stage 8.0 (TID 10, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:17 INFO Executor: Running task 0.0 in stage 8.0 (TID 9)
26/06/26 13:26:17 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:0+989586
26/06/26 13:26:17 INFO Executor: Running task 1.0 in stage 8.0 (TID 10)
26/06/26 13:26:17 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:989586+989587
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 204
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 217
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 136
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 151
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 182
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 99
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 113
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 159
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 210
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 221
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 76
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 78
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 127
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 218
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 119
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 148
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 206
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 79
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 169
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 149
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 211
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 144
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 82
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 84
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 96
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 178
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 94
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 110
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 202
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 163
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 81
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 118
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 209
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 130
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 89
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 123
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 133
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 216
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 187
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 158
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 222
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 156
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 90
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 208
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 85
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 168
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 147
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 126
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 92
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 87
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 220
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 104
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 170
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 196
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 195
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 111
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 129
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 140
26/06/26 13:26:17 INFO BlockManagerInfo: Removed broadcast_6_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 11.9 KB, free: 366.1 MB)
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 105
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 153
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 80
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 207
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 107
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 203
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 112
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 93
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 165
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 193
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 86
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 101
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 171
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 180
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 125
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 213
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 88
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 115
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 141
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 181
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 145
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 197
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 77
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 173
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 186
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 175
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 95
26/06/26 13:26:17 INFO BlockManagerInfo: Removed broadcast_8_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 18.4 KB, free: 366.2 MB)
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 137
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 146
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 142
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 161
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 194
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 155
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 166
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 106
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 121
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 184
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 135
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 132
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 122
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 138
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 189
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 128
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 134
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 97
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 120
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 143
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 164
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 131
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 174
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 177
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 124
26/06/26 13:26:17 INFO ContextCleaner: Cleaned shuffle 0
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 199
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 200
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 116
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 91
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 192
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 83
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 179
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 176
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 160
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 108
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 201
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 219
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 191
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 167
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 190
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 150
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 109
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 152
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 172
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 103
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 162
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 117
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 212
26/06/26 13:26:17 INFO BlockManagerInfo: Removed broadcast_7_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 11.7 KB, free: 366.2 MB)
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 185
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 98
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 188
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 100
26/06/26 13:26:17 INFO BlockManagerInfo: Removed broadcast_10_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.2 MB)
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 102
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 183
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 139
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 154
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 157
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 205
26/06/26 13:26:17 INFO BlockManagerInfo: Removed broadcast_9_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 12.4 KB, free: 366.2 MB)
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 114
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 198
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 214
26/06/26 13:26:17 INFO ContextCleaner: Cleaned accumulator 215
26/06/26 13:26:18 INFO PythonRunner: Times: total = 978, boot = -497, init = 536, finish = 939
26/06/26 13:26:18 INFO Executor: Finished task 0.0 in stage 8.0 (TID 9). 2173 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 0.0 in stage 8.0 (TID 9) in 1076 ms on localhost (executor driver) (1/2)
26/06/26 13:26:18 INFO PythonRunner: Times: total = 1056, boot = -470, init = 527, finish = 999
26/06/26 13:26:18 INFO Executor: Finished task 1.0 in stage 8.0 (TID 10). 2216 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 1.0 in stage 8.0 (TID 10) in 1109 ms on localhost (executor driver) (2/2)
26/06/26 13:26:18 INFO TaskSchedulerImpl: Removed TaskSet 8.0, whose tasks have all completed, from pool 
26/06/26 13:26:18 INFO DAGScheduler: ShuffleMapStage 8 (count at NativeMethodAccessorImpl.java:0) finished in 1.162 s
26/06/26 13:26:18 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:18 INFO DAGScheduler: running: Set()
26/06/26 13:26:18 INFO DAGScheduler: waiting: Set(ResultStage 9)
26/06/26 13:26:18 INFO DAGScheduler: failed: Set()
26/06/26 13:26:18 INFO DAGScheduler: Submitting ResultStage 9 (MapPartitionsRDD[44] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_12 stored as values in memory (estimated size 7.3 KB, free 365.1 MB)
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_12_piece0 stored as bytes in memory (estimated size 3.8 KB, free 365.1 MB)
26/06/26 13:26:18 INFO BlockManagerInfo: Added broadcast_12_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.2 MB)
26/06/26 13:26:18 INFO SparkContext: Created broadcast 12 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:18 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 9 (MapPartitionsRDD[44] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:18 INFO TaskSchedulerImpl: Adding task set 9.0 with 1 tasks
26/06/26 13:26:18 INFO TaskSetManager: Starting task 0.0 in stage 9.0 (TID 11, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:18 INFO Executor: Running task 0.0 in stage 9.0 (TID 11)
26/06/26 13:26:18 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:18 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:18 INFO Executor: Finished task 0.0 in stage 9.0 (TID 11). 1782 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 0.0 in stage 9.0 (TID 11) in 35 ms on localhost (executor driver) (1/1)
26/06/26 13:26:18 INFO TaskSchedulerImpl: Removed TaskSet 9.0, whose tasks have all completed, from pool 
26/06/26 13:26:18 INFO DAGScheduler: ResultStage 9 (count at NativeMethodAccessorImpl.java:0) finished in 0.083 s
26/06/26 13:26:18 INFO DAGScheduler: Job 7 finished: count at NativeMethodAccessorImpl.java:0, took 1.286447 s
('Ratings :', 100000)
26/06/26 13:26:18 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:18 INFO DAGScheduler: Registering RDD 47 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:18 INFO DAGScheduler: Got job 8 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:18 INFO DAGScheduler: Final stage: ResultStage 11 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:18 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 10)
26/06/26 13:26:18 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 10)
26/06/26 13:26:18 INFO DAGScheduler: Submitting ShuffleMapStage 10 (MapPartitionsRDD[47] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_13 stored as values in memory (estimated size 32.8 KB, free 365.1 MB)
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_13_piece0 stored as bytes in memory (estimated size 17.0 KB, free 365.1 MB)
26/06/26 13:26:18 INFO BlockManagerInfo: Added broadcast_13_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 17.0 KB, free: 366.2 MB)
26/06/26 13:26:18 INFO SparkContext: Created broadcast 13 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:18 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 10 (MapPartitionsRDD[47] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:18 INFO TaskSchedulerImpl: Adding task set 10.0 with 2 tasks
26/06/26 13:26:18 INFO TaskSetManager: Starting task 0.0 in stage 10.0 (TID 12, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:18 INFO TaskSetManager: Starting task 1.0 in stage 10.0 (TID 13, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:18 INFO Executor: Running task 0.0 in stage 10.0 (TID 12)
26/06/26 13:26:18 INFO Executor: Running task 1.0 in stage 10.0 (TID 13)
26/06/26 13:26:18 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:118172+118172
26/06/26 13:26:18 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:0+118172
26/06/26 13:26:18 INFO PythonRunner: Times: total = 64, boot = -407, init = 410, finish = 61
26/06/26 13:26:18 INFO Executor: Finished task 0.0 in stage 10.0 (TID 12). 2173 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 0.0 in stage 10.0 (TID 12) in 191 ms on localhost (executor driver) (1/2)
26/06/26 13:26:18 INFO PythonRunner: Times: total = 156, boot = -322, init = 411, finish = 67
26/06/26 13:26:18 INFO Executor: Finished task 1.0 in stage 10.0 (TID 13). 2130 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 1.0 in stage 10.0 (TID 13) in 238 ms on localhost (executor driver) (2/2)
26/06/26 13:26:18 INFO TaskSchedulerImpl: Removed TaskSet 10.0, whose tasks have all completed, from pool 
26/06/26 13:26:18 INFO DAGScheduler: ShuffleMapStage 10 (count at NativeMethodAccessorImpl.java:0) finished in 0.264 s
26/06/26 13:26:18 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:18 INFO DAGScheduler: running: Set()
26/06/26 13:26:18 INFO DAGScheduler: waiting: Set(ResultStage 11)
26/06/26 13:26:18 INFO DAGScheduler: failed: Set()
26/06/26 13:26:18 INFO DAGScheduler: Submitting ResultStage 11 (MapPartitionsRDD[50] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_14 stored as values in memory (estimated size 7.3 KB, free 365.0 MB)
26/06/26 13:26:18 INFO MemoryStore: Block broadcast_14_piece0 stored as bytes in memory (estimated size 3.8 KB, free 365.0 MB)
26/06/26 13:26:18 INFO BlockManagerInfo: Added broadcast_14_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.2 MB)
26/06/26 13:26:18 INFO SparkContext: Created broadcast 14 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:18 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 11 (MapPartitionsRDD[50] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:18 INFO TaskSchedulerImpl: Adding task set 11.0 with 1 tasks
26/06/26 13:26:18 INFO TaskSetManager: Starting task 0.0 in stage 11.0 (TID 14, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:18 INFO Executor: Running task 0.0 in stage 11.0 (TID 14)
26/06/26 13:26:18 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:18 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:18 INFO Executor: Finished task 0.0 in stage 11.0 (TID 14). 1825 bytes result sent to driver
26/06/26 13:26:18 INFO TaskSetManager: Finished task 0.0 in stage 11.0 (TID 14) in 56 ms on localhost (executor driver) (1/1)
26/06/26 13:26:18 INFO TaskSchedulerImpl: Removed TaskSet 11.0, whose tasks have all completed, from pool 
26/06/26 13:26:18 INFO DAGScheduler: ResultStage 11 (count at NativeMethodAccessorImpl.java:0) finished in 0.076 s
26/06/26 13:26:18 INFO DAGScheduler: Job 8 finished: count at NativeMethodAccessorImpl.java:0, took 0.364856 s
('Movies :', 1682)

After Removing Duplicates
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 23.753821 ms
26/06/26 13:26:19 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 22.316358 ms
26/06/26 13:26:19 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 14.007738 ms
26/06/26 13:26:19 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:19 INFO DAGScheduler: Registering RDD 53 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:19 INFO DAGScheduler: Registering RDD 56 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:19 INFO DAGScheduler: Got job 9 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:19 INFO DAGScheduler: Final stage: ResultStage 14 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:19 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 13)
26/06/26 13:26:19 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 13)
26/06/26 13:26:19 INFO DAGScheduler: Submitting ShuffleMapStage 12 (MapPartitionsRDD[53] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:19 INFO MemoryStore: Block broadcast_15 stored as values in memory (estimated size 28.3 KB, free 365.0 MB)
26/06/26 13:26:19 INFO MemoryStore: Block broadcast_15_piece0 stored as bytes in memory (estimated size 14.3 KB, free 365.0 MB)
26/06/26 13:26:19 INFO BlockManagerInfo: Added broadcast_15_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 14.3 KB, free: 366.2 MB)
26/06/26 13:26:19 INFO SparkContext: Created broadcast 15 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:19 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 12 (MapPartitionsRDD[53] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:19 INFO TaskSchedulerImpl: Adding task set 12.0 with 2 tasks
26/06/26 13:26:19 INFO TaskSetManager: Starting task 0.0 in stage 12.0 (TID 15, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:19 INFO TaskSetManager: Starting task 1.0 in stage 12.0 (TID 16, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:19 INFO Executor: Running task 1.0 in stage 12.0 (TID 16)
26/06/26 13:26:19 INFO Executor: Running task 0.0 in stage 12.0 (TID 15)
26/06/26 13:26:19 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:0+11314
26/06/26 13:26:19 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:11314+11314
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 5.354632 ms
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 6.764475 ms
26/06/26 13:26:19 INFO CodeGenerator: Code generated in 139.496769 ms
26/06/26 13:26:19 INFO PythonRunner: Times: total = 95, boot = -672, init = 734, finish = 33
26/06/26 13:26:19 INFO PythonRunner: Times: total = 125, boot = -567, init = 662, finish = 30
26/06/26 13:26:20 INFO Executor: Finished task 1.0 in stage 12.0 (TID 16). 2655 bytes result sent to driver
26/06/26 13:26:20 INFO TaskSetManager: Finished task 1.0 in stage 12.0 (TID 16) in 1065 ms on localhost (executor driver) (1/2)
26/06/26 13:26:20 INFO Executor: Finished task 0.0 in stage 12.0 (TID 15). 2655 bytes result sent to driver
26/06/26 13:26:20 INFO TaskSetManager: Finished task 0.0 in stage 12.0 (TID 15) in 1202 ms on localhost (executor driver) (2/2)
26/06/26 13:26:20 INFO TaskSchedulerImpl: Removed TaskSet 12.0, whose tasks have all completed, from pool 
26/06/26 13:26:20 INFO DAGScheduler: ShuffleMapStage 12 (count at NativeMethodAccessorImpl.java:0) finished in 1.232 s
26/06/26 13:26:20 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:20 INFO DAGScheduler: running: Set()
26/06/26 13:26:20 INFO DAGScheduler: waiting: Set(ShuffleMapStage 13, ResultStage 14)
26/06/26 13:26:20 INFO DAGScheduler: failed: Set()
26/06/26 13:26:20 INFO DAGScheduler: Submitting ShuffleMapStage 13 (MapPartitionsRDD[56] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:20 INFO MemoryStore: Block broadcast_16 stored as values in memory (estimated size 33.0 KB, free 365.0 MB)
26/06/26 13:26:20 INFO MemoryStore: Block broadcast_16_piece0 stored as bytes in memory (estimated size 17.0 KB, free 365.0 MB)
26/06/26 13:26:20 INFO BlockManagerInfo: Added broadcast_16_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 17.0 KB, free: 366.1 MB)
26/06/26 13:26:20 INFO SparkContext: Created broadcast 16 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:20 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 13 (MapPartitionsRDD[56] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:20 INFO TaskSchedulerImpl: Adding task set 13.0 with 200 tasks
26/06/26 13:26:20 INFO TaskSetManager: Starting task 92.0 in stage 13.0 (TID 17, localhost, executor driver, partition 92, PROCESS_LOCAL, 7743 bytes)
26/06/26 13:26:20 INFO TaskSetManager: Starting task 180.0 in stage 13.0 (TID 18, localhost, executor driver, partition 180, PROCESS_LOCAL, 7743 bytes)
26/06/26 13:26:20 INFO TaskSetManager: Starting task 0.0 in stage 13.0 (TID 19, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:20 INFO TaskSetManager: Starting task 1.0 in stage 13.0 (TID 20, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:20 INFO Executor: Running task 180.0 in stage 13.0 (TID 18)
26/06/26 13:26:20 INFO Executor: Running task 92.0 in stage 13.0 (TID 17)
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 0 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 0 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:20 INFO Executor: Running task 0.0 in stage 13.0 (TID 19)
26/06/26 13:26:20 INFO Executor: Finished task 180.0 in stage 13.0 (TID 18). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:20 INFO Executor: Finished task 92.0 in stage 13.0 (TID 17). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO TaskSetManager: Starting task 2.0 in stage 13.0 (TID 21, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:20 INFO TaskSetManager: Starting task 3.0 in stage 13.0 (TID 22, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:20 INFO TaskSetManager: Finished task 180.0 in stage 13.0 (TID 18) in 38 ms on localhost (executor driver) (1/200)
26/06/26 13:26:20 INFO TaskSetManager: Finished task 92.0 in stage 13.0 (TID 17) in 39 ms on localhost (executor driver) (2/200)
26/06/26 13:26:20 INFO Executor: Running task 1.0 in stage 13.0 (TID 20)
26/06/26 13:26:20 INFO Executor: Running task 2.0 in stage 13.0 (TID 21)
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:20 INFO Executor: Running task 3.0 in stage 13.0 (TID 22)
26/06/26 13:26:20 INFO Executor: Finished task 0.0 in stage 13.0 (TID 19). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO Executor: Finished task 1.0 in stage 13.0 (TID 20). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO TaskSetManager: Starting task 4.0 in stage 13.0 (TID 23, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:20 INFO Executor: Running task 4.0 in stage 13.0 (TID 23)
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:20 INFO TaskSetManager: Starting task 5.0 in stage 13.0 (TID 24, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:20 INFO Executor: Running task 5.0 in stage 13.0 (TID 24)
26/06/26 13:26:20 INFO TaskSetManager: Finished task 0.0 in stage 13.0 (TID 19) in 82 ms on localhost (executor driver) (3/200)
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 31 ms
26/06/26 13:26:20 INFO Executor: Finished task 2.0 in stage 13.0 (TID 21). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO Executor: Finished task 3.0 in stage 13.0 (TID 22). 3629 bytes result sent to driver
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:20 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:20 INFO Executor: Finished task 5.0 in stage 13.0 (TID 24). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 4.0 in stage 13.0 (TID 23). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 6.0 in stage 13.0 (TID 25, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 7.0 in stage 13.0 (TID 26, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 8.0 in stage 13.0 (TID 27, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 9.0 in stage 13.0 (TID 28, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 1.0 in stage 13.0 (TID 20) in 541 ms on localhost (executor driver) (4/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 3.0 in stage 13.0 (TID 22) in 509 ms on localhost (executor driver) (5/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 5.0 in stage 13.0 (TID 24) in 470 ms on localhost (executor driver) (6/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 4.0 in stage 13.0 (TID 23) in 471 ms on localhost (executor driver) (7/200)
26/06/26 13:26:21 INFO Executor: Running task 9.0 in stage 13.0 (TID 28)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 8.0 in stage 13.0 (TID 27)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 6.0 in stage 13.0 (TID 25)
26/06/26 13:26:21 INFO Executor: Running task 7.0 in stage 13.0 (TID 26)
26/06/26 13:26:21 INFO Executor: Finished task 9.0 in stage 13.0 (TID 28). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 10.0 in stage 13.0 (TID 29, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 2.0 in stage 13.0 (TID 21) in 540 ms on localhost (executor driver) (8/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 9.0 in stage 13.0 (TID 28) in 33 ms on localhost (executor driver) (9/200)
26/06/26 13:26:21 INFO Executor: Running task 10.0 in stage 13.0 (TID 29)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 10.0 in stage 13.0 (TID 29). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 11.0 in stage 13.0 (TID 30, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 10.0 in stage 13.0 (TID 29) in 18 ms on localhost (executor driver) (10/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 7.0 in stage 13.0 (TID 26). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Starting task 12.0 in stage 13.0 (TID 31, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 7.0 in stage 13.0 (TID 26) in 70 ms on localhost (executor driver) (11/200)
26/06/26 13:26:21 INFO Executor: Running task 12.0 in stage 13.0 (TID 31)
26/06/26 13:26:21 INFO Executor: Finished task 6.0 in stage 13.0 (TID 25). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 13.0 in stage 13.0 (TID 32, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 13.0 in stage 13.0 (TID 32)
26/06/26 13:26:21 INFO Executor: Running task 11.0 in stage 13.0 (TID 30)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 11.0 in stage 13.0 (TID 30). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 8.0 in stage 13.0 (TID 27). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Finished task 6.0 in stage 13.0 (TID 25) in 522 ms on localhost (executor driver) (12/200)
26/06/26 13:26:21 INFO Executor: Finished task 13.0 in stage 13.0 (TID 32). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Finished task 11.0 in stage 13.0 (TID 30) in 72 ms on localhost (executor driver) (13/200)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 14.0 in stage 13.0 (TID 33, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 15.0 in stage 13.0 (TID 34, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 14.0 in stage 13.0 (TID 33)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 16.0 in stage 13.0 (TID 35, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 8.0 in stage 13.0 (TID 27) in 124 ms on localhost (executor driver) (14/200)
26/06/26 13:26:21 INFO Executor: Running task 15.0 in stage 13.0 (TID 34)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 13.0 in stage 13.0 (TID 32) in 51 ms on localhost (executor driver) (15/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 16.0 in stage 13.0 (TID 35)
26/06/26 13:26:21 INFO Executor: Finished task 14.0 in stage 13.0 (TID 33). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 17.0 in stage 13.0 (TID 36, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 17.0 in stage 13.0 (TID 36)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 14.0 in stage 13.0 (TID 33) in 34 ms on localhost (executor driver) (16/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 16.0 in stage 13.0 (TID 35). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 18.0 in stage 13.0 (TID 37, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 16.0 in stage 13.0 (TID 35) in 43 ms on localhost (executor driver) (17/200)
26/06/26 13:26:21 INFO Executor: Running task 18.0 in stage 13.0 (TID 37)
26/06/26 13:26:21 INFO Executor: Finished task 12.0 in stage 13.0 (TID 31). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 17.0 in stage 13.0 (TID 36). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 15.0 in stage 13.0 (TID 34). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 19.0 in stage 13.0 (TID 38, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 20.0 in stage 13.0 (TID 39, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 21.0 in stage 13.0 (TID 40, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 12.0 in stage 13.0 (TID 31) in 133 ms on localhost (executor driver) (18/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 17.0 in stage 13.0 (TID 36) in 61 ms on localhost (executor driver) (19/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 15.0 in stage 13.0 (TID 34) in 80 ms on localhost (executor driver) (20/200)
26/06/26 13:26:21 INFO Executor: Finished task 18.0 in stage 13.0 (TID 37). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 22.0 in stage 13.0 (TID 41, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 19.0 in stage 13.0 (TID 38)
26/06/26 13:26:21 INFO Executor: Running task 20.0 in stage 13.0 (TID 39)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 19.0 in stage 13.0 (TID 38). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Finished task 18.0 in stage 13.0 (TID 37) in 58 ms on localhost (executor driver) (21/200)
26/06/26 13:26:21 INFO Executor: Running task 22.0 in stage 13.0 (TID 41)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 23.0 in stage 13.0 (TID 42, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Running task 21.0 in stage 13.0 (TID 40)
26/06/26 13:26:21 INFO Executor: Finished task 20.0 in stage 13.0 (TID 39). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 24.0 in stage 13.0 (TID 43, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 23.0 in stage 13.0 (TID 42)
26/06/26 13:26:21 INFO Executor: Running task 24.0 in stage 13.0 (TID 43)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Finished task 20.0 in stage 13.0 (TID 39) in 100 ms on localhost (executor driver) (22/200)
26/06/26 13:26:21 INFO Executor: Finished task 23.0 in stage 13.0 (TID 42). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 25.0 in stage 13.0 (TID 44, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Finished task 24.0 in stage 13.0 (TID 43). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Starting task 26.0 in stage 13.0 (TID 45, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 26.0 in stage 13.0 (TID 45)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 23.0 in stage 13.0 (TID 42) in 87 ms on localhost (executor driver) (23/200)
26/06/26 13:26:21 INFO Executor: Finished task 21.0 in stage 13.0 (TID 40). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Finished task 24.0 in stage 13.0 (TID 43) in 77 ms on localhost (executor driver) (24/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 19.0 in stage 13.0 (TID 38) in 147 ms on localhost (executor driver) (25/200)
26/06/26 13:26:21 INFO Executor: Finished task 22.0 in stage 13.0 (TID 41). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 26.0 in stage 13.0 (TID 45). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 27.0 in stage 13.0 (TID 46, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 28.0 in stage 13.0 (TID 47, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 29.0 in stage 13.0 (TID 48, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 25.0 in stage 13.0 (TID 44)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 25.0 in stage 13.0 (TID 44). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 28.0 in stage 13.0 (TID 47)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO Executor: Running task 29.0 in stage 13.0 (TID 48)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 30.0 in stage 13.0 (TID 49, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 25.0 in stage 13.0 (TID 44) in 86 ms on localhost (executor driver) (26/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 26.0 in stage 13.0 (TID 45) in 84 ms on localhost (executor driver) (27/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 22.0 in stage 13.0 (TID 41) in 184 ms on localhost (executor driver) (28/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 21.0 in stage 13.0 (TID 40) in 191 ms on localhost (executor driver) (29/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 27.0 in stage 13.0 (TID 46)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 32 ms
26/06/26 13:26:21 INFO Executor: Finished task 27.0 in stage 13.0 (TID 46). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 28.0 in stage 13.0 (TID 47). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 30.0 in stage 13.0 (TID 49)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 30.0 in stage 13.0 (TID 49). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 29.0 in stage 13.0 (TID 48). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 31.0 in stage 13.0 (TID 50, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 32.0 in stage 13.0 (TID 51, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 33.0 in stage 13.0 (TID 52, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 34.0 in stage 13.0 (TID 53, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 31.0 in stage 13.0 (TID 50)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 31.0 in stage 13.0 (TID 50). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 33.0 in stage 13.0 (TID 52)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 33.0 in stage 13.0 (TID 52). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 34.0 in stage 13.0 (TID 53)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 34.0 in stage 13.0 (TID 53). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 32.0 in stage 13.0 (TID 51)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 32.0 in stage 13.0 (TID 51). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 35.0 in stage 13.0 (TID 54, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 36.0 in stage 13.0 (TID 55, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 37.0 in stage 13.0 (TID 56, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 38.0 in stage 13.0 (TID 57, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 36.0 in stage 13.0 (TID 55)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 27.0 in stage 13.0 (TID 46) in 251 ms on localhost (executor driver) (30/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 28.0 in stage 13.0 (TID 47) in 229 ms on localhost (executor driver) (31/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 30.0 in stage 13.0 (TID 49) in 190 ms on localhost (executor driver) (32/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 29.0 in stage 13.0 (TID 48) in 228 ms on localhost (executor driver) (33/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 31.0 in stage 13.0 (TID 50) in 72 ms on localhost (executor driver) (34/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 33.0 in stage 13.0 (TID 52) in 72 ms on localhost (executor driver) (35/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 34.0 in stage 13.0 (TID 53) in 72 ms on localhost (executor driver) (36/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 32.0 in stage 13.0 (TID 51) in 73 ms on localhost (executor driver) (37/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 38.0 in stage 13.0 (TID 57)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Running task 37.0 in stage 13.0 (TID 56)
26/06/26 13:26:21 INFO Executor: Finished task 36.0 in stage 13.0 (TID 55). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Running task 35.0 in stage 13.0 (TID 54)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 39.0 in stage 13.0 (TID 58, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 36.0 in stage 13.0 (TID 55) in 40 ms on localhost (executor driver) (38/200)
26/06/26 13:26:21 INFO Executor: Running task 39.0 in stage 13.0 (TID 58)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 38.0 in stage 13.0 (TID 57). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 35.0 in stage 13.0 (TID 54). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 37.0 in stage 13.0 (TID 56). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 40.0 in stage 13.0 (TID 59, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 41.0 in stage 13.0 (TID 60, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 42.0 in stage 13.0 (TID 61, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 37.0 in stage 13.0 (TID 56) in 95 ms on localhost (executor driver) (39/200)
26/06/26 13:26:21 INFO Executor: Running task 40.0 in stage 13.0 (TID 59)
26/06/26 13:26:21 INFO Executor: Running task 42.0 in stage 13.0 (TID 61)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO TaskSetManager: Finished task 38.0 in stage 13.0 (TID 57) in 99 ms on localhost (executor driver) (40/200)
26/06/26 13:26:21 INFO Executor: Finished task 40.0 in stage 13.0 (TID 59). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 41.0 in stage 13.0 (TID 60)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 35.0 in stage 13.0 (TID 54) in 108 ms on localhost (executor driver) (41/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Starting task 43.0 in stage 13.0 (TID 62, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 40.0 in stage 13.0 (TID 59) in 30 ms on localhost (executor driver) (42/200)
26/06/26 13:26:21 INFO Executor: Running task 43.0 in stage 13.0 (TID 62)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 41.0 in stage 13.0 (TID 60). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 44.0 in stage 13.0 (TID 63, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 41.0 in stage 13.0 (TID 60) in 77 ms on localhost (executor driver) (43/200)
26/06/26 13:26:21 INFO Executor: Finished task 39.0 in stage 13.0 (TID 58). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 45.0 in stage 13.0 (TID 64, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 44.0 in stage 13.0 (TID 63)
26/06/26 13:26:21 INFO Executor: Finished task 42.0 in stage 13.0 (TID 61). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 43.0 in stage 13.0 (TID 62). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:21 INFO Executor: Finished task 44.0 in stage 13.0 (TID 63). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 46.0 in stage 13.0 (TID 65, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 47.0 in stage 13.0 (TID 66, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 48.0 in stage 13.0 (TID 67, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 47.0 in stage 13.0 (TID 66)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 39.0 in stage 13.0 (TID 58) in 184 ms on localhost (executor driver) (44/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 44.0 in stage 13.0 (TID 63) in 77 ms on localhost (executor driver) (45/200)
26/06/26 13:26:21 INFO Executor: Running task 48.0 in stage 13.0 (TID 67)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 43.0 in stage 13.0 (TID 62) in 107 ms on localhost (executor driver) (46/200)
26/06/26 13:26:21 INFO Executor: Running task 45.0 in stage 13.0 (TID 64)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO TaskSetManager: Finished task 42.0 in stage 13.0 (TID 61) in 140 ms on localhost (executor driver) (47/200)
26/06/26 13:26:21 INFO Executor: Finished task 47.0 in stage 13.0 (TID 66). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Running task 46.0 in stage 13.0 (TID 65)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 49.0 in stage 13.0 (TID 68, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 47.0 in stage 13.0 (TID 66) in 18 ms on localhost (executor driver) (48/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 4 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:21 INFO Executor: Finished task 46.0 in stage 13.0 (TID 65). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO Executor: Finished task 48.0 in stage 13.0 (TID 67). 3672 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 50.0 in stage 13.0 (TID 69, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Starting task 51.0 in stage 13.0 (TID 70, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 46.0 in stage 13.0 (TID 65) in 59 ms on localhost (executor driver) (49/200)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 48.0 in stage 13.0 (TID 67) in 54 ms on localhost (executor driver) (50/200)
26/06/26 13:26:21 INFO Executor: Running task 49.0 in stage 13.0 (TID 68)
26/06/26 13:26:21 INFO Executor: Running task 50.0 in stage 13.0 (TID 69)
26/06/26 13:26:21 INFO Executor: Finished task 45.0 in stage 13.0 (TID 64). 3629 bytes result sent to driver
26/06/26 13:26:21 INFO TaskSetManager: Starting task 52.0 in stage 13.0 (TID 71, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:21 INFO Executor: Running task 52.0 in stage 13.0 (TID 71)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:21 INFO Executor: Running task 51.0 in stage 13.0 (TID 70)
26/06/26 13:26:21 INFO TaskSetManager: Finished task 45.0 in stage 13.0 (TID 64) in 114 ms on localhost (executor driver) (51/200)
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:21 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 333
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 325
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 264
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 323
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 296
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 345
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 305
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 269
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 281
26/06/26 13:26:22 INFO Executor: Finished task 50.0 in stage 13.0 (TID 69). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 53.0 in stage 13.0 (TID 72, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 50.0 in stage 13.0 (TID 69) in 356 ms on localhost (executor driver) (52/200)
26/06/26 13:26:22 INFO ContextCleaner: Cleaned shuffle 2
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 327
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 280
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 346
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 295
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 344
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 270
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 342
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 310
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 283
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 300
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 313
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 274
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 339
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 340
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 314
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 273
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 331
26/06/26 13:26:22 INFO Executor: Running task 53.0 in stage 13.0 (TID 72)
26/06/26 13:26:22 INFO BlockManagerInfo: Removed broadcast_12_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:22 INFO Executor: Finished task 52.0 in stage 13.0 (TID 71). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 54.0 in stage 13.0 (TID 73, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 54.0 in stage 13.0 (TID 73)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 52.0 in stage 13.0 (TID 71) in 350 ms on localhost (executor driver) (53/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 49.0 in stage 13.0 (TID 68). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 55.0 in stage 13.0 (TID 74, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 49.0 in stage 13.0 (TID 68) in 407 ms on localhost (executor driver) (54/200)
26/06/26 13:26:22 INFO Executor: Running task 55.0 in stage 13.0 (TID 74)
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 309
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 326
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 351
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 291
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 268
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 284
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 302
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 286
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 329
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 289
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 321
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 304
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 279
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 320
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 282
26/06/26 13:26:22 INFO BlockManagerInfo: Removed broadcast_14_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:22 INFO Executor: Finished task 54.0 in stage 13.0 (TID 73). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 56.0 in stage 13.0 (TID 75, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 53.0 in stage 13.0 (TID 72). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 56.0 in stage 13.0 (TID 75)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 54.0 in stage 13.0 (TID 73) in 20 ms on localhost (executor driver) (55/200)
26/06/26 13:26:22 INFO Executor: Finished task 51.0 in stage 13.0 (TID 70). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 57.0 in stage 13.0 (TID 76, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 58.0 in stage 13.0 (TID 77, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 55.0 in stage 13.0 (TID 74). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 58.0 in stage 13.0 (TID 77)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 53.0 in stage 13.0 (TID 72) in 41 ms on localhost (executor driver) (56/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 51.0 in stage 13.0 (TID 70) in 391 ms on localhost (executor driver) (57/200)
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 347
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 319
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 265
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 271
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 322
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 266
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 272
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 294
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 334
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 298
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 335
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 337
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 317
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 311
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 301
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 275
26/06/26 13:26:22 INFO TaskSetManager: Starting task 59.0 in stage 13.0 (TID 78, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:22 INFO BlockManagerInfo: Removed broadcast_15_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 14.3 KB, free: 366.2 MB)
26/06/26 13:26:22 INFO Executor: Running task 57.0 in stage 13.0 (TID 76)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 56.0 in stage 13.0 (TID 75). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 263
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 287
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 288
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 324
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 343
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 297
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 315
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 262
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 348
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 303
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 285
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 332
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 350
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 312
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 299
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 293
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 318
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 330
26/06/26 13:26:22 INFO Executor: Running task 59.0 in stage 13.0 (TID 78)
26/06/26 13:26:22 INFO BlockManagerInfo: Removed broadcast_13_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 17.0 KB, free: 366.2 MB)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 60.0 in stage 13.0 (TID 79, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 307
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 308
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 338
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 267
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 306
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 278
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 316
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 349
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 341
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 290
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 352
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 328
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 353
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 276
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 277
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 292
26/06/26 13:26:22 INFO ContextCleaner: Cleaned accumulator 336
26/06/26 13:26:22 INFO TaskSetManager: Finished task 56.0 in stage 13.0 (TID 75) in 38 ms on localhost (executor driver) (58/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 55.0 in stage 13.0 (TID 74) in 50 ms on localhost (executor driver) (59/200)
26/06/26 13:26:22 INFO Executor: Finished task 58.0 in stage 13.0 (TID 77). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 61.0 in stage 13.0 (TID 80, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 59.0 in stage 13.0 (TID 78). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 61.0 in stage 13.0 (TID 80)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 62.0 in stage 13.0 (TID 81, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 58.0 in stage 13.0 (TID 77) in 33 ms on localhost (executor driver) (60/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 59.0 in stage 13.0 (TID 78) in 30 ms on localhost (executor driver) (61/200)
26/06/26 13:26:22 INFO Executor: Finished task 57.0 in stage 13.0 (TID 76). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 63.0 in stage 13.0 (TID 82, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 57.0 in stage 13.0 (TID 76) in 39 ms on localhost (executor driver) (62/200)
26/06/26 13:26:22 INFO Executor: Running task 60.0 in stage 13.0 (TID 79)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 62.0 in stage 13.0 (TID 81)
26/06/26 13:26:22 INFO Executor: Running task 63.0 in stage 13.0 (TID 82)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 60.0 in stage 13.0 (TID 79). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 64.0 in stage 13.0 (TID 83, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 64.0 in stage 13.0 (TID 83)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 60.0 in stage 13.0 (TID 79) in 29 ms on localhost (executor driver) (63/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 61.0 in stage 13.0 (TID 80). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 63.0 in stage 13.0 (TID 82). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 62.0 in stage 13.0 (TID 81). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 65.0 in stage 13.0 (TID 84, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 66.0 in stage 13.0 (TID 85, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 64.0 in stage 13.0 (TID 83). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 67.0 in stage 13.0 (TID 86, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 68.0 in stage 13.0 (TID 87, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 65.0 in stage 13.0 (TID 84)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 61.0 in stage 13.0 (TID 80) in 50 ms on localhost (executor driver) (64/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 63.0 in stage 13.0 (TID 82) in 45 ms on localhost (executor driver) (65/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 62.0 in stage 13.0 (TID 81) in 50 ms on localhost (executor driver) (66/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 64.0 in stage 13.0 (TID 83) in 26 ms on localhost (executor driver) (67/200)
26/06/26 13:26:22 INFO Executor: Running task 68.0 in stage 13.0 (TID 87)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 67.0 in stage 13.0 (TID 86)
26/06/26 13:26:22 INFO Executor: Running task 66.0 in stage 13.0 (TID 85)
26/06/26 13:26:22 INFO Executor: Finished task 65.0 in stage 13.0 (TID 84). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 69.0 in stage 13.0 (TID 88, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 65.0 in stage 13.0 (TID 84) in 17 ms on localhost (executor driver) (68/200)
26/06/26 13:26:22 INFO Executor: Running task 69.0 in stage 13.0 (TID 88)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 68.0 in stage 13.0 (TID 87). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 70.0 in stage 13.0 (TID 89, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 68.0 in stage 13.0 (TID 87) in 30 ms on localhost (executor driver) (69/200)
26/06/26 13:26:22 INFO Executor: Running task 70.0 in stage 13.0 (TID 89)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 67.0 in stage 13.0 (TID 86). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 71.0 in stage 13.0 (TID 90, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 67.0 in stage 13.0 (TID 86) in 48 ms on localhost (executor driver) (70/200)
26/06/26 13:26:22 INFO Executor: Running task 71.0 in stage 13.0 (TID 90)
26/06/26 13:26:22 INFO Executor: Finished task 66.0 in stage 13.0 (TID 85). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 72.0 in stage 13.0 (TID 91, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 66.0 in stage 13.0 (TID 85) in 54 ms on localhost (executor driver) (71/200)
26/06/26 13:26:22 INFO Executor: Running task 72.0 in stage 13.0 (TID 91)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 70.0 in stage 13.0 (TID 89). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 69.0 in stage 13.0 (TID 88). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 73.0 in stage 13.0 (TID 92, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 74.0 in stage 13.0 (TID 93, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 74.0 in stage 13.0 (TID 93)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 69.0 in stage 13.0 (TID 88) in 51 ms on localhost (executor driver) (72/200)
26/06/26 13:26:22 INFO Executor: Running task 73.0 in stage 13.0 (TID 92)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 70.0 in stage 13.0 (TID 89) in 44 ms on localhost (executor driver) (73/200)
26/06/26 13:26:22 INFO Executor: Finished task 72.0 in stage 13.0 (TID 91). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 73.0 in stage 13.0 (TID 92). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 75.0 in stage 13.0 (TID 94, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 76.0 in stage 13.0 (TID 95, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 72.0 in stage 13.0 (TID 91) in 28 ms on localhost (executor driver) (74/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 73.0 in stage 13.0 (TID 92) in 18 ms on localhost (executor driver) (75/200)
26/06/26 13:26:22 INFO Executor: Running task 76.0 in stage 13.0 (TID 95)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 71.0 in stage 13.0 (TID 90). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 77.0 in stage 13.0 (TID 96, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 77.0 in stage 13.0 (TID 96)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 74.0 in stage 13.0 (TID 93). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 75.0 in stage 13.0 (TID 94)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 77.0 in stage 13.0 (TID 96). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 78.0 in stage 13.0 (TID 97, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 76.0 in stage 13.0 (TID 95). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 79.0 in stage 13.0 (TID 98, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 80.0 in stage 13.0 (TID 99, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 79.0 in stage 13.0 (TID 98)
26/06/26 13:26:22 INFO Executor: Running task 78.0 in stage 13.0 (TID 97)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO TaskSetManager: Finished task 71.0 in stage 13.0 (TID 90) in 70 ms on localhost (executor driver) (76/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 74.0 in stage 13.0 (TID 93) in 53 ms on localhost (executor driver) (77/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 77.0 in stage 13.0 (TID 96) in 22 ms on localhost (executor driver) (78/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 76.0 in stage 13.0 (TID 95) in 37 ms on localhost (executor driver) (79/200)
26/06/26 13:26:22 INFO Executor: Finished task 79.0 in stage 13.0 (TID 98). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 81.0 in stage 13.0 (TID 100, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 10 ms
26/06/26 13:26:22 INFO Executor: Finished task 75.0 in stage 13.0 (TID 94). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 80.0 in stage 13.0 (TID 99)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 82.0 in stage 13.0 (TID 101, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 75.0 in stage 13.0 (TID 94) in 51 ms on localhost (executor driver) (80/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 79.0 in stage 13.0 (TID 98) in 20 ms on localhost (executor driver) (81/200)
26/06/26 13:26:22 INFO Executor: Finished task 80.0 in stage 13.0 (TID 99). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 82.0 in stage 13.0 (TID 101)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 83.0 in stage 13.0 (TID 102, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 78.0 in stage 13.0 (TID 97). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 84.0 in stage 13.0 (TID 103, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 84.0 in stage 13.0 (TID 103)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 82.0 in stage 13.0 (TID 101). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Finished task 80.0 in stage 13.0 (TID 99) in 32 ms on localhost (executor driver) (82/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 78.0 in stage 13.0 (TID 97) in 33 ms on localhost (executor driver) (83/200)
26/06/26 13:26:22 INFO Executor: Running task 81.0 in stage 13.0 (TID 100)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 85.0 in stage 13.0 (TID 104, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 82.0 in stage 13.0 (TID 101) in 15 ms on localhost (executor driver) (84/200)
26/06/26 13:26:22 INFO Executor: Running task 83.0 in stage 13.0 (TID 102)
26/06/26 13:26:22 INFO Executor: Running task 85.0 in stage 13.0 (TID 104)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 84.0 in stage 13.0 (TID 103). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 86.0 in stage 13.0 (TID 105, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 86.0 in stage 13.0 (TID 105)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 84.0 in stage 13.0 (TID 103) in 24 ms on localhost (executor driver) (85/200)
26/06/26 13:26:22 INFO Executor: Finished task 83.0 in stage 13.0 (TID 102). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 87.0 in stage 13.0 (TID 106, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 83.0 in stage 13.0 (TID 102) in 26 ms on localhost (executor driver) (86/200)
26/06/26 13:26:22 INFO Executor: Finished task 86.0 in stage 13.0 (TID 105). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 88.0 in stage 13.0 (TID 107, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 88.0 in stage 13.0 (TID 107)
26/06/26 13:26:22 INFO Executor: Finished task 81.0 in stage 13.0 (TID 100). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 89.0 in stage 13.0 (TID 108, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 85.0 in stage 13.0 (TID 104). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 89.0 in stage 13.0 (TID 108)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 90.0 in stage 13.0 (TID 109, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 86.0 in stage 13.0 (TID 105) in 18 ms on localhost (executor driver) (87/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 81.0 in stage 13.0 (TID 100) in 46 ms on localhost (executor driver) (88/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 85.0 in stage 13.0 (TID 104) in 27 ms on localhost (executor driver) (89/200)
26/06/26 13:26:22 INFO Executor: Finished task 89.0 in stage 13.0 (TID 108). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 87.0 in stage 13.0 (TID 106)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 91.0 in stage 13.0 (TID 110, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 89.0 in stage 13.0 (TID 108) in 12 ms on localhost (executor driver) (90/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 87.0 in stage 13.0 (TID 106). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 90.0 in stage 13.0 (TID 109)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 93.0 in stage 13.0 (TID 111, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 88.0 in stage 13.0 (TID 107). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO TaskSetManager: Starting task 94.0 in stage 13.0 (TID 112, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 91.0 in stage 13.0 (TID 110)
26/06/26 13:26:22 INFO Executor: Running task 94.0 in stage 13.0 (TID 112)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO Executor: Running task 93.0 in stage 13.0 (TID 111)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 87.0 in stage 13.0 (TID 106) in 32 ms on localhost (executor driver) (91/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 88.0 in stage 13.0 (TID 107) in 31 ms on localhost (executor driver) (92/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 93.0 in stage 13.0 (TID 111). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 95.0 in stage 13.0 (TID 113, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 93.0 in stage 13.0 (TID 111) in 18 ms on localhost (executor driver) (93/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 25 ms
26/06/26 13:26:22 INFO Executor: Finished task 90.0 in stage 13.0 (TID 109). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 96.0 in stage 13.0 (TID 114, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 90.0 in stage 13.0 (TID 109) in 52 ms on localhost (executor driver) (94/200)
26/06/26 13:26:22 INFO Executor: Running task 96.0 in stage 13.0 (TID 114)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 91.0 in stage 13.0 (TID 110). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 94.0 in stage 13.0 (TID 112). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Finished task 91.0 in stage 13.0 (TID 110) in 53 ms on localhost (executor driver) (95/200)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 97.0 in stage 13.0 (TID 115, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 98.0 in stage 13.0 (TID 116, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 97.0 in stage 13.0 (TID 115)
26/06/26 13:26:22 INFO Executor: Finished task 96.0 in stage 13.0 (TID 114). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Running task 98.0 in stage 13.0 (TID 116)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 95.0 in stage 13.0 (TID 113)
26/06/26 13:26:22 INFO Executor: Finished task 98.0 in stage 13.0 (TID 116). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 99.0 in stage 13.0 (TID 117, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 100.0 in stage 13.0 (TID 118, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 99.0 in stage 13.0 (TID 117)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 96.0 in stage 13.0 (TID 114) in 46 ms on localhost (executor driver) (96/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 100.0 in stage 13.0 (TID 118)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 94.0 in stage 13.0 (TID 112) in 82 ms on localhost (executor driver) (97/200)
26/06/26 13:26:22 INFO Executor: Finished task 97.0 in stage 13.0 (TID 115). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Finished task 98.0 in stage 13.0 (TID 116) in 31 ms on localhost (executor driver) (98/200)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 101.0 in stage 13.0 (TID 119, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 101.0 in stage 13.0 (TID 119)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 95.0 in stage 13.0 (TID 113). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 102.0 in stage 13.0 (TID 120, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 99.0 in stage 13.0 (TID 117). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 103.0 in stage 13.0 (TID 121, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 103.0 in stage 13.0 (TID 121)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 97.0 in stage 13.0 (TID 115) in 49 ms on localhost (executor driver) (99/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 99.0 in stage 13.0 (TID 117) in 26 ms on localhost (executor driver) (100/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 95.0 in stage 13.0 (TID 113) in 87 ms on localhost (executor driver) (101/200)
26/06/26 13:26:22 INFO Executor: Finished task 100.0 in stage 13.0 (TID 118). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 103.0 in stage 13.0 (TID 121). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 104.0 in stage 13.0 (TID 122, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 105.0 in stage 13.0 (TID 123, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 100.0 in stage 13.0 (TID 118) in 33 ms on localhost (executor driver) (102/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 103.0 in stage 13.0 (TID 121) in 12 ms on localhost (executor driver) (103/200)
26/06/26 13:26:22 INFO Executor: Running task 105.0 in stage 13.0 (TID 123)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 102.0 in stage 13.0 (TID 120)
26/06/26 13:26:22 INFO Executor: Finished task 105.0 in stage 13.0 (TID 123). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 106.0 in stage 13.0 (TID 124, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 105.0 in stage 13.0 (TID 123) in 10 ms on localhost (executor driver) (104/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 101.0 in stage 13.0 (TID 119). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 107.0 in stage 13.0 (TID 125, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 107.0 in stage 13.0 (TID 125)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 106.0 in stage 13.0 (TID 124)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 101.0 in stage 13.0 (TID 119) in 45 ms on localhost (executor driver) (105/200)
26/06/26 13:26:22 INFO Executor: Running task 104.0 in stage 13.0 (TID 122)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 106.0 in stage 13.0 (TID 124). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 108.0 in stage 13.0 (TID 126, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 106.0 in stage 13.0 (TID 124) in 43 ms on localhost (executor driver) (106/200)
26/06/26 13:26:22 INFO Executor: Running task 108.0 in stage 13.0 (TID 126)
26/06/26 13:26:22 INFO Executor: Finished task 104.0 in stage 13.0 (TID 122). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 107.0 in stage 13.0 (TID 125). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 109.0 in stage 13.0 (TID 127, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 110.0 in stage 13.0 (TID 128, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 104.0 in stage 13.0 (TID 122) in 68 ms on localhost (executor driver) (107/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 107.0 in stage 13.0 (TID 125) in 51 ms on localhost (executor driver) (108/200)
26/06/26 13:26:22 INFO Executor: Running task 109.0 in stage 13.0 (TID 127)
26/06/26 13:26:22 INFO Executor: Finished task 102.0 in stage 13.0 (TID 120). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 111.0 in stage 13.0 (TID 129, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 110.0 in stage 13.0 (TID 128)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 102.0 in stage 13.0 (TID 120) in 84 ms on localhost (executor driver) (109/200)
26/06/26 13:26:22 INFO Executor: Running task 111.0 in stage 13.0 (TID 129)
26/06/26 13:26:22 INFO Executor: Finished task 108.0 in stage 13.0 (TID 126). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 112.0 in stage 13.0 (TID 130, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 108.0 in stage 13.0 (TID 126) in 39 ms on localhost (executor driver) (110/200)
26/06/26 13:26:22 INFO Executor: Running task 112.0 in stage 13.0 (TID 130)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 111.0 in stage 13.0 (TID 129). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 113.0 in stage 13.0 (TID 131, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 110.0 in stage 13.0 (TID 128). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 112.0 in stage 13.0 (TID 130). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 113.0 in stage 13.0 (TID 131)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 114.0 in stage 13.0 (TID 132, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 115.0 in stage 13.0 (TID 133, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 111.0 in stage 13.0 (TID 129) in 77 ms on localhost (executor driver) (111/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 110.0 in stage 13.0 (TID 128) in 82 ms on localhost (executor driver) (112/200)
26/06/26 13:26:22 INFO Executor: Running task 114.0 in stage 13.0 (TID 132)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 112.0 in stage 13.0 (TID 130) in 60 ms on localhost (executor driver) (113/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 113.0 in stage 13.0 (TID 131). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 116.0 in stage 13.0 (TID 134, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 113.0 in stage 13.0 (TID 131) in 30 ms on localhost (executor driver) (114/200)
26/06/26 13:26:22 INFO Executor: Finished task 114.0 in stage 13.0 (TID 132). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 116.0 in stage 13.0 (TID 134)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 117.0 in stage 13.0 (TID 135, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 114.0 in stage 13.0 (TID 132) in 24 ms on localhost (executor driver) (115/200)
26/06/26 13:26:22 INFO Executor: Finished task 116.0 in stage 13.0 (TID 134). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 117.0 in stage 13.0 (TID 135)
26/06/26 13:26:22 INFO Executor: Running task 115.0 in stage 13.0 (TID 133)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 118.0 in stage 13.0 (TID 136, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 116.0 in stage 13.0 (TID 134) in 26 ms on localhost (executor driver) (116/200)
26/06/26 13:26:22 INFO Executor: Running task 118.0 in stage 13.0 (TID 136)
26/06/26 13:26:22 INFO Executor: Finished task 109.0 in stage 13.0 (TID 127). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO TaskSetManager: Starting task 119.0 in stage 13.0 (TID 137, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 109.0 in stage 13.0 (TID 127) in 129 ms on localhost (executor driver) (117/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Running task 119.0 in stage 13.0 (TID 137)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 33 ms
26/06/26 13:26:22 INFO Executor: Finished task 118.0 in stage 13.0 (TID 136). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 120.0 in stage 13.0 (TID 138, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 115.0 in stage 13.0 (TID 133). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 121.0 in stage 13.0 (TID 139, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 118.0 in stage 13.0 (TID 136) in 53 ms on localhost (executor driver) (118/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 115.0 in stage 13.0 (TID 133) in 88 ms on localhost (executor driver) (119/200)
26/06/26 13:26:22 INFO Executor: Running task 120.0 in stage 13.0 (TID 138)
26/06/26 13:26:22 INFO Executor: Running task 121.0 in stage 13.0 (TID 139)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 117.0 in stage 13.0 (TID 135). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 122.0 in stage 13.0 (TID 140, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 122.0 in stage 13.0 (TID 140)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 117.0 in stage 13.0 (TID 135) in 86 ms on localhost (executor driver) (120/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 119.0 in stage 13.0 (TID 137). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 122.0 in stage 13.0 (TID 140). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 123.0 in stage 13.0 (TID 141, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 124.0 in stage 13.0 (TID 142, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 124.0 in stage 13.0 (TID 142)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 119.0 in stage 13.0 (TID 137) in 83 ms on localhost (executor driver) (121/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 122.0 in stage 13.0 (TID 140) in 28 ms on localhost (executor driver) (122/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 121.0 in stage 13.0 (TID 139). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 124.0 in stage 13.0 (TID 142). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 125.0 in stage 13.0 (TID 143, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 126.0 in stage 13.0 (TID 144, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 121.0 in stage 13.0 (TID 139) in 56 ms on localhost (executor driver) (123/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 124.0 in stage 13.0 (TID 142) in 19 ms on localhost (executor driver) (124/200)
26/06/26 13:26:22 INFO Executor: Running task 125.0 in stage 13.0 (TID 143)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 120.0 in stage 13.0 (TID 138). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 123.0 in stage 13.0 (TID 141)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 127.0 in stage 13.0 (TID 145, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 120.0 in stage 13.0 (TID 138) in 68 ms on localhost (executor driver) (125/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 125.0 in stage 13.0 (TID 143). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 128.0 in stage 13.0 (TID 146, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 127.0 in stage 13.0 (TID 145)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 125.0 in stage 13.0 (TID 143) in 20 ms on localhost (executor driver) (126/200)
26/06/26 13:26:22 INFO Executor: Running task 128.0 in stage 13.0 (TID 146)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Running task 126.0 in stage 13.0 (TID 144)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Finished task 127.0 in stage 13.0 (TID 145). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 129.0 in stage 13.0 (TID 147, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Finished task 126.0 in stage 13.0 (TID 144). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Finished task 123.0 in stage 13.0 (TID 141). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO Executor: Running task 129.0 in stage 13.0 (TID 147)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 127.0 in stage 13.0 (TID 145) in 27 ms on localhost (executor driver) (127/200)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 130.0 in stage 13.0 (TID 148, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:22 INFO TaskSetManager: Starting task 131.0 in stage 13.0 (TID 149, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO TaskSetManager: Finished task 126.0 in stage 13.0 (TID 144) in 40 ms on localhost (executor driver) (128/200)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 123.0 in stage 13.0 (TID 141) in 59 ms on localhost (executor driver) (129/200)
26/06/26 13:26:22 INFO Executor: Running task 131.0 in stage 13.0 (TID 149)
26/06/26 13:26:22 INFO Executor: Finished task 129.0 in stage 13.0 (TID 147). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 132.0 in stage 13.0 (TID 150, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 130.0 in stage 13.0 (TID 148)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 129.0 in stage 13.0 (TID 147) in 9 ms on localhost (executor driver) (130/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:22 INFO Executor: Running task 132.0 in stage 13.0 (TID 150)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO Executor: Finished task 131.0 in stage 13.0 (TID 149). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 133.0 in stage 13.0 (TID 151, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 133.0 in stage 13.0 (TID 151)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 131.0 in stage 13.0 (TID 149) in 27 ms on localhost (executor driver) (131/200)
26/06/26 13:26:22 INFO Executor: Finished task 130.0 in stage 13.0 (TID 148). 3629 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 134.0 in stage 13.0 (TID 152, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 134.0 in stage 13.0 (TID 152)
26/06/26 13:26:22 INFO Executor: Finished task 128.0 in stage 13.0 (TID 146). 3672 bytes result sent to driver
26/06/26 13:26:22 INFO TaskSetManager: Starting task 135.0 in stage 13.0 (TID 153, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:22 INFO Executor: Running task 135.0 in stage 13.0 (TID 153)
26/06/26 13:26:22 INFO TaskSetManager: Finished task 130.0 in stage 13.0 (TID 148) in 40 ms on localhost (executor driver) (132/200)
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:22 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 128.0 in stage 13.0 (TID 146) in 80 ms on localhost (executor driver) (133/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO Executor: Finished task 132.0 in stage 13.0 (TID 150). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 136.0 in stage 13.0 (TID 154, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 132.0 in stage 13.0 (TID 150) in 66 ms on localhost (executor driver) (134/200)
26/06/26 13:26:23 INFO Executor: Running task 136.0 in stage 13.0 (TID 154)
26/06/26 13:26:23 INFO Executor: Finished task 133.0 in stage 13.0 (TID 151). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 137.0 in stage 13.0 (TID 155, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 133.0 in stage 13.0 (TID 151) in 54 ms on localhost (executor driver) (135/200)
26/06/26 13:26:23 INFO Executor: Running task 137.0 in stage 13.0 (TID 155)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO Executor: Finished task 134.0 in stage 13.0 (TID 152). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 138.0 in stage 13.0 (TID 156, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 138.0 in stage 13.0 (TID 156)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 134.0 in stage 13.0 (TID 152) in 58 ms on localhost (executor driver) (136/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 137.0 in stage 13.0 (TID 155). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 138.0 in stage 13.0 (TID 156). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 135.0 in stage 13.0 (TID 153). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 139.0 in stage 13.0 (TID 157, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 140.0 in stage 13.0 (TID 158, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 141.0 in stage 13.0 (TID 159, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 139.0 in stage 13.0 (TID 157)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 137.0 in stage 13.0 (TID 155) in 24 ms on localhost (executor driver) (137/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 138.0 in stage 13.0 (TID 156) in 10 ms on localhost (executor driver) (138/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 135.0 in stage 13.0 (TID 153) in 65 ms on localhost (executor driver) (139/200)
26/06/26 13:26:23 INFO Executor: Finished task 136.0 in stage 13.0 (TID 154). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO Executor: Running task 141.0 in stage 13.0 (TID 159)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 142.0 in stage 13.0 (TID 160, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 142.0 in stage 13.0 (TID 160)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 136.0 in stage 13.0 (TID 154) in 46 ms on localhost (executor driver) (140/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 140.0 in stage 13.0 (TID 158)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 139.0 in stage 13.0 (TID 157). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 143.0 in stage 13.0 (TID 161, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 143.0 in stage 13.0 (TID 161)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 141.0 in stage 13.0 (TID 159). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 144.0 in stage 13.0 (TID 162, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 141.0 in stage 13.0 (TID 159) in 56 ms on localhost (executor driver) (141/200)
26/06/26 13:26:23 INFO Executor: Running task 144.0 in stage 13.0 (TID 162)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 139.0 in stage 13.0 (TID 157) in 81 ms on localhost (executor driver) (142/200)
26/06/26 13:26:23 INFO Executor: Finished task 142.0 in stage 13.0 (TID 160). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 145.0 in stage 13.0 (TID 163, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 142.0 in stage 13.0 (TID 160) in 70 ms on localhost (executor driver) (143/200)
26/06/26 13:26:23 INFO Executor: Running task 145.0 in stage 13.0 (TID 163)
26/06/26 13:26:23 INFO Executor: Finished task 143.0 in stage 13.0 (TID 161). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 146.0 in stage 13.0 (TID 164, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 143.0 in stage 13.0 (TID 161) in 59 ms on localhost (executor driver) (144/200)
26/06/26 13:26:23 INFO Executor: Running task 146.0 in stage 13.0 (TID 164)
26/06/26 13:26:23 INFO Executor: Finished task 140.0 in stage 13.0 (TID 158). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 147.0 in stage 13.0 (TID 165, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 140.0 in stage 13.0 (TID 158) in 120 ms on localhost (executor driver) (145/200)
26/06/26 13:26:23 INFO Executor: Running task 147.0 in stage 13.0 (TID 165)
26/06/26 13:26:23 INFO Executor: Finished task 146.0 in stage 13.0 (TID 164). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 148.0 in stage 13.0 (TID 166, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 148.0 in stage 13.0 (TID 166)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 146.0 in stage 13.0 (TID 164) in 49 ms on localhost (executor driver) (146/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 144.0 in stage 13.0 (TID 162). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 149.0 in stage 13.0 (TID 167, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 144.0 in stage 13.0 (TID 162) in 100 ms on localhost (executor driver) (147/200)
26/06/26 13:26:23 INFO Executor: Running task 149.0 in stage 13.0 (TID 167)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 77 ms
26/06/26 13:26:23 INFO Executor: Finished task 149.0 in stage 13.0 (TID 167). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 150.0 in stage 13.0 (TID 168, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Finished task 148.0 in stage 13.0 (TID 166). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Finished task 149.0 in stage 13.0 (TID 167) in 100 ms on localhost (executor driver) (148/200)
26/06/26 13:26:23 INFO Executor: Running task 150.0 in stage 13.0 (TID 168)
26/06/26 13:26:23 INFO Executor: Finished task 147.0 in stage 13.0 (TID 165). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 151.0 in stage 13.0 (TID 169, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Finished task 145.0 in stage 13.0 (TID 163). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 152.0 in stage 13.0 (TID 170, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 152.0 in stage 13.0 (TID 170)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 153.0 in stage 13.0 (TID 171, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 153.0 in stage 13.0 (TID 171)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 151.0 in stage 13.0 (TID 169)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 148.0 in stage 13.0 (TID 166) in 124 ms on localhost (executor driver) (149/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 147.0 in stage 13.0 (TID 165) in 151 ms on localhost (executor driver) (150/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 145.0 in stage 13.0 (TID 163) in 186 ms on localhost (executor driver) (151/200)
26/06/26 13:26:23 INFO Executor: Finished task 150.0 in stage 13.0 (TID 168). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 154.0 in stage 13.0 (TID 172, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 150.0 in stage 13.0 (TID 168) in 25 ms on localhost (executor driver) (152/200)
26/06/26 13:26:23 INFO Executor: Finished task 152.0 in stage 13.0 (TID 170). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 155.0 in stage 13.0 (TID 173, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 152.0 in stage 13.0 (TID 170) in 23 ms on localhost (executor driver) (153/200)
26/06/26 13:26:23 INFO Executor: Running task 155.0 in stage 13.0 (TID 173)
26/06/26 13:26:23 INFO Executor: Finished task 151.0 in stage 13.0 (TID 169). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 156.0 in stage 13.0 (TID 174, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 156.0 in stage 13.0 (TID 174)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 151.0 in stage 13.0 (TID 169) in 36 ms on localhost (executor driver) (154/200)
26/06/26 13:26:23 INFO Executor: Running task 154.0 in stage 13.0 (TID 172)
26/06/26 13:26:23 INFO Executor: Finished task 153.0 in stage 13.0 (TID 171). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 157.0 in stage 13.0 (TID 175, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 157.0 in stage 13.0 (TID 175)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 153.0 in stage 13.0 (TID 171) in 58 ms on localhost (executor driver) (155/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 156.0 in stage 13.0 (TID 174). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 157.0 in stage 13.0 (TID 175). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 154.0 in stage 13.0 (TID 172). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 158.0 in stage 13.0 (TID 176, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 159.0 in stage 13.0 (TID 177, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 160.0 in stage 13.0 (TID 178, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 156.0 in stage 13.0 (TID 174) in 78 ms on localhost (executor driver) (156/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 157.0 in stage 13.0 (TID 175) in 62 ms on localhost (executor driver) (157/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 154.0 in stage 13.0 (TID 172) in 100 ms on localhost (executor driver) (158/200)
26/06/26 13:26:23 INFO Executor: Finished task 155.0 in stage 13.0 (TID 173). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Running task 158.0 in stage 13.0 (TID 176)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 161.0 in stage 13.0 (TID 179, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 155.0 in stage 13.0 (TID 173) in 104 ms on localhost (executor driver) (159/200)
26/06/26 13:26:23 INFO Executor: Running task 160.0 in stage 13.0 (TID 178)
26/06/26 13:26:23 INFO Executor: Running task 161.0 in stage 13.0 (TID 179)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 159.0 in stage 13.0 (TID 177)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 158.0 in stage 13.0 (TID 176). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 162.0 in stage 13.0 (TID 180, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 158.0 in stage 13.0 (TID 176) in 37 ms on localhost (executor driver) (160/200)
26/06/26 13:26:23 INFO Executor: Finished task 161.0 in stage 13.0 (TID 179). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 159.0 in stage 13.0 (TID 177). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 163.0 in stage 13.0 (TID 181, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 164.0 in stage 13.0 (TID 182, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 164.0 in stage 13.0 (TID 182)
26/06/26 13:26:23 INFO Executor: Running task 163.0 in stage 13.0 (TID 181)
26/06/26 13:26:23 INFO Executor: Finished task 160.0 in stage 13.0 (TID 178). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 162.0 in stage 13.0 (TID 180)
26/06/26 13:26:23 INFO Executor: Finished task 164.0 in stage 13.0 (TID 182). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 161.0 in stage 13.0 (TID 179) in 43 ms on localhost (executor driver) (161/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 159.0 in stage 13.0 (TID 177) in 53 ms on localhost (executor driver) (162/200)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 165.0 in stage 13.0 (TID 183, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 166.0 in stage 13.0 (TID 184, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 160.0 in stage 13.0 (TID 178) in 53 ms on localhost (executor driver) (163/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 164.0 in stage 13.0 (TID 182) in 16 ms on localhost (executor driver) (164/200)
26/06/26 13:26:23 INFO Executor: Running task 166.0 in stage 13.0 (TID 184)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO Executor: Finished task 162.0 in stage 13.0 (TID 180). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 167.0 in stage 13.0 (TID 185, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 162.0 in stage 13.0 (TID 180) in 31 ms on localhost (executor driver) (165/200)
26/06/26 13:26:23 INFO Executor: Running task 165.0 in stage 13.0 (TID 183)
26/06/26 13:26:23 INFO Executor: Running task 167.0 in stage 13.0 (TID 185)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 166.0 in stage 13.0 (TID 184). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 168.0 in stage 13.0 (TID 186, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 166.0 in stage 13.0 (TID 184) in 21 ms on localhost (executor driver) (166/200)
26/06/26 13:26:23 INFO Executor: Running task 168.0 in stage 13.0 (TID 186)
26/06/26 13:26:23 INFO Executor: Finished task 163.0 in stage 13.0 (TID 181). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 169.0 in stage 13.0 (TID 187, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 169.0 in stage 13.0 (TID 187)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 163.0 in stage 13.0 (TID 181) in 53 ms on localhost (executor driver) (167/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 34 ms
26/06/26 13:26:23 INFO Executor: Finished task 167.0 in stage 13.0 (TID 185). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 168.0 in stage 13.0 (TID 186). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 170.0 in stage 13.0 (TID 188, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 171.0 in stage 13.0 (TID 189, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 170.0 in stage 13.0 (TID 188)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 170.0 in stage 13.0 (TID 188). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 172.0 in stage 13.0 (TID 190, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 171.0 in stage 13.0 (TID 189)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 167.0 in stage 13.0 (TID 185) in 55 ms on localhost (executor driver) (168/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 170.0 in stage 13.0 (TID 188) in 12 ms on localhost (executor driver) (169/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 168.0 in stage 13.0 (TID 186) in 45 ms on localhost (executor driver) (170/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 172.0 in stage 13.0 (TID 190)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 171.0 in stage 13.0 (TID 189). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 173.0 in stage 13.0 (TID 191, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 173.0 in stage 13.0 (TID 191)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 171.0 in stage 13.0 (TID 189) in 40 ms on localhost (executor driver) (171/200)
26/06/26 13:26:23 INFO Executor: Finished task 165.0 in stage 13.0 (TID 183). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 174.0 in stage 13.0 (TID 192, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 165.0 in stage 13.0 (TID 183) in 102 ms on localhost (executor driver) (172/200)
26/06/26 13:26:23 INFO Executor: Finished task 172.0 in stage 13.0 (TID 190). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 175.0 in stage 13.0 (TID 193, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 175.0 in stage 13.0 (TID 193)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 73 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 172.0 in stage 13.0 (TID 190) in 51 ms on localhost (executor driver) (173/200)
26/06/26 13:26:23 INFO Executor: Running task 174.0 in stage 13.0 (TID 192)
26/06/26 13:26:23 INFO Executor: Finished task 175.0 in stage 13.0 (TID 193). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 173.0 in stage 13.0 (TID 191). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 176.0 in stage 13.0 (TID 194, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 177.0 in stage 13.0 (TID 195, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Finished task 169.0 in stage 13.0 (TID 187). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 178.0 in stage 13.0 (TID 196, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 176.0 in stage 13.0 (TID 194)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 175.0 in stage 13.0 (TID 193) in 22 ms on localhost (executor driver) (174/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 173.0 in stage 13.0 (TID 191) in 36 ms on localhost (executor driver) (175/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 169.0 in stage 13.0 (TID 187) in 90 ms on localhost (executor driver) (176/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 174.0 in stage 13.0 (TID 192). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 179.0 in stage 13.0 (TID 197, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 174.0 in stage 13.0 (TID 192) in 37 ms on localhost (executor driver) (177/200)
26/06/26 13:26:23 INFO Executor: Running task 179.0 in stage 13.0 (TID 197)
26/06/26 13:26:23 INFO Executor: Running task 178.0 in stage 13.0 (TID 196)
26/06/26 13:26:23 INFO Executor: Running task 177.0 in stage 13.0 (TID 195)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 176.0 in stage 13.0 (TID 194). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 181.0 in stage 13.0 (TID 198, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 176.0 in stage 13.0 (TID 194) in 33 ms on localhost (executor driver) (178/200)
26/06/26 13:26:23 INFO Executor: Finished task 177.0 in stage 13.0 (TID 195). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 182.0 in stage 13.0 (TID 199, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 182.0 in stage 13.0 (TID 199)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 177.0 in stage 13.0 (TID 195) in 39 ms on localhost (executor driver) (179/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 179.0 in stage 13.0 (TID 197). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 182.0 in stage 13.0 (TID 199). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 183.0 in stage 13.0 (TID 200, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 181.0 in stage 13.0 (TID 198)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 184.0 in stage 13.0 (TID 201, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 179.0 in stage 13.0 (TID 197) in 33 ms on localhost (executor driver) (180/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 182.0 in stage 13.0 (TID 199) in 12 ms on localhost (executor driver) (181/200)
26/06/26 13:26:23 INFO Executor: Running task 184.0 in stage 13.0 (TID 201)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 183.0 in stage 13.0 (TID 200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 178.0 in stage 13.0 (TID 196). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 185.0 in stage 13.0 (TID 202, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 178.0 in stage 13.0 (TID 196) in 64 ms on localhost (executor driver) (182/200)
26/06/26 13:26:23 INFO Executor: Running task 185.0 in stage 13.0 (TID 202)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 184.0 in stage 13.0 (TID 201). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 186.0 in stage 13.0 (TID 203, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 184.0 in stage 13.0 (TID 201) in 32 ms on localhost (executor driver) (183/200)
26/06/26 13:26:23 INFO Executor: Finished task 183.0 in stage 13.0 (TID 200). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Running task 186.0 in stage 13.0 (TID 203)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 187.0 in stage 13.0 (TID 204, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 183.0 in stage 13.0 (TID 200) in 40 ms on localhost (executor driver) (184/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 187.0 in stage 13.0 (TID 204)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO Executor: Finished task 185.0 in stage 13.0 (TID 202). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 188.0 in stage 13.0 (TID 205, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 188.0 in stage 13.0 (TID 205)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 185.0 in stage 13.0 (TID 202) in 49 ms on localhost (executor driver) (185/200)
26/06/26 13:26:23 INFO Executor: Finished task 181.0 in stage 13.0 (TID 198). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 186.0 in stage 13.0 (TID 203). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 189.0 in stage 13.0 (TID 206, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 190.0 in stage 13.0 (TID 207, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 186.0 in stage 13.0 (TID 203) in 39 ms on localhost (executor driver) (186/200)
26/06/26 13:26:23 INFO Executor: Finished task 187.0 in stage 13.0 (TID 204). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Finished task 181.0 in stage 13.0 (TID 198) in 88 ms on localhost (executor driver) (187/200)
26/06/26 13:26:23 INFO Executor: Running task 189.0 in stage 13.0 (TID 206)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 191.0 in stage 13.0 (TID 208, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 187.0 in stage 13.0 (TID 204) in 47 ms on localhost (executor driver) (188/200)
26/06/26 13:26:23 INFO Executor: Finished task 189.0 in stage 13.0 (TID 206). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 192.0 in stage 13.0 (TID 209, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 189.0 in stage 13.0 (TID 206) in 17 ms on localhost (executor driver) (189/200)
26/06/26 13:26:23 INFO Executor: Running task 192.0 in stage 13.0 (TID 209)
26/06/26 13:26:23 INFO Executor: Finished task 188.0 in stage 13.0 (TID 205). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 193.0 in stage 13.0 (TID 210, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 193.0 in stage 13.0 (TID 210)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 188.0 in stage 13.0 (TID 205) in 38 ms on localhost (executor driver) (190/200)
26/06/26 13:26:23 INFO Executor: Running task 190.0 in stage 13.0 (TID 207)
26/06/26 13:26:23 INFO Executor: Finished task 192.0 in stage 13.0 (TID 209). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 193.0 in stage 13.0 (TID 210). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 194.0 in stage 13.0 (TID 211, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO TaskSetManager: Starting task 195.0 in stage 13.0 (TID 212, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Finished task 192.0 in stage 13.0 (TID 209) in 17 ms on localhost (executor driver) (191/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 193.0 in stage 13.0 (TID 210) in 11 ms on localhost (executor driver) (192/200)
26/06/26 13:26:23 INFO Executor: Running task 194.0 in stage 13.0 (TID 211)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 190.0 in stage 13.0 (TID 207). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Running task 191.0 in stage 13.0 (TID 208)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO TaskSetManager: Starting task 196.0 in stage 13.0 (TID 213, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 190.0 in stage 13.0 (TID 207) in 48 ms on localhost (executor driver) (193/200)
26/06/26 13:26:23 INFO Executor: Running task 195.0 in stage 13.0 (TID 212)
26/06/26 13:26:23 INFO Executor: Running task 196.0 in stage 13.0 (TID 213)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 194.0 in stage 13.0 (TID 211). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 197.0 in stage 13.0 (TID 214, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 194.0 in stage 13.0 (TID 211) in 42 ms on localhost (executor driver) (194/200)
26/06/26 13:26:23 INFO Executor: Finished task 195.0 in stage 13.0 (TID 212). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 191.0 in stage 13.0 (TID 208). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Starting task 198.0 in stage 13.0 (TID 215, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:23 INFO Executor: Running task 198.0 in stage 13.0 (TID 215)
26/06/26 13:26:23 INFO TaskSetManager: Starting task 199.0 in stage 13.0 (TID 216, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 195.0 in stage 13.0 (TID 212) in 55 ms on localhost (executor driver) (195/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 191.0 in stage 13.0 (TID 208) in 75 ms on localhost (executor driver) (196/200)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Running task 199.0 in stage 13.0 (TID 216)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 199.0 in stage 13.0 (TID 216). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Finished task 199.0 in stage 13.0 (TID 216) in 13 ms on localhost (executor driver) (197/200)
26/06/26 13:26:23 INFO Executor: Running task 197.0 in stage 13.0 (TID 214)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:23 INFO Executor: Finished task 198.0 in stage 13.0 (TID 215). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 196.0 in stage 13.0 (TID 213). 3629 bytes result sent to driver
26/06/26 13:26:23 INFO Executor: Finished task 197.0 in stage 13.0 (TID 214). 3672 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Finished task 197.0 in stage 13.0 (TID 214) in 77 ms on localhost (executor driver) (198/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 196.0 in stage 13.0 (TID 213) in 103 ms on localhost (executor driver) (199/200)
26/06/26 13:26:23 INFO TaskSetManager: Finished task 198.0 in stage 13.0 (TID 215) in 64 ms on localhost (executor driver) (200/200)
26/06/26 13:26:23 INFO TaskSchedulerImpl: Removed TaskSet 13.0, whose tasks have all completed, from pool 
26/06/26 13:26:23 INFO DAGScheduler: ShuffleMapStage 13 (count at NativeMethodAccessorImpl.java:0) finished in 3.417 s
26/06/26 13:26:23 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:23 INFO DAGScheduler: running: Set()
26/06/26 13:26:23 INFO DAGScheduler: waiting: Set(ResultStage 14)
26/06/26 13:26:23 INFO DAGScheduler: failed: Set()
26/06/26 13:26:23 INFO DAGScheduler: Submitting ResultStage 14 (MapPartitionsRDD[59] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:23 INFO MemoryStore: Block broadcast_17 stored as values in memory (estimated size 7.3 KB, free 365.1 MB)
26/06/26 13:26:23 INFO MemoryStore: Block broadcast_17_piece0 stored as bytes in memory (estimated size 3.8 KB, free 365.1 MB)
26/06/26 13:26:23 INFO BlockManagerInfo: Added broadcast_17_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.2 MB)
26/06/26 13:26:23 INFO SparkContext: Created broadcast 17 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:23 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 14 (MapPartitionsRDD[59] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:23 INFO TaskSchedulerImpl: Adding task set 14.0 with 1 tasks
26/06/26 13:26:23 INFO TaskSetManager: Starting task 0.0 in stage 14.0 (TID 217, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:23 INFO Executor: Running task 0.0 in stage 14.0 (TID 217)
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:23 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 6 ms
26/06/26 13:26:23 INFO Executor: Finished task 0.0 in stage 14.0 (TID 217). 1782 bytes result sent to driver
26/06/26 13:26:23 INFO TaskSetManager: Finished task 0.0 in stage 14.0 (TID 217) in 73 ms on localhost (executor driver) (1/1)
26/06/26 13:26:23 INFO TaskSchedulerImpl: Removed TaskSet 14.0, whose tasks have all completed, from pool 
26/06/26 13:26:23 INFO DAGScheduler: ResultStage 14 (count at NativeMethodAccessorImpl.java:0) finished in 0.089 s
26/06/26 13:26:23 INFO DAGScheduler: Job 9 finished: count at NativeMethodAccessorImpl.java:0, took 4.809241 s
('Users :', 943)
26/06/26 13:26:24 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:24 INFO CodeGenerator: Code generated in 31.673535 ms
26/06/26 13:26:24 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:24 INFO CodeGenerator: Code generated in 88.549681 ms
26/06/26 13:26:24 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:24 INFO DAGScheduler: Registering RDD 62 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:24 INFO DAGScheduler: Registering RDD 65 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:24 INFO DAGScheduler: Got job 10 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:24 INFO DAGScheduler: Final stage: ResultStage 17 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:24 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 16)
26/06/26 13:26:24 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 16)
26/06/26 13:26:24 INFO DAGScheduler: Submitting ShuffleMapStage 15 (MapPartitionsRDD[62] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:24 INFO MemoryStore: Block broadcast_18 stored as values in memory (estimated size 28.4 KB, free 365.0 MB)
26/06/26 13:26:24 INFO MemoryStore: Block broadcast_18_piece0 stored as bytes in memory (estimated size 14.2 KB, free 365.0 MB)
26/06/26 13:26:24 INFO BlockManagerInfo: Added broadcast_18_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 14.2 KB, free: 366.2 MB)
26/06/26 13:26:24 INFO SparkContext: Created broadcast 18 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:24 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 15 (MapPartitionsRDD[62] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:24 INFO TaskSchedulerImpl: Adding task set 15.0 with 2 tasks
26/06/26 13:26:24 INFO TaskSetManager: Starting task 0.0 in stage 15.0 (TID 218, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:24 INFO TaskSetManager: Starting task 1.0 in stage 15.0 (TID 219, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:24 INFO Executor: Running task 1.0 in stage 15.0 (TID 219)
26/06/26 13:26:24 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:989586+989587
26/06/26 13:26:24 INFO Executor: Running task 0.0 in stage 15.0 (TID 218)
26/06/26 13:26:24 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:0+989586
26/06/26 13:26:24 INFO CodeGenerator: Code generated in 7.06015 ms
26/06/26 13:26:24 INFO CodeGenerator: Code generated in 9.565903 ms
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 439
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 443
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 454
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 449
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 430
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 446
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 444
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 445
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 436
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 456
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 448
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 447
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 455
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 452
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 432
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 451
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 431
26/06/26 13:26:24 INFO BlockManagerInfo: Removed broadcast_17_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.2 MB)
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 450
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 453
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 435
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 442
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 440
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 438
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 437
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 434
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 433
26/06/26 13:26:24 INFO ContextCleaner: Cleaned accumulator 441
26/06/26 13:26:25 INFO PythonRunner: Times: total = 987, boot = -4944, init = 4956, finish = 975
26/06/26 13:26:25 INFO PythonRunner: Times: total = 986, boot = -4892, init = 5056, finish = 822
26/06/26 13:26:25 INFO Executor: Finished task 1.0 in stage 15.0 (TID 219). 2698 bytes result sent to driver
26/06/26 13:26:25 INFO TaskSetManager: Finished task 1.0 in stage 15.0 (TID 219) in 1663 ms on localhost (executor driver) (1/2)
26/06/26 13:26:25 INFO Executor: Finished task 0.0 in stage 15.0 (TID 218). 2698 bytes result sent to driver
26/06/26 13:26:25 INFO TaskSetManager: Finished task 0.0 in stage 15.0 (TID 218) in 1668 ms on localhost (executor driver) (2/2)
26/06/26 13:26:25 INFO TaskSchedulerImpl: Removed TaskSet 15.0, whose tasks have all completed, from pool 
26/06/26 13:26:25 INFO DAGScheduler: ShuffleMapStage 15 (count at NativeMethodAccessorImpl.java:0) finished in 1.695 s
26/06/26 13:26:25 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:25 INFO DAGScheduler: running: Set()
26/06/26 13:26:25 INFO DAGScheduler: waiting: Set(ShuffleMapStage 16, ResultStage 17)
26/06/26 13:26:25 INFO DAGScheduler: failed: Set()
26/06/26 13:26:25 INFO DAGScheduler: Submitting ShuffleMapStage 16 (MapPartitionsRDD[65] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:25 INFO MemoryStore: Block broadcast_19 stored as values in memory (estimated size 33.0 KB, free 365.0 MB)
26/06/26 13:26:25 INFO MemoryStore: Block broadcast_19_piece0 stored as bytes in memory (estimated size 16.9 KB, free 365.0 MB)
26/06/26 13:26:25 INFO BlockManagerInfo: Added broadcast_19_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 16.9 KB, free: 366.1 MB)
26/06/26 13:26:25 INFO SparkContext: Created broadcast 19 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:25 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 16 (MapPartitionsRDD[65] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:25 INFO TaskSchedulerImpl: Adding task set 16.0 with 200 tasks
26/06/26 13:26:25 INFO TaskSetManager: Starting task 0.0 in stage 16.0 (TID 220, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:25 INFO TaskSetManager: Starting task 1.0 in stage 16.0 (TID 221, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:25 INFO TaskSetManager: Starting task 2.0 in stage 16.0 (TID 222, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:25 INFO TaskSetManager: Starting task 3.0 in stage 16.0 (TID 223, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:25 INFO Executor: Running task 1.0 in stage 16.0 (TID 221)
26/06/26 13:26:25 INFO Executor: Running task 0.0 in stage 16.0 (TID 220)
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:25 INFO Executor: Running task 2.0 in stage 16.0 (TID 222)
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:25 INFO Executor: Running task 3.0 in stage 16.0 (TID 223)
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:25 INFO Executor: Finished task 1.0 in stage 16.0 (TID 221). 3629 bytes result sent to driver
26/06/26 13:26:25 INFO Executor: Finished task 3.0 in stage 16.0 (TID 223). 3629 bytes result sent to driver
26/06/26 13:26:25 INFO TaskSetManager: Starting task 4.0 in stage 16.0 (TID 224, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:25 INFO Executor: Finished task 2.0 in stage 16.0 (TID 222). 3629 bytes result sent to driver
26/06/26 13:26:25 INFO Executor: Running task 4.0 in stage 16.0 (TID 224)
26/06/26 13:26:25 INFO TaskSetManager: Starting task 5.0 in stage 16.0 (TID 225, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:25 INFO TaskSetManager: Starting task 6.0 in stage 16.0 (TID 226, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:25 INFO TaskSetManager: Finished task 1.0 in stage 16.0 (TID 221) in 22 ms on localhost (executor driver) (1/200)
26/06/26 13:26:25 INFO TaskSetManager: Finished task 3.0 in stage 16.0 (TID 223) in 22 ms on localhost (executor driver) (2/200)
26/06/26 13:26:25 INFO TaskSetManager: Finished task 2.0 in stage 16.0 (TID 222) in 23 ms on localhost (executor driver) (3/200)
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:25 INFO Executor: Finished task 0.0 in stage 16.0 (TID 220). 3629 bytes result sent to driver
26/06/26 13:26:25 INFO Executor: Running task 6.0 in stage 16.0 (TID 226)
26/06/26 13:26:25 INFO Executor: Running task 5.0 in stage 16.0 (TID 225)
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:25 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 7.0 in stage 16.0 (TID 227, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 0.0 in stage 16.0 (TID 220) in 35 ms on localhost (executor driver) (4/200)
26/06/26 13:26:26 INFO Executor: Finished task 6.0 in stage 16.0 (TID 226). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 7.0 in stage 16.0 (TID 227)
26/06/26 13:26:26 INFO Executor: Finished task 5.0 in stage 16.0 (TID 225). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 4.0 in stage 16.0 (TID 224). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 8.0 in stage 16.0 (TID 228, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 9.0 in stage 16.0 (TID 229, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 10.0 in stage 16.0 (TID 230, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 8.0 in stage 16.0 (TID 228)
26/06/26 13:26:26 INFO Executor: Finished task 7.0 in stage 16.0 (TID 227). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 6.0 in stage 16.0 (TID 226) in 25 ms on localhost (executor driver) (5/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 5.0 in stage 16.0 (TID 225) in 25 ms on localhost (executor driver) (6/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 4.0 in stage 16.0 (TID 224) in 26 ms on localhost (executor driver) (7/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 10.0 in stage 16.0 (TID 230)
26/06/26 13:26:26 INFO Executor: Running task 9.0 in stage 16.0 (TID 229)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 11.0 in stage 16.0 (TID 231, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 7.0 in stage 16.0 (TID 227) in 18 ms on localhost (executor driver) (8/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 4 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Running task 11.0 in stage 16.0 (TID 231)
26/06/26 13:26:26 INFO Executor: Finished task 8.0 in stage 16.0 (TID 228). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 12.0 in stage 16.0 (TID 232, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 8.0 in stage 16.0 (TID 228) in 18 ms on localhost (executor driver) (9/200)
26/06/26 13:26:26 INFO Executor: Running task 12.0 in stage 16.0 (TID 232)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 12.0 in stage 16.0 (TID 232). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 15 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 13.0 in stage 16.0 (TID 233, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 11.0 in stage 16.0 (TID 231). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 12.0 in stage 16.0 (TID 232) in 18 ms on localhost (executor driver) (10/200)
26/06/26 13:26:26 INFO Executor: Finished task 10.0 in stage 16.0 (TID 230). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 13.0 in stage 16.0 (TID 233)
26/06/26 13:26:26 INFO Executor: Finished task 9.0 in stage 16.0 (TID 229). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 14.0 in stage 16.0 (TID 234, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 15.0 in stage 16.0 (TID 235, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 16.0 in stage 16.0 (TID 236, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 13.0 in stage 16.0 (TID 233). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 17.0 in stage 16.0 (TID 237, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 11.0 in stage 16.0 (TID 231) in 40 ms on localhost (executor driver) (11/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 10.0 in stage 16.0 (TID 230) in 47 ms on localhost (executor driver) (12/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 9.0 in stage 16.0 (TID 229) in 47 ms on localhost (executor driver) (13/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 13.0 in stage 16.0 (TID 233) in 17 ms on localhost (executor driver) (14/200)
26/06/26 13:26:26 INFO Executor: Running task 16.0 in stage 16.0 (TID 236)
26/06/26 13:26:26 INFO Executor: Running task 17.0 in stage 16.0 (TID 237)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 15.0 in stage 16.0 (TID 235)
26/06/26 13:26:26 INFO Executor: Running task 14.0 in stage 16.0 (TID 234)
26/06/26 13:26:26 INFO Executor: Finished task 17.0 in stage 16.0 (TID 237). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 18.0 in stage 16.0 (TID 238, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 17.0 in stage 16.0 (TID 237) in 11 ms on localhost (executor driver) (15/200)
26/06/26 13:26:26 INFO Executor: Running task 18.0 in stage 16.0 (TID 238)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 14.0 in stage 16.0 (TID 234). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 18.0 in stage 16.0 (TID 238). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 19.0 in stage 16.0 (TID 239, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 16.0 in stage 16.0 (TID 236). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 14.0 in stage 16.0 (TID 234) in 29 ms on localhost (executor driver) (16/200)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 20.0 in stage 16.0 (TID 240, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 16.0 in stage 16.0 (TID 236) in 29 ms on localhost (executor driver) (17/200)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 21.0 in stage 16.0 (TID 241, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 18.0 in stage 16.0 (TID 238) in 13 ms on localhost (executor driver) (18/200)
26/06/26 13:26:26 INFO Executor: Running task 21.0 in stage 16.0 (TID 241)
26/06/26 13:26:26 INFO Executor: Running task 20.0 in stage 16.0 (TID 240)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 19.0 in stage 16.0 (TID 239)
26/06/26 13:26:26 INFO Executor: Finished task 21.0 in stage 16.0 (TID 241). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 22.0 in stage 16.0 (TID 242, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 21.0 in stage 16.0 (TID 241) in 10 ms on localhost (executor driver) (19/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Finished task 20.0 in stage 16.0 (TID 240). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 23.0 in stage 16.0 (TID 243, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 20.0 in stage 16.0 (TID 240) in 14 ms on localhost (executor driver) (20/200)
26/06/26 13:26:26 INFO Executor: Running task 23.0 in stage 16.0 (TID 243)
26/06/26 13:26:26 INFO Executor: Running task 22.0 in stage 16.0 (TID 242)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 23.0 in stage 16.0 (TID 243). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 24.0 in stage 16.0 (TID 244, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 23.0 in stage 16.0 (TID 243) in 6 ms on localhost (executor driver) (21/200)
26/06/26 13:26:26 INFO Executor: Running task 24.0 in stage 16.0 (TID 244)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 24.0 in stage 16.0 (TID 244). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 25.0 in stage 16.0 (TID 245, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 24.0 in stage 16.0 (TID 244) in 7 ms on localhost (executor driver) (22/200)
26/06/26 13:26:26 INFO Executor: Running task 25.0 in stage 16.0 (TID 245)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 25.0 in stage 16.0 (TID 245). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 26.0 in stage 16.0 (TID 246, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 26.0 in stage 16.0 (TID 246)
26/06/26 13:26:26 INFO Executor: Finished task 19.0 in stage 16.0 (TID 239). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 27.0 in stage 16.0 (TID 247, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 19.0 in stage 16.0 (TID 239) in 57 ms on localhost (executor driver) (23/200)
26/06/26 13:26:26 INFO Executor: Running task 27.0 in stage 16.0 (TID 247)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 26.0 in stage 16.0 (TID 246). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 27.0 in stage 16.0 (TID 247). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 22.0 in stage 16.0 (TID 242). 3586 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 15.0 in stage 16.0 (TID 235). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 25.0 in stage 16.0 (TID 245) in 31 ms on localhost (executor driver) (24/200)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 28.0 in stage 16.0 (TID 248, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 29.0 in stage 16.0 (TID 249, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 30.0 in stage 16.0 (TID 250, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 31.0 in stage 16.0 (TID 251, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 22.0 in stage 16.0 (TID 242) in 61 ms on localhost (executor driver) (25/200)
26/06/26 13:26:26 INFO Executor: Running task 28.0 in stage 16.0 (TID 248)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 15.0 in stage 16.0 (TID 235) in 101 ms on localhost (executor driver) (26/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 26.0 in stage 16.0 (TID 246) in 33 ms on localhost (executor driver) (27/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 27.0 in stage 16.0 (TID 247) in 17 ms on localhost (executor driver) (28/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 31.0 in stage 16.0 (TID 251)
26/06/26 13:26:26 INFO Executor: Running task 29.0 in stage 16.0 (TID 249)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 30.0 in stage 16.0 (TID 250)
26/06/26 13:26:26 INFO Executor: Finished task 28.0 in stage 16.0 (TID 248). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 32.0 in stage 16.0 (TID 252, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 32.0 in stage 16.0 (TID 252)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 28.0 in stage 16.0 (TID 248) in 17 ms on localhost (executor driver) (29/200)
26/06/26 13:26:26 INFO Executor: Finished task 31.0 in stage 16.0 (TID 251). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 29.0 in stage 16.0 (TID 249). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 30.0 in stage 16.0 (TID 250). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 32.0 in stage 16.0 (TID 252). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 33.0 in stage 16.0 (TID 253, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 34.0 in stage 16.0 (TID 254, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 35.0 in stage 16.0 (TID 255, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 34.0 in stage 16.0 (TID 254)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 36.0 in stage 16.0 (TID 256, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 31.0 in stage 16.0 (TID 251) in 25 ms on localhost (executor driver) (30/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 29.0 in stage 16.0 (TID 249) in 27 ms on localhost (executor driver) (31/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 30.0 in stage 16.0 (TID 250) in 26 ms on localhost (executor driver) (32/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 32.0 in stage 16.0 (TID 252) in 10 ms on localhost (executor driver) (33/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Running task 36.0 in stage 16.0 (TID 256)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 34.0 in stage 16.0 (TID 254). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 33.0 in stage 16.0 (TID 253)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 36.0 in stage 16.0 (TID 256). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 37.0 in stage 16.0 (TID 257, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 38.0 in stage 16.0 (TID 258, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 34.0 in stage 16.0 (TID 254) in 17 ms on localhost (executor driver) (34/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 36.0 in stage 16.0 (TID 256) in 18 ms on localhost (executor driver) (35/200)
26/06/26 13:26:26 INFO Executor: Running task 37.0 in stage 16.0 (TID 257)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Running task 35.0 in stage 16.0 (TID 255)
26/06/26 13:26:26 INFO Executor: Running task 38.0 in stage 16.0 (TID 258)
26/06/26 13:26:26 INFO Executor: Finished task 37.0 in stage 16.0 (TID 257). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 33.0 in stage 16.0 (TID 253). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 39.0 in stage 16.0 (TID 259, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 40.0 in stage 16.0 (TID 260, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 37.0 in stage 16.0 (TID 257) in 39 ms on localhost (executor driver) (36/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 33.0 in stage 16.0 (TID 253) in 48 ms on localhost (executor driver) (37/200)
26/06/26 13:26:26 INFO Executor: Running task 39.0 in stage 16.0 (TID 259)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 39.0 in stage 16.0 (TID 259). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 40.0 in stage 16.0 (TID 260)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 41.0 in stage 16.0 (TID 261, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 41.0 in stage 16.0 (TID 261)
26/06/26 13:26:26 INFO Executor: Finished task 40.0 in stage 16.0 (TID 260). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 39.0 in stage 16.0 (TID 259) in 19 ms on localhost (executor driver) (38/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 42.0 in stage 16.0 (TID 262, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 40.0 in stage 16.0 (TID 260) in 24 ms on localhost (executor driver) (39/200)
26/06/26 13:26:26 INFO Executor: Running task 42.0 in stage 16.0 (TID 262)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 41.0 in stage 16.0 (TID 261). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 43.0 in stage 16.0 (TID 263, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 41.0 in stage 16.0 (TID 261) in 16 ms on localhost (executor driver) (40/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 38.0 in stage 16.0 (TID 258). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 44.0 in stage 16.0 (TID 264, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 44.0 in stage 16.0 (TID 264)
26/06/26 13:26:26 INFO Executor: Running task 43.0 in stage 16.0 (TID 263)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 35.0 in stage 16.0 (TID 255). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 45.0 in stage 16.0 (TID 265, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 35.0 in stage 16.0 (TID 255) in 119 ms on localhost (executor driver) (41/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 38.0 in stage 16.0 (TID 258) in 103 ms on localhost (executor driver) (42/200)
26/06/26 13:26:26 INFO Executor: Running task 45.0 in stage 16.0 (TID 265)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 45.0 in stage 16.0 (TID 265). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 46.0 in stage 16.0 (TID 266, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 45.0 in stage 16.0 (TID 265) in 11 ms on localhost (executor driver) (43/200)
26/06/26 13:26:26 INFO Executor: Finished task 42.0 in stage 16.0 (TID 262). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 47.0 in stage 16.0 (TID 267, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 42.0 in stage 16.0 (TID 262) in 62 ms on localhost (executor driver) (44/200)
26/06/26 13:26:26 INFO Executor: Finished task 43.0 in stage 16.0 (TID 263). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 47.0 in stage 16.0 (TID 267)
26/06/26 13:26:26 INFO Executor: Finished task 44.0 in stage 16.0 (TID 264). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 48.0 in stage 16.0 (TID 268, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 49.0 in stage 16.0 (TID 269, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 43.0 in stage 16.0 (TID 263) in 57 ms on localhost (executor driver) (45/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 44.0 in stage 16.0 (TID 264) in 32 ms on localhost (executor driver) (46/200)
26/06/26 13:26:26 INFO Executor: Running task 46.0 in stage 16.0 (TID 266)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 47.0 in stage 16.0 (TID 267). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 46.0 in stage 16.0 (TID 266). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 50.0 in stage 16.0 (TID 270, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 51.0 in stage 16.0 (TID 271, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 47.0 in stage 16.0 (TID 267) in 16 ms on localhost (executor driver) (47/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 46.0 in stage 16.0 (TID 266) in 18 ms on localhost (executor driver) (48/200)
26/06/26 13:26:26 INFO Executor: Running task 48.0 in stage 16.0 (TID 268)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 48.0 in stage 16.0 (TID 268). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 52.0 in stage 16.0 (TID 272, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 48.0 in stage 16.0 (TID 268) in 23 ms on localhost (executor driver) (49/200)
26/06/26 13:26:26 INFO Executor: Running task 50.0 in stage 16.0 (TID 270)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 49.0 in stage 16.0 (TID 269)
26/06/26 13:26:26 INFO Executor: Finished task 50.0 in stage 16.0 (TID 270). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 53.0 in stage 16.0 (TID 273, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 50.0 in stage 16.0 (TID 270) in 23 ms on localhost (executor driver) (50/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 52.0 in stage 16.0 (TID 272)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 51.0 in stage 16.0 (TID 271)
26/06/26 13:26:26 INFO Executor: Running task 53.0 in stage 16.0 (TID 273)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 49.0 in stage 16.0 (TID 269). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 54.0 in stage 16.0 (TID 274, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 51.0 in stage 16.0 (TID 271). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 54.0 in stage 16.0 (TID 274)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 49.0 in stage 16.0 (TID 269) in 45 ms on localhost (executor driver) (51/200)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 55.0 in stage 16.0 (TID 275, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 51.0 in stage 16.0 (TID 271) in 37 ms on localhost (executor driver) (52/200)
26/06/26 13:26:26 INFO Executor: Running task 55.0 in stage 16.0 (TID 275)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 52.0 in stage 16.0 (TID 272). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 53.0 in stage 16.0 (TID 273). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 56.0 in stage 16.0 (TID 276, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 57.0 in stage 16.0 (TID 277, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 53.0 in stage 16.0 (TID 273) in 24 ms on localhost (executor driver) (53/200)
26/06/26 13:26:26 INFO Executor: Finished task 55.0 in stage 16.0 (TID 275). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 58.0 in stage 16.0 (TID 278, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 55.0 in stage 16.0 (TID 275) in 11 ms on localhost (executor driver) (54/200)
26/06/26 13:26:26 INFO Executor: Running task 58.0 in stage 16.0 (TID 278)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 52.0 in stage 16.0 (TID 272) in 39 ms on localhost (executor driver) (55/200)
26/06/26 13:26:26 INFO Executor: Finished task 58.0 in stage 16.0 (TID 278). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 59.0 in stage 16.0 (TID 279, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 58.0 in stage 16.0 (TID 278) in 8 ms on localhost (executor driver) (56/200)
26/06/26 13:26:26 INFO Executor: Running task 57.0 in stage 16.0 (TID 277)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Finished task 57.0 in stage 16.0 (TID 277). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 60.0 in stage 16.0 (TID 280, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 57.0 in stage 16.0 (TID 277) in 26 ms on localhost (executor driver) (57/200)
26/06/26 13:26:26 INFO Executor: Running task 56.0 in stage 16.0 (TID 276)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Finished task 54.0 in stage 16.0 (TID 274). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 56.0 in stage 16.0 (TID 276). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 61.0 in stage 16.0 (TID 281, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 62.0 in stage 16.0 (TID 282, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 54.0 in stage 16.0 (TID 274) in 48 ms on localhost (executor driver) (58/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 56.0 in stage 16.0 (TID 276) in 39 ms on localhost (executor driver) (59/200)
26/06/26 13:26:26 INFO Executor: Running task 59.0 in stage 16.0 (TID 279)
26/06/26 13:26:26 INFO Executor: Running task 62.0 in stage 16.0 (TID 282)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 59.0 in stage 16.0 (TID 279). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 63.0 in stage 16.0 (TID 283, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 62.0 in stage 16.0 (TID 282). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 59.0 in stage 16.0 (TID 279) in 37 ms on localhost (executor driver) (60/200)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 64.0 in stage 16.0 (TID 284, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 62.0 in stage 16.0 (TID 282) in 10 ms on localhost (executor driver) (61/200)
26/06/26 13:26:26 INFO Executor: Running task 64.0 in stage 16.0 (TID 284)
26/06/26 13:26:26 INFO Executor: Running task 60.0 in stage 16.0 (TID 280)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:26 INFO Executor: Finished task 60.0 in stage 16.0 (TID 280). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 65.0 in stage 16.0 (TID 285, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 60.0 in stage 16.0 (TID 280) in 30 ms on localhost (executor driver) (62/200)
26/06/26 13:26:26 INFO Executor: Finished task 64.0 in stage 16.0 (TID 284). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 66.0 in stage 16.0 (TID 286, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 61.0 in stage 16.0 (TID 281)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 64.0 in stage 16.0 (TID 284) in 11 ms on localhost (executor driver) (63/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 66.0 in stage 16.0 (TID 286)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Running task 63.0 in stage 16.0 (TID 283)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Finished task 66.0 in stage 16.0 (TID 286). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 63.0 in stage 16.0 (TID 283). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 67.0 in stage 16.0 (TID 287, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 68.0 in stage 16.0 (TID 288, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 66.0 in stage 16.0 (TID 286) in 18 ms on localhost (executor driver) (64/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 63.0 in stage 16.0 (TID 283) in 29 ms on localhost (executor driver) (65/200)
26/06/26 13:26:26 INFO Executor: Running task 65.0 in stage 16.0 (TID 285)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Finished task 65.0 in stage 16.0 (TID 285). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 69.0 in stage 16.0 (TID 289, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 65.0 in stage 16.0 (TID 285) in 32 ms on localhost (executor driver) (66/200)
26/06/26 13:26:26 INFO Executor: Running task 69.0 in stage 16.0 (TID 289)
26/06/26 13:26:26 INFO Executor: Finished task 61.0 in stage 16.0 (TID 281). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 70.0 in stage 16.0 (TID 290, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 68.0 in stage 16.0 (TID 288)
26/06/26 13:26:26 INFO Executor: Running task 67.0 in stage 16.0 (TID 287)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 61 ms
26/06/26 13:26:26 INFO Executor: Finished task 68.0 in stage 16.0 (TID 288). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 71.0 in stage 16.0 (TID 291, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 68.0 in stage 16.0 (TID 288) in 91 ms on localhost (executor driver) (67/200)
26/06/26 13:26:26 INFO Executor: Running task 71.0 in stage 16.0 (TID 291)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 61.0 in stage 16.0 (TID 281) in 134 ms on localhost (executor driver) (68/200)
26/06/26 13:26:26 INFO Executor: Running task 70.0 in stage 16.0 (TID 290)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 69.0 in stage 16.0 (TID 289). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 72.0 in stage 16.0 (TID 292, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 67.0 in stage 16.0 (TID 287). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 73.0 in stage 16.0 (TID 293, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 73.0 in stage 16.0 (TID 293)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 69.0 in stage 16.0 (TID 289) in 98 ms on localhost (executor driver) (69/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 67.0 in stage 16.0 (TID 287) in 112 ms on localhost (executor driver) (70/200)
26/06/26 13:26:26 INFO Executor: Finished task 73.0 in stage 16.0 (TID 293). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 74.0 in stage 16.0 (TID 294, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 73.0 in stage 16.0 (TID 293) in 11 ms on localhost (executor driver) (71/200)
26/06/26 13:26:26 INFO Executor: Running task 72.0 in stage 16.0 (TID 292)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 71.0 in stage 16.0 (TID 291). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 72.0 in stage 16.0 (TID 292). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 75.0 in stage 16.0 (TID 295, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 76.0 in stage 16.0 (TID 296, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 71.0 in stage 16.0 (TID 291) in 40 ms on localhost (executor driver) (72/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 72.0 in stage 16.0 (TID 292) in 26 ms on localhost (executor driver) (73/200)
26/06/26 13:26:26 INFO Executor: Running task 74.0 in stage 16.0 (TID 294)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 76.0 in stage 16.0 (TID 296)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 70.0 in stage 16.0 (TID 290). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 75.0 in stage 16.0 (TID 295)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 77.0 in stage 16.0 (TID 297, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 77.0 in stage 16.0 (TID 297)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 70.0 in stage 16.0 (TID 290) in 82 ms on localhost (executor driver) (74/200)
26/06/26 13:26:26 INFO Executor: Finished task 75.0 in stage 16.0 (TID 295). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 77.0 in stage 16.0 (TID 297). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 78.0 in stage 16.0 (TID 298, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 79.0 in stage 16.0 (TID 299, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 79.0 in stage 16.0 (TID 299)
26/06/26 13:26:26 INFO Executor: Finished task 74.0 in stage 16.0 (TID 294). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 80.0 in stage 16.0 (TID 300, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 78.0 in stage 16.0 (TID 298)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 80.0 in stage 16.0 (TID 300)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 75.0 in stage 16.0 (TID 295) in 121 ms on localhost (executor driver) (75/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 77.0 in stage 16.0 (TID 297) in 97 ms on localhost (executor driver) (76/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:26 INFO Executor: Finished task 78.0 in stage 16.0 (TID 298). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 79.0 in stage 16.0 (TID 299). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Finished task 74.0 in stage 16.0 (TID 294) in 141 ms on localhost (executor driver) (77/200)
26/06/26 13:26:26 INFO Executor: Finished task 76.0 in stage 16.0 (TID 296). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 81.0 in stage 16.0 (TID 301, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 82.0 in stage 16.0 (TID 302, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 83.0 in stage 16.0 (TID 303, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 82.0 in stage 16.0 (TID 302)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 78.0 in stage 16.0 (TID 298) in 181 ms on localhost (executor driver) (78/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 79.0 in stage 16.0 (TID 299) in 180 ms on localhost (executor driver) (79/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 76.0 in stage 16.0 (TID 296) in 289 ms on localhost (executor driver) (80/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Running task 81.0 in stage 16.0 (TID 301)
26/06/26 13:26:26 INFO Executor: Finished task 82.0 in stage 16.0 (TID 302). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 83.0 in stage 16.0 (TID 303)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 84.0 in stage 16.0 (TID 304, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 82.0 in stage 16.0 (TID 302) in 69 ms on localhost (executor driver) (81/200)
26/06/26 13:26:26 INFO Executor: Running task 84.0 in stage 16.0 (TID 304)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO Executor: Finished task 84.0 in stage 16.0 (TID 304). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 85.0 in stage 16.0 (TID 305, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 84.0 in stage 16.0 (TID 304) in 15 ms on localhost (executor driver) (82/200)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 23 ms
26/06/26 13:26:26 INFO Executor: Finished task 81.0 in stage 16.0 (TID 301). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 85.0 in stage 16.0 (TID 305)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 86.0 in stage 16.0 (TID 306, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 86.0 in stage 16.0 (TID 306)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 81.0 in stage 16.0 (TID 301) in 99 ms on localhost (executor driver) (83/200)
26/06/26 13:26:26 INFO Executor: Finished task 83.0 in stage 16.0 (TID 303). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 80.0 in stage 16.0 (TID 300). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 87.0 in stage 16.0 (TID 307, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 88.0 in stage 16.0 (TID 308, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Finished task 86.0 in stage 16.0 (TID 306). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 88.0 in stage 16.0 (TID 308)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 89.0 in stage 16.0 (TID 309, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 87.0 in stage 16.0 (TID 307)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 83.0 in stage 16.0 (TID 303) in 112 ms on localhost (executor driver) (84/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 80.0 in stage 16.0 (TID 300) in 292 ms on localhost (executor driver) (85/200)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 86.0 in stage 16.0 (TID 306) in 20 ms on localhost (executor driver) (86/200)
26/06/26 13:26:26 INFO Executor: Finished task 87.0 in stage 16.0 (TID 307). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:26 INFO TaskSetManager: Starting task 90.0 in stage 16.0 (TID 310, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 87.0 in stage 16.0 (TID 307) in 16 ms on localhost (executor driver) (87/200)
26/06/26 13:26:26 INFO Executor: Finished task 88.0 in stage 16.0 (TID 308). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Running task 89.0 in stage 16.0 (TID 309)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 91.0 in stage 16.0 (TID 311, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 91.0 in stage 16.0 (TID 311)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:26 INFO TaskSetManager: Finished task 88.0 in stage 16.0 (TID 308) in 21 ms on localhost (executor driver) (88/200)
26/06/26 13:26:26 INFO Executor: Finished task 85.0 in stage 16.0 (TID 305). 3629 bytes result sent to driver
26/06/26 13:26:26 INFO Executor: Finished task 89.0 in stage 16.0 (TID 309). 3672 bytes result sent to driver
26/06/26 13:26:26 INFO TaskSetManager: Starting task 92.0 in stage 16.0 (TID 312, localhost, executor driver, partition 92, ANY, 7743 bytes)
26/06/26 13:26:26 INFO TaskSetManager: Starting task 93.0 in stage 16.0 (TID 313, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:26 INFO Executor: Running task 93.0 in stage 16.0 (TID 313)
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:26 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:26 INFO Executor: Running task 90.0 in stage 16.0 (TID 310)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 85.0 in stage 16.0 (TID 305) in 57 ms on localhost (executor driver) (89/200)
26/06/26 13:26:26 INFO Executor: Running task 92.0 in stage 16.0 (TID 312)
26/06/26 13:26:26 INFO TaskSetManager: Finished task 89.0 in stage 16.0 (TID 309) in 32 ms on localhost (executor driver) (90/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:27 INFO Executor: Finished task 93.0 in stage 16.0 (TID 313). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 94.0 in stage 16.0 (TID 314, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 93.0 in stage 16.0 (TID 313) in 20 ms on localhost (executor driver) (91/200)
26/06/26 13:26:27 INFO Executor: Running task 94.0 in stage 16.0 (TID 314)
26/06/26 13:26:27 INFO Executor: Finished task 91.0 in stage 16.0 (TID 311). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 95.0 in stage 16.0 (TID 315, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 94.0 in stage 16.0 (TID 314). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 95.0 in stage 16.0 (TID 315)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 91.0 in stage 16.0 (TID 311) in 47 ms on localhost (executor driver) (92/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 95.0 in stage 16.0 (TID 315). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 96.0 in stage 16.0 (TID 316, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 96.0 in stage 16.0 (TID 316)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 97.0 in stage 16.0 (TID 317, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 95.0 in stage 16.0 (TID 315) in 14 ms on localhost (executor driver) (93/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 94.0 in stage 16.0 (TID 314) in 35 ms on localhost (executor driver) (94/200)
26/06/26 13:26:27 INFO Executor: Finished task 96.0 in stage 16.0 (TID 316). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 98.0 in stage 16.0 (TID 318, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 96.0 in stage 16.0 (TID 316) in 14 ms on localhost (executor driver) (95/200)
26/06/26 13:26:27 INFO Executor: Finished task 92.0 in stage 16.0 (TID 312). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 90.0 in stage 16.0 (TID 310). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 99.0 in stage 16.0 (TID 319, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 100.0 in stage 16.0 (TID 320, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 99.0 in stage 16.0 (TID 319)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 92.0 in stage 16.0 (TID 312) in 68 ms on localhost (executor driver) (96/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 90.0 in stage 16.0 (TID 310) in 79 ms on localhost (executor driver) (97/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 97.0 in stage 16.0 (TID 317)
26/06/26 13:26:27 INFO Executor: Finished task 99.0 in stage 16.0 (TID 319). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 101.0 in stage 16.0 (TID 321, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 100.0 in stage 16.0 (TID 320)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 99.0 in stage 16.0 (TID 319) in 15 ms on localhost (executor driver) (98/200)
26/06/26 13:26:27 INFO Executor: Running task 98.0 in stage 16.0 (TID 318)
26/06/26 13:26:27 INFO Executor: Finished task 100.0 in stage 16.0 (TID 320). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 102.0 in stage 16.0 (TID 322, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 100.0 in stage 16.0 (TID 320) in 17 ms on localhost (executor driver) (99/200)
26/06/26 13:26:27 INFO Executor: Running task 101.0 in stage 16.0 (TID 321)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 97.0 in stage 16.0 (TID 317). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 101.0 in stage 16.0 (TID 321). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 103.0 in stage 16.0 (TID 323, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 104.0 in stage 16.0 (TID 324, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 98.0 in stage 16.0 (TID 318). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 105.0 in stage 16.0 (TID 325, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 105.0 in stage 16.0 (TID 325)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 97.0 in stage 16.0 (TID 317) in 54 ms on localhost (executor driver) (100/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 101.0 in stage 16.0 (TID 321) in 28 ms on localhost (executor driver) (101/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 98.0 in stage 16.0 (TID 318) in 46 ms on localhost (executor driver) (102/200)
26/06/26 13:26:27 INFO Executor: Finished task 105.0 in stage 16.0 (TID 325). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 106.0 in stage 16.0 (TID 326, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 106.0 in stage 16.0 (TID 326)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 105.0 in stage 16.0 (TID 325) in 12 ms on localhost (executor driver) (103/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:27 INFO Executor: Running task 104.0 in stage 16.0 (TID 324)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 106.0 in stage 16.0 (TID 326). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 102.0 in stage 16.0 (TID 322)
26/06/26 13:26:27 INFO Executor: Finished task 104.0 in stage 16.0 (TID 324). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 107.0 in stage 16.0 (TID 327, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 108.0 in stage 16.0 (TID 328, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 107.0 in stage 16.0 (TID 327)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 106.0 in stage 16.0 (TID 326) in 17 ms on localhost (executor driver) (104/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 104.0 in stage 16.0 (TID 324) in 31 ms on localhost (executor driver) (105/200)
26/06/26 13:26:27 INFO Executor: Finished task 102.0 in stage 16.0 (TID 322). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 108.0 in stage 16.0 (TID 328)
26/06/26 13:26:27 INFO Executor: Finished task 107.0 in stage 16.0 (TID 327). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 109.0 in stage 16.0 (TID 329, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 110.0 in stage 16.0 (TID 330, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 102.0 in stage 16.0 (TID 322) in 46 ms on localhost (executor driver) (106/200)
26/06/26 13:26:27 INFO Executor: Running task 109.0 in stage 16.0 (TID 329)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 107.0 in stage 16.0 (TID 327) in 12 ms on localhost (executor driver) (107/200)
26/06/26 13:26:27 INFO Executor: Finished task 108.0 in stage 16.0 (TID 328). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 103.0 in stage 16.0 (TID 323)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 109.0 in stage 16.0 (TID 329). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 111.0 in stage 16.0 (TID 331, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 112.0 in stage 16.0 (TID 332, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 111.0 in stage 16.0 (TID 331)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 108.0 in stage 16.0 (TID 328) in 22 ms on localhost (executor driver) (108/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 109.0 in stage 16.0 (TID 329) in 12 ms on localhost (executor driver) (109/200)
26/06/26 13:26:27 INFO Executor: Finished task 103.0 in stage 16.0 (TID 323). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 111.0 in stage 16.0 (TID 331). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 113.0 in stage 16.0 (TID 333, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 112.0 in stage 16.0 (TID 332)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 114.0 in stage 16.0 (TID 334, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 113.0 in stage 16.0 (TID 333)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 114.0 in stage 16.0 (TID 334)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 103.0 in stage 16.0 (TID 323) in 61 ms on localhost (executor driver) (110/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 111.0 in stage 16.0 (TID 331) in 15 ms on localhost (executor driver) (111/200)
26/06/26 13:26:27 INFO Executor: Finished task 113.0 in stage 16.0 (TID 333). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 115.0 in stage 16.0 (TID 335, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 114.0 in stage 16.0 (TID 334). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 113.0 in stage 16.0 (TID 333) in 11 ms on localhost (executor driver) (112/200)
26/06/26 13:26:27 INFO Executor: Running task 110.0 in stage 16.0 (TID 330)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 116.0 in stage 16.0 (TID 336, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 115.0 in stage 16.0 (TID 335)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 115.0 in stage 16.0 (TID 335). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 117.0 in stage 16.0 (TID 337, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 117.0 in stage 16.0 (TID 337)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 117.0 in stage 16.0 (TID 337). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 118.0 in stage 16.0 (TID 338, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO Executor: Running task 118.0 in stage 16.0 (TID 338)
26/06/26 13:26:27 INFO Executor: Finished task 112.0 in stage 16.0 (TID 332). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 118.0 in stage 16.0 (TID 338). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 119.0 in stage 16.0 (TID 339, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 120.0 in stage 16.0 (TID 340, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 119.0 in stage 16.0 (TID 339)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 114.0 in stage 16.0 (TID 334) in 32 ms on localhost (executor driver) (113/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 117.0 in stage 16.0 (TID 337) in 15 ms on localhost (executor driver) (114/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 115.0 in stage 16.0 (TID 335) in 22 ms on localhost (executor driver) (115/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 112.0 in stage 16.0 (TID 332) in 42 ms on localhost (executor driver) (116/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 118.0 in stage 16.0 (TID 338) in 9 ms on localhost (executor driver) (117/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 31 ms
26/06/26 13:26:27 INFO Executor: Finished task 110.0 in stage 16.0 (TID 330). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 120.0 in stage 16.0 (TID 340)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 121.0 in stage 16.0 (TID 341, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 110.0 in stage 16.0 (TID 330) in 76 ms on localhost (executor driver) (118/200)
26/06/26 13:26:27 INFO Executor: Running task 116.0 in stage 16.0 (TID 336)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 121.0 in stage 16.0 (TID 341)
26/06/26 13:26:27 INFO Executor: Finished task 119.0 in stage 16.0 (TID 339). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 122.0 in stage 16.0 (TID 342, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 119.0 in stage 16.0 (TID 339) in 41 ms on localhost (executor driver) (119/200)
26/06/26 13:26:27 INFO Executor: Finished task 120.0 in stage 16.0 (TID 340). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 123.0 in stage 16.0 (TID 343, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 123.0 in stage 16.0 (TID 343)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 120.0 in stage 16.0 (TID 340) in 49 ms on localhost (executor driver) (120/200)
26/06/26 13:26:27 INFO Executor: Running task 122.0 in stage 16.0 (TID 342)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 123.0 in stage 16.0 (TID 343). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 121.0 in stage 16.0 (TID 341). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 116.0 in stage 16.0 (TID 336). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 122.0 in stage 16.0 (TID 342). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 124.0 in stage 16.0 (TID 344, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 125.0 in stage 16.0 (TID 345, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 126.0 in stage 16.0 (TID 346, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 127.0 in stage 16.0 (TID 347, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 127.0 in stage 16.0 (TID 347)
26/06/26 13:26:27 INFO Executor: Running task 126.0 in stage 16.0 (TID 346)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 123.0 in stage 16.0 (TID 343) in 43 ms on localhost (executor driver) (121/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 121.0 in stage 16.0 (TID 341) in 62 ms on localhost (executor driver) (122/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 116.0 in stage 16.0 (TID 336) in 106 ms on localhost (executor driver) (123/200)
26/06/26 13:26:27 INFO Executor: Running task 125.0 in stage 16.0 (TID 345)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 122.0 in stage 16.0 (TID 342) in 48 ms on localhost (executor driver) (124/200)
26/06/26 13:26:27 INFO Executor: Running task 124.0 in stage 16.0 (TID 344)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 8 ms
26/06/26 13:26:27 INFO Executor: Finished task 127.0 in stage 16.0 (TID 347). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 128.0 in stage 16.0 (TID 348, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 127.0 in stage 16.0 (TID 347) in 21 ms on localhost (executor driver) (125/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Running task 128.0 in stage 16.0 (TID 348)
26/06/26 13:26:27 INFO Executor: Finished task 125.0 in stage 16.0 (TID 345). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 128.0 in stage 16.0 (TID 348). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 129.0 in stage 16.0 (TID 349, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 130.0 in stage 16.0 (TID 350, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 128.0 in stage 16.0 (TID 348) in 17 ms on localhost (executor driver) (126/200)
26/06/26 13:26:27 INFO Executor: Finished task 126.0 in stage 16.0 (TID 346). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 131.0 in stage 16.0 (TID 351, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 131.0 in stage 16.0 (TID 351)
26/06/26 13:26:27 INFO Executor: Running task 130.0 in stage 16.0 (TID 350)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 125.0 in stage 16.0 (TID 345) in 45 ms on localhost (executor driver) (127/200)
26/06/26 13:26:27 INFO Executor: Finished task 131.0 in stage 16.0 (TID 351). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 132.0 in stage 16.0 (TID 352, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 129.0 in stage 16.0 (TID 349)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 131.0 in stage 16.0 (TID 351) in 17 ms on localhost (executor driver) (128/200)
26/06/26 13:26:27 INFO Executor: Running task 132.0 in stage 16.0 (TID 352)
26/06/26 13:26:27 INFO Executor: Finished task 124.0 in stage 16.0 (TID 344). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 126.0 in stage 16.0 (TID 346) in 59 ms on localhost (executor driver) (129/200)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 133.0 in stage 16.0 (TID 353, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 124.0 in stage 16.0 (TID 344) in 64 ms on localhost (executor driver) (130/200)
26/06/26 13:26:27 INFO Executor: Running task 133.0 in stage 16.0 (TID 353)
26/06/26 13:26:27 INFO Executor: Finished task 130.0 in stage 16.0 (TID 350). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 132.0 in stage 16.0 (TID 352). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 129.0 in stage 16.0 (TID 349). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 134.0 in stage 16.0 (TID 354, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 135.0 in stage 16.0 (TID 355, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 135.0 in stage 16.0 (TID 355)
26/06/26 13:26:27 INFO Executor: Running task 134.0 in stage 16.0 (TID 354)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 133.0 in stage 16.0 (TID 353). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 135.0 in stage 16.0 (TID 355). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 136.0 in stage 16.0 (TID 356, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 137.0 in stage 16.0 (TID 357, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 138.0 in stage 16.0 (TID 358, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 137.0 in stage 16.0 (TID 357)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 133.0 in stage 16.0 (TID 353) in 24 ms on localhost (executor driver) (131/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 135.0 in stage 16.0 (TID 355) in 8 ms on localhost (executor driver) (132/200)
26/06/26 13:26:27 INFO Executor: Running task 138.0 in stage 16.0 (TID 358)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 129.0 in stage 16.0 (TID 349) in 58 ms on localhost (executor driver) (133/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 132.0 in stage 16.0 (TID 352) in 49 ms on localhost (executor driver) (134/200)
26/06/26 13:26:27 INFO Executor: Finished task 137.0 in stage 16.0 (TID 357). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 130.0 in stage 16.0 (TID 350) in 59 ms on localhost (executor driver) (135/200)
26/06/26 13:26:27 INFO Executor: Finished task 138.0 in stage 16.0 (TID 358). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 139.0 in stage 16.0 (TID 359, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 136.0 in stage 16.0 (TID 356)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 140.0 in stage 16.0 (TID 360, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 138.0 in stage 16.0 (TID 358) in 11 ms on localhost (executor driver) (136/200)
26/06/26 13:26:27 INFO Executor: Running task 139.0 in stage 16.0 (TID 359)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 137.0 in stage 16.0 (TID 357) in 11 ms on localhost (executor driver) (137/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 134.0 in stage 16.0 (TID 354). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 141.0 in stage 16.0 (TID 361, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 134.0 in stage 16.0 (TID 354) in 24 ms on localhost (executor driver) (138/200)
26/06/26 13:26:27 INFO Executor: Finished task 136.0 in stage 16.0 (TID 356). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 142.0 in stage 16.0 (TID 362, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 6 ms
26/06/26 13:26:27 INFO Executor: Running task 140.0 in stage 16.0 (TID 360)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 139.0 in stage 16.0 (TID 359). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 142.0 in stage 16.0 (TID 362)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 143.0 in stage 16.0 (TID 363, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 140.0 in stage 16.0 (TID 360). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 144.0 in stage 16.0 (TID 364, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 144.0 in stage 16.0 (TID 364)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 136.0 in stage 16.0 (TID 356) in 33 ms on localhost (executor driver) (139/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 139.0 in stage 16.0 (TID 359) in 22 ms on localhost (executor driver) (140/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 140.0 in stage 16.0 (TID 360) in 21 ms on localhost (executor driver) (141/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 142.0 in stage 16.0 (TID 362). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 143.0 in stage 16.0 (TID 363)
26/06/26 13:26:27 INFO Executor: Finished task 144.0 in stage 16.0 (TID 364). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 145.0 in stage 16.0 (TID 365, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 146.0 in stage 16.0 (TID 366, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 142.0 in stage 16.0 (TID 362) in 19 ms on localhost (executor driver) (142/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 144.0 in stage 16.0 (TID 364) in 8 ms on localhost (executor driver) (143/200)
26/06/26 13:26:27 INFO Executor: Running task 146.0 in stage 16.0 (TID 366)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Running task 145.0 in stage 16.0 (TID 365)
26/06/26 13:26:27 INFO Executor: Finished task 146.0 in stage 16.0 (TID 366). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 141.0 in stage 16.0 (TID 361)
26/06/26 13:26:27 INFO Executor: Finished task 143.0 in stage 16.0 (TID 363). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 147.0 in stage 16.0 (TID 367, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 148.0 in stage 16.0 (TID 368, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 147.0 in stage 16.0 (TID 367)
26/06/26 13:26:27 INFO Executor: Running task 148.0 in stage 16.0 (TID 368)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 146.0 in stage 16.0 (TID 366) in 17 ms on localhost (executor driver) (144/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 143.0 in stage 16.0 (TID 363) in 25 ms on localhost (executor driver) (145/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 141.0 in stage 16.0 (TID 361). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 149.0 in stage 16.0 (TID 369, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 148.0 in stage 16.0 (TID 368). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 141.0 in stage 16.0 (TID 361) in 43 ms on localhost (executor driver) (146/200)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 150.0 in stage 16.0 (TID 370, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 148.0 in stage 16.0 (TID 368) in 10 ms on localhost (executor driver) (147/200)
26/06/26 13:26:27 INFO Executor: Finished task 147.0 in stage 16.0 (TID 367). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 151.0 in stage 16.0 (TID 371, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 151.0 in stage 16.0 (TID 371)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 147.0 in stage 16.0 (TID 367) in 13 ms on localhost (executor driver) (148/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 151.0 in stage 16.0 (TID 371). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 152.0 in stage 16.0 (TID 372, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 151.0 in stage 16.0 (TID 371) in 11 ms on localhost (executor driver) (149/200)
26/06/26 13:26:27 INFO Executor: Running task 150.0 in stage 16.0 (TID 370)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 149.0 in stage 16.0 (TID 369)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 150.0 in stage 16.0 (TID 370). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 153.0 in stage 16.0 (TID 373, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 150.0 in stage 16.0 (TID 370) in 18 ms on localhost (executor driver) (150/200)
26/06/26 13:26:27 INFO Executor: Running task 152.0 in stage 16.0 (TID 372)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 149.0 in stage 16.0 (TID 369). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 145.0 in stage 16.0 (TID 365). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 152.0 in stage 16.0 (TID 372). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 154.0 in stage 16.0 (TID 374, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 155.0 in stage 16.0 (TID 375, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 156.0 in stage 16.0 (TID 376, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 149.0 in stage 16.0 (TID 369) in 33 ms on localhost (executor driver) (151/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 145.0 in stage 16.0 (TID 365) in 54 ms on localhost (executor driver) (152/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 152.0 in stage 16.0 (TID 372) in 20 ms on localhost (executor driver) (153/200)
26/06/26 13:26:27 INFO Executor: Running task 154.0 in stage 16.0 (TID 374)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 155.0 in stage 16.0 (TID 375)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 154.0 in stage 16.0 (TID 374). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 157.0 in stage 16.0 (TID 377, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 154.0 in stage 16.0 (TID 374) in 9 ms on localhost (executor driver) (154/200)
26/06/26 13:26:27 INFO Executor: Running task 157.0 in stage 16.0 (TID 377)
26/06/26 13:26:27 INFO Executor: Running task 156.0 in stage 16.0 (TID 376)
26/06/26 13:26:27 INFO Executor: Running task 153.0 in stage 16.0 (TID 373)
26/06/26 13:26:27 INFO Executor: Finished task 155.0 in stage 16.0 (TID 375). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 157.0 in stage 16.0 (TID 377). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 158.0 in stage 16.0 (TID 378, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 158.0 in stage 16.0 (TID 378)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 153.0 in stage 16.0 (TID 373). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 155.0 in stage 16.0 (TID 375) in 31 ms on localhost (executor driver) (155/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 158.0 in stage 16.0 (TID 378). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 156.0 in stage 16.0 (TID 376). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 159.0 in stage 16.0 (TID 379, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 159.0 in stage 16.0 (TID 379)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 160.0 in stage 16.0 (TID 380, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 161.0 in stage 16.0 (TID 381, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 162.0 in stage 16.0 (TID 382, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 153.0 in stage 16.0 (TID 373) in 50 ms on localhost (executor driver) (156/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 158.0 in stage 16.0 (TID 378) in 13 ms on localhost (executor driver) (157/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 156.0 in stage 16.0 (TID 376) in 38 ms on localhost (executor driver) (158/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 157.0 in stage 16.0 (TID 377) in 30 ms on localhost (executor driver) (159/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 162.0 in stage 16.0 (TID 382)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 159.0 in stage 16.0 (TID 379). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 162.0 in stage 16.0 (TID 382). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 163.0 in stage 16.0 (TID 383, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 164.0 in stage 16.0 (TID 384, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 161.0 in stage 16.0 (TID 381)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 159.0 in stage 16.0 (TID 379) in 17 ms on localhost (executor driver) (160/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 162.0 in stage 16.0 (TID 382) in 16 ms on localhost (executor driver) (161/200)
26/06/26 13:26:27 INFO Executor: Running task 160.0 in stage 16.0 (TID 380)
26/06/26 13:26:27 INFO Executor: Finished task 161.0 in stage 16.0 (TID 381). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 164.0 in stage 16.0 (TID 384)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO Executor: Running task 163.0 in stage 16.0 (TID 383)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 165.0 in stage 16.0 (TID 385, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 161.0 in stage 16.0 (TID 381) in 19 ms on localhost (executor driver) (162/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 163.0 in stage 16.0 (TID 383). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 165.0 in stage 16.0 (TID 385)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 160.0 in stage 16.0 (TID 380). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 39 ms
26/06/26 13:26:27 INFO Executor: Finished task 165.0 in stage 16.0 (TID 385). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 164.0 in stage 16.0 (TID 384). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 166.0 in stage 16.0 (TID 386, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 167.0 in stage 16.0 (TID 387, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 168.0 in stage 16.0 (TID 388, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 169.0 in stage 16.0 (TID 389, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 165.0 in stage 16.0 (TID 385) in 49 ms on localhost (executor driver) (163/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 164.0 in stage 16.0 (TID 384) in 58 ms on localhost (executor driver) (164/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 163.0 in stage 16.0 (TID 383) in 58 ms on localhost (executor driver) (165/200)
26/06/26 13:26:27 INFO Executor: Running task 168.0 in stage 16.0 (TID 388)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 160.0 in stage 16.0 (TID 380) in 71 ms on localhost (executor driver) (166/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 166.0 in stage 16.0 (TID 386)
26/06/26 13:26:27 INFO Executor: Finished task 168.0 in stage 16.0 (TID 388). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 169.0 in stage 16.0 (TID 389)
26/06/26 13:26:27 INFO Executor: Running task 167.0 in stage 16.0 (TID 387)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 166.0 in stage 16.0 (TID 386). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 167.0 in stage 16.0 (TID 387). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 170.0 in stage 16.0 (TID 390, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 171.0 in stage 16.0 (TID 391, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 172.0 in stage 16.0 (TID 392, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 168.0 in stage 16.0 (TID 388) in 19 ms on localhost (executor driver) (167/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 166.0 in stage 16.0 (TID 386) in 21 ms on localhost (executor driver) (168/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 167.0 in stage 16.0 (TID 387) in 20 ms on localhost (executor driver) (169/200)
26/06/26 13:26:27 INFO Executor: Running task 170.0 in stage 16.0 (TID 390)
26/06/26 13:26:27 INFO Executor: Finished task 169.0 in stage 16.0 (TID 389). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 173.0 in stage 16.0 (TID 393, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 169.0 in stage 16.0 (TID 389) in 23 ms on localhost (executor driver) (170/200)
26/06/26 13:26:27 INFO Executor: Running task 173.0 in stage 16.0 (TID 393)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 170.0 in stage 16.0 (TID 390). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 171.0 in stage 16.0 (TID 391)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 174.0 in stage 16.0 (TID 394, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 170.0 in stage 16.0 (TID 390) in 14 ms on localhost (executor driver) (171/200)
26/06/26 13:26:27 INFO Executor: Running task 172.0 in stage 16.0 (TID 392)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO Executor: Running task 174.0 in stage 16.0 (TID 394)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 173.0 in stage 16.0 (TID 393). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 175.0 in stage 16.0 (TID 395, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 173.0 in stage 16.0 (TID 393) in 28 ms on localhost (executor driver) (172/200)
26/06/26 13:26:27 INFO Executor: Running task 175.0 in stage 16.0 (TID 395)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 172.0 in stage 16.0 (TID 392). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 174.0 in stage 16.0 (TID 394). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 176.0 in stage 16.0 (TID 396, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 176.0 in stage 16.0 (TID 396)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 177.0 in stage 16.0 (TID 397, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 172.0 in stage 16.0 (TID 392) in 52 ms on localhost (executor driver) (173/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 174.0 in stage 16.0 (TID 394) in 39 ms on localhost (executor driver) (174/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 176.0 in stage 16.0 (TID 396). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 177.0 in stage 16.0 (TID 397)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 177.0 in stage 16.0 (TID 397). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 178.0 in stage 16.0 (TID 398, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 179.0 in stage 16.0 (TID 399, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 179.0 in stage 16.0 (TID 399)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 176.0 in stage 16.0 (TID 396) in 31 ms on localhost (executor driver) (175/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 177.0 in stage 16.0 (TID 397) in 30 ms on localhost (executor driver) (176/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 73 ms
26/06/26 13:26:27 INFO Executor: Finished task 179.0 in stage 16.0 (TID 399). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 180.0 in stage 16.0 (TID 400, localhost, executor driver, partition 180, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 179.0 in stage 16.0 (TID 399) in 20 ms on localhost (executor driver) (177/200)
26/06/26 13:26:27 INFO Executor: Finished task 171.0 in stage 16.0 (TID 391). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 175.0 in stage 16.0 (TID 395). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 180.0 in stage 16.0 (TID 400)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 178.0 in stage 16.0 (TID 398)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 181.0 in stage 16.0 (TID 401, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 182.0 in stage 16.0 (TID 402, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 180.0 in stage 16.0 (TID 400). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 183.0 in stage 16.0 (TID 403, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 171.0 in stage 16.0 (TID 391) in 113 ms on localhost (executor driver) (178/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 175.0 in stage 16.0 (TID 395) in 86 ms on localhost (executor driver) (179/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 180.0 in stage 16.0 (TID 400) in 15 ms on localhost (executor driver) (180/200)
26/06/26 13:26:27 INFO Executor: Running task 181.0 in stage 16.0 (TID 401)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 5 ms
26/06/26 13:26:27 INFO Executor: Running task 183.0 in stage 16.0 (TID 403)
26/06/26 13:26:27 INFO Executor: Finished task 181.0 in stage 16.0 (TID 401). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 184.0 in stage 16.0 (TID 404, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 181.0 in stage 16.0 (TID 401) in 12 ms on localhost (executor driver) (181/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 178.0 in stage 16.0 (TID 398). 3672 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 182.0 in stage 16.0 (TID 402)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 185.0 in stage 16.0 (TID 405, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 178.0 in stage 16.0 (TID 398) in 50 ms on localhost (executor driver) (182/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 185.0 in stage 16.0 (TID 405)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 184.0 in stage 16.0 (TID 404)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 183.0 in stage 16.0 (TID 403). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 186.0 in stage 16.0 (TID 406, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 183.0 in stage 16.0 (TID 403) in 39 ms on localhost (executor driver) (183/200)
26/06/26 13:26:27 INFO Executor: Running task 186.0 in stage 16.0 (TID 406)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 185.0 in stage 16.0 (TID 405). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 184.0 in stage 16.0 (TID 404). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 182.0 in stage 16.0 (TID 402). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 187.0 in stage 16.0 (TID 407, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 187.0 in stage 16.0 (TID 407)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 188.0 in stage 16.0 (TID 408, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 189.0 in stage 16.0 (TID 409, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 184.0 in stage 16.0 (TID 404) in 51 ms on localhost (executor driver) (184/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 182.0 in stage 16.0 (TID 402) in 63 ms on localhost (executor driver) (185/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO Executor: Running task 189.0 in stage 16.0 (TID 409)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 185.0 in stage 16.0 (TID 405) in 49 ms on localhost (executor driver) (186/200)
26/06/26 13:26:27 INFO Executor: Running task 188.0 in stage 16.0 (TID 408)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 186.0 in stage 16.0 (TID 406). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 190.0 in stage 16.0 (TID 410, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 190.0 in stage 16.0 (TID 410)
26/06/26 13:26:27 INFO Executor: Finished task 189.0 in stage 16.0 (TID 409). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 186.0 in stage 16.0 (TID 406) in 54 ms on localhost (executor driver) (187/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Starting task 191.0 in stage 16.0 (TID 411, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 189.0 in stage 16.0 (TID 409) in 36 ms on localhost (executor driver) (188/200)
26/06/26 13:26:27 INFO Executor: Running task 191.0 in stage 16.0 (TID 411)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 188.0 in stage 16.0 (TID 408). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 192.0 in stage 16.0 (TID 412, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 192.0 in stage 16.0 (TID 412)
26/06/26 13:26:27 INFO Executor: Finished task 190.0 in stage 16.0 (TID 410). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 188.0 in stage 16.0 (TID 408) in 45 ms on localhost (executor driver) (189/200)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 193.0 in stage 16.0 (TID 413, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Finished task 187.0 in stage 16.0 (TID 407). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 194.0 in stage 16.0 (TID 414, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 194.0 in stage 16.0 (TID 414)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 190.0 in stage 16.0 (TID 410) in 29 ms on localhost (executor driver) (190/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 187.0 in stage 16.0 (TID 407) in 55 ms on localhost (executor driver) (191/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Running task 193.0 in stage 16.0 (TID 413)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 191.0 in stage 16.0 (TID 411). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 195.0 in stage 16.0 (TID 415, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 195.0 in stage 16.0 (TID 415)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 191.0 in stage 16.0 (TID 411) in 27 ms on localhost (executor driver) (192/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 193.0 in stage 16.0 (TID 413). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 192.0 in stage 16.0 (TID 412). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Finished task 194.0 in stage 16.0 (TID 414). 3586 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 196.0 in stage 16.0 (TID 416, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:27 INFO Executor: Running task 196.0 in stage 16.0 (TID 416)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 197.0 in stage 16.0 (TID 417, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Starting task 198.0 in stage 16.0 (TID 418, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO TaskSetManager: Finished task 193.0 in stage 16.0 (TID 413) in 25 ms on localhost (executor driver) (193/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 192.0 in stage 16.0 (TID 412) in 32 ms on localhost (executor driver) (194/200)
26/06/26 13:26:27 INFO Executor: Running task 197.0 in stage 16.0 (TID 417)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 194.0 in stage 16.0 (TID 414) in 24 ms on localhost (executor driver) (195/200)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Running task 198.0 in stage 16.0 (TID 418)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:27 INFO Executor: Finished task 195.0 in stage 16.0 (TID 415). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Starting task 199.0 in stage 16.0 (TID 419, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 195.0 in stage 16.0 (TID 415) in 30 ms on localhost (executor driver) (196/200)
26/06/26 13:26:27 INFO Executor: Finished task 196.0 in stage 16.0 (TID 416). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 196.0 in stage 16.0 (TID 416) in 24 ms on localhost (executor driver) (197/200)
26/06/26 13:26:27 INFO Executor: Finished task 198.0 in stage 16.0 (TID 418). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO Executor: Running task 199.0 in stage 16.0 (TID 419)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 198.0 in stage 16.0 (TID 418) in 40 ms on localhost (executor driver) (198/200)
26/06/26 13:26:27 INFO Executor: Finished task 197.0 in stage 16.0 (TID 417). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 199.0 in stage 16.0 (TID 419). 3629 bytes result sent to driver
26/06/26 13:26:27 INFO TaskSetManager: Finished task 197.0 in stage 16.0 (TID 417) in 59 ms on localhost (executor driver) (199/200)
26/06/26 13:26:27 INFO TaskSetManager: Finished task 199.0 in stage 16.0 (TID 419) in 39 ms on localhost (executor driver) (200/200)
26/06/26 13:26:27 INFO TaskSchedulerImpl: Removed TaskSet 16.0, whose tasks have all completed, from pool 
26/06/26 13:26:27 INFO DAGScheduler: ShuffleMapStage 16 (count at NativeMethodAccessorImpl.java:0) finished in 1.956 s
26/06/26 13:26:27 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:27 INFO DAGScheduler: running: Set()
26/06/26 13:26:27 INFO DAGScheduler: waiting: Set(ResultStage 17)
26/06/26 13:26:27 INFO DAGScheduler: failed: Set()
26/06/26 13:26:27 INFO DAGScheduler: Submitting ResultStage 17 (MapPartitionsRDD[68] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:27 INFO MemoryStore: Block broadcast_20 stored as values in memory (estimated size 7.3 KB, free 365.0 MB)
26/06/26 13:26:27 INFO MemoryStore: Block broadcast_20_piece0 stored as bytes in memory (estimated size 3.8 KB, free 365.0 MB)
26/06/26 13:26:27 INFO BlockManagerInfo: Added broadcast_20_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:27 INFO SparkContext: Created broadcast 20 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:27 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 17 (MapPartitionsRDD[68] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:27 INFO TaskSchedulerImpl: Adding task set 17.0 with 1 tasks
26/06/26 13:26:27 INFO TaskSetManager: Starting task 0.0 in stage 17.0 (TID 420, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:27 INFO Executor: Running task 0.0 in stage 17.0 (TID 420)
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:27 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:27 INFO Executor: Finished task 0.0 in stage 17.0 (TID 420). 1782 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Finished task 0.0 in stage 17.0 (TID 420) in 133 ms on localhost (executor driver) (1/1)
26/06/26 13:26:28 INFO TaskSchedulerImpl: Removed TaskSet 17.0, whose tasks have all completed, from pool 
26/06/26 13:26:28 INFO DAGScheduler: ResultStage 17 (count at NativeMethodAccessorImpl.java:0) finished in 0.144 s
26/06/26 13:26:28 INFO DAGScheduler: Job 10 finished: count at NativeMethodAccessorImpl.java:0, took 3.820198 s
('Ratings :', 100000)
26/06/26 13:26:28 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:28 INFO HashAggregateExec: spark.sql.codegen.aggregate.map.twolevel.enabled is set to true, but current version of codegened fast hashmap does not support this aggregate.
26/06/26 13:26:28 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
26/06/26 13:26:28 INFO DAGScheduler: Registering RDD 71 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:28 INFO DAGScheduler: Registering RDD 74 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:28 INFO DAGScheduler: Got job 11 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:28 INFO DAGScheduler: Final stage: ResultStage 20 (count at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:28 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 19)
26/06/26 13:26:28 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 19)
26/06/26 13:26:28 INFO DAGScheduler: Submitting ShuffleMapStage 18 (MapPartitionsRDD[71] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:28 INFO MemoryStore: Block broadcast_21 stored as values in memory (estimated size 38.1 KB, free 364.9 MB)
26/06/26 13:26:28 INFO MemoryStore: Block broadcast_21_piece0 stored as bytes in memory (estimated size 19.2 KB, free 364.9 MB)
26/06/26 13:26:28 INFO BlockManagerInfo: Added broadcast_21_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 19.2 KB, free: 366.1 MB)
26/06/26 13:26:28 INFO SparkContext: Created broadcast 21 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:28 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 18 (MapPartitionsRDD[71] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:28 INFO TaskSchedulerImpl: Adding task set 18.0 with 2 tasks
26/06/26 13:26:28 INFO TaskSetManager: Starting task 0.0 in stage 18.0 (TID 421, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 1.0 in stage 18.0 (TID 422, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:28 INFO Executor: Running task 0.0 in stage 18.0 (TID 421)
26/06/26 13:26:28 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:0+118172
26/06/26 13:26:28 INFO Executor: Running task 1.0 in stage 18.0 (TID 422)
26/06/26 13:26:28 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:118172+118172
26/06/26 13:26:28 INFO PythonRunner: Times: total = 71, boot = -2947, init = 2970, finish = 48
26/06/26 13:26:28 INFO Executor: Finished task 1.0 in stage 18.0 (TID 422). 2655 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Finished task 1.0 in stage 18.0 (TID 422) in 178 ms on localhost (executor driver) (1/2)
26/06/26 13:26:28 INFO PythonRunner: Times: total = 139, boot = -2952, init = 2961, finish = 130
26/06/26 13:26:28 INFO BlockManagerInfo: Removed broadcast_20_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:28 INFO ContextCleaner: Cleaned accumulator 559
26/06/26 13:26:28 INFO ContextCleaner: Cleaned accumulator 558
26/06/26 13:26:28 INFO Executor: Finished task 0.0 in stage 18.0 (TID 421). 2698 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Finished task 0.0 in stage 18.0 (TID 421) in 553 ms on localhost (executor driver) (2/2)
26/06/26 13:26:28 INFO TaskSchedulerImpl: Removed TaskSet 18.0, whose tasks have all completed, from pool 
26/06/26 13:26:28 INFO DAGScheduler: ShuffleMapStage 18 (count at NativeMethodAccessorImpl.java:0) finished in 0.573 s
26/06/26 13:26:28 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:28 INFO DAGScheduler: running: Set()
26/06/26 13:26:28 INFO DAGScheduler: waiting: Set(ShuffleMapStage 19, ResultStage 20)
26/06/26 13:26:28 INFO DAGScheduler: failed: Set()
26/06/26 13:26:28 INFO DAGScheduler: Submitting ShuffleMapStage 19 (MapPartitionsRDD[74] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:28 INFO MemoryStore: Block broadcast_22 stored as values in memory (estimated size 42.8 KB, free 364.9 MB)
26/06/26 13:26:28 INFO MemoryStore: Block broadcast_22_piece0 stored as bytes in memory (estimated size 21.8 KB, free 364.9 MB)
26/06/26 13:26:28 INFO BlockManagerInfo: Added broadcast_22_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 21.8 KB, free: 366.1 MB)
26/06/26 13:26:28 INFO SparkContext: Created broadcast 22 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:28 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 19 (MapPartitionsRDD[74] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:28 INFO TaskSchedulerImpl: Adding task set 19.0 with 200 tasks
26/06/26 13:26:28 INFO TaskSetManager: Starting task 0.0 in stage 19.0 (TID 423, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 1.0 in stage 19.0 (TID 424, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 2.0 in stage 19.0 (TID 425, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 3.0 in stage 19.0 (TID 426, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:28 INFO Executor: Running task 3.0 in stage 19.0 (TID 426)
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO Executor: Running task 0.0 in stage 19.0 (TID 423)
26/06/26 13:26:28 INFO Executor: Running task 2.0 in stage 19.0 (TID 425)
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO Executor: Finished task 3.0 in stage 19.0 (TID 426). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO TaskSetManager: Starting task 4.0 in stage 19.0 (TID 427, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:28 INFO Executor: Running task 4.0 in stage 19.0 (TID 427)
26/06/26 13:26:28 INFO Executor: Running task 1.0 in stage 19.0 (TID 424)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 3.0 in stage 19.0 (TID 426) in 19 ms on localhost (executor driver) (1/200)
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO Executor: Finished task 0.0 in stage 19.0 (TID 423). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Starting task 5.0 in stage 19.0 (TID 428, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 0.0 in stage 19.0 (TID 423) in 44 ms on localhost (executor driver) (2/200)
26/06/26 13:26:28 INFO Executor: Running task 5.0 in stage 19.0 (TID 428)
26/06/26 13:26:28 INFO Executor: Finished task 4.0 in stage 19.0 (TID 427). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO Executor: Finished task 2.0 in stage 19.0 (TID 425). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Starting task 6.0 in stage 19.0 (TID 429, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:28 INFO Executor: Finished task 1.0 in stage 19.0 (TID 424). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Starting task 7.0 in stage 19.0 (TID 430, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:28 INFO Executor: Running task 6.0 in stage 19.0 (TID 429)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 8.0 in stage 19.0 (TID 431, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO Executor: Running task 7.0 in stage 19.0 (TID 430)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 4.0 in stage 19.0 (TID 427) in 44 ms on localhost (executor driver) (3/200)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 2.0 in stage 19.0 (TID 425) in 61 ms on localhost (executor driver) (4/200)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 1.0 in stage 19.0 (TID 424) in 62 ms on localhost (executor driver) (5/200)
26/06/26 13:26:28 INFO Executor: Running task 8.0 in stage 19.0 (TID 431)
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:28 INFO Executor: Finished task 8.0 in stage 19.0 (TID 431). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Starting task 9.0 in stage 19.0 (TID 432, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 8.0 in stage 19.0 (TID 431) in 60 ms on localhost (executor driver) (6/200)
26/06/26 13:26:28 INFO Executor: Running task 9.0 in stage 19.0 (TID 432)
26/06/26 13:26:28 INFO Executor: Finished task 7.0 in stage 19.0 (TID 430). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:28 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:28 INFO TaskSetManager: Starting task 10.0 in stage 19.0 (TID 433, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:28 INFO Executor: Finished task 6.0 in stage 19.0 (TID 429). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Finished task 7.0 in stage 19.0 (TID 430) in 76 ms on localhost (executor driver) (7/200)
26/06/26 13:26:28 INFO TaskSetManager: Starting task 11.0 in stage 19.0 (TID 434, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 6.0 in stage 19.0 (TID 429) in 78 ms on localhost (executor driver) (8/200)
26/06/26 13:26:28 INFO Executor: Finished task 9.0 in stage 19.0 (TID 432). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO TaskSetManager: Starting task 12.0 in stage 19.0 (TID 435, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:28 INFO TaskSetManager: Finished task 9.0 in stage 19.0 (TID 432) in 20 ms on localhost (executor driver) (9/200)
26/06/26 13:26:28 INFO Executor: Running task 12.0 in stage 19.0 (TID 435)
26/06/26 13:26:28 INFO Executor: Finished task 5.0 in stage 19.0 (TID 428). 3629 bytes result sent to driver
26/06/26 13:26:28 INFO Executor: Running task 11.0 in stage 19.0 (TID 434)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 13.0 in stage 19.0 (TID 436, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 13.0 in stage 19.0 (TID 436)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 5.0 in stage 19.0 (TID 428) in 105 ms on localhost (executor driver) (10/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 10.0 in stage 19.0 (TID 433)
26/06/26 13:26:29 INFO Executor: Finished task 12.0 in stage 19.0 (TID 435). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 13.0 in stage 19.0 (TID 436). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 14.0 in stage 19.0 (TID 437, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 12.0 in stage 19.0 (TID 435) in 35 ms on localhost (executor driver) (11/200)
26/06/26 13:26:29 INFO Executor: Running task 14.0 in stage 19.0 (TID 437)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 13.0 in stage 19.0 (TID 436) in 24 ms on localhost (executor driver) (12/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 15.0 in stage 19.0 (TID 438, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 15.0 in stage 19.0 (TID 438)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 11.0 in stage 19.0 (TID 434). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 10.0 in stage 19.0 (TID 433). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 15.0 in stage 19.0 (TID 438). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 16.0 in stage 19.0 (TID 439, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 17.0 in stage 19.0 (TID 440, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 14.0 in stage 19.0 (TID 437). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 18.0 in stage 19.0 (TID 441, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 16.0 in stage 19.0 (TID 439)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 19.0 in stage 19.0 (TID 442, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 11.0 in stage 19.0 (TID 434) in 59 ms on localhost (executor driver) (13/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 10.0 in stage 19.0 (TID 433) in 68 ms on localhost (executor driver) (14/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 15.0 in stage 19.0 (TID 438) in 18 ms on localhost (executor driver) (15/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 14.0 in stage 19.0 (TID 437) in 22 ms on localhost (executor driver) (16/200)
26/06/26 13:26:29 INFO Executor: Running task 19.0 in stage 19.0 (TID 442)
26/06/26 13:26:29 INFO Executor: Running task 18.0 in stage 19.0 (TID 441)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 16.0 in stage 19.0 (TID 439). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 17.0 in stage 19.0 (TID 440)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 20.0 in stage 19.0 (TID 443, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 16.0 in stage 19.0 (TID 439) in 18 ms on localhost (executor driver) (17/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 20.0 in stage 19.0 (TID 443)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 19.0 in stage 19.0 (TID 442). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 21.0 in stage 19.0 (TID 444, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 19.0 in stage 19.0 (TID 442) in 32 ms on localhost (executor driver) (18/200)
26/06/26 13:26:29 INFO Executor: Finished task 18.0 in stage 19.0 (TID 441). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 22.0 in stage 19.0 (TID 445, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 18.0 in stage 19.0 (TID 441) in 35 ms on localhost (executor driver) (19/200)
26/06/26 13:26:29 INFO Executor: Running task 22.0 in stage 19.0 (TID 445)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 21.0 in stage 19.0 (TID 444)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 20.0 in stage 19.0 (TID 443). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 23.0 in stage 19.0 (TID 446, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 20.0 in stage 19.0 (TID 443) in 43 ms on localhost (executor driver) (20/200)
26/06/26 13:26:29 INFO Executor: Running task 23.0 in stage 19.0 (TID 446)
26/06/26 13:26:29 INFO Executor: Finished task 21.0 in stage 19.0 (TID 444). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 24.0 in stage 19.0 (TID 447, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 21.0 in stage 19.0 (TID 444) in 35 ms on localhost (executor driver) (21/200)
26/06/26 13:26:29 INFO Executor: Finished task 22.0 in stage 19.0 (TID 445). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 25.0 in stage 19.0 (TID 448, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 17.0 in stage 19.0 (TID 440). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 24.0 in stage 19.0 (TID 447)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 26.0 in stage 19.0 (TID 449, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 26.0 in stage 19.0 (TID 449)
26/06/26 13:26:29 INFO Executor: Running task 25.0 in stage 19.0 (TID 448)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 17.0 in stage 19.0 (TID 440) in 87 ms on localhost (executor driver) (22/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 22.0 in stage 19.0 (TID 445) in 52 ms on localhost (executor driver) (23/200)
26/06/26 13:26:29 INFO Executor: Finished task 23.0 in stage 19.0 (TID 446). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 24.0 in stage 19.0 (TID 447). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 25.0 in stage 19.0 (TID 448). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 26.0 in stage 19.0 (TID 449). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 27.0 in stage 19.0 (TID 450, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 28.0 in stage 19.0 (TID 451, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 29.0 in stage 19.0 (TID 452, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 30.0 in stage 19.0 (TID 453, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 24.0 in stage 19.0 (TID 447) in 51 ms on localhost (executor driver) (24/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 25.0 in stage 19.0 (TID 448) in 50 ms on localhost (executor driver) (25/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 26.0 in stage 19.0 (TID 449) in 50 ms on localhost (executor driver) (26/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 23.0 in stage 19.0 (TID 446) in 62 ms on localhost (executor driver) (27/200)
26/06/26 13:26:29 INFO Executor: Running task 27.0 in stage 19.0 (TID 450)
26/06/26 13:26:29 INFO Executor: Running task 30.0 in stage 19.0 (TID 453)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 29.0 in stage 19.0 (TID 452)
26/06/26 13:26:29 INFO Executor: Finished task 27.0 in stage 19.0 (TID 450). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 31.0 in stage 19.0 (TID 454, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 28.0 in stage 19.0 (TID 451)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 27.0 in stage 19.0 (TID 450) in 56 ms on localhost (executor driver) (28/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 30.0 in stage 19.0 (TID 453). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 32.0 in stage 19.0 (TID 455, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 32.0 in stage 19.0 (TID 455)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 30.0 in stage 19.0 (TID 453) in 61 ms on localhost (executor driver) (29/200)
26/06/26 13:26:29 INFO Executor: Running task 31.0 in stage 19.0 (TID 454)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 28.0 in stage 19.0 (TID 451). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 33.0 in stage 19.0 (TID 456, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 28.0 in stage 19.0 (TID 451) in 76 ms on localhost (executor driver) (30/200)
26/06/26 13:26:29 INFO Executor: Finished task 31.0 in stage 19.0 (TID 454). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 34.0 in stage 19.0 (TID 457, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 31.0 in stage 19.0 (TID 454) in 50 ms on localhost (executor driver) (31/200)
26/06/26 13:26:29 INFO Executor: Finished task 29.0 in stage 19.0 (TID 452). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 35.0 in stage 19.0 (TID 458, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 35.0 in stage 19.0 (TID 458)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO Executor: Running task 34.0 in stage 19.0 (TID 457)
26/06/26 13:26:29 INFO Executor: Running task 33.0 in stage 19.0 (TID 456)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 9 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 29.0 in stage 19.0 (TID 452) in 91 ms on localhost (executor driver) (32/200)
26/06/26 13:26:29 INFO Executor: Finished task 34.0 in stage 19.0 (TID 457). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 36.0 in stage 19.0 (TID 459, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 36.0 in stage 19.0 (TID 459)
26/06/26 13:26:29 INFO Executor: Finished task 33.0 in stage 19.0 (TID 456). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 34.0 in stage 19.0 (TID 457) in 29 ms on localhost (executor driver) (33/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 37.0 in stage 19.0 (TID 460, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 33.0 in stage 19.0 (TID 456) in 32 ms on localhost (executor driver) (34/200)
26/06/26 13:26:29 INFO Executor: Running task 37.0 in stage 19.0 (TID 460)
26/06/26 13:26:29 INFO Executor: Finished task 32.0 in stage 19.0 (TID 455). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 35.0 in stage 19.0 (TID 458). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 37.0 in stage 19.0 (TID 460). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 36.0 in stage 19.0 (TID 459). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 38.0 in stage 19.0 (TID 461, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 39.0 in stage 19.0 (TID 462, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 40.0 in stage 19.0 (TID 463, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 41.0 in stage 19.0 (TID 464, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 39.0 in stage 19.0 (TID 462)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 32.0 in stage 19.0 (TID 455) in 122 ms on localhost (executor driver) (35/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 35.0 in stage 19.0 (TID 458) in 87 ms on localhost (executor driver) (36/200)
26/06/26 13:26:29 INFO Executor: Running task 40.0 in stage 19.0 (TID 463)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 37.0 in stage 19.0 (TID 460) in 60 ms on localhost (executor driver) (37/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 36.0 in stage 19.0 (TID 459) in 72 ms on localhost (executor driver) (38/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Running task 41.0 in stage 19.0 (TID 464)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Running task 38.0 in stage 19.0 (TID 461)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 39.0 in stage 19.0 (TID 462). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 40.0 in stage 19.0 (TID 463). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 41.0 in stage 19.0 (TID 464). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 38.0 in stage 19.0 (TID 461). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 42.0 in stage 19.0 (TID 465, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 43.0 in stage 19.0 (TID 466, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 44.0 in stage 19.0 (TID 467, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 45.0 in stage 19.0 (TID 468, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 44.0 in stage 19.0 (TID 467)
26/06/26 13:26:29 INFO Executor: Running task 42.0 in stage 19.0 (TID 465)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 39.0 in stage 19.0 (TID 462) in 76 ms on localhost (executor driver) (39/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 40.0 in stage 19.0 (TID 463) in 76 ms on localhost (executor driver) (40/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 41.0 in stage 19.0 (TID 464) in 77 ms on localhost (executor driver) (41/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 38.0 in stage 19.0 (TID 461) in 79 ms on localhost (executor driver) (42/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 45.0 in stage 19.0 (TID 468)
26/06/26 13:26:29 INFO Executor: Running task 43.0 in stage 19.0 (TID 466)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 45.0 in stage 19.0 (TID 468). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 42.0 in stage 19.0 (TID 465). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 44.0 in stage 19.0 (TID 467). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 43.0 in stage 19.0 (TID 466). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 46.0 in stage 19.0 (TID 469, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 47.0 in stage 19.0 (TID 470, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 47.0 in stage 19.0 (TID 470)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 48.0 in stage 19.0 (TID 471, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 49.0 in stage 19.0 (TID 472, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 48.0 in stage 19.0 (TID 471)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 45.0 in stage 19.0 (TID 468) in 53 ms on localhost (executor driver) (43/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 42.0 in stage 19.0 (TID 465) in 58 ms on localhost (executor driver) (44/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 44.0 in stage 19.0 (TID 467) in 58 ms on localhost (executor driver) (45/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 43.0 in stage 19.0 (TID 466) in 58 ms on localhost (executor driver) (46/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 46.0 in stage 19.0 (TID 469)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 48.0 in stage 19.0 (TID 471). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 49.0 in stage 19.0 (TID 472)
26/06/26 13:26:29 INFO Executor: Finished task 46.0 in stage 19.0 (TID 469). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 49.0 in stage 19.0 (TID 472). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 50.0 in stage 19.0 (TID 473, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 51.0 in stage 19.0 (TID 474, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 52.0 in stage 19.0 (TID 475, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 48.0 in stage 19.0 (TID 471) in 19 ms on localhost (executor driver) (47/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 46.0 in stage 19.0 (TID 469) in 20 ms on localhost (executor driver) (48/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 49.0 in stage 19.0 (TID 472) in 19 ms on localhost (executor driver) (49/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 47.0 in stage 19.0 (TID 470). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 51.0 in stage 19.0 (TID 474)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 53.0 in stage 19.0 (TID 476, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 50.0 in stage 19.0 (TID 473)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 47.0 in stage 19.0 (TID 470) in 31 ms on localhost (executor driver) (50/200)
26/06/26 13:26:29 INFO Executor: Finished task 50.0 in stage 19.0 (TID 473). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 54.0 in stage 19.0 (TID 477, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 50.0 in stage 19.0 (TID 473) in 19 ms on localhost (executor driver) (51/200)
26/06/26 13:26:29 INFO Executor: Running task 52.0 in stage 19.0 (TID 475)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:29 INFO Executor: Running task 53.0 in stage 19.0 (TID 476)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 51.0 in stage 19.0 (TID 474). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 55.0 in stage 19.0 (TID 478, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 51.0 in stage 19.0 (TID 474) in 38 ms on localhost (executor driver) (52/200)
26/06/26 13:26:29 INFO Executor: Running task 54.0 in stage 19.0 (TID 477)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 54.0 in stage 19.0 (TID 477). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 56.0 in stage 19.0 (TID 479, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 54.0 in stage 19.0 (TID 477) in 51 ms on localhost (executor driver) (53/200)
26/06/26 13:26:29 INFO Executor: Finished task 52.0 in stage 19.0 (TID 475). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 57.0 in stage 19.0 (TID 480, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 52.0 in stage 19.0 (TID 475) in 76 ms on localhost (executor driver) (54/200)
26/06/26 13:26:29 INFO Executor: Finished task 53.0 in stage 19.0 (TID 476). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 57.0 in stage 19.0 (TID 480)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 58.0 in stage 19.0 (TID 481, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 58.0 in stage 19.0 (TID 481)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 53.0 in stage 19.0 (TID 476) in 71 ms on localhost (executor driver) (55/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 57.0 in stage 19.0 (TID 480). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 58.0 in stage 19.0 (TID 481). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 59.0 in stage 19.0 (TID 482, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 60.0 in stage 19.0 (TID 483, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 59.0 in stage 19.0 (TID 482)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 58.0 in stage 19.0 (TID 481) in 9 ms on localhost (executor driver) (56/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 57.0 in stage 19.0 (TID 480) in 12 ms on localhost (executor driver) (57/200)
26/06/26 13:26:29 INFO Executor: Running task 56.0 in stage 19.0 (TID 479)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 59.0 in stage 19.0 (TID 482). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 60.0 in stage 19.0 (TID 483)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 61.0 in stage 19.0 (TID 484, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 61.0 in stage 19.0 (TID 484)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 59.0 in stage 19.0 (TID 482) in 13 ms on localhost (executor driver) (58/200)
26/06/26 13:26:29 INFO Executor: Finished task 56.0 in stage 19.0 (TID 479). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 61.0 in stage 19.0 (TID 484). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 62.0 in stage 19.0 (TID 485, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 63.0 in stage 19.0 (TID 486, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 62.0 in stage 19.0 (TID 485)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 56.0 in stage 19.0 (TID 479) in 41 ms on localhost (executor driver) (59/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 61.0 in stage 19.0 (TID 484) in 18 ms on localhost (executor driver) (60/200)
26/06/26 13:26:29 INFO Executor: Running task 63.0 in stage 19.0 (TID 486)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 63.0 in stage 19.0 (TID 486). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 62.0 in stage 19.0 (TID 485). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 60.0 in stage 19.0 (TID 483). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 64.0 in stage 19.0 (TID 487, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 65.0 in stage 19.0 (TID 488, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 66.0 in stage 19.0 (TID 489, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 63.0 in stage 19.0 (TID 486) in 20 ms on localhost (executor driver) (61/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 62.0 in stage 19.0 (TID 485) in 21 ms on localhost (executor driver) (62/200)
26/06/26 13:26:29 INFO Executor: Running task 64.0 in stage 19.0 (TID 487)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 60.0 in stage 19.0 (TID 483) in 35 ms on localhost (executor driver) (63/200)
26/06/26 13:26:29 INFO Executor: Running task 65.0 in stage 19.0 (TID 488)
26/06/26 13:26:29 INFO Executor: Running task 66.0 in stage 19.0 (TID 489)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 64.0 in stage 19.0 (TID 487). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 67.0 in stage 19.0 (TID 490, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 55.0 in stage 19.0 (TID 478)
26/06/26 13:26:29 INFO Executor: Finished task 65.0 in stage 19.0 (TID 488). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 67.0 in stage 19.0 (TID 490)
26/06/26 13:26:29 INFO Executor: Finished task 66.0 in stage 19.0 (TID 489). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 64.0 in stage 19.0 (TID 487) in 24 ms on localhost (executor driver) (64/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 68.0 in stage 19.0 (TID 491, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 69.0 in stage 19.0 (TID 492, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO TaskSetManager: Finished task 65.0 in stage 19.0 (TID 488) in 25 ms on localhost (executor driver) (65/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 66.0 in stage 19.0 (TID 489) in 25 ms on localhost (executor driver) (66/200)
26/06/26 13:26:29 INFO Executor: Running task 68.0 in stage 19.0 (TID 491)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 69.0 in stage 19.0 (TID 492)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 67.0 in stage 19.0 (TID 490). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 70.0 in stage 19.0 (TID 493, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 67.0 in stage 19.0 (TID 490) in 24 ms on localhost (executor driver) (67/200)
26/06/26 13:26:29 INFO Executor: Running task 70.0 in stage 19.0 (TID 493)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 55.0 in stage 19.0 (TID 478). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 71.0 in stage 19.0 (TID 494, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 71.0 in stage 19.0 (TID 494)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 55.0 in stage 19.0 (TID 478) in 135 ms on localhost (executor driver) (68/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 68.0 in stage 19.0 (TID 491). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 71.0 in stage 19.0 (TID 494). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 72.0 in stage 19.0 (TID 495, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 73.0 in stage 19.0 (TID 496, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 70.0 in stage 19.0 (TID 493). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 74.0 in stage 19.0 (TID 497, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 69.0 in stage 19.0 (TID 492). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 71.0 in stage 19.0 (TID 494) in 16 ms on localhost (executor driver) (69/200)
26/06/26 13:26:29 INFO Executor: Running task 73.0 in stage 19.0 (TID 496)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 75.0 in stage 19.0 (TID 498, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 75.0 in stage 19.0 (TID 498)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 73.0 in stage 19.0 (TID 496). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 75.0 in stage 19.0 (TID 498). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 72.0 in stage 19.0 (TID 495)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 69.0 in stage 19.0 (TID 492) in 51 ms on localhost (executor driver) (70/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 68.0 in stage 19.0 (TID 491) in 52 ms on localhost (executor driver) (71/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 70.0 in stage 19.0 (TID 493) in 37 ms on localhost (executor driver) (72/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 76.0 in stage 19.0 (TID 499, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 77.0 in stage 19.0 (TID 500, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 73.0 in stage 19.0 (TID 496) in 10 ms on localhost (executor driver) (73/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 75.0 in stage 19.0 (TID 498) in 9 ms on localhost (executor driver) (74/200)
26/06/26 13:26:29 INFO Executor: Finished task 72.0 in stage 19.0 (TID 495). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 76.0 in stage 19.0 (TID 499)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 76.0 in stage 19.0 (TID 499). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 74.0 in stage 19.0 (TID 497)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 78.0 in stage 19.0 (TID 501, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 79.0 in stage 19.0 (TID 502, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 72.0 in stage 19.0 (TID 495) in 27 ms on localhost (executor driver) (75/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 76.0 in stage 19.0 (TID 499) in 17 ms on localhost (executor driver) (76/200)
26/06/26 13:26:29 INFO Executor: Running task 77.0 in stage 19.0 (TID 500)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 74.0 in stage 19.0 (TID 497). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 77.0 in stage 19.0 (TID 500). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 80.0 in stage 19.0 (TID 503, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 81.0 in stage 19.0 (TID 504, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 74.0 in stage 19.0 (TID 497) in 33 ms on localhost (executor driver) (77/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 77.0 in stage 19.0 (TID 500) in 24 ms on localhost (executor driver) (78/200)
26/06/26 13:26:29 INFO Executor: Running task 80.0 in stage 19.0 (TID 503)
26/06/26 13:26:29 INFO Executor: Running task 79.0 in stage 19.0 (TID 502)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 80.0 in stage 19.0 (TID 503). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 79.0 in stage 19.0 (TID 502). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 82.0 in stage 19.0 (TID 505, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 81.0 in stage 19.0 (TID 504)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 83.0 in stage 19.0 (TID 506, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 80.0 in stage 19.0 (TID 503) in 8 ms on localhost (executor driver) (79/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 79.0 in stage 19.0 (TID 502) in 17 ms on localhost (executor driver) (80/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 83.0 in stage 19.0 (TID 506)
26/06/26 13:26:29 INFO Executor: Finished task 81.0 in stage 19.0 (TID 504). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 78.0 in stage 19.0 (TID 501)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 78.0 in stage 19.0 (TID 501). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 83.0 in stage 19.0 (TID 506). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 82.0 in stage 19.0 (TID 505)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 84.0 in stage 19.0 (TID 507, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 85.0 in stage 19.0 (TID 508, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 86.0 in stage 19.0 (TID 509, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 81.0 in stage 19.0 (TID 504) in 23 ms on localhost (executor driver) (81/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 78.0 in stage 19.0 (TID 501) in 32 ms on localhost (executor driver) (82/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 83.0 in stage 19.0 (TID 506) in 15 ms on localhost (executor driver) (83/200)
26/06/26 13:26:29 INFO Executor: Finished task 82.0 in stage 19.0 (TID 505). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 85.0 in stage 19.0 (TID 508)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 87.0 in stage 19.0 (TID 510, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 82.0 in stage 19.0 (TID 505) in 23 ms on localhost (executor driver) (84/200)
26/06/26 13:26:29 INFO Executor: Running task 84.0 in stage 19.0 (TID 507)
26/06/26 13:26:29 INFO Executor: Finished task 85.0 in stage 19.0 (TID 508). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 86.0 in stage 19.0 (TID 509)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 84.0 in stage 19.0 (TID 507). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 87.0 in stage 19.0 (TID 510)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 88.0 in stage 19.0 (TID 511, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 89.0 in stage 19.0 (TID 512, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 85.0 in stage 19.0 (TID 508) in 20 ms on localhost (executor driver) (85/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 84.0 in stage 19.0 (TID 507) in 21 ms on localhost (executor driver) (86/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 87.0 in stage 19.0 (TID 510). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 89.0 in stage 19.0 (TID 512)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 90.0 in stage 19.0 (TID 513, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 87.0 in stage 19.0 (TID 510) in 25 ms on localhost (executor driver) (87/200)
26/06/26 13:26:29 INFO Executor: Finished task 86.0 in stage 19.0 (TID 509). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 90.0 in stage 19.0 (TID 513)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 90.0 in stage 19.0 (TID 513). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 89.0 in stage 19.0 (TID 512). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 91.0 in stage 19.0 (TID 514, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 92.0 in stage 19.0 (TID 515, localhost, executor driver, partition 92, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 93.0 in stage 19.0 (TID 516, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 86.0 in stage 19.0 (TID 509) in 47 ms on localhost (executor driver) (88/200)
26/06/26 13:26:29 INFO Executor: Running task 93.0 in stage 19.0 (TID 516)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 90.0 in stage 19.0 (TID 513) in 17 ms on localhost (executor driver) (89/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 89.0 in stage 19.0 (TID 512) in 30 ms on localhost (executor driver) (90/200)
26/06/26 13:26:29 INFO Executor: Running task 88.0 in stage 19.0 (TID 511)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO Executor: Running task 91.0 in stage 19.0 (TID 514)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Running task 92.0 in stage 19.0 (TID 515)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 91.0 in stage 19.0 (TID 514). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 94.0 in stage 19.0 (TID 517, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 92.0 in stage 19.0 (TID 515). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 91.0 in stage 19.0 (TID 514) in 19 ms on localhost (executor driver) (91/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 95.0 in stage 19.0 (TID 518, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 93.0 in stage 19.0 (TID 516). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 96.0 in stage 19.0 (TID 519, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 93.0 in stage 19.0 (TID 516) in 19 ms on localhost (executor driver) (92/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 92.0 in stage 19.0 (TID 515) in 20 ms on localhost (executor driver) (93/200)
26/06/26 13:26:29 INFO Executor: Running task 96.0 in stage 19.0 (TID 519)
26/06/26 13:26:29 INFO Executor: Finished task 88.0 in stage 19.0 (TID 511). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 97.0 in stage 19.0 (TID 520, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 88.0 in stage 19.0 (TID 511) in 49 ms on localhost (executor driver) (94/200)
26/06/26 13:26:29 INFO Executor: Running task 97.0 in stage 19.0 (TID 520)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 95.0 in stage 19.0 (TID 518)
26/06/26 13:26:29 INFO Executor: Finished task 97.0 in stage 19.0 (TID 520). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 98.0 in stage 19.0 (TID 521, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 97.0 in stage 19.0 (TID 520) in 5 ms on localhost (executor driver) (95/200)
26/06/26 13:26:29 INFO Executor: Running task 94.0 in stage 19.0 (TID 517)
26/06/26 13:26:29 INFO Executor: Finished task 96.0 in stage 19.0 (TID 519). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 99.0 in stage 19.0 (TID 522, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 96.0 in stage 19.0 (TID 519) in 9 ms on localhost (executor driver) (96/200)
26/06/26 13:26:29 INFO Executor: Running task 99.0 in stage 19.0 (TID 522)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Running task 98.0 in stage 19.0 (TID 521)
26/06/26 13:26:29 INFO Executor: Finished task 94.0 in stage 19.0 (TID 517). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 99.0 in stage 19.0 (TID 522). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Starting task 100.0 in stage 19.0 (TID 523, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 101.0 in stage 19.0 (TID 524, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 98.0 in stage 19.0 (TID 521). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 95.0 in stage 19.0 (TID 518). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 100.0 in stage 19.0 (TID 523)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 94.0 in stage 19.0 (TID 517) in 21 ms on localhost (executor driver) (97/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 99.0 in stage 19.0 (TID 522) in 11 ms on localhost (executor driver) (98/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 102.0 in stage 19.0 (TID 525, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 103.0 in stage 19.0 (TID 526, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 98.0 in stage 19.0 (TID 521) in 15 ms on localhost (executor driver) (99/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 95.0 in stage 19.0 (TID 518) in 21 ms on localhost (executor driver) (100/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 100.0 in stage 19.0 (TID 523). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 104.0 in stage 19.0 (TID 527, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 102.0 in stage 19.0 (TID 525)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 100.0 in stage 19.0 (TID 523) in 10 ms on localhost (executor driver) (101/200)
26/06/26 13:26:29 INFO Executor: Running task 103.0 in stage 19.0 (TID 526)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 102.0 in stage 19.0 (TID 525). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 105.0 in stage 19.0 (TID 528, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 105.0 in stage 19.0 (TID 528)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO Executor: Running task 104.0 in stage 19.0 (TID 527)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 25 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 103.0 in stage 19.0 (TID 526). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 104.0 in stage 19.0 (TID 527). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 105.0 in stage 19.0 (TID 528). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 101.0 in stage 19.0 (TID 524)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 101.0 in stage 19.0 (TID 524). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 102.0 in stage 19.0 (TID 525) in 26 ms on localhost (executor driver) (102/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 106.0 in stage 19.0 (TID 529, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 107.0 in stage 19.0 (TID 530, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 103.0 in stage 19.0 (TID 526) in 69 ms on localhost (executor driver) (103/200)
26/06/26 13:26:29 INFO Executor: Running task 106.0 in stage 19.0 (TID 529)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 104.0 in stage 19.0 (TID 527) in 63 ms on localhost (executor driver) (104/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 108.0 in stage 19.0 (TID 531, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 109.0 in stage 19.0 (TID 532, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 105.0 in stage 19.0 (TID 528) in 58 ms on localhost (executor driver) (105/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 101.0 in stage 19.0 (TID 524) in 73 ms on localhost (executor driver) (106/200)
26/06/26 13:26:29 INFO Executor: Running task 109.0 in stage 19.0 (TID 532)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Running task 108.0 in stage 19.0 (TID 531)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 108.0 in stage 19.0 (TID 531). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 110.0 in stage 19.0 (TID 533, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 107.0 in stage 19.0 (TID 530)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 109.0 in stage 19.0 (TID 532). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 108.0 in stage 19.0 (TID 531) in 13 ms on localhost (executor driver) (107/200)
26/06/26 13:26:29 INFO Executor: Finished task 107.0 in stage 19.0 (TID 530). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 111.0 in stage 19.0 (TID 534, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 112.0 in stage 19.0 (TID 535, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 110.0 in stage 19.0 (TID 533)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 109.0 in stage 19.0 (TID 532) in 29 ms on localhost (executor driver) (108/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 107.0 in stage 19.0 (TID 530) in 32 ms on localhost (executor driver) (109/200)
26/06/26 13:26:29 INFO Executor: Running task 112.0 in stage 19.0 (TID 535)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 110.0 in stage 19.0 (TID 533). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 113.0 in stage 19.0 (TID 536, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Finished task 112.0 in stage 19.0 (TID 535). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Finished task 106.0 in stage 19.0 (TID 529). 3672 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 110.0 in stage 19.0 (TID 533) in 29 ms on localhost (executor driver) (110/200)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 114.0 in stage 19.0 (TID 537, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:29 INFO TaskSetManager: Starting task 115.0 in stage 19.0 (TID 538, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 114.0 in stage 19.0 (TID 537)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 114.0 in stage 19.0 (TID 537). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 116.0 in stage 19.0 (TID 539, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 111.0 in stage 19.0 (TID 534)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 111.0 in stage 19.0 (TID 534). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 117.0 in stage 19.0 (TID 540, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 116.0 in stage 19.0 (TID 539)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 116.0 in stage 19.0 (TID 539). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 118.0 in stage 19.0 (TID 541, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 113.0 in stage 19.0 (TID 536)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 113.0 in stage 19.0 (TID 536). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 119.0 in stage 19.0 (TID 542, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 118.0 in stage 19.0 (TID 541)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 118.0 in stage 19.0 (TID 541). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 120.0 in stage 19.0 (TID 543, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 119.0 in stage 19.0 (TID 542)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 119.0 in stage 19.0 (TID 542). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 121.0 in stage 19.0 (TID 544, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 121.0 in stage 19.0 (TID 544)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 121.0 in stage 19.0 (TID 544). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 122.0 in stage 19.0 (TID 545, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 120.0 in stage 19.0 (TID 543)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 120.0 in stage 19.0 (TID 543). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 123.0 in stage 19.0 (TID 546, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 117.0 in stage 19.0 (TID 540)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 117.0 in stage 19.0 (TID 540). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 124.0 in stage 19.0 (TID 547, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 122.0 in stage 19.0 (TID 545)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 122.0 in stage 19.0 (TID 545). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 125.0 in stage 19.0 (TID 548, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 123.0 in stage 19.0 (TID 546)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 123.0 in stage 19.0 (TID 546). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 126.0 in stage 19.0 (TID 549, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 124.0 in stage 19.0 (TID 547)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 124.0 in stage 19.0 (TID 547). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 127.0 in stage 19.0 (TID 550, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 125.0 in stage 19.0 (TID 548)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:29 INFO Executor: Finished task 125.0 in stage 19.0 (TID 548). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Starting task 128.0 in stage 19.0 (TID 551, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:29 INFO Executor: Running task 127.0 in stage 19.0 (TID 550)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO TaskSetManager: Finished task 112.0 in stage 19.0 (TID 535) in 99 ms on localhost (executor driver) (111/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 106.0 in stage 19.0 (TID 529) in 126 ms on localhost (executor driver) (112/200)
26/06/26 13:26:29 INFO Executor: Running task 128.0 in stage 19.0 (TID 551)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 114.0 in stage 19.0 (TID 537) in 85 ms on localhost (executor driver) (113/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 111.0 in stage 19.0 (TID 534) in 103 ms on localhost (executor driver) (114/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 116.0 in stage 19.0 (TID 539) in 82 ms on localhost (executor driver) (115/200)
26/06/26 13:26:29 INFO TaskSetManager: Finished task 113.0 in stage 19.0 (TID 536) in 90 ms on localhost (executor driver) (116/200)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:29 INFO Executor: Finished task 128.0 in stage 19.0 (TID 551). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 126.0 in stage 19.0 (TID 549)
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:29 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 126.0 in stage 19.0 (TID 549). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO Executor: Running task 115.0 in stage 19.0 (TID 538)
26/06/26 13:26:30 INFO Executor: Finished task 127.0 in stage 19.0 (TID 550). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 115.0 in stage 19.0 (TID 538). 3629 bytes result sent to driver
26/06/26 13:26:29 INFO TaskSetManager: Finished task 118.0 in stage 19.0 (TID 541) in 64 ms on localhost (executor driver) (117/200)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 129.0 in stage 19.0 (TID 552, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 130.0 in stage 19.0 (TID 553, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 131.0 in stage 19.0 (TID 554, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 132.0 in stage 19.0 (TID 555, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 131.0 in stage 19.0 (TID 554)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 131.0 in stage 19.0 (TID 554). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 133.0 in stage 19.0 (TID 556, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 130.0 in stage 19.0 (TID 553)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 130.0 in stage 19.0 (TID 553). 3586 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 134.0 in stage 19.0 (TID 557, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 132.0 in stage 19.0 (TID 555)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 132.0 in stage 19.0 (TID 555). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 135.0 in stage 19.0 (TID 558, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 133.0 in stage 19.0 (TID 556)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 133.0 in stage 19.0 (TID 556). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 136.0 in stage 19.0 (TID 559, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 134.0 in stage 19.0 (TID 557)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 134.0 in stage 19.0 (TID 557). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 137.0 in stage 19.0 (TID 560, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 136.0 in stage 19.0 (TID 559)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 136.0 in stage 19.0 (TID 559). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 138.0 in stage 19.0 (TID 561, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 135.0 in stage 19.0 (TID 558)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 135.0 in stage 19.0 (TID 558). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 139.0 in stage 19.0 (TID 562, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 137.0 in stage 19.0 (TID 560)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 137.0 in stage 19.0 (TID 560). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 140.0 in stage 19.0 (TID 563, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 139.0 in stage 19.0 (TID 562)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 139.0 in stage 19.0 (TID 562). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 141.0 in stage 19.0 (TID 564, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 138.0 in stage 19.0 (TID 561)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 138.0 in stage 19.0 (TID 561). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 142.0 in stage 19.0 (TID 565, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 140.0 in stage 19.0 (TID 563)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 120.0 in stage 19.0 (TID 543) in 134 ms on localhost (executor driver) (118/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 122.0 in stage 19.0 (TID 545) in 126 ms on localhost (executor driver) (119/200)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Running task 129.0 in stage 19.0 (TID 552)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO Executor: Running task 142.0 in stage 19.0 (TID 565)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 123.0 in stage 19.0 (TID 546) in 122 ms on localhost (executor driver) (120/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 124.0 in stage 19.0 (TID 547) in 125 ms on localhost (executor driver) (121/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 125.0 in stage 19.0 (TID 548) in 121 ms on localhost (executor driver) (122/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 128.0 in stage 19.0 (TID 551) in 105 ms on localhost (executor driver) (123/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 126.0 in stage 19.0 (TID 549) in 115 ms on localhost (executor driver) (124/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 127.0 in stage 19.0 (TID 550) in 110 ms on localhost (executor driver) (125/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 115.0 in stage 19.0 (TID 538) in 181 ms on localhost (executor driver) (126/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 131.0 in stage 19.0 (TID 554) in 71 ms on localhost (executor driver) (127/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 130.0 in stage 19.0 (TID 553) in 72 ms on localhost (executor driver) (128/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 132.0 in stage 19.0 (TID 555) in 72 ms on localhost (executor driver) (129/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 133.0 in stage 19.0 (TID 556) in 68 ms on localhost (executor driver) (130/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 134.0 in stage 19.0 (TID 557) in 64 ms on localhost (executor driver) (131/200)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 129.0 in stage 19.0 (TID 552). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 136.0 in stage 19.0 (TID 559) in 55 ms on localhost (executor driver) (132/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 135.0 in stage 19.0 (TID 558) in 61 ms on localhost (executor driver) (133/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 137.0 in stage 19.0 (TID 560) in 55 ms on localhost (executor driver) (134/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 139.0 in stage 19.0 (TID 562) in 48 ms on localhost (executor driver) (135/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 138.0 in stage 19.0 (TID 561) in 52 ms on localhost (executor driver) (136/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 121.0 in stage 19.0 (TID 544) in 147 ms on localhost (executor driver) (137/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 119.0 in stage 19.0 (TID 542) in 157 ms on localhost (executor driver) (138/200)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 143.0 in stage 19.0 (TID 566, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Finished task 142.0 in stage 19.0 (TID 565). 3672 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 144.0 in stage 19.0 (TID 567, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 141.0 in stage 19.0 (TID 564)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 141.0 in stage 19.0 (TID 564). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 145.0 in stage 19.0 (TID 568, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Finished task 140.0 in stage 19.0 (TID 563). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 146.0 in stage 19.0 (TID 569, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 146.0 in stage 19.0 (TID 569)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 146.0 in stage 19.0 (TID 569). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 147.0 in stage 19.0 (TID 570, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 144.0 in stage 19.0 (TID 567)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 144.0 in stage 19.0 (TID 567). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 148.0 in stage 19.0 (TID 571, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 145.0 in stage 19.0 (TID 568)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO TaskSetManager: Finished task 117.0 in stage 19.0 (TID 540) in 212 ms on localhost (executor driver) (139/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 129.0 in stage 19.0 (TID 552) in 120 ms on localhost (executor driver) (140/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 142.0 in stage 19.0 (TID 565) in 65 ms on localhost (executor driver) (141/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 141.0 in stage 19.0 (TID 564) in 74 ms on localhost (executor driver) (142/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 140.0 in stage 19.0 (TID 563) in 86 ms on localhost (executor driver) (143/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 146.0 in stage 19.0 (TID 569) in 28 ms on localhost (executor driver) (144/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 144.0 in stage 19.0 (TID 567) in 41 ms on localhost (executor driver) (145/200)
26/06/26 13:26:30 INFO Executor: Running task 143.0 in stage 19.0 (TID 566)
26/06/26 13:26:30 INFO Executor: Finished task 145.0 in stage 19.0 (TID 568). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 149.0 in stage 19.0 (TID 572, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 147.0 in stage 19.0 (TID 570)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 143.0 in stage 19.0 (TID 566). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 145.0 in stage 19.0 (TID 568) in 36 ms on localhost (executor driver) (146/200)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 147.0 in stage 19.0 (TID 570). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 150.0 in stage 19.0 (TID 573, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 151.0 in stage 19.0 (TID 574, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 148.0 in stage 19.0 (TID 571)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 148.0 in stage 19.0 (TID 571). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 152.0 in stage 19.0 (TID 575, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 149.0 in stage 19.0 (TID 572)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 149.0 in stage 19.0 (TID 572). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 153.0 in stage 19.0 (TID 576, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 152.0 in stage 19.0 (TID 575)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 152.0 in stage 19.0 (TID 575). 3672 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 154.0 in stage 19.0 (TID 577, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 150.0 in stage 19.0 (TID 573)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 150.0 in stage 19.0 (TID 573). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 155.0 in stage 19.0 (TID 578, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 153.0 in stage 19.0 (TID 576)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 153.0 in stage 19.0 (TID 576). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 156.0 in stage 19.0 (TID 579, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 154.0 in stage 19.0 (TID 577)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 154.0 in stage 19.0 (TID 577). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 157.0 in stage 19.0 (TID 580, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 155.0 in stage 19.0 (TID 578)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 143.0 in stage 19.0 (TID 566) in 112 ms on localhost (executor driver) (147/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 147.0 in stage 19.0 (TID 570) in 89 ms on localhost (executor driver) (148/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 148.0 in stage 19.0 (TID 571) in 80 ms on localhost (executor driver) (149/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 149.0 in stage 19.0 (TID 572) in 68 ms on localhost (executor driver) (150/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 152.0 in stage 19.0 (TID 575) in 46 ms on localhost (executor driver) (151/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 150.0 in stage 19.0 (TID 573) in 57 ms on localhost (executor driver) (152/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 153.0 in stage 19.0 (TID 576) in 39 ms on localhost (executor driver) (153/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 154.0 in stage 19.0 (TID 577) in 32 ms on localhost (executor driver) (154/200)
26/06/26 13:26:30 INFO Executor: Running task 151.0 in stage 19.0 (TID 574)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Running task 156.0 in stage 19.0 (TID 579)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 151.0 in stage 19.0 (TID 574). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 158.0 in stage 19.0 (TID 581, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 157.0 in stage 19.0 (TID 580)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 151.0 in stage 19.0 (TID 574) in 78 ms on localhost (executor driver) (155/200)
26/06/26 13:26:30 INFO Executor: Running task 158.0 in stage 19.0 (TID 581)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 157.0 in stage 19.0 (TID 580). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 159.0 in stage 19.0 (TID 582, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 40 ms
26/06/26 13:26:30 INFO Executor: Finished task 158.0 in stage 19.0 (TID 581). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 157.0 in stage 19.0 (TID 580) in 49 ms on localhost (executor driver) (156/200)
26/06/26 13:26:30 INFO Executor: Finished task 155.0 in stage 19.0 (TID 578). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 160.0 in stage 19.0 (TID 583, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 161.0 in stage 19.0 (TID 584, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 160.0 in stage 19.0 (TID 583)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 160.0 in stage 19.0 (TID 583). 3672 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 162.0 in stage 19.0 (TID 585, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Finished task 156.0 in stage 19.0 (TID 579). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 163.0 in stage 19.0 (TID 586, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 163.0 in stage 19.0 (TID 586)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 163.0 in stage 19.0 (TID 586). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 164.0 in stage 19.0 (TID 587, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 159.0 in stage 19.0 (TID 582)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 159.0 in stage 19.0 (TID 582). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 165.0 in stage 19.0 (TID 588, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 164.0 in stage 19.0 (TID 587)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 164.0 in stage 19.0 (TID 587). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 166.0 in stage 19.0 (TID 589, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 162.0 in stage 19.0 (TID 585)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 162.0 in stage 19.0 (TID 585). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 167.0 in stage 19.0 (TID 590, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 165.0 in stage 19.0 (TID 588)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 165.0 in stage 19.0 (TID 588). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 168.0 in stage 19.0 (TID 591, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 166.0 in stage 19.0 (TID 589)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 158.0 in stage 19.0 (TID 581) in 85 ms on localhost (executor driver) (157/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 155.0 in stage 19.0 (TID 578) in 130 ms on localhost (executor driver) (158/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 160.0 in stage 19.0 (TID 583) in 63 ms on localhost (executor driver) (159/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 156.0 in stage 19.0 (TID 579) in 124 ms on localhost (executor driver) (160/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 163.0 in stage 19.0 (TID 586) in 50 ms on localhost (executor driver) (161/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 159.0 in stage 19.0 (TID 582) in 70 ms on localhost (executor driver) (162/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 164.0 in stage 19.0 (TID 587) in 43 ms on localhost (executor driver) (163/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 162.0 in stage 19.0 (TID 585) in 52 ms on localhost (executor driver) (164/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 165.0 in stage 19.0 (TID 588) in 32 ms on localhost (executor driver) (165/200)
26/06/26 13:26:30 INFO Executor: Running task 161.0 in stage 19.0 (TID 584)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 161.0 in stage 19.0 (TID 584). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 169.0 in stage 19.0 (TID 592, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 161.0 in stage 19.0 (TID 584) in 76 ms on localhost (executor driver) (166/200)
26/06/26 13:26:30 INFO Executor: Running task 169.0 in stage 19.0 (TID 592)
26/06/26 13:26:30 INFO Executor: Running task 167.0 in stage 19.0 (TID 590)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 166.0 in stage 19.0 (TID 589). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 14 ms
26/06/26 13:26:30 INFO TaskSetManager: Starting task 170.0 in stage 19.0 (TID 593, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 170.0 in stage 19.0 (TID 593)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Running task 168.0 in stage 19.0 (TID 591)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 168.0 in stage 19.0 (TID 591). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Finished task 169.0 in stage 19.0 (TID 592). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 166.0 in stage 19.0 (TID 589) in 162 ms on localhost (executor driver) (167/200)
26/06/26 13:26:30 INFO Executor: Finished task 170.0 in stage 19.0 (TID 593). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 171.0 in stage 19.0 (TID 594, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 172.0 in stage 19.0 (TID 595, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 173.0 in stage 19.0 (TID 596, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 172.0 in stage 19.0 (TID 595)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 172.0 in stage 19.0 (TID 595). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 171.0 in stage 19.0 (TID 594)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 174.0 in stage 19.0 (TID 597, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 168.0 in stage 19.0 (TID 591) in 172 ms on localhost (executor driver) (168/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 169.0 in stage 19.0 (TID 592) in 156 ms on localhost (executor driver) (169/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 170.0 in stage 19.0 (TID 593) in 59 ms on localhost (executor driver) (170/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 172.0 in stage 19.0 (TID 595) in 12 ms on localhost (executor driver) (171/200)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 171.0 in stage 19.0 (TID 594). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 174.0 in stage 19.0 (TID 597)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 174.0 in stage 19.0 (TID 597). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 173.0 in stage 19.0 (TID 596)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO TaskSetManager: Starting task 175.0 in stage 19.0 (TID 598, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 176.0 in stage 19.0 (TID 599, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 171.0 in stage 19.0 (TID 594) in 33 ms on localhost (executor driver) (172/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 174.0 in stage 19.0 (TID 597) in 22 ms on localhost (executor driver) (173/200)
26/06/26 13:26:30 INFO Executor: Finished task 167.0 in stage 19.0 (TID 590). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 175.0 in stage 19.0 (TID 598)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 177.0 in stage 19.0 (TID 600, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 177.0 in stage 19.0 (TID 600)
26/06/26 13:26:30 INFO Executor: Finished task 173.0 in stage 19.0 (TID 596). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 175.0 in stage 19.0 (TID 598). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 178.0 in stage 19.0 (TID 601, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 179.0 in stage 19.0 (TID 602, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 175.0 in stage 19.0 (TID 598) in 8 ms on localhost (executor driver) (174/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 167.0 in stage 19.0 (TID 590) in 210 ms on localhost (executor driver) (175/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 173.0 in stage 19.0 (TID 596) in 39 ms on localhost (executor driver) (176/200)
26/06/26 13:26:30 INFO Executor: Running task 176.0 in stage 19.0 (TID 599)
26/06/26 13:26:30 INFO Executor: Finished task 177.0 in stage 19.0 (TID 600). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO TaskSetManager: Starting task 180.0 in stage 19.0 (TID 603, localhost, executor driver, partition 180, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 179.0 in stage 19.0 (TID 602)
26/06/26 13:26:30 INFO Executor: Running task 180.0 in stage 19.0 (TID 603)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 176.0 in stage 19.0 (TID 599). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 177.0 in stage 19.0 (TID 600) in 17 ms on localhost (executor driver) (177/200)
26/06/26 13:26:30 INFO Executor: Running task 178.0 in stage 19.0 (TID 601)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 179.0 in stage 19.0 (TID 602). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Finished task 180.0 in stage 19.0 (TID 603). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 181.0 in stage 19.0 (TID 604, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 182.0 in stage 19.0 (TID 605, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 183.0 in stage 19.0 (TID 606, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Finished task 178.0 in stage 19.0 (TID 601). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 176.0 in stage 19.0 (TID 599) in 27 ms on localhost (executor driver) (178/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 179.0 in stage 19.0 (TID 602) in 138 ms on localhost (executor driver) (179/200)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 184.0 in stage 19.0 (TID 607, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 180.0 in stage 19.0 (TID 603) in 134 ms on localhost (executor driver) (180/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 178.0 in stage 19.0 (TID 601) in 143 ms on localhost (executor driver) (181/200)
26/06/26 13:26:30 INFO Executor: Running task 184.0 in stage 19.0 (TID 607)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 184.0 in stage 19.0 (TID 607). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 185.0 in stage 19.0 (TID 608, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 181.0 in stage 19.0 (TID 604)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 181.0 in stage 19.0 (TID 604). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 186.0 in stage 19.0 (TID 609, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 182.0 in stage 19.0 (TID 605)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 182.0 in stage 19.0 (TID 605). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 187.0 in stage 19.0 (TID 610, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 183.0 in stage 19.0 (TID 606)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 183.0 in stage 19.0 (TID 606). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 184.0 in stage 19.0 (TID 607) in 83 ms on localhost (executor driver) (182/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 181.0 in stage 19.0 (TID 604) in 205 ms on localhost (executor driver) (183/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 182.0 in stage 19.0 (TID 605) in 206 ms on localhost (executor driver) (184/200)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 188.0 in stage 19.0 (TID 611, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 188.0 in stage 19.0 (TID 611)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 188.0 in stage 19.0 (TID 611). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 189.0 in stage 19.0 (TID 612, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 185.0 in stage 19.0 (TID 608)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 185.0 in stage 19.0 (TID 608). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 190.0 in stage 19.0 (TID 613, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 187.0 in stage 19.0 (TID 610)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 187.0 in stage 19.0 (TID 610). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 191.0 in stage 19.0 (TID 614, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 186.0 in stage 19.0 (TID 609)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 186.0 in stage 19.0 (TID 609). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 192.0 in stage 19.0 (TID 615, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 190.0 in stage 19.0 (TID 613)
26/06/26 13:26:30 INFO Executor: Running task 189.0 in stage 19.0 (TID 612)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 190.0 in stage 19.0 (TID 613). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Finished task 189.0 in stage 19.0 (TID 612). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 191.0 in stage 19.0 (TID 614)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 193.0 in stage 19.0 (TID 616, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 194.0 in stage 19.0 (TID 617, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 193.0 in stage 19.0 (TID 616)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 191.0 in stage 19.0 (TID 614). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 192.0 in stage 19.0 (TID 615)
26/06/26 13:26:30 INFO Executor: Finished task 193.0 in stage 19.0 (TID 616). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 195.0 in stage 19.0 (TID 618, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 196.0 in stage 19.0 (TID 619, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 196.0 in stage 19.0 (TID 619)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 196.0 in stage 19.0 (TID 619). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Finished task 192.0 in stage 19.0 (TID 615). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 197.0 in stage 19.0 (TID 620, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Starting task 198.0 in stage 19.0 (TID 621, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 183.0 in stage 19.0 (TID 606) in 258 ms on localhost (executor driver) (185/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 188.0 in stage 19.0 (TID 611) in 49 ms on localhost (executor driver) (186/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 185.0 in stage 19.0 (TID 608) in 72 ms on localhost (executor driver) (187/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 187.0 in stage 19.0 (TID 610) in 61 ms on localhost (executor driver) (188/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 186.0 in stage 19.0 (TID 609) in 66 ms on localhost (executor driver) (189/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 190.0 in stage 19.0 (TID 613) in 36 ms on localhost (executor driver) (190/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 189.0 in stage 19.0 (TID 612) in 44 ms on localhost (executor driver) (191/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 191.0 in stage 19.0 (TID 614) in 33 ms on localhost (executor driver) (192/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 193.0 in stage 19.0 (TID 616) in 19 ms on localhost (executor driver) (193/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 196.0 in stage 19.0 (TID 619) in 13 ms on localhost (executor driver) (194/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 192.0 in stage 19.0 (TID 615) in 27 ms on localhost (executor driver) (195/200)
26/06/26 13:26:30 INFO Executor: Running task 197.0 in stage 19.0 (TID 620)
26/06/26 13:26:30 INFO Executor: Running task 194.0 in stage 19.0 (TID 617)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 197.0 in stage 19.0 (TID 620). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Finished task 194.0 in stage 19.0 (TID 617). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Starting task 199.0 in stage 19.0 (TID 622, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:30 INFO Executor: Running task 195.0 in stage 19.0 (TID 618)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 195.0 in stage 19.0 (TID 618). 3672 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 198.0 in stage 19.0 (TID 621)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:30 INFO Executor: Finished task 198.0 in stage 19.0 (TID 621). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO Executor: Running task 199.0 in stage 19.0 (TID 622)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 199.0 in stage 19.0 (TID 622). 3629 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 197.0 in stage 19.0 (TID 620) in 41 ms on localhost (executor driver) (196/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 194.0 in stage 19.0 (TID 617) in 54 ms on localhost (executor driver) (197/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 195.0 in stage 19.0 (TID 618) in 48 ms on localhost (executor driver) (198/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 198.0 in stage 19.0 (TID 621) in 43 ms on localhost (executor driver) (199/200)
26/06/26 13:26:30 INFO TaskSetManager: Finished task 199.0 in stage 19.0 (TID 622) in 22 ms on localhost (executor driver) (200/200)
26/06/26 13:26:30 INFO TaskSchedulerImpl: Removed TaskSet 19.0, whose tasks have all completed, from pool 
26/06/26 13:26:30 INFO DAGScheduler: ShuffleMapStage 19 (count at NativeMethodAccessorImpl.java:0) finished in 2.058 s
26/06/26 13:26:30 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:30 INFO DAGScheduler: running: Set()
26/06/26 13:26:30 INFO DAGScheduler: waiting: Set(ResultStage 20)
26/06/26 13:26:30 INFO DAGScheduler: failed: Set()
26/06/26 13:26:30 INFO DAGScheduler: Submitting ResultStage 20 (MapPartitionsRDD[77] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:30 INFO MemoryStore: Block broadcast_23 stored as values in memory (estimated size 7.3 KB, free 364.8 MB)
26/06/26 13:26:30 INFO MemoryStore: Block broadcast_23_piece0 stored as bytes in memory (estimated size 3.8 KB, free 364.8 MB)
26/06/26 13:26:30 INFO BlockManagerInfo: Added broadcast_23_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:30 INFO SparkContext: Created broadcast 23 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:30 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 20 (MapPartitionsRDD[77] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:30 INFO TaskSchedulerImpl: Adding task set 20.0 with 1 tasks
26/06/26 13:26:30 INFO TaskSetManager: Starting task 0.0 in stage 20.0 (TID 623, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:30 INFO Executor: Running task 0.0 in stage 20.0 (TID 623)
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:30 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:30 INFO Executor: Finished task 0.0 in stage 20.0 (TID 623). 1782 bytes result sent to driver
26/06/26 13:26:30 INFO TaskSetManager: Finished task 0.0 in stage 20.0 (TID 623) in 74 ms on localhost (executor driver) (1/1)
26/06/26 13:26:30 INFO TaskSchedulerImpl: Removed TaskSet 20.0, whose tasks have all completed, from pool 
26/06/26 13:26:30 INFO DAGScheduler: ResultStage 20 (count at NativeMethodAccessorImpl.java:0) finished in 0.088 s
26/06/26 13:26:30 INFO DAGScheduler: Job 11 finished: count at NativeMethodAccessorImpl.java:0, took 2.778071 s
('Movies :', 1682)

Missing Values
26/06/26 13:26:32 INFO CodeGenerator: Code generated in 56.185215 ms
26/06/26 13:26:32 INFO CodeGenerator: Code generated in 27.147686 ms
26/06/26 13:26:32 INFO CodeGenerator: Code generated in 56.053257 ms
26/06/26 13:26:32 INFO CodeGenerator: Code generated in 48.346777 ms
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 40.152582 ms
26/06/26 13:26:33 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:33 INFO DAGScheduler: Registering RDD 81 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:33 INFO DAGScheduler: Registering RDD 86 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:33 INFO DAGScheduler: Got job 12 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:33 INFO DAGScheduler: Final stage: ResultStage 23 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:33 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 22)
26/06/26 13:26:33 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 22)
26/06/26 13:26:33 INFO DAGScheduler: Submitting ShuffleMapStage 21 (MapPartitionsRDD[81] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:33 INFO MemoryStore: Block broadcast_24 stored as values in memory (estimated size 27.3 KB, free 364.8 MB)
26/06/26 13:26:33 INFO MemoryStore: Block broadcast_24_piece0 stored as bytes in memory (estimated size 14.2 KB, free 364.8 MB)
26/06/26 13:26:33 INFO BlockManagerInfo: Added broadcast_24_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 14.2 KB, free: 366.1 MB)
26/06/26 13:26:33 INFO SparkContext: Created broadcast 24 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:33 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 21 (MapPartitionsRDD[81] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:33 INFO TaskSchedulerImpl: Adding task set 21.0 with 2 tasks
26/06/26 13:26:33 INFO TaskSetManager: Starting task 0.0 in stage 21.0 (TID 624, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:33 INFO TaskSetManager: Starting task 1.0 in stage 21.0 (TID 625, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:33 INFO Executor: Running task 1.0 in stage 21.0 (TID 625)
26/06/26 13:26:33 INFO Executor: Running task 0.0 in stage 21.0 (TID 624)
26/06/26 13:26:33 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:0+11314
26/06/26 13:26:33 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.user:11314+11314
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 36.481756 ms
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 15.035575 ms
26/06/26 13:26:33 INFO PythonRunner: Times: total = 60, boot = -4850, init = 4896, finish = 14
26/06/26 13:26:33 INFO PythonRunner: Times: total = 52, boot = -4786, init = 4828, finish = 10
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 21.993179 ms
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 30.609277 ms
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 6.99996 ms
26/06/26 13:26:33 INFO CodeGenerator: Code generated in 18.674618 ms
26/06/26 13:26:33 INFO Executor: Finished task 0.0 in stage 21.0 (TID 624). 2555 bytes result sent to driver
26/06/26 13:26:33 INFO Executor: Finished task 1.0 in stage 21.0 (TID 625). 2555 bytes result sent to driver
26/06/26 13:26:33 INFO TaskSetManager: Finished task 0.0 in stage 21.0 (TID 624) in 783 ms on localhost (executor driver) (1/2)
26/06/26 13:26:33 INFO TaskSetManager: Finished task 1.0 in stage 21.0 (TID 625) in 788 ms on localhost (executor driver) (2/2)
26/06/26 13:26:33 INFO TaskSchedulerImpl: Removed TaskSet 21.0, whose tasks have all completed, from pool 
26/06/26 13:26:33 INFO DAGScheduler: ShuffleMapStage 21 (showString at NativeMethodAccessorImpl.java:0) finished in 0.807 s
26/06/26 13:26:33 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:33 INFO DAGScheduler: running: Set()
26/06/26 13:26:33 INFO DAGScheduler: waiting: Set(ShuffleMapStage 22, ResultStage 23)
26/06/26 13:26:33 INFO DAGScheduler: failed: Set()
26/06/26 13:26:33 INFO DAGScheduler: Submitting ShuffleMapStage 22 (MapPartitionsRDD[86] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:33 INFO MemoryStore: Block broadcast_25 stored as values in memory (estimated size 38.0 KB, free 364.8 MB)
26/06/26 13:26:33 INFO MemoryStore: Block broadcast_25_piece0 stored as bytes in memory (estimated size 18.8 KB, free 364.7 MB)
26/06/26 13:26:33 INFO BlockManagerInfo: Added broadcast_25_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 18.8 KB, free: 366.1 MB)
26/06/26 13:26:33 INFO SparkContext: Created broadcast 25 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:33 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 22 (MapPartitionsRDD[86] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:33 INFO TaskSchedulerImpl: Adding task set 22.0 with 200 tasks
26/06/26 13:26:33 INFO TaskSetManager: Starting task 92.0 in stage 22.0 (TID 626, localhost, executor driver, partition 92, PROCESS_LOCAL, 7743 bytes)
26/06/26 13:26:33 INFO TaskSetManager: Starting task 180.0 in stage 22.0 (TID 627, localhost, executor driver, partition 180, PROCESS_LOCAL, 7743 bytes)
26/06/26 13:26:33 INFO TaskSetManager: Starting task 0.0 in stage 22.0 (TID 628, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:33 INFO TaskSetManager: Starting task 1.0 in stage 22.0 (TID 629, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:33 INFO Executor: Running task 0.0 in stage 22.0 (TID 628)
26/06/26 13:26:33 INFO Executor: Running task 180.0 in stage 22.0 (TID 627)
26/06/26 13:26:33 INFO Executor: Running task 92.0 in stage 22.0 (TID 626)
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Getting 0 non-empty blocks out of 2 blocks
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:33 INFO Executor: Running task 1.0 in stage 22.0 (TID 629)
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Getting 0 non-empty blocks out of 2 blocks
26/06/26 13:26:33 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:33 INFO Executor: Finished task 180.0 in stage 22.0 (TID 627). 3249 bytes result sent to driver
26/06/26 13:26:33 INFO TaskSetManager: Starting task 2.0 in stage 22.0 (TID 630, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 2.0 in stage 22.0 (TID 630)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO CodeGenerator: Code generated in 14.346185 ms
26/06/26 13:26:34 INFO Executor: Finished task 92.0 in stage 22.0 (TID 626). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 3.0 in stage 22.0 (TID 631, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 180.0 in stage 22.0 (TID 627) in 51 ms on localhost (executor driver) (1/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 92.0 in stage 22.0 (TID 626) in 52 ms on localhost (executor driver) (2/200)
26/06/26 13:26:34 INFO Executor: Running task 3.0 in stage 22.0 (TID 631)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO CodeGenerator: Code generated in 30.551296 ms
26/06/26 13:26:34 INFO CodeGenerator: Code generated in 14.567105 ms
26/06/26 13:26:34 INFO Executor: Finished task 1.0 in stage 22.0 (TID 629). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 4.0 in stage 22.0 (TID 632, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 2.0 in stage 22.0 (TID 630). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 4.0 in stage 22.0 (TID 632)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 1.0 in stage 22.0 (TID 629) in 116 ms on localhost (executor driver) (3/200)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 5.0 in stage 22.0 (TID 633, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 2.0 in stage 22.0 (TID 630) in 94 ms on localhost (executor driver) (4/200)
26/06/26 13:26:34 INFO Executor: Finished task 3.0 in stage 22.0 (TID 631). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 6.0 in stage 22.0 (TID 634, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 5.0 in stage 22.0 (TID 633)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 6.0 in stage 22.0 (TID 634)
26/06/26 13:26:34 INFO Executor: Finished task 4.0 in stage 22.0 (TID 632). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 7.0 in stage 22.0 (TID 635, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 4.0 in stage 22.0 (TID 632) in 28 ms on localhost (executor driver) (5/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 3.0 in stage 22.0 (TID 631) in 94 ms on localhost (executor driver) (6/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 0.0 in stage 22.0 (TID 628). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 8.0 in stage 22.0 (TID 636, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 0.0 in stage 22.0 (TID 628) in 149 ms on localhost (executor driver) (7/200)
26/06/26 13:26:34 INFO Executor: Running task 8.0 in stage 22.0 (TID 636)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Running task 7.0 in stage 22.0 (TID 635)
26/06/26 13:26:34 INFO Executor: Finished task 6.0 in stage 22.0 (TID 634). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 9.0 in stage 22.0 (TID 637, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 6.0 in stage 22.0 (TID 634) in 35 ms on localhost (executor driver) (8/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 9.0 in stage 22.0 (TID 637)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 8.0 in stage 22.0 (TID 636). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 10.0 in stage 22.0 (TID 638, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 5.0 in stage 22.0 (TID 633). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 10.0 in stage 22.0 (TID 638)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 8.0 in stage 22.0 (TID 636) in 35 ms on localhost (executor driver) (9/200)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 11.0 in stage 22.0 (TID 639, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 5.0 in stage 22.0 (TID 633) in 70 ms on localhost (executor driver) (10/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 11.0 in stage 22.0 (TID 639)
26/06/26 13:26:34 INFO Executor: Finished task 7.0 in stage 22.0 (TID 635). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 12.0 in stage 22.0 (TID 640, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 7.0 in stage 22.0 (TID 635) in 74 ms on localhost (executor driver) (11/200)
26/06/26 13:26:34 INFO Executor: Finished task 9.0 in stage 22.0 (TID 637). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 10.0 in stage 22.0 (TID 638). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 13.0 in stage 22.0 (TID 641, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 14.0 in stage 22.0 (TID 642, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 9.0 in stage 22.0 (TID 637) in 58 ms on localhost (executor driver) (12/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 10.0 in stage 22.0 (TID 638) in 42 ms on localhost (executor driver) (13/200)
26/06/26 13:26:34 INFO Executor: Running task 13.0 in stage 22.0 (TID 641)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 14.0 in stage 22.0 (TID 642)
26/06/26 13:26:34 INFO Executor: Finished task 11.0 in stage 22.0 (TID 639). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 12.0 in stage 22.0 (TID 640)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 15.0 in stage 22.0 (TID 643, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 15.0 in stage 22.0 (TID 643)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 11.0 in stage 22.0 (TID 639) in 106 ms on localhost (executor driver) (14/200)
26/06/26 13:26:34 INFO Executor: Finished task 14.0 in stage 22.0 (TID 642). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 12.0 in stage 22.0 (TID 640). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 13.0 in stage 22.0 (TID 641). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 16.0 in stage 22.0 (TID 644, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 16.0 in stage 22.0 (TID 644)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 17.0 in stage 22.0 (TID 645, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 18.0 in stage 22.0 (TID 646, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 17.0 in stage 22.0 (TID 645)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 13.0 in stage 22.0 (TID 641) in 142 ms on localhost (executor driver) (15/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 12.0 in stage 22.0 (TID 640) in 156 ms on localhost (executor driver) (16/200)
26/06/26 13:26:34 INFO Executor: Running task 18.0 in stage 22.0 (TID 646)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 14.0 in stage 22.0 (TID 642) in 159 ms on localhost (executor driver) (17/200)
26/06/26 13:26:34 INFO Executor: Finished task 16.0 in stage 22.0 (TID 644). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO BlockManagerInfo: Removed broadcast_24_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 14.2 KB, free: 366.1 MB)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 19.0 in stage 22.0 (TID 647, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 15.0 in stage 22.0 (TID 643). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 20.0 in stage 22.0 (TID 648, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 16.0 in stage 22.0 (TID 644) in 82 ms on localhost (executor driver) (18/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 15.0 in stage 22.0 (TID 643) in 137 ms on localhost (executor driver) (19/200)
26/06/26 13:26:34 INFO Executor: Running task 19.0 in stage 22.0 (TID 647)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 18.0 in stage 22.0 (TID 646). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 17.0 in stage 22.0 (TID 645). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 20.0 in stage 22.0 (TID 648)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 21.0 in stage 22.0 (TID 649, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 21.0 in stage 22.0 (TID 649)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 22.0 in stage 22.0 (TID 650, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:34 INFO BlockManagerInfo: Removed broadcast_23_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 3.8 KB, free: 366.1 MB)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 18.0 in stage 22.0 (TID 646) in 67 ms on localhost (executor driver) (20/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 17.0 in stage 22.0 (TID 645) in 68 ms on localhost (executor driver) (21/200)
26/06/26 13:26:34 INFO ContextCleaner: Cleaned accumulator 661
26/06/26 13:26:34 INFO ContextCleaner: Cleaned accumulator 662
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 22.0 in stage 22.0 (TID 650)
26/06/26 13:26:34 INFO Executor: Finished task 20.0 in stage 22.0 (TID 648). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 9 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 23.0 in stage 22.0 (TID 651, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 20.0 in stage 22.0 (TID 648) in 61 ms on localhost (executor driver) (22/200)
26/06/26 13:26:34 INFO Executor: Finished task 21.0 in stage 22.0 (TID 649). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 24.0 in stage 22.0 (TID 652, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 24.0 in stage 22.0 (TID 652)
26/06/26 13:26:34 INFO Executor: Running task 23.0 in stage 22.0 (TID 651)
26/06/26 13:26:34 INFO Executor: Finished task 19.0 in stage 22.0 (TID 647). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Finished task 21.0 in stage 22.0 (TID 649) in 32 ms on localhost (executor driver) (23/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 25.0 in stage 22.0 (TID 653, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 19.0 in stage 22.0 (TID 647) in 81 ms on localhost (executor driver) (24/200)
26/06/26 13:26:34 INFO Executor: Running task 25.0 in stage 22.0 (TID 653)
26/06/26 13:26:34 INFO Executor: Finished task 23.0 in stage 22.0 (TID 651). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 26.0 in stage 22.0 (TID 654, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 26.0 in stage 22.0 (TID 654)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 23.0 in stage 22.0 (TID 651) in 29 ms on localhost (executor driver) (25/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 22.0 in stage 22.0 (TID 650). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 24.0 in stage 22.0 (TID 652). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 27.0 in stage 22.0 (TID 655, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 28.0 in stage 22.0 (TID 656, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 24.0 in stage 22.0 (TID 652) in 35 ms on localhost (executor driver) (26/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 22.0 in stage 22.0 (TID 650) in 65 ms on localhost (executor driver) (27/200)
26/06/26 13:26:34 INFO Executor: Running task 28.0 in stage 22.0 (TID 656)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 27.0 in stage 22.0 (TID 655)
26/06/26 13:26:34 INFO Executor: Finished task 26.0 in stage 22.0 (TID 654). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 25.0 in stage 22.0 (TID 653). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 29.0 in stage 22.0 (TID 657, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 30.0 in stage 22.0 (TID 658, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 29.0 in stage 22.0 (TID 657)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 26.0 in stage 22.0 (TID 654) in 45 ms on localhost (executor driver) (28/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 25.0 in stage 22.0 (TID 653) in 58 ms on localhost (executor driver) (29/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Running task 30.0 in stage 22.0 (TID 658)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 27.0 in stage 22.0 (TID 655). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 29.0 in stage 22.0 (TID 657). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 31.0 in stage 22.0 (TID 659, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 32.0 in stage 22.0 (TID 660, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 27.0 in stage 22.0 (TID 655) in 100 ms on localhost (executor driver) (30/200)
26/06/26 13:26:34 INFO Executor: Running task 31.0 in stage 22.0 (TID 659)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 29.0 in stage 22.0 (TID 657) in 69 ms on localhost (executor driver) (31/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 32.0 in stage 22.0 (TID 660)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 28.0 in stage 22.0 (TID 656). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 30.0 in stage 22.0 (TID 658). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 33.0 in stage 22.0 (TID 661, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 34.0 in stage 22.0 (TID 662, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 28.0 in stage 22.0 (TID 656) in 150 ms on localhost (executor driver) (32/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 30.0 in stage 22.0 (TID 658) in 118 ms on localhost (executor driver) (33/200)
26/06/26 13:26:34 INFO Executor: Finished task 32.0 in stage 22.0 (TID 660). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 35.0 in stage 22.0 (TID 663, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 35.0 in stage 22.0 (TID 663)
26/06/26 13:26:34 INFO Executor: Running task 34.0 in stage 22.0 (TID 662)
26/06/26 13:26:34 INFO Executor: Finished task 31.0 in stage 22.0 (TID 659). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 4 ms
26/06/26 13:26:34 INFO Executor: Running task 33.0 in stage 22.0 (TID 661)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 36.0 in stage 22.0 (TID 664, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO TaskSetManager: Finished task 31.0 in stage 22.0 (TID 659) in 65 ms on localhost (executor driver) (34/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 5 ms
26/06/26 13:26:34 INFO Executor: Running task 36.0 in stage 22.0 (TID 664)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 32.0 in stage 22.0 (TID 660) in 80 ms on localhost (executor driver) (35/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 35.0 in stage 22.0 (TID 663). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 37.0 in stage 22.0 (TID 665, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 35.0 in stage 22.0 (TID 663) in 39 ms on localhost (executor driver) (36/200)
26/06/26 13:26:34 INFO Executor: Running task 37.0 in stage 22.0 (TID 665)
26/06/26 13:26:34 INFO Executor: Finished task 36.0 in stage 22.0 (TID 664). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 38.0 in stage 22.0 (TID 666, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 36.0 in stage 22.0 (TID 664) in 53 ms on localhost (executor driver) (37/200)
26/06/26 13:26:34 INFO Executor: Finished task 34.0 in stage 22.0 (TID 662). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO TaskSetManager: Starting task 39.0 in stage 22.0 (TID 667, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 34.0 in stage 22.0 (TID 662) in 66 ms on localhost (executor driver) (38/200)
26/06/26 13:26:34 INFO Executor: Running task 39.0 in stage 22.0 (TID 667)
26/06/26 13:26:34 INFO Executor: Finished task 33.0 in stage 22.0 (TID 661). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 13 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 40.0 in stage 22.0 (TID 668, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 38.0 in stage 22.0 (TID 666)
26/06/26 13:26:34 INFO Executor: Running task 40.0 in stage 22.0 (TID 668)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 33.0 in stage 22.0 (TID 661) in 79 ms on localhost (executor driver) (39/200)
26/06/26 13:26:34 INFO Executor: Finished task 39.0 in stage 22.0 (TID 667). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 41.0 in stage 22.0 (TID 669, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 40.0 in stage 22.0 (TID 668). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Finished task 39.0 in stage 22.0 (TID 667) in 34 ms on localhost (executor driver) (40/200)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 42.0 in stage 22.0 (TID 670, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 40.0 in stage 22.0 (TID 668) in 25 ms on localhost (executor driver) (41/200)
26/06/26 13:26:34 INFO Executor: Finished task 37.0 in stage 22.0 (TID 665). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 41.0 in stage 22.0 (TID 669)
26/06/26 13:26:34 INFO Executor: Running task 42.0 in stage 22.0 (TID 670)
26/06/26 13:26:34 INFO Executor: Finished task 38.0 in stage 22.0 (TID 666). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 43.0 in stage 22.0 (TID 671, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 44.0 in stage 22.0 (TID 672, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 37.0 in stage 22.0 (TID 665) in 68 ms on localhost (executor driver) (42/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 38.0 in stage 22.0 (TID 666) in 49 ms on localhost (executor driver) (43/200)
26/06/26 13:26:34 INFO Executor: Running task 43.0 in stage 22.0 (TID 671)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 44.0 in stage 22.0 (TID 672)
26/06/26 13:26:34 INFO Executor: Finished task 43.0 in stage 22.0 (TID 671). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 45.0 in stage 22.0 (TID 673, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 45.0 in stage 22.0 (TID 673)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 43.0 in stage 22.0 (TID 671) in 19 ms on localhost (executor driver) (44/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 41.0 in stage 22.0 (TID 669). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 46.0 in stage 22.0 (TID 674, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 41.0 in stage 22.0 (TID 669) in 44 ms on localhost (executor driver) (45/200)
26/06/26 13:26:34 INFO Executor: Running task 46.0 in stage 22.0 (TID 674)
26/06/26 13:26:34 INFO Executor: Finished task 44.0 in stage 22.0 (TID 672). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 47.0 in stage 22.0 (TID 675, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 42.0 in stage 22.0 (TID 670). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 47.0 in stage 22.0 (TID 675)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 44.0 in stage 22.0 (TID 672) in 40 ms on localhost (executor driver) (46/200)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 48.0 in stage 22.0 (TID 676, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 42.0 in stage 22.0 (TID 670) in 48 ms on localhost (executor driver) (47/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 45.0 in stage 22.0 (TID 673). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 49.0 in stage 22.0 (TID 677, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 49.0 in stage 22.0 (TID 677)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 45.0 in stage 22.0 (TID 673) in 39 ms on localhost (executor driver) (48/200)
26/06/26 13:26:34 INFO Executor: Running task 48.0 in stage 22.0 (TID 676)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 47.0 in stage 22.0 (TID 675). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 50.0 in stage 22.0 (TID 678, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 47.0 in stage 22.0 (TID 675) in 79 ms on localhost (executor driver) (49/200)
26/06/26 13:26:34 INFO Executor: Finished task 48.0 in stage 22.0 (TID 676). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 46.0 in stage 22.0 (TID 674). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 50.0 in stage 22.0 (TID 678)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 51.0 in stage 22.0 (TID 679, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 52.0 in stage 22.0 (TID 680, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 51.0 in stage 22.0 (TID 679)
26/06/26 13:26:34 INFO Executor: Finished task 49.0 in stage 22.0 (TID 677). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Finished task 48.0 in stage 22.0 (TID 676) in 89 ms on localhost (executor driver) (50/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 46.0 in stage 22.0 (TID 674) in 98 ms on localhost (executor driver) (51/200)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 53.0 in stage 22.0 (TID 681, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 49.0 in stage 22.0 (TID 677) in 78 ms on localhost (executor driver) (52/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 53.0 in stage 22.0 (TID 681)
26/06/26 13:26:34 INFO Executor: Running task 52.0 in stage 22.0 (TID 680)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Finished task 52.0 in stage 22.0 (TID 680). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 54.0 in stage 22.0 (TID 682, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 52.0 in stage 22.0 (TID 680) in 46 ms on localhost (executor driver) (53/200)
26/06/26 13:26:34 INFO Executor: Running task 54.0 in stage 22.0 (TID 682)
26/06/26 13:26:34 INFO Executor: Finished task 51.0 in stage 22.0 (TID 679). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 50.0 in stage 22.0 (TID 678). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 53.0 in stage 22.0 (TID 681). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 55.0 in stage 22.0 (TID 683, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 56.0 in stage 22.0 (TID 684, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 57.0 in stage 22.0 (TID 685, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 55.0 in stage 22.0 (TID 683)
26/06/26 13:26:34 INFO Executor: Running task 56.0 in stage 22.0 (TID 684)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 50.0 in stage 22.0 (TID 678) in 70 ms on localhost (executor driver) (54/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 53.0 in stage 22.0 (TID 681) in 58 ms on localhost (executor driver) (55/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 51.0 in stage 22.0 (TID 679) in 61 ms on localhost (executor driver) (56/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO Executor: Running task 57.0 in stage 22.0 (TID 685)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 54.0 in stage 22.0 (TID 682). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 58.0 in stage 22.0 (TID 686, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 54.0 in stage 22.0 (TID 682) in 48 ms on localhost (executor driver) (57/200)
26/06/26 13:26:34 INFO Executor: Running task 58.0 in stage 22.0 (TID 686)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 55.0 in stage 22.0 (TID 683). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 59.0 in stage 22.0 (TID 687, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 57.0 in stage 22.0 (TID 685). 3292 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 59.0 in stage 22.0 (TID 687)
26/06/26 13:26:34 INFO TaskSetManager: Starting task 60.0 in stage 22.0 (TID 688, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 55.0 in stage 22.0 (TID 683) in 43 ms on localhost (executor driver) (58/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 57.0 in stage 22.0 (TID 685) in 42 ms on localhost (executor driver) (59/200)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 56.0 in stage 22.0 (TID 684). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 61.0 in stage 22.0 (TID 689, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 60.0 in stage 22.0 (TID 688)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 56.0 in stage 22.0 (TID 684) in 58 ms on localhost (executor driver) (60/200)
26/06/26 13:26:34 INFO Executor: Finished task 58.0 in stage 22.0 (TID 686). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Running task 61.0 in stage 22.0 (TID 689)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:34 INFO TaskSetManager: Starting task 62.0 in stage 22.0 (TID 690, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Finished task 60.0 in stage 22.0 (TID 688). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 63.0 in stage 22.0 (TID 691, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 63.0 in stage 22.0 (TID 691)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO TaskSetManager: Finished task 58.0 in stage 22.0 (TID 686) in 44 ms on localhost (executor driver) (61/200)
26/06/26 13:26:34 INFO TaskSetManager: Finished task 60.0 in stage 22.0 (TID 688) in 36 ms on localhost (executor driver) (62/200)
26/06/26 13:26:34 INFO Executor: Running task 62.0 in stage 22.0 (TID 690)
26/06/26 13:26:34 INFO Executor: Finished task 59.0 in stage 22.0 (TID 687). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Starting task 64.0 in stage 22.0 (TID 692, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:34 INFO Executor: Running task 64.0 in stage 22.0 (TID 692)
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:34 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:34 INFO Executor: Finished task 61.0 in stage 22.0 (TID 689). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO Executor: Finished task 62.0 in stage 22.0 (TID 690). 3249 bytes result sent to driver
26/06/26 13:26:34 INFO TaskSetManager: Finished task 59.0 in stage 22.0 (TID 687) in 47 ms on localhost (executor driver) (63/200)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 65.0 in stage 22.0 (TID 693, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 65.0 in stage 22.0 (TID 693)
26/06/26 13:26:34 INFO Executor: Finished task 63.0 in stage 22.0 (TID 691). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 66.0 in stage 22.0 (TID 694, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 67.0 in stage 22.0 (TID 695, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 61.0 in stage 22.0 (TID 689) in 42 ms on localhost (executor driver) (64/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 62.0 in stage 22.0 (TID 690) in 29 ms on localhost (executor driver) (65/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 63.0 in stage 22.0 (TID 691) in 27 ms on localhost (executor driver) (66/200)
26/06/26 13:26:35 INFO Executor: Running task 66.0 in stage 22.0 (TID 694)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 64.0 in stage 22.0 (TID 692). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 67.0 in stage 22.0 (TID 695)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO TaskSetManager: Starting task 68.0 in stage 22.0 (TID 696, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 68.0 in stage 22.0 (TID 696)
26/06/26 13:26:35 INFO Executor: Finished task 66.0 in stage 22.0 (TID 694). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 69.0 in stage 22.0 (TID 697, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 69.0 in stage 22.0 (TID 697)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 67.0 in stage 22.0 (TID 695). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Finished task 64.0 in stage 22.0 (TID 692) in 42 ms on localhost (executor driver) (67/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 66.0 in stage 22.0 (TID 694) in 29 ms on localhost (executor driver) (68/200)
26/06/26 13:26:35 INFO Executor: Finished task 65.0 in stage 22.0 (TID 693). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 69.0 in stage 22.0 (TID 697). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 70.0 in stage 22.0 (TID 698, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 71.0 in stage 22.0 (TID 699, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 72.0 in stage 22.0 (TID 700, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 71.0 in stage 22.0 (TID 699)
26/06/26 13:26:35 INFO Executor: Running task 70.0 in stage 22.0 (TID 698)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 72.0 in stage 22.0 (TID 700)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 67.0 in stage 22.0 (TID 695) in 49 ms on localhost (executor driver) (69/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 65.0 in stage 22.0 (TID 693) in 52 ms on localhost (executor driver) (70/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 69.0 in stage 22.0 (TID 697) in 28 ms on localhost (executor driver) (71/200)
26/06/26 13:26:35 INFO Executor: Finished task 70.0 in stage 22.0 (TID 698). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 68.0 in stage 22.0 (TID 696). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 71.0 in stage 22.0 (TID 699). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 72.0 in stage 22.0 (TID 700). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 73.0 in stage 22.0 (TID 701, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 74.0 in stage 22.0 (TID 702, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 75.0 in stage 22.0 (TID 703, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 76.0 in stage 22.0 (TID 704, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 70.0 in stage 22.0 (TID 698) in 23 ms on localhost (executor driver) (72/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 68.0 in stage 22.0 (TID 696) in 45 ms on localhost (executor driver) (73/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 71.0 in stage 22.0 (TID 699) in 24 ms on localhost (executor driver) (74/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 72.0 in stage 22.0 (TID 700) in 24 ms on localhost (executor driver) (75/200)
26/06/26 13:26:35 INFO Executor: Running task 73.0 in stage 22.0 (TID 701)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 74.0 in stage 22.0 (TID 702)
26/06/26 13:26:35 INFO Executor: Running task 75.0 in stage 22.0 (TID 703)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 76.0 in stage 22.0 (TID 704)
26/06/26 13:26:35 INFO Executor: Finished task 73.0 in stage 22.0 (TID 701). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 77.0 in stage 22.0 (TID 705, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 73.0 in stage 22.0 (TID 701) in 16 ms on localhost (executor driver) (76/200)
26/06/26 13:26:35 INFO Executor: Running task 77.0 in stage 22.0 (TID 705)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 74.0 in stage 22.0 (TID 702). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 77.0 in stage 22.0 (TID 705). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 78.0 in stage 22.0 (TID 706, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 79.0 in stage 22.0 (TID 707, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 78.0 in stage 22.0 (TID 706)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO TaskSetManager: Finished task 74.0 in stage 22.0 (TID 702) in 29 ms on localhost (executor driver) (77/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 77.0 in stage 22.0 (TID 705) in 13 ms on localhost (executor driver) (78/200)
26/06/26 13:26:35 INFO Executor: Running task 79.0 in stage 22.0 (TID 707)
26/06/26 13:26:35 INFO Executor: Finished task 76.0 in stage 22.0 (TID 704). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 75.0 in stage 22.0 (TID 703). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 80.0 in stage 22.0 (TID 708, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 81.0 in stage 22.0 (TID 709, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 80.0 in stage 22.0 (TID 708)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 81.0 in stage 22.0 (TID 709)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Finished task 76.0 in stage 22.0 (TID 704) in 62 ms on localhost (executor driver) (79/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 75.0 in stage 22.0 (TID 703) in 64 ms on localhost (executor driver) (80/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 78.0 in stage 22.0 (TID 706). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 80.0 in stage 22.0 (TID 708). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 82.0 in stage 22.0 (TID 710, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 82.0 in stage 22.0 (TID 710)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 83.0 in stage 22.0 (TID 711, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Finished task 79.0 in stage 22.0 (TID 707). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 84.0 in stage 22.0 (TID 712, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 81.0 in stage 22.0 (TID 709). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 84.0 in stage 22.0 (TID 712)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 85.0 in stage 22.0 (TID 713, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 83.0 in stage 22.0 (TID 711)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 85.0 in stage 22.0 (TID 713)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 78.0 in stage 22.0 (TID 706) in 95 ms on localhost (executor driver) (81/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 80.0 in stage 22.0 (TID 708) in 64 ms on localhost (executor driver) (82/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 79.0 in stage 22.0 (TID 707) in 96 ms on localhost (executor driver) (83/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 81.0 in stage 22.0 (TID 709) in 63 ms on localhost (executor driver) (84/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 83.0 in stage 22.0 (TID 711). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 86.0 in stage 22.0 (TID 714, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 83.0 in stage 22.0 (TID 711) in 31 ms on localhost (executor driver) (85/200)
26/06/26 13:26:35 INFO Executor: Running task 86.0 in stage 22.0 (TID 714)
26/06/26 13:26:35 INFO Executor: Finished task 84.0 in stage 22.0 (TID 712). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Starting task 87.0 in stage 22.0 (TID 715, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 84.0 in stage 22.0 (TID 712) in 45 ms on localhost (executor driver) (86/200)
26/06/26 13:26:35 INFO Executor: Finished task 85.0 in stage 22.0 (TID 713). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 88.0 in stage 22.0 (TID 716, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 87.0 in stage 22.0 (TID 715)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 85.0 in stage 22.0 (TID 713) in 55 ms on localhost (executor driver) (87/200)
26/06/26 13:26:35 INFO Executor: Running task 88.0 in stage 22.0 (TID 716)
26/06/26 13:26:35 INFO Executor: Finished task 82.0 in stage 22.0 (TID 710). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 89.0 in stage 22.0 (TID 717, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 82.0 in stage 22.0 (TID 710) in 74 ms on localhost (executor driver) (88/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO Executor: Finished task 86.0 in stage 22.0 (TID 714). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 90.0 in stage 22.0 (TID 718, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Finished task 86.0 in stage 22.0 (TID 714) in 46 ms on localhost (executor driver) (89/200)
26/06/26 13:26:35 INFO Executor: Running task 89.0 in stage 22.0 (TID 717)
26/06/26 13:26:35 INFO Executor: Finished task 88.0 in stage 22.0 (TID 716). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 90.0 in stage 22.0 (TID 718)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 14 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Starting task 91.0 in stage 22.0 (TID 719, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 88.0 in stage 22.0 (TID 716) in 58 ms on localhost (executor driver) (90/200)
26/06/26 13:26:35 INFO Executor: Running task 91.0 in stage 22.0 (TID 719)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO Executor: Finished task 87.0 in stage 22.0 (TID 715). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 93.0 in stage 22.0 (TID 720, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 87.0 in stage 22.0 (TID 715) in 81 ms on localhost (executor driver) (91/200)
26/06/26 13:26:35 INFO Executor: Finished task 90.0 in stage 22.0 (TID 718). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 89.0 in stage 22.0 (TID 717). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 94.0 in stage 22.0 (TID 721, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 95.0 in stage 22.0 (TID 722, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 90.0 in stage 22.0 (TID 718) in 64 ms on localhost (executor driver) (92/200)
26/06/26 13:26:35 INFO Executor: Finished task 91.0 in stage 22.0 (TID 719). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 94.0 in stage 22.0 (TID 721)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 89.0 in stage 22.0 (TID 717) in 69 ms on localhost (executor driver) (93/200)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 96.0 in stage 22.0 (TID 723, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 91.0 in stage 22.0 (TID 719) in 25 ms on localhost (executor driver) (94/200)
26/06/26 13:26:35 INFO Executor: Running task 95.0 in stage 22.0 (TID 722)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 93.0 in stage 22.0 (TID 720)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO Executor: Finished task 94.0 in stage 22.0 (TID 721). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 97.0 in stage 22.0 (TID 724, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 96.0 in stage 22.0 (TID 723)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 94.0 in stage 22.0 (TID 721) in 25 ms on localhost (executor driver) (95/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 97.0 in stage 22.0 (TID 724)
26/06/26 13:26:35 INFO Executor: Finished task 93.0 in stage 22.0 (TID 720). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 98.0 in stage 22.0 (TID 725, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 98.0 in stage 22.0 (TID 725)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 93.0 in stage 22.0 (TID 720) in 43 ms on localhost (executor driver) (96/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 95.0 in stage 22.0 (TID 722). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 99.0 in stage 22.0 (TID 726, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 95.0 in stage 22.0 (TID 722) in 45 ms on localhost (executor driver) (97/200)
26/06/26 13:26:35 INFO Executor: Running task 99.0 in stage 22.0 (TID 726)
26/06/26 13:26:35 INFO Executor: Finished task 96.0 in stage 22.0 (TID 723). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 98.0 in stage 22.0 (TID 725). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 100.0 in stage 22.0 (TID 727, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 101.0 in stage 22.0 (TID 728, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Finished task 97.0 in stage 22.0 (TID 724). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 101.0 in stage 22.0 (TID 728)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 96.0 in stage 22.0 (TID 723) in 47 ms on localhost (executor driver) (98/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 98.0 in stage 22.0 (TID 725) in 21 ms on localhost (executor driver) (99/200)
26/06/26 13:26:35 INFO Executor: Running task 100.0 in stage 22.0 (TID 727)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 102.0 in stage 22.0 (TID 729, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 97.0 in stage 22.0 (TID 724) in 31 ms on localhost (executor driver) (100/200)
26/06/26 13:26:35 INFO Executor: Running task 102.0 in stage 22.0 (TID 729)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 99.0 in stage 22.0 (TID 726). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 102.0 in stage 22.0 (TID 729). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:35 INFO TaskSetManager: Starting task 103.0 in stage 22.0 (TID 730, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 104.0 in stage 22.0 (TID 731, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 99.0 in stage 22.0 (TID 726) in 28 ms on localhost (executor driver) (101/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 102.0 in stage 22.0 (TID 729) in 20 ms on localhost (executor driver) (102/200)
26/06/26 13:26:35 INFO Executor: Running task 104.0 in stage 22.0 (TID 731)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 101.0 in stage 22.0 (TID 728). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Running task 103.0 in stage 22.0 (TID 730)
26/06/26 13:26:35 INFO Executor: Finished task 100.0 in stage 22.0 (TID 727). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 104.0 in stage 22.0 (TID 731). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 105.0 in stage 22.0 (TID 732, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 106.0 in stage 22.0 (TID 733, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 107.0 in stage 22.0 (TID 734, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 101.0 in stage 22.0 (TID 728) in 32 ms on localhost (executor driver) (103/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 100.0 in stage 22.0 (TID 727) in 34 ms on localhost (executor driver) (104/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 104.0 in stage 22.0 (TID 731) in 12 ms on localhost (executor driver) (105/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 105.0 in stage 22.0 (TID 732)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO Executor: Running task 106.0 in stage 22.0 (TID 733)
26/06/26 13:26:35 INFO Executor: Running task 107.0 in stage 22.0 (TID 734)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 9 ms
26/06/26 13:26:35 INFO Executor: Finished task 105.0 in stage 22.0 (TID 732). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 108.0 in stage 22.0 (TID 735, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 108.0 in stage 22.0 (TID 735)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 105.0 in stage 22.0 (TID 732) in 114 ms on localhost (executor driver) (106/200)
26/06/26 13:26:35 INFO Executor: Finished task 106.0 in stage 22.0 (TID 733). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 103.0 in stage 22.0 (TID 730). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO Executor: Finished task 107.0 in stage 22.0 (TID 734). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 109.0 in stage 22.0 (TID 736, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 110.0 in stage 22.0 (TID 737, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Starting task 111.0 in stage 22.0 (TID 738, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 111.0 in stage 22.0 (TID 738)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 106.0 in stage 22.0 (TID 733) in 128 ms on localhost (executor driver) (107/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 103.0 in stage 22.0 (TID 730) in 139 ms on localhost (executor driver) (108/200)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 107.0 in stage 22.0 (TID 734) in 128 ms on localhost (executor driver) (109/200)
26/06/26 13:26:35 INFO Executor: Running task 109.0 in stage 22.0 (TID 736)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 110.0 in stage 22.0 (TID 737)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 111.0 in stage 22.0 (TID 738). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 112.0 in stage 22.0 (TID 739, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 112.0 in stage 22.0 (TID 739)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Finished task 111.0 in stage 22.0 (TID 738) in 18 ms on localhost (executor driver) (110/200)
26/06/26 13:26:35 INFO Executor: Finished task 112.0 in stage 22.0 (TID 739). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 113.0 in stage 22.0 (TID 740, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 113.0 in stage 22.0 (TID 740)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 112.0 in stage 22.0 (TID 739) in 12 ms on localhost (executor driver) (111/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Finished task 108.0 in stage 22.0 (TID 735). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 114.0 in stage 22.0 (TID 741, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 108.0 in stage 22.0 (TID 735) in 255 ms on localhost (executor driver) (112/200)
26/06/26 13:26:35 INFO Executor: Finished task 109.0 in stage 22.0 (TID 736). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 115.0 in stage 22.0 (TID 742, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 109.0 in stage 22.0 (TID 736) in 165 ms on localhost (executor driver) (113/200)
26/06/26 13:26:35 INFO Executor: Finished task 110.0 in stage 22.0 (TID 737). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 116.0 in stage 22.0 (TID 743, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 110.0 in stage 22.0 (TID 737) in 167 ms on localhost (executor driver) (114/200)
26/06/26 13:26:35 INFO Executor: Running task 116.0 in stage 22.0 (TID 743)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 115.0 in stage 22.0 (TID 742)
26/06/26 13:26:35 INFO Executor: Finished task 113.0 in stage 22.0 (TID 740). 3292 bytes result sent to driver
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO TaskSetManager: Starting task 117.0 in stage 22.0 (TID 744, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 114.0 in stage 22.0 (TID 741)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:35 INFO Executor: Running task 117.0 in stage 22.0 (TID 744)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 113.0 in stage 22.0 (TID 740) in 203 ms on localhost (executor driver) (115/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:35 INFO Executor: Finished task 117.0 in stage 22.0 (TID 744). 3249 bytes result sent to driver
26/06/26 13:26:35 INFO TaskSetManager: Starting task 118.0 in stage 22.0 (TID 745, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:35 INFO Executor: Running task 118.0 in stage 22.0 (TID 745)
26/06/26 13:26:35 INFO TaskSetManager: Finished task 117.0 in stage 22.0 (TID 744) in 54 ms on localhost (executor driver) (116/200)
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:35 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Finished task 115.0 in stage 22.0 (TID 742). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 119.0 in stage 22.0 (TID 746, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 115.0 in stage 22.0 (TID 742) in 703 ms on localhost (executor driver) (117/200)
26/06/26 13:26:36 INFO Executor: Running task 119.0 in stage 22.0 (TID 746)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 114.0 in stage 22.0 (TID 741). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 120.0 in stage 22.0 (TID 747, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 114.0 in stage 22.0 (TID 741) in 737 ms on localhost (executor driver) (118/200)
26/06/26 13:26:36 INFO Executor: Running task 120.0 in stage 22.0 (TID 747)
26/06/26 13:26:36 INFO Executor: Finished task 119.0 in stage 22.0 (TID 746). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 116.0 in stage 22.0 (TID 743). 3292 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Starting task 121.0 in stage 22.0 (TID 748, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 121.0 in stage 22.0 (TID 748)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 122.0 in stage 22.0 (TID 749, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 116.0 in stage 22.0 (TID 743) in 740 ms on localhost (executor driver) (119/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 120.0 in stage 22.0 (TID 747). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 121.0 in stage 22.0 (TID 748). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Finished task 119.0 in stage 22.0 (TID 746) in 53 ms on localhost (executor driver) (120/200)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 123.0 in stage 22.0 (TID 750, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 124.0 in stage 22.0 (TID 751, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 120.0 in stage 22.0 (TID 747) in 22 ms on localhost (executor driver) (121/200)
26/06/26 13:26:36 INFO Executor: Running task 122.0 in stage 22.0 (TID 749)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 121.0 in stage 22.0 (TID 748) in 16 ms on localhost (executor driver) (122/200)
26/06/26 13:26:36 INFO Executor: Running task 123.0 in stage 22.0 (TID 750)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 124.0 in stage 22.0 (TID 751)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 122.0 in stage 22.0 (TID 749). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 118.0 in stage 22.0 (TID 745). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 125.0 in stage 22.0 (TID 752, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 126.0 in stage 22.0 (TID 753, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 122.0 in stage 22.0 (TID 749) in 40 ms on localhost (executor driver) (123/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 118.0 in stage 22.0 (TID 745) in 686 ms on localhost (executor driver) (124/200)
26/06/26 13:26:36 INFO Executor: Running task 126.0 in stage 22.0 (TID 753)
26/06/26 13:26:36 INFO Executor: Finished task 124.0 in stage 22.0 (TID 751). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 127.0 in stage 22.0 (TID 754, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 127.0 in stage 22.0 (TID 754)
26/06/26 13:26:36 INFO Executor: Running task 125.0 in stage 22.0 (TID 752)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 127.0 in stage 22.0 (TID 754). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 128.0 in stage 22.0 (TID 755, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 128.0 in stage 22.0 (TID 755)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 124.0 in stage 22.0 (TID 751) in 50 ms on localhost (executor driver) (125/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 127.0 in stage 22.0 (TID 754) in 22 ms on localhost (executor driver) (126/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 123.0 in stage 22.0 (TID 750). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 126.0 in stage 22.0 (TID 753). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 129.0 in stage 22.0 (TID 756, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 130.0 in stage 22.0 (TID 757, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 130.0 in stage 22.0 (TID 757)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 123.0 in stage 22.0 (TID 750) in 72 ms on localhost (executor driver) (127/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 126.0 in stage 22.0 (TID 753) in 45 ms on localhost (executor driver) (128/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 129.0 in stage 22.0 (TID 756)
26/06/26 13:26:36 INFO Executor: Finished task 125.0 in stage 22.0 (TID 752). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 131.0 in stage 22.0 (TID 758, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 131.0 in stage 22.0 (TID 758)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 125.0 in stage 22.0 (TID 752) in 55 ms on localhost (executor driver) (129/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 131.0 in stage 22.0 (TID 758). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 130.0 in stage 22.0 (TID 757). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 132.0 in stage 22.0 (TID 759, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 133.0 in stage 22.0 (TID 760, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 131.0 in stage 22.0 (TID 758) in 43 ms on localhost (executor driver) (130/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 130.0 in stage 22.0 (TID 757) in 56 ms on localhost (executor driver) (131/200)
26/06/26 13:26:36 INFO Executor: Finished task 128.0 in stage 22.0 (TID 755). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 134.0 in stage 22.0 (TID 761, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 134.0 in stage 22.0 (TID 761)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Finished task 128.0 in stage 22.0 (TID 755) in 88 ms on localhost (executor driver) (132/200)
26/06/26 13:26:36 INFO Executor: Finished task 129.0 in stage 22.0 (TID 756). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 135.0 in stage 22.0 (TID 762, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 135.0 in stage 22.0 (TID 762)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 129.0 in stage 22.0 (TID 756) in 86 ms on localhost (executor driver) (133/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Running task 132.0 in stage 22.0 (TID 759)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 133.0 in stage 22.0 (TID 760)
26/06/26 13:26:36 INFO Executor: Finished task 134.0 in stage 22.0 (TID 761). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 136.0 in stage 22.0 (TID 763, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 136.0 in stage 22.0 (TID 763)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 134.0 in stage 22.0 (TID 761) in 56 ms on localhost (executor driver) (134/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 6 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 132.0 in stage 22.0 (TID 759). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 137.0 in stage 22.0 (TID 764, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Finished task 135.0 in stage 22.0 (TID 762). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Finished task 132.0 in stage 22.0 (TID 759) in 94 ms on localhost (executor driver) (135/200)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 138.0 in stage 22.0 (TID 765, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 135.0 in stage 22.0 (TID 762) in 67 ms on localhost (executor driver) (136/200)
26/06/26 13:26:36 INFO Executor: Running task 137.0 in stage 22.0 (TID 764)
26/06/26 13:26:36 INFO Executor: Finished task 133.0 in stage 22.0 (TID 760). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 136.0 in stage 22.0 (TID 763). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 139.0 in stage 22.0 (TID 766, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 133.0 in stage 22.0 (TID 760) in 103 ms on localhost (executor driver) (137/200)
26/06/26 13:26:36 INFO Executor: Running task 139.0 in stage 22.0 (TID 766)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Starting task 140.0 in stage 22.0 (TID 767, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 138.0 in stage 22.0 (TID 765)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 136.0 in stage 22.0 (TID 763) in 37 ms on localhost (executor driver) (138/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 140.0 in stage 22.0 (TID 767)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Finished task 139.0 in stage 22.0 (TID 766). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 137.0 in stage 22.0 (TID 764). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 138.0 in stage 22.0 (TID 765). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 141.0 in stage 22.0 (TID 768, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 142.0 in stage 22.0 (TID 769, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 143.0 in stage 22.0 (TID 770, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 142.0 in stage 22.0 (TID 769)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 139.0 in stage 22.0 (TID 766) in 82 ms on localhost (executor driver) (139/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 137.0 in stage 22.0 (TID 764) in 104 ms on localhost (executor driver) (140/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 138.0 in stage 22.0 (TID 765) in 89 ms on localhost (executor driver) (141/200)
26/06/26 13:26:36 INFO Executor: Running task 143.0 in stage 22.0 (TID 770)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 141.0 in stage 22.0 (TID 768)
26/06/26 13:26:36 INFO Executor: Finished task 142.0 in stage 22.0 (TID 769). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO TaskSetManager: Starting task 144.0 in stage 22.0 (TID 771, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 144.0 in stage 22.0 (TID 771)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Finished task 141.0 in stage 22.0 (TID 768). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 145.0 in stage 22.0 (TID 772, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 145.0 in stage 22.0 (TID 772)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Finished task 144.0 in stage 22.0 (TID 771). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 146.0 in stage 22.0 (TID 773, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Finished task 140.0 in stage 22.0 (TID 767). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Finished task 141.0 in stage 22.0 (TID 768) in 72 ms on localhost (executor driver) (142/200)
26/06/26 13:26:36 INFO Executor: Finished task 145.0 in stage 22.0 (TID 772). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Finished task 144.0 in stage 22.0 (TID 771) in 28 ms on localhost (executor driver) (143/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 142.0 in stage 22.0 (TID 769) in 45 ms on localhost (executor driver) (144/200)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 147.0 in stage 22.0 (TID 774, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 148.0 in stage 22.0 (TID 775, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 140.0 in stage 22.0 (TID 767) in 125 ms on localhost (executor driver) (145/200)
26/06/26 13:26:36 INFO Executor: Running task 148.0 in stage 22.0 (TID 775)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 145.0 in stage 22.0 (TID 772) in 20 ms on localhost (executor driver) (146/200)
26/06/26 13:26:36 INFO Executor: Finished task 143.0 in stage 22.0 (TID 770). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Running task 146.0 in stage 22.0 (TID 773)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 149.0 in stage 22.0 (TID 776, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 149.0 in stage 22.0 (TID 776)
26/06/26 13:26:36 INFO Executor: Running task 147.0 in stage 22.0 (TID 774)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 143.0 in stage 22.0 (TID 770) in 60 ms on localhost (executor driver) (147/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Finished task 148.0 in stage 22.0 (TID 775). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Starting task 150.0 in stage 22.0 (TID 777, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 150.0 in stage 22.0 (TID 777)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Finished task 148.0 in stage 22.0 (TID 775) in 35 ms on localhost (executor driver) (148/200)
26/06/26 13:26:36 INFO Executor: Finished task 147.0 in stage 22.0 (TID 774). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 151.0 in stage 22.0 (TID 778, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 151.0 in stage 22.0 (TID 778)
26/06/26 13:26:36 INFO Executor: Finished task 149.0 in stage 22.0 (TID 776). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 152.0 in stage 22.0 (TID 779, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO TaskSetManager: Finished task 147.0 in stage 22.0 (TID 774) in 60 ms on localhost (executor driver) (149/200)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 149.0 in stage 22.0 (TID 776) in 46 ms on localhost (executor driver) (150/200)
26/06/26 13:26:36 INFO Executor: Running task 152.0 in stage 22.0 (TID 779)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:36 INFO Executor: Finished task 151.0 in stage 22.0 (TID 778). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 153.0 in stage 22.0 (TID 780, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 151.0 in stage 22.0 (TID 778) in 67 ms on localhost (executor driver) (151/200)
26/06/26 13:26:36 INFO Executor: Finished task 150.0 in stage 22.0 (TID 777). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 154.0 in stage 22.0 (TID 781, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 154.0 in stage 22.0 (TID 781)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO Executor: Running task 153.0 in stage 22.0 (TID 780)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Finished task 150.0 in stage 22.0 (TID 777) in 105 ms on localhost (executor driver) (152/200)
26/06/26 13:26:36 INFO Executor: Finished task 154.0 in stage 22.0 (TID 781). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 155.0 in stage 22.0 (TID 782, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 155.0 in stage 22.0 (TID 782)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 154.0 in stage 22.0 (TID 781) in 16 ms on localhost (executor driver) (153/200)
26/06/26 13:26:36 INFO Executor: Finished task 146.0 in stage 22.0 (TID 773). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO TaskSetManager: Starting task 156.0 in stage 22.0 (TID 783, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Finished task 152.0 in stage 22.0 (TID 779). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Running task 156.0 in stage 22.0 (TID 783)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 146.0 in stage 22.0 (TID 773) in 154 ms on localhost (executor driver) (154/200)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 157.0 in stage 22.0 (TID 784, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 157.0 in stage 22.0 (TID 784)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO TaskSetManager: Finished task 152.0 in stage 22.0 (TID 779) in 121 ms on localhost (executor driver) (155/200)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:36 INFO Executor: Finished task 157.0 in stage 22.0 (TID 784). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 158.0 in stage 22.0 (TID 785, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Finished task 157.0 in stage 22.0 (TID 784) in 33 ms on localhost (executor driver) (156/200)
26/06/26 13:26:36 INFO Executor: Finished task 156.0 in stage 22.0 (TID 783). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 159.0 in stage 22.0 (TID 786, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Finished task 155.0 in stage 22.0 (TID 782). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Running task 158.0 in stage 22.0 (TID 785)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:36 INFO TaskSetManager: Starting task 160.0 in stage 22.0 (TID 787, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Finished task 153.0 in stage 22.0 (TID 780). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO Executor: Finished task 158.0 in stage 22.0 (TID 785). 3249 bytes result sent to driver
26/06/26 13:26:36 INFO TaskSetManager: Starting task 161.0 in stage 22.0 (TID 788, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:36 INFO TaskSetManager: Starting task 162.0 in stage 22.0 (TID 789, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:36 INFO Executor: Running task 160.0 in stage 22.0 (TID 787)
26/06/26 13:26:36 INFO Executor: Running task 162.0 in stage 22.0 (TID 789)
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:36 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 156.0 in stage 22.0 (TID 783) in 92 ms on localhost (executor driver) (157/200)
26/06/26 13:26:37 INFO Executor: Finished task 162.0 in stage 22.0 (TID 789). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Running task 159.0 in stage 22.0 (TID 786)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Running task 161.0 in stage 22.0 (TID 788)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 159.0 in stage 22.0 (TID 786). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 155.0 in stage 22.0 (TID 782) in 102 ms on localhost (executor driver) (158/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 158.0 in stage 22.0 (TID 785) in 67 ms on localhost (executor driver) (159/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 153.0 in stage 22.0 (TID 780) in 153 ms on localhost (executor driver) (160/200)
26/06/26 13:26:37 INFO Executor: Finished task 160.0 in stage 22.0 (TID 787). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 163.0 in stage 22.0 (TID 790, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 164.0 in stage 22.0 (TID 791, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 165.0 in stage 22.0 (TID 792, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Finished task 161.0 in stage 22.0 (TID 788). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 166.0 in stage 22.0 (TID 793, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 163.0 in stage 22.0 (TID 790)
26/06/26 13:26:37 INFO Executor: Running task 166.0 in stage 22.0 (TID 793)
26/06/26 13:26:37 INFO Executor: Running task 165.0 in stage 22.0 (TID 792)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 166.0 in stage 22.0 (TID 793). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 167.0 in stage 22.0 (TID 794, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 8 ms
26/06/26 13:26:37 INFO Executor: Finished task 165.0 in stage 22.0 (TID 792). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 163.0 in stage 22.0 (TID 790). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 168.0 in stage 22.0 (TID 795, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 169.0 in stage 22.0 (TID 796, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 168.0 in stage 22.0 (TID 795)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 168.0 in stage 22.0 (TID 795). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Running task 169.0 in stage 22.0 (TID 796)
26/06/26 13:26:37 INFO Executor: Running task 167.0 in stage 22.0 (TID 794)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:37 INFO Executor: Finished task 167.0 in stage 22.0 (TID 794). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 170.0 in stage 22.0 (TID 797, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 171.0 in stage 22.0 (TID 798, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 171.0 in stage 22.0 (TID 798)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 171.0 in stage 22.0 (TID 798). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 172.0 in stage 22.0 (TID 799, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 170.0 in stage 22.0 (TID 797)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 162.0 in stage 22.0 (TID 789) in 102 ms on localhost (executor driver) (161/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 159.0 in stage 22.0 (TID 786) in 127 ms on localhost (executor driver) (162/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 160.0 in stage 22.0 (TID 787) in 105 ms on localhost (executor driver) (163/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 161.0 in stage 22.0 (TID 788) in 104 ms on localhost (executor driver) (164/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 166.0 in stage 22.0 (TID 793) in 59 ms on localhost (executor driver) (165/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 165.0 in stage 22.0 (TID 792) in 62 ms on localhost (executor driver) (166/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 163.0 in stage 22.0 (TID 790) in 63 ms on localhost (executor driver) (167/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 168.0 in stage 22.0 (TID 795) in 44 ms on localhost (executor driver) (168/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 167.0 in stage 22.0 (TID 794) in 50 ms on localhost (executor driver) (169/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 171.0 in stage 22.0 (TID 798) in 23 ms on localhost (executor driver) (170/200)
26/06/26 13:26:37 INFO Executor: Running task 164.0 in stage 22.0 (TID 791)
26/06/26 13:26:37 INFO Executor: Finished task 170.0 in stage 22.0 (TID 797). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 173.0 in stage 22.0 (TID 800, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 172.0 in stage 22.0 (TID 799)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 170.0 in stage 22.0 (TID 797) in 47 ms on localhost (executor driver) (171/200)
26/06/26 13:26:37 INFO Executor: Finished task 172.0 in stage 22.0 (TID 799). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 174.0 in stage 22.0 (TID 801, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Finished task 164.0 in stage 22.0 (TID 791). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Running task 174.0 in stage 22.0 (TID 801)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 175.0 in stage 22.0 (TID 802, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 173.0 in stage 22.0 (TID 800)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 174.0 in stage 22.0 (TID 801). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 173.0 in stage 22.0 (TID 800). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 176.0 in stage 22.0 (TID 803, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 177.0 in stage 22.0 (TID 804, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 175.0 in stage 22.0 (TID 802)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 174.0 in stage 22.0 (TID 801) in 12 ms on localhost (executor driver) (172/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 173.0 in stage 22.0 (TID 800) in 23 ms on localhost (executor driver) (173/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 172.0 in stage 22.0 (TID 799) in 37 ms on localhost (executor driver) (174/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 164.0 in stage 22.0 (TID 791) in 90 ms on localhost (executor driver) (175/200)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 175.0 in stage 22.0 (TID 802). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 178.0 in stage 22.0 (TID 805, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 176.0 in stage 22.0 (TID 803)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 175.0 in stage 22.0 (TID 802) in 24 ms on localhost (executor driver) (176/200)
26/06/26 13:26:37 INFO Executor: Running task 177.0 in stage 22.0 (TID 804)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:37 INFO Executor: Finished task 176.0 in stage 22.0 (TID 803). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 179.0 in stage 22.0 (TID 806, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 178.0 in stage 22.0 (TID 805)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 176.0 in stage 22.0 (TID 803) in 27 ms on localhost (executor driver) (177/200)
26/06/26 13:26:37 INFO Executor: Finished task 177.0 in stage 22.0 (TID 804). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 178.0 in stage 22.0 (TID 805). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 181.0 in stage 22.0 (TID 807, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 182.0 in stage 22.0 (TID 808, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 179.0 in stage 22.0 (TID 806)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 179.0 in stage 22.0 (TID 806). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 183.0 in stage 22.0 (TID 809, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 181.0 in stage 22.0 (TID 807)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 177.0 in stage 22.0 (TID 804) in 47 ms on localhost (executor driver) (178/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 178.0 in stage 22.0 (TID 805) in 37 ms on localhost (executor driver) (179/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 179.0 in stage 22.0 (TID 806) in 26 ms on localhost (executor driver) (180/200)
26/06/26 13:26:37 INFO Executor: Running task 182.0 in stage 22.0 (TID 808)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 181.0 in stage 22.0 (TID 807). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 184.0 in stage 22.0 (TID 810, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 183.0 in stage 22.0 (TID 809)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 182.0 in stage 22.0 (TID 808). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 181.0 in stage 22.0 (TID 807) in 25 ms on localhost (executor driver) (181/200)
26/06/26 13:26:37 INFO Executor: Finished task 183.0 in stage 22.0 (TID 809). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 185.0 in stage 22.0 (TID 811, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 186.0 in stage 22.0 (TID 812, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 184.0 in stage 22.0 (TID 810)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 184.0 in stage 22.0 (TID 810). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 187.0 in stage 22.0 (TID 813, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 185.0 in stage 22.0 (TID 811)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 182.0 in stage 22.0 (TID 808) in 46 ms on localhost (executor driver) (182/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 183.0 in stage 22.0 (TID 809) in 34 ms on localhost (executor driver) (183/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 184.0 in stage 22.0 (TID 810) in 27 ms on localhost (executor driver) (184/200)
26/06/26 13:26:37 INFO Executor: Running task 186.0 in stage 22.0 (TID 812)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 185.0 in stage 22.0 (TID 811). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 188.0 in stage 22.0 (TID 814, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 187.0 in stage 22.0 (TID 813)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 186.0 in stage 22.0 (TID 812). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 169.0 in stage 22.0 (TID 796). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 185.0 in stage 22.0 (TID 811) in 24 ms on localhost (executor driver) (185/200)
26/06/26 13:26:37 INFO Executor: Finished task 187.0 in stage 22.0 (TID 813). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 189.0 in stage 22.0 (TID 815, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 190.0 in stage 22.0 (TID 816, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 191.0 in stage 22.0 (TID 817, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 188.0 in stage 22.0 (TID 814)
26/06/26 13:26:37 INFO Executor: Running task 190.0 in stage 22.0 (TID 816)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 186.0 in stage 22.0 (TID 812) in 32 ms on localhost (executor driver) (186/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 169.0 in stage 22.0 (TID 796) in 166 ms on localhost (executor driver) (187/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 187.0 in stage 22.0 (TID 813) in 22 ms on localhost (executor driver) (188/200)
26/06/26 13:26:37 INFO Executor: Running task 191.0 in stage 22.0 (TID 817)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 188.0 in stage 22.0 (TID 814). 3292 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 192.0 in stage 22.0 (TID 818, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 189.0 in stage 22.0 (TID 815)
26/06/26 13:26:37 INFO Executor: Finished task 191.0 in stage 22.0 (TID 817). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 190.0 in stage 22.0 (TID 816). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 188.0 in stage 22.0 (TID 814) in 19 ms on localhost (executor driver) (189/200)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Starting task 193.0 in stage 22.0 (TID 819, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 194.0 in stage 22.0 (TID 820, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 193.0 in stage 22.0 (TID 819)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 190.0 in stage 22.0 (TID 816) in 16 ms on localhost (executor driver) (190/200)
26/06/26 13:26:37 INFO Executor: Running task 194.0 in stage 22.0 (TID 820)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 191.0 in stage 22.0 (TID 817) in 17 ms on localhost (executor driver) (191/200)
26/06/26 13:26:37 INFO Executor: Finished task 189.0 in stage 22.0 (TID 815). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:37 INFO TaskSetManager: Starting task 195.0 in stage 22.0 (TID 821, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 195.0 in stage 22.0 (TID 821)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 194.0 in stage 22.0 (TID 820). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 189.0 in stage 22.0 (TID 815) in 27 ms on localhost (executor driver) (192/200)
26/06/26 13:26:37 INFO Executor: Finished task 195.0 in stage 22.0 (TID 821). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 9 ms
26/06/26 13:26:37 INFO TaskSetManager: Starting task 196.0 in stage 22.0 (TID 822, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 197.0 in stage 22.0 (TID 823, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Running task 196.0 in stage 22.0 (TID 822)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Running task 192.0 in stage 22.0 (TID 818)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO TaskSetManager: Finished task 194.0 in stage 22.0 (TID 820) in 19 ms on localhost (executor driver) (193/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 195.0 in stage 22.0 (TID 821) in 16 ms on localhost (executor driver) (194/200)
26/06/26 13:26:37 INFO Executor: Running task 197.0 in stage 22.0 (TID 823)
26/06/26 13:26:37 INFO Executor: Finished task 196.0 in stage 22.0 (TID 822). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 192.0 in stage 22.0 (TID 818). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Finished task 193.0 in stage 22.0 (TID 819). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Starting task 198.0 in stage 22.0 (TID 824, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:37 INFO TaskSetManager: Starting task 199.0 in stage 22.0 (TID 825, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:37 INFO Executor: Finished task 197.0 in stage 22.0 (TID 823). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 196.0 in stage 22.0 (TID 822) in 23 ms on localhost (executor driver) (195/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 192.0 in stage 22.0 (TID 818) in 42 ms on localhost (executor driver) (196/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 193.0 in stage 22.0 (TID 819) in 35 ms on localhost (executor driver) (197/200)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 197.0 in stage 22.0 (TID 823) in 23 ms on localhost (executor driver) (198/200)
26/06/26 13:26:37 INFO Executor: Running task 198.0 in stage 22.0 (TID 824)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:37 INFO Executor: Finished task 198.0 in stage 22.0 (TID 824). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO Executor: Running task 199.0 in stage 22.0 (TID 825)
26/06/26 13:26:37 INFO TaskSetManager: Finished task 198.0 in stage 22.0 (TID 824) in 40 ms on localhost (executor driver) (199/200)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 199.0 in stage 22.0 (TID 825). 3249 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 199.0 in stage 22.0 (TID 825) in 65 ms on localhost (executor driver) (200/200)
26/06/26 13:26:37 INFO TaskSchedulerImpl: Removed TaskSet 22.0, whose tasks have all completed, from pool 
26/06/26 13:26:37 INFO DAGScheduler: ShuffleMapStage 22 (showString at NativeMethodAccessorImpl.java:0) finished in 3.439 s
26/06/26 13:26:37 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:37 INFO DAGScheduler: running: Set()
26/06/26 13:26:37 INFO DAGScheduler: waiting: Set(ResultStage 23)
26/06/26 13:26:37 INFO DAGScheduler: failed: Set()
26/06/26 13:26:37 INFO DAGScheduler: Submitting ResultStage 23 (MapPartitionsRDD[90] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:37 INFO MemoryStore: Block broadcast_26 stored as values in memory (estimated size 10.2 KB, free 364.8 MB)
26/06/26 13:26:37 INFO MemoryStore: Block broadcast_26_piece0 stored as bytes in memory (estimated size 4.6 KB, free 364.8 MB)
26/06/26 13:26:37 INFO BlockManagerInfo: Added broadcast_26_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 4.6 KB, free: 366.1 MB)
26/06/26 13:26:37 INFO SparkContext: Created broadcast 26 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:37 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 23 (MapPartitionsRDD[90] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:37 INFO TaskSchedulerImpl: Adding task set 23.0 with 1 tasks
26/06/26 13:26:37 INFO TaskSetManager: Starting task 0.0 in stage 23.0 (TID 826, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:37 INFO Executor: Running task 0.0 in stage 23.0 (TID 826)
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:37 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:37 INFO Executor: Finished task 0.0 in stage 23.0 (TID 826). 1630 bytes result sent to driver
26/06/26 13:26:37 INFO TaskSetManager: Finished task 0.0 in stage 23.0 (TID 826) in 79 ms on localhost (executor driver) (1/1)
26/06/26 13:26:37 INFO TaskSchedulerImpl: Removed TaskSet 23.0, whose tasks have all completed, from pool 
26/06/26 13:26:37 INFO DAGScheduler: ResultStage 23 (showString at NativeMethodAccessorImpl.java:0) finished in 0.097 s
26/06/26 13:26:37 INFO DAGScheduler: Job 12 finished: showString at NativeMethodAccessorImpl.java:0, took 4.434086 s
+-------+---+------+----------+--------+
|user_id|age|gender|occupation|zip_code|
+-------+---+------+----------+--------+
|      0|  0|     0|         0|       0|
+-------+---+------+----------+--------+

26/06/26 13:26:37 INFO BlockManagerInfo: Removed broadcast_26_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 4.6 KB, free: 366.1 MB)
26/06/26 13:26:38 INFO CodeGenerator: Code generated in 46.34409 ms
26/06/26 13:26:38 INFO CodeGenerator: Code generated in 47.482314 ms
26/06/26 13:26:38 INFO CodeGenerator: Code generated in 62.193517 ms
26/06/26 13:26:38 INFO CodeGenerator: Code generated in 135.621255 ms
26/06/26 13:26:38 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:38 INFO DAGScheduler: Registering RDD 93 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:38 INFO DAGScheduler: Registering RDD 96 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:38 INFO DAGScheduler: Got job 13 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:38 INFO DAGScheduler: Final stage: ResultStage 26 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:38 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 25)
26/06/26 13:26:38 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 25)
26/06/26 13:26:38 INFO DAGScheduler: Submitting ShuffleMapStage 24 (MapPartitionsRDD[93] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:38 INFO MemoryStore: Block broadcast_27 stored as values in memory (estimated size 39.1 KB, free 364.8 MB)
26/06/26 13:26:38 INFO MemoryStore: Block broadcast_27_piece0 stored as bytes in memory (estimated size 18.9 KB, free 364.7 MB)
26/06/26 13:26:38 INFO BlockManagerInfo: Added broadcast_27_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 18.9 KB, free: 366.1 MB)
26/06/26 13:26:38 INFO SparkContext: Created broadcast 27 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:38 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 24 (MapPartitionsRDD[93] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:38 INFO TaskSchedulerImpl: Adding task set 24.0 with 2 tasks
26/06/26 13:26:38 INFO TaskSetManager: Starting task 0.0 in stage 24.0 (TID 827, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:38 INFO TaskSetManager: Starting task 1.0 in stage 24.0 (TID 828, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:38 INFO Executor: Running task 0.0 in stage 24.0 (TID 827)
26/06/26 13:26:38 INFO Executor: Running task 1.0 in stage 24.0 (TID 828)
26/06/26 13:26:38 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:989586+989587
26/06/26 13:26:38 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.data:0+989586
26/06/26 13:26:38 INFO CodeGenerator: Code generated in 45.118884 ms
26/06/26 13:26:39 INFO CodeGenerator: Code generated in 201.729959 ms
26/06/26 13:26:39 INFO PythonRunner: Times: total = 1078, boot = -5627, init = 5733, finish = 972
26/06/26 13:26:39 INFO PythonRunner: Times: total = 884, boot = -5737, init = 5753, finish = 868
26/06/26 13:26:40 INFO Executor: Finished task 0.0 in stage 24.0 (TID 827). 2655 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Finished task 0.0 in stage 24.0 (TID 827) in 1693 ms on localhost (executor driver) (1/2)
26/06/26 13:26:40 INFO Executor: Finished task 1.0 in stage 24.0 (TID 828). 2655 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Finished task 1.0 in stage 24.0 (TID 828) in 1757 ms on localhost (executor driver) (2/2)
26/06/26 13:26:40 INFO TaskSchedulerImpl: Removed TaskSet 24.0, whose tasks have all completed, from pool 
26/06/26 13:26:40 INFO DAGScheduler: ShuffleMapStage 24 (showString at NativeMethodAccessorImpl.java:0) finished in 1.787 s
26/06/26 13:26:40 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:40 INFO DAGScheduler: running: Set()
26/06/26 13:26:40 INFO DAGScheduler: waiting: Set(ShuffleMapStage 25, ResultStage 26)
26/06/26 13:26:40 INFO DAGScheduler: failed: Set()
26/06/26 13:26:40 INFO DAGScheduler: Submitting ShuffleMapStage 25 (MapPartitionsRDD[96] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:40 INFO MemoryStore: Block broadcast_28 stored as values in memory (estimated size 42.1 KB, free 364.7 MB)
26/06/26 13:26:40 INFO MemoryStore: Block broadcast_28_piece0 stored as bytes in memory (estimated size 20.7 KB, free 364.7 MB)
26/06/26 13:26:40 INFO BlockManagerInfo: Added broadcast_28_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 20.7 KB, free: 366.0 MB)
26/06/26 13:26:40 INFO SparkContext: Created broadcast 28 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:40 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 25 (MapPartitionsRDD[96] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:40 INFO TaskSchedulerImpl: Adding task set 25.0 with 200 tasks
26/06/26 13:26:40 INFO TaskSetManager: Starting task 0.0 in stage 25.0 (TID 829, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 1.0 in stage 25.0 (TID 830, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 2.0 in stage 25.0 (TID 831, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 3.0 in stage 25.0 (TID 832, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 1.0 in stage 25.0 (TID 830)
26/06/26 13:26:40 INFO Executor: Running task 2.0 in stage 25.0 (TID 831)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 3.0 in stage 25.0 (TID 832)
26/06/26 13:26:40 INFO Executor: Finished task 2.0 in stage 25.0 (TID 831). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 0.0 in stage 25.0 (TID 829)
26/06/26 13:26:40 INFO Executor: Finished task 1.0 in stage 25.0 (TID 830). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 4.0 in stage 25.0 (TID 833, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 5.0 in stage 25.0 (TID 834, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 2.0 in stage 25.0 (TID 831) in 32 ms on localhost (executor driver) (1/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 1.0 in stage 25.0 (TID 830) in 32 ms on localhost (executor driver) (2/200)
26/06/26 13:26:40 INFO Executor: Running task 4.0 in stage 25.0 (TID 833)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 3.0 in stage 25.0 (TID 832). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 6.0 in stage 25.0 (TID 835, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 5.0 in stage 25.0 (TID 834)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 3.0 in stage 25.0 (TID 832) in 40 ms on localhost (executor driver) (3/200)
26/06/26 13:26:40 INFO Executor: Running task 6.0 in stage 25.0 (TID 835)
26/06/26 13:26:40 INFO Executor: Finished task 4.0 in stage 25.0 (TID 833). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 7.0 in stage 25.0 (TID 836, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 0.0 in stage 25.0 (TID 829). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Finished task 4.0 in stage 25.0 (TID 833) in 14 ms on localhost (executor driver) (4/200)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 8.0 in stage 25.0 (TID 837, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 0.0 in stage 25.0 (TID 829) in 46 ms on localhost (executor driver) (5/200)
26/06/26 13:26:40 INFO Executor: Running task 7.0 in stage 25.0 (TID 836)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 5.0 in stage 25.0 (TID 834). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 9.0 in stage 25.0 (TID 838, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 9.0 in stage 25.0 (TID 838)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO TaskSetManager: Finished task 5.0 in stage 25.0 (TID 834) in 24 ms on localhost (executor driver) (6/200)
26/06/26 13:26:40 INFO Executor: Running task 8.0 in stage 25.0 (TID 837)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 9.0 in stage 25.0 (TID 838). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 10.0 in stage 25.0 (TID 839, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 10.0 in stage 25.0 (TID 839)
26/06/26 13:26:40 INFO Executor: Finished task 8.0 in stage 25.0 (TID 837). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO TaskSetManager: Finished task 9.0 in stage 25.0 (TID 838) in 16 ms on localhost (executor driver) (7/200)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 11.0 in stage 25.0 (TID 840, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 8.0 in stage 25.0 (TID 837) in 26 ms on localhost (executor driver) (8/200)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 7.0 in stage 25.0 (TID 836). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Running task 11.0 in stage 25.0 (TID 840)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 12.0 in stage 25.0 (TID 841, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 10.0 in stage 25.0 (TID 839). 3672 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 13.0 in stage 25.0 (TID 842, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 13.0 in stage 25.0 (TID 842)
26/06/26 13:26:40 INFO Executor: Running task 12.0 in stage 25.0 (TID 841)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 6.0 in stage 25.0 (TID 835). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 14.0 in stage 25.0 (TID 843, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 13.0 in stage 25.0 (TID 842). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Finished task 12.0 in stage 25.0 (TID 841). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 15.0 in stage 25.0 (TID 844, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 16.0 in stage 25.0 (TID 845, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 16.0 in stage 25.0 (TID 845)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 10.0 in stage 25.0 (TID 839) in 31 ms on localhost (executor driver) (9/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 7.0 in stage 25.0 (TID 836) in 48 ms on localhost (executor driver) (10/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 13.0 in stage 25.0 (TID 842) in 13 ms on localhost (executor driver) (11/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 6.0 in stage 25.0 (TID 835) in 54 ms on localhost (executor driver) (12/200)
26/06/26 13:26:40 INFO Executor: Finished task 11.0 in stage 25.0 (TID 840). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Finished task 12.0 in stage 25.0 (TID 841) in 14 ms on localhost (executor driver) (13/200)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 14.0 in stage 25.0 (TID 843)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO TaskSetManager: Starting task 17.0 in stage 25.0 (TID 846, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 16.0 in stage 25.0 (TID 845). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 18.0 in stage 25.0 (TID 847, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 18.0 in stage 25.0 (TID 847)
26/06/26 13:26:40 INFO Executor: Finished task 14.0 in stage 25.0 (TID 843). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Finished task 11.0 in stage 25.0 (TID 840) in 37 ms on localhost (executor driver) (14/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 16.0 in stage 25.0 (TID 845) in 16 ms on localhost (executor driver) (15/200)
26/06/26 13:26:40 INFO Executor: Running task 17.0 in stage 25.0 (TID 846)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 15.0 in stage 25.0 (TID 844)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 19.0 in stage 25.0 (TID 848, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 19.0 in stage 25.0 (TID 848)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 14.0 in stage 25.0 (TID 843) in 27 ms on localhost (executor driver) (16/200)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 18.0 in stage 25.0 (TID 847). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 20.0 in stage 25.0 (TID 849, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 17.0 in stage 25.0 (TID 846). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 21.0 in stage 25.0 (TID 850, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 21.0 in stage 25.0 (TID 850)
26/06/26 13:26:40 INFO Executor: Finished task 19.0 in stage 25.0 (TID 848). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO TaskSetManager: Starting task 22.0 in stage 25.0 (TID 851, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 17.0 in stage 25.0 (TID 846) in 24 ms on localhost (executor driver) (17/200)
26/06/26 13:26:40 INFO Executor: Running task 20.0 in stage 25.0 (TID 849)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 19.0 in stage 25.0 (TID 848) in 11 ms on localhost (executor driver) (18/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 18.0 in stage 25.0 (TID 847) in 21 ms on localhost (executor driver) (19/200)
26/06/26 13:26:40 INFO Executor: Running task 22.0 in stage 25.0 (TID 851)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 15.0 in stage 25.0 (TID 844). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 23.0 in stage 25.0 (TID 852, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 15.0 in stage 25.0 (TID 844) in 44 ms on localhost (executor driver) (20/200)
26/06/26 13:26:40 INFO Executor: Running task 23.0 in stage 25.0 (TID 852)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 20.0 in stage 25.0 (TID 849). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 24.0 in stage 25.0 (TID 853, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 21.0 in stage 25.0 (TID 850). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 25.0 in stage 25.0 (TID 854, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 22.0 in stage 25.0 (TID 851). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Running task 24.0 in stage 25.0 (TID 853)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 20.0 in stage 25.0 (TID 849) in 31 ms on localhost (executor driver) (21/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 21.0 in stage 25.0 (TID 850) in 31 ms on localhost (executor driver) (22/200)
26/06/26 13:26:40 INFO Executor: Finished task 23.0 in stage 25.0 (TID 852). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 25.0 in stage 25.0 (TID 854)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO TaskSetManager: Starting task 26.0 in stage 25.0 (TID 855, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 27.0 in stage 25.0 (TID 856, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 22.0 in stage 25.0 (TID 851) in 35 ms on localhost (executor driver) (23/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 23.0 in stage 25.0 (TID 852) in 29 ms on localhost (executor driver) (24/200)
26/06/26 13:26:40 INFO Executor: Running task 27.0 in stage 25.0 (TID 856)
26/06/26 13:26:40 INFO Executor: Finished task 25.0 in stage 25.0 (TID 854). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Running task 26.0 in stage 25.0 (TID 855)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO Executor: Finished task 26.0 in stage 25.0 (TID 855). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 28.0 in stage 25.0 (TID 857, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 25.0 in stage 25.0 (TID 854) in 23 ms on localhost (executor driver) (25/200)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 29.0 in stage 25.0 (TID 858, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 26.0 in stage 25.0 (TID 855) in 18 ms on localhost (executor driver) (26/200)
26/06/26 13:26:40 INFO Executor: Running task 29.0 in stage 25.0 (TID 858)
26/06/26 13:26:40 INFO Executor: Finished task 27.0 in stage 25.0 (TID 856). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 24.0 in stage 25.0 (TID 853). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 30.0 in stage 25.0 (TID 859, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 31.0 in stage 25.0 (TID 860, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 30.0 in stage 25.0 (TID 859)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 27.0 in stage 25.0 (TID 856) in 40 ms on localhost (executor driver) (27/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 24.0 in stage 25.0 (TID 853) in 50 ms on localhost (executor driver) (28/200)
26/06/26 13:26:40 INFO Executor: Running task 28.0 in stage 25.0 (TID 857)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 31.0 in stage 25.0 (TID 860)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:40 INFO Executor: Finished task 29.0 in stage 25.0 (TID 858). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 32.0 in stage 25.0 (TID 861, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 29.0 in stage 25.0 (TID 858) in 30 ms on localhost (executor driver) (29/200)
26/06/26 13:26:40 INFO Executor: Running task 32.0 in stage 25.0 (TID 861)
26/06/26 13:26:40 INFO Executor: Finished task 28.0 in stage 25.0 (TID 857). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Finished task 31.0 in stage 25.0 (TID 860). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 30.0 in stage 25.0 (TID 859). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 33.0 in stage 25.0 (TID 862, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Running task 33.0 in stage 25.0 (TID 862)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 34.0 in stage 25.0 (TID 863, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 35.0 in stage 25.0 (TID 864, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 28.0 in stage 25.0 (TID 857) in 73 ms on localhost (executor driver) (30/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 31.0 in stage 25.0 (TID 860) in 46 ms on localhost (executor driver) (31/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 30.0 in stage 25.0 (TID 859) in 46 ms on localhost (executor driver) (32/200)
26/06/26 13:26:40 INFO Executor: Running task 35.0 in stage 25.0 (TID 864)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 33.0 in stage 25.0 (TID 862). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 36.0 in stage 25.0 (TID 865, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 33.0 in stage 25.0 (TID 862) in 17 ms on localhost (executor driver) (33/200)
26/06/26 13:26:40 INFO Executor: Running task 36.0 in stage 25.0 (TID 865)
26/06/26 13:26:40 INFO Executor: Running task 34.0 in stage 25.0 (TID 863)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Finished task 32.0 in stage 25.0 (TID 861). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 37.0 in stage 25.0 (TID 866, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:40 INFO Executor: Finished task 35.0 in stage 25.0 (TID 864). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Finished task 36.0 in stage 25.0 (TID 865). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Finished task 34.0 in stage 25.0 (TID 863). 3672 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Running task 37.0 in stage 25.0 (TID 866)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 32.0 in stage 25.0 (TID 861) in 89 ms on localhost (executor driver) (34/200)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 38.0 in stage 25.0 (TID 867, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 39.0 in stage 25.0 (TID 868, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 40.0 in stage 25.0 (TID 869, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO TaskSetManager: Finished task 35.0 in stage 25.0 (TID 864) in 59 ms on localhost (executor driver) (35/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 36.0 in stage 25.0 (TID 865) in 45 ms on localhost (executor driver) (36/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 34.0 in stage 25.0 (TID 863) in 61 ms on localhost (executor driver) (37/200)
26/06/26 13:26:40 INFO Executor: Running task 38.0 in stage 25.0 (TID 867)
26/06/26 13:26:40 INFO Executor: Running task 40.0 in stage 25.0 (TID 869)
26/06/26 13:26:40 INFO Executor: Finished task 37.0 in stage 25.0 (TID 866). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 39.0 in stage 25.0 (TID 868)
26/06/26 13:26:40 INFO ContextCleaner: Cleaned accumulator 763
26/06/26 13:26:40 INFO Executor: Finished task 38.0 in stage 25.0 (TID 867). 3672 bytes result sent to driver
26/06/26 13:26:40 INFO TaskSetManager: Starting task 41.0 in stage 25.0 (TID 870, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 42.0 in stage 25.0 (TID 871, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 37.0 in stage 25.0 (TID 866) in 69 ms on localhost (executor driver) (38/200)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 38.0 in stage 25.0 (TID 867) in 52 ms on localhost (executor driver) (39/200)
26/06/26 13:26:40 INFO Executor: Finished task 40.0 in stage 25.0 (TID 869). 3672 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Running task 42.0 in stage 25.0 (TID 871)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO TaskSetManager: Starting task 43.0 in stage 25.0 (TID 872, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:40 INFO BlockManagerInfo: Removed broadcast_27_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 18.9 KB, free: 366.1 MB)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 41.0 in stage 25.0 (TID 870)
26/06/26 13:26:40 INFO TaskSetManager: Finished task 40.0 in stage 25.0 (TID 869) in 66 ms on localhost (executor driver) (40/200)
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:40 INFO Executor: Running task 43.0 in stage 25.0 (TID 872)
26/06/26 13:26:40 INFO Executor: Finished task 42.0 in stage 25.0 (TID 871). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO Executor: Finished task 41.0 in stage 25.0 (TID 870). 3629 bytes result sent to driver
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:40 INFO TaskSetManager: Starting task 44.0 in stage 25.0 (TID 873, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:40 INFO TaskSetManager: Starting task 45.0 in stage 25.0 (TID 874, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 42.0 in stage 25.0 (TID 871) in 32 ms on localhost (executor driver) (41/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 41.0 in stage 25.0 (TID 870) in 73 ms on localhost (executor driver) (42/200)
26/06/26 13:26:41 INFO ContextCleaner: Cleaned accumulator 764
26/06/26 13:26:41 INFO Executor: Finished task 39.0 in stage 25.0 (TID 868). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 43.0 in stage 25.0 (TID 872). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 45.0 in stage 25.0 (TID 874)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 46.0 in stage 25.0 (TID 875, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 47.0 in stage 25.0 (TID 876, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 47.0 in stage 25.0 (TID 876)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 43.0 in stage 25.0 (TID 872) in 29 ms on localhost (executor driver) (43/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 39.0 in stage 25.0 (TID 868) in 88 ms on localhost (executor driver) (44/200)
26/06/26 13:26:41 INFO Executor: Running task 46.0 in stage 25.0 (TID 875)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Finished task 46.0 in stage 25.0 (TID 875). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 48.0 in stage 25.0 (TID 877, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 48.0 in stage 25.0 (TID 877)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 46.0 in stage 25.0 (TID 875) in 7 ms on localhost (executor driver) (45/200)
26/06/26 13:26:41 INFO Executor: Running task 44.0 in stage 25.0 (TID 873)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 45.0 in stage 25.0 (TID 874). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 47.0 in stage 25.0 (TID 876). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 49.0 in stage 25.0 (TID 878, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 50.0 in stage 25.0 (TID 879, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 47.0 in stage 25.0 (TID 876) in 14 ms on localhost (executor driver) (46/200)
26/06/26 13:26:41 INFO Executor: Running task 50.0 in stage 25.0 (TID 879)
26/06/26 13:26:41 INFO Executor: Finished task 44.0 in stage 25.0 (TID 873). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 49.0 in stage 25.0 (TID 878)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 51.0 in stage 25.0 (TID 880, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 44.0 in stage 25.0 (TID 873) in 27 ms on localhost (executor driver) (47/200)
26/06/26 13:26:41 INFO Executor: Running task 51.0 in stage 25.0 (TID 880)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 45.0 in stage 25.0 (TID 874) in 34 ms on localhost (executor driver) (48/200)
26/06/26 13:26:41 INFO Executor: Finished task 49.0 in stage 25.0 (TID 878). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 51.0 in stage 25.0 (TID 880). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 50.0 in stage 25.0 (TID 879). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 52.0 in stage 25.0 (TID 881, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 53.0 in stage 25.0 (TID 882, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 54.0 in stage 25.0 (TID 883, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 48.0 in stage 25.0 (TID 877). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 52.0 in stage 25.0 (TID 881)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 55.0 in stage 25.0 (TID 884, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 51.0 in stage 25.0 (TID 880) in 10 ms on localhost (executor driver) (49/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 50.0 in stage 25.0 (TID 879) in 12 ms on localhost (executor driver) (50/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 48.0 in stage 25.0 (TID 877) in 20 ms on localhost (executor driver) (51/200)
26/06/26 13:26:41 INFO Executor: Running task 53.0 in stage 25.0 (TID 882)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 49.0 in stage 25.0 (TID 878) in 13 ms on localhost (executor driver) (52/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 54.0 in stage 25.0 (TID 883)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 52.0 in stage 25.0 (TID 881). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 56.0 in stage 25.0 (TID 885, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 55.0 in stage 25.0 (TID 884)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 52.0 in stage 25.0 (TID 881) in 10 ms on localhost (executor driver) (53/200)
26/06/26 13:26:41 INFO Executor: Running task 56.0 in stage 25.0 (TID 885)
26/06/26 13:26:41 INFO Executor: Finished task 54.0 in stage 25.0 (TID 883). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 57.0 in stage 25.0 (TID 886, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 54.0 in stage 25.0 (TID 883) in 18 ms on localhost (executor driver) (54/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 57.0 in stage 25.0 (TID 886)
26/06/26 13:26:41 INFO Executor: Finished task 53.0 in stage 25.0 (TID 882). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 56.0 in stage 25.0 (TID 885). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 55.0 in stage 25.0 (TID 884). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 58.0 in stage 25.0 (TID 887, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 58.0 in stage 25.0 (TID 887)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 59.0 in stage 25.0 (TID 888, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 60.0 in stage 25.0 (TID 889, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 53.0 in stage 25.0 (TID 882) in 42 ms on localhost (executor driver) (55/200)
26/06/26 13:26:41 INFO Executor: Running task 60.0 in stage 25.0 (TID 889)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 56.0 in stage 25.0 (TID 885) in 34 ms on localhost (executor driver) (56/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 55.0 in stage 25.0 (TID 884) in 43 ms on localhost (executor driver) (57/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:41 INFO Executor: Finished task 57.0 in stage 25.0 (TID 886). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 59.0 in stage 25.0 (TID 888)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 61.0 in stage 25.0 (TID 890, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 57.0 in stage 25.0 (TID 886) in 40 ms on localhost (executor driver) (58/200)
26/06/26 13:26:41 INFO Executor: Running task 61.0 in stage 25.0 (TID 890)
26/06/26 13:26:41 INFO Executor: Finished task 58.0 in stage 25.0 (TID 887). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 62.0 in stage 25.0 (TID 891, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 62.0 in stage 25.0 (TID 891)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 58.0 in stage 25.0 (TID 887) in 27 ms on localhost (executor driver) (59/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 61.0 in stage 25.0 (TID 890). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 63.0 in stage 25.0 (TID 892, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 61.0 in stage 25.0 (TID 890) in 23 ms on localhost (executor driver) (60/200)
26/06/26 13:26:41 INFO Executor: Finished task 59.0 in stage 25.0 (TID 888). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 62.0 in stage 25.0 (TID 891). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 60.0 in stage 25.0 (TID 889). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 64.0 in stage 25.0 (TID 893, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 63.0 in stage 25.0 (TID 892)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 65.0 in stage 25.0 (TID 894, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 66.0 in stage 25.0 (TID 895, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 65.0 in stage 25.0 (TID 894)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 63.0 in stage 25.0 (TID 892). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 59.0 in stage 25.0 (TID 888) in 51 ms on localhost (executor driver) (61/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 62.0 in stage 25.0 (TID 891) in 25 ms on localhost (executor driver) (62/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 60.0 in stage 25.0 (TID 889) in 51 ms on localhost (executor driver) (63/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 67.0 in stage 25.0 (TID 896, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 65.0 in stage 25.0 (TID 894). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 63.0 in stage 25.0 (TID 892) in 15 ms on localhost (executor driver) (64/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 68.0 in stage 25.0 (TID 897, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 65.0 in stage 25.0 (TID 894) in 10 ms on localhost (executor driver) (65/200)
26/06/26 13:26:41 INFO Executor: Running task 66.0 in stage 25.0 (TID 895)
26/06/26 13:26:41 INFO Executor: Running task 64.0 in stage 25.0 (TID 893)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 68.0 in stage 25.0 (TID 897)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 66.0 in stage 25.0 (TID 895). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 69.0 in stage 25.0 (TID 898, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 66.0 in stage 25.0 (TID 895) in 19 ms on localhost (executor driver) (66/200)
26/06/26 13:26:41 INFO Executor: Running task 69.0 in stage 25.0 (TID 898)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 68.0 in stage 25.0 (TID 897). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 70.0 in stage 25.0 (TID 899, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 70.0 in stage 25.0 (TID 899)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 68.0 in stage 25.0 (TID 897) in 19 ms on localhost (executor driver) (67/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Running task 67.0 in stage 25.0 (TID 896)
26/06/26 13:26:41 INFO Executor: Finished task 64.0 in stage 25.0 (TID 893). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 71.0 in stage 25.0 (TID 900, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 64.0 in stage 25.0 (TID 893) in 42 ms on localhost (executor driver) (68/200)
26/06/26 13:26:41 INFO Executor: Finished task 67.0 in stage 25.0 (TID 896). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 72.0 in stage 25.0 (TID 901, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 67.0 in stage 25.0 (TID 896) in 34 ms on localhost (executor driver) (69/200)
26/06/26 13:26:41 INFO Executor: Finished task 69.0 in stage 25.0 (TID 898). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 71.0 in stage 25.0 (TID 900)
26/06/26 13:26:41 INFO Executor: Finished task 70.0 in stage 25.0 (TID 899). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 72.0 in stage 25.0 (TID 901)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 73.0 in stage 25.0 (TID 902, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 74.0 in stage 25.0 (TID 903, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 69.0 in stage 25.0 (TID 898) in 27 ms on localhost (executor driver) (70/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 70.0 in stage 25.0 (TID 899) in 18 ms on localhost (executor driver) (71/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 71.0 in stage 25.0 (TID 900). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 74.0 in stage 25.0 (TID 903)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 75.0 in stage 25.0 (TID 904, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 72.0 in stage 25.0 (TID 901). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 76.0 in stage 25.0 (TID 905, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 76.0 in stage 25.0 (TID 905)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 71.0 in stage 25.0 (TID 900) in 25 ms on localhost (executor driver) (72/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 72.0 in stage 25.0 (TID 901) in 24 ms on localhost (executor driver) (73/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 74.0 in stage 25.0 (TID 903). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 75.0 in stage 25.0 (TID 904)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 76.0 in stage 25.0 (TID 905). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 77.0 in stage 25.0 (TID 906, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 78.0 in stage 25.0 (TID 907, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 77.0 in stage 25.0 (TID 906)
26/06/26 13:26:41 INFO Executor: Finished task 75.0 in stage 25.0 (TID 904). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 74.0 in stage 25.0 (TID 903) in 32 ms on localhost (executor driver) (74/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 76.0 in stage 25.0 (TID 905) in 15 ms on localhost (executor driver) (75/200)
26/06/26 13:26:41 INFO Executor: Running task 73.0 in stage 25.0 (TID 902)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 79.0 in stage 25.0 (TID 908, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 77.0 in stage 25.0 (TID 906). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 80.0 in stage 25.0 (TID 909, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 80.0 in stage 25.0 (TID 909)
26/06/26 13:26:41 INFO Executor: Finished task 73.0 in stage 25.0 (TID 902). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 75.0 in stage 25.0 (TID 904) in 28 ms on localhost (executor driver) (76/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 77.0 in stage 25.0 (TID 906) in 13 ms on localhost (executor driver) (77/200)
26/06/26 13:26:41 INFO Executor: Running task 79.0 in stage 25.0 (TID 908)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Finished task 80.0 in stage 25.0 (TID 909). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 81.0 in stage 25.0 (TID 910, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 82.0 in stage 25.0 (TID 911, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 73.0 in stage 25.0 (TID 902) in 47 ms on localhost (executor driver) (78/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 80.0 in stage 25.0 (TID 909) in 9 ms on localhost (executor driver) (79/200)
26/06/26 13:26:41 INFO Executor: Running task 82.0 in stage 25.0 (TID 911)
26/06/26 13:26:41 INFO Executor: Running task 81.0 in stage 25.0 (TID 910)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 78.0 in stage 25.0 (TID 907)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 82.0 in stage 25.0 (TID 911). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 79.0 in stage 25.0 (TID 908). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:41 INFO Executor: Finished task 81.0 in stage 25.0 (TID 910). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 83.0 in stage 25.0 (TID 912, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 84.0 in stage 25.0 (TID 913, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 85.0 in stage 25.0 (TID 914, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 79.0 in stage 25.0 (TID 908) in 22 ms on localhost (executor driver) (80/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 81.0 in stage 25.0 (TID 910) in 12 ms on localhost (executor driver) (81/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 82.0 in stage 25.0 (TID 911) in 12 ms on localhost (executor driver) (82/200)
26/06/26 13:26:41 INFO Executor: Running task 84.0 in stage 25.0 (TID 913)
26/06/26 13:26:41 INFO Executor: Finished task 78.0 in stage 25.0 (TID 907). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 86.0 in stage 25.0 (TID 915, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 78.0 in stage 25.0 (TID 907) in 34 ms on localhost (executor driver) (83/200)
26/06/26 13:26:41 INFO Executor: Running task 86.0 in stage 25.0 (TID 915)
26/06/26 13:26:41 INFO Executor: Finished task 84.0 in stage 25.0 (TID 913). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 83.0 in stage 25.0 (TID 912)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 87.0 in stage 25.0 (TID 916, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 84.0 in stage 25.0 (TID 913) in 16 ms on localhost (executor driver) (84/200)
26/06/26 13:26:41 INFO Executor: Running task 85.0 in stage 25.0 (TID 914)
26/06/26 13:26:41 INFO Executor: Finished task 86.0 in stage 25.0 (TID 915). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 88.0 in stage 25.0 (TID 917, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 88.0 in stage 25.0 (TID 917)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 86.0 in stage 25.0 (TID 915) in 15 ms on localhost (executor driver) (85/200)
26/06/26 13:26:41 INFO Executor: Running task 87.0 in stage 25.0 (TID 916)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 85.0 in stage 25.0 (TID 914). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 89.0 in stage 25.0 (TID 918, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 89.0 in stage 25.0 (TID 918)
26/06/26 13:26:41 INFO Executor: Finished task 83.0 in stage 25.0 (TID 912). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 85.0 in stage 25.0 (TID 914) in 39 ms on localhost (executor driver) (86/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 90.0 in stage 25.0 (TID 919, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 90.0 in stage 25.0 (TID 919)
26/06/26 13:26:41 INFO Executor: Finished task 87.0 in stage 25.0 (TID 916). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 91.0 in stage 25.0 (TID 920, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 83.0 in stage 25.0 (TID 912) in 43 ms on localhost (executor driver) (87/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 87.0 in stage 25.0 (TID 916) in 30 ms on localhost (executor driver) (88/200)
26/06/26 13:26:41 INFO Executor: Finished task 88.0 in stage 25.0 (TID 917). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 91.0 in stage 25.0 (TID 920)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 92.0 in stage 25.0 (TID 921, localhost, executor driver, partition 92, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 88.0 in stage 25.0 (TID 917) in 39 ms on localhost (executor driver) (89/200)
26/06/26 13:26:41 INFO Executor: Running task 92.0 in stage 25.0 (TID 921)
26/06/26 13:26:41 INFO Executor: Finished task 89.0 in stage 25.0 (TID 918). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 93.0 in stage 25.0 (TID 922, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 89.0 in stage 25.0 (TID 918) in 27 ms on localhost (executor driver) (90/200)
26/06/26 13:26:41 INFO Executor: Running task 93.0 in stage 25.0 (TID 922)
26/06/26 13:26:41 INFO Executor: Finished task 92.0 in stage 25.0 (TID 921). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 91.0 in stage 25.0 (TID 920). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 90.0 in stage 25.0 (TID 919). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 94.0 in stage 25.0 (TID 923, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 95.0 in stage 25.0 (TID 924, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 96.0 in stage 25.0 (TID 925, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 95.0 in stage 25.0 (TID 924)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 91.0 in stage 25.0 (TID 920) in 28 ms on localhost (executor driver) (91/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 90.0 in stage 25.0 (TID 919) in 30 ms on localhost (executor driver) (92/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 92.0 in stage 25.0 (TID 921) in 22 ms on localhost (executor driver) (93/200)
26/06/26 13:26:41 INFO Executor: Finished task 93.0 in stage 25.0 (TID 922). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 95.0 in stage 25.0 (TID 924). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 96.0 in stage 25.0 (TID 925)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 97.0 in stage 25.0 (TID 926, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 98.0 in stage 25.0 (TID 927, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 93.0 in stage 25.0 (TID 922) in 20 ms on localhost (executor driver) (94/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 95.0 in stage 25.0 (TID 924) in 13 ms on localhost (executor driver) (95/200)
26/06/26 13:26:41 INFO Executor: Running task 98.0 in stage 25.0 (TID 927)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 94.0 in stage 25.0 (TID 923)
26/06/26 13:26:41 INFO Executor: Finished task 98.0 in stage 25.0 (TID 927). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 99.0 in stage 25.0 (TID 928, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 99.0 in stage 25.0 (TID 928)
26/06/26 13:26:41 INFO Executor: Finished task 96.0 in stage 25.0 (TID 925). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 98.0 in stage 25.0 (TID 927) in 24 ms on localhost (executor driver) (96/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 100.0 in stage 25.0 (TID 929, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 99.0 in stage 25.0 (TID 928). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 94.0 in stage 25.0 (TID 923). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 97.0 in stage 25.0 (TID 926)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 100.0 in stage 25.0 (TID 929)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 101.0 in stage 25.0 (TID 930, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 97.0 in stage 25.0 (TID 926). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 101.0 in stage 25.0 (TID 930)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 102.0 in stage 25.0 (TID 931, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 103.0 in stage 25.0 (TID 932, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 96.0 in stage 25.0 (TID 925) in 69 ms on localhost (executor driver) (97/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 94.0 in stage 25.0 (TID 923) in 70 ms on localhost (executor driver) (98/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 97.0 in stage 25.0 (TID 926) in 58 ms on localhost (executor driver) (99/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 99.0 in stage 25.0 (TID 928) in 41 ms on localhost (executor driver) (100/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 103.0 in stage 25.0 (TID 932)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 100.0 in stage 25.0 (TID 929). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 102.0 in stage 25.0 (TID 931)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 104.0 in stage 25.0 (TID 933, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 100.0 in stage 25.0 (TID 929) in 45 ms on localhost (executor driver) (101/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 103.0 in stage 25.0 (TID 932). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 105.0 in stage 25.0 (TID 934, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 105.0 in stage 25.0 (TID 934)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 103.0 in stage 25.0 (TID 932) in 20 ms on localhost (executor driver) (102/200)
26/06/26 13:26:41 INFO Executor: Finished task 102.0 in stage 25.0 (TID 931). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 105.0 in stage 25.0 (TID 934). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 106.0 in stage 25.0 (TID 935, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 107.0 in stage 25.0 (TID 936, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 106.0 in stage 25.0 (TID 935)
26/06/26 13:26:41 INFO Executor: Finished task 101.0 in stage 25.0 (TID 930). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 102.0 in stage 25.0 (TID 931) in 34 ms on localhost (executor driver) (103/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 105.0 in stage 25.0 (TID 934) in 14 ms on localhost (executor driver) (104/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 108.0 in stage 25.0 (TID 937, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 101.0 in stage 25.0 (TID 930) in 61 ms on localhost (executor driver) (105/200)
26/06/26 13:26:41 INFO Executor: Running task 104.0 in stage 25.0 (TID 933)
26/06/26 13:26:41 INFO Executor: Finished task 106.0 in stage 25.0 (TID 935). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 107.0 in stage 25.0 (TID 936)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 104.0 in stage 25.0 (TID 933). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 109.0 in stage 25.0 (TID 938, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 110.0 in stage 25.0 (TID 939, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 106.0 in stage 25.0 (TID 935) in 17 ms on localhost (executor driver) (106/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 104.0 in stage 25.0 (TID 933) in 30 ms on localhost (executor driver) (107/200)
26/06/26 13:26:41 INFO Executor: Running task 110.0 in stage 25.0 (TID 939)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 107.0 in stage 25.0 (TID 936). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 111.0 in stage 25.0 (TID 940, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 107.0 in stage 25.0 (TID 936) in 28 ms on localhost (executor driver) (108/200)
26/06/26 13:26:41 INFO Executor: Running task 111.0 in stage 25.0 (TID 940)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 110.0 in stage 25.0 (TID 939). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 112.0 in stage 25.0 (TID 941, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 110.0 in stage 25.0 (TID 939) in 20 ms on localhost (executor driver) (109/200)
26/06/26 13:26:41 INFO Executor: Running task 112.0 in stage 25.0 (TID 941)
26/06/26 13:26:41 INFO Executor: Running task 108.0 in stage 25.0 (TID 937)
26/06/26 13:26:41 INFO Executor: Running task 109.0 in stage 25.0 (TID 938)
26/06/26 13:26:41 INFO Executor: Finished task 111.0 in stage 25.0 (TID 940). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Finished task 108.0 in stage 25.0 (TID 937). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 113.0 in stage 25.0 (TID 942, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 114.0 in stage 25.0 (TID 943, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 114.0 in stage 25.0 (TID 943)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 111.0 in stage 25.0 (TID 940) in 20 ms on localhost (executor driver) (110/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 108.0 in stage 25.0 (TID 937) in 41 ms on localhost (executor driver) (111/200)
26/06/26 13:26:41 INFO Executor: Running task 113.0 in stage 25.0 (TID 942)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 112.0 in stage 25.0 (TID 941). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 114.0 in stage 25.0 (TID 943). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 113.0 in stage 25.0 (TID 942). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 109.0 in stage 25.0 (TID 938). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 115.0 in stage 25.0 (TID 944, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 116.0 in stage 25.0 (TID 945, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 117.0 in stage 25.0 (TID 946, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 118.0 in stage 25.0 (TID 947, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 109.0 in stage 25.0 (TID 938) in 50 ms on localhost (executor driver) (112/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 114.0 in stage 25.0 (TID 943) in 21 ms on localhost (executor driver) (113/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 113.0 in stage 25.0 (TID 942) in 22 ms on localhost (executor driver) (114/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 112.0 in stage 25.0 (TID 941) in 31 ms on localhost (executor driver) (115/200)
26/06/26 13:26:41 INFO Executor: Running task 117.0 in stage 25.0 (TID 946)
26/06/26 13:26:41 INFO Executor: Running task 115.0 in stage 25.0 (TID 944)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 118.0 in stage 25.0 (TID 947)
26/06/26 13:26:41 INFO Executor: Finished task 115.0 in stage 25.0 (TID 944). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 119.0 in stage 25.0 (TID 948, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 115.0 in stage 25.0 (TID 944) in 13 ms on localhost (executor driver) (116/200)
26/06/26 13:26:41 INFO Executor: Running task 116.0 in stage 25.0 (TID 945)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 119.0 in stage 25.0 (TID 948)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 117.0 in stage 25.0 (TID 946). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 120.0 in stage 25.0 (TID 949, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 120.0 in stage 25.0 (TID 949)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 117.0 in stage 25.0 (TID 946) in 21 ms on localhost (executor driver) (117/200)
26/06/26 13:26:41 INFO Executor: Finished task 116.0 in stage 25.0 (TID 945). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 121.0 in stage 25.0 (TID 950, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 116.0 in stage 25.0 (TID 945) in 24 ms on localhost (executor driver) (118/200)
26/06/26 13:26:41 INFO Executor: Finished task 118.0 in stage 25.0 (TID 947). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 121.0 in stage 25.0 (TID 950)
26/06/26 13:26:41 INFO Executor: Finished task 119.0 in stage 25.0 (TID 948). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 120.0 in stage 25.0 (TID 949). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 122.0 in stage 25.0 (TID 951, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 123.0 in stage 25.0 (TID 952, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 124.0 in stage 25.0 (TID 953, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 124.0 in stage 25.0 (TID 953)
26/06/26 13:26:41 INFO Executor: Running task 122.0 in stage 25.0 (TID 951)
26/06/26 13:26:41 INFO Executor: Finished task 121.0 in stage 25.0 (TID 950). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 125.0 in stage 25.0 (TID 954, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 118.0 in stage 25.0 (TID 947) in 33 ms on localhost (executor driver) (119/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 119.0 in stage 25.0 (TID 948) in 22 ms on localhost (executor driver) (120/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 120.0 in stage 25.0 (TID 949) in 14 ms on localhost (executor driver) (121/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 121.0 in stage 25.0 (TID 950) in 10 ms on localhost (executor driver) (122/200)
26/06/26 13:26:41 INFO Executor: Running task 125.0 in stage 25.0 (TID 954)
26/06/26 13:26:41 INFO Executor: Finished task 122.0 in stage 25.0 (TID 951). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 123.0 in stage 25.0 (TID 952)
26/06/26 13:26:41 INFO Executor: Finished task 124.0 in stage 25.0 (TID 953). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 126.0 in stage 25.0 (TID 955, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 127.0 in stage 25.0 (TID 956, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 123.0 in stage 25.0 (TID 952). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 126.0 in stage 25.0 (TID 955)
26/06/26 13:26:41 INFO Executor: Running task 127.0 in stage 25.0 (TID 956)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 122.0 in stage 25.0 (TID 951) in 19 ms on localhost (executor driver) (123/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 124.0 in stage 25.0 (TID 953) in 30 ms on localhost (executor driver) (124/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 128.0 in stage 25.0 (TID 957, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 128.0 in stage 25.0 (TID 957)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 123.0 in stage 25.0 (TID 952) in 33 ms on localhost (executor driver) (125/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 125.0 in stage 25.0 (TID 954). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 129.0 in stage 25.0 (TID 958, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 125.0 in stage 25.0 (TID 954) in 36 ms on localhost (executor driver) (126/200)
26/06/26 13:26:41 INFO Executor: Running task 129.0 in stage 25.0 (TID 958)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 128.0 in stage 25.0 (TID 957). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 130.0 in stage 25.0 (TID 959, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 130.0 in stage 25.0 (TID 959)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 128.0 in stage 25.0 (TID 957) in 26 ms on localhost (executor driver) (127/200)
26/06/26 13:26:41 INFO Executor: Finished task 127.0 in stage 25.0 (TID 956). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 131.0 in stage 25.0 (TID 960, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 131.0 in stage 25.0 (TID 960)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 127.0 in stage 25.0 (TID 956) in 46 ms on localhost (executor driver) (128/200)
26/06/26 13:26:41 INFO Executor: Finished task 126.0 in stage 25.0 (TID 955). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 129.0 in stage 25.0 (TID 958). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 131.0 in stage 25.0 (TID 960). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 5 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 132.0 in stage 25.0 (TID 961, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 133.0 in stage 25.0 (TID 962, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 134.0 in stage 25.0 (TID 963, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 126.0 in stage 25.0 (TID 955) in 59 ms on localhost (executor driver) (129/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 131.0 in stage 25.0 (TID 960) in 15 ms on localhost (executor driver) (130/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 129.0 in stage 25.0 (TID 958) in 41 ms on localhost (executor driver) (131/200)
26/06/26 13:26:41 INFO Executor: Running task 134.0 in stage 25.0 (TID 963)
26/06/26 13:26:41 INFO Executor: Finished task 130.0 in stage 25.0 (TID 959). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 133.0 in stage 25.0 (TID 962)
26/06/26 13:26:41 INFO Executor: Running task 132.0 in stage 25.0 (TID 961)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 135.0 in stage 25.0 (TID 964, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 130.0 in stage 25.0 (TID 959) in 28 ms on localhost (executor driver) (132/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 134.0 in stage 25.0 (TID 963). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 135.0 in stage 25.0 (TID 964)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 132.0 in stage 25.0 (TID 961). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 136.0 in stage 25.0 (TID 965, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 137.0 in stage 25.0 (TID 966, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 135.0 in stage 25.0 (TID 964). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 136.0 in stage 25.0 (TID 965)
26/06/26 13:26:41 INFO Executor: Finished task 133.0 in stage 25.0 (TID 962). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 138.0 in stage 25.0 (TID 967, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 139.0 in stage 25.0 (TID 968, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 134.0 in stage 25.0 (TID 963) in 40 ms on localhost (executor driver) (133/200)
26/06/26 13:26:41 INFO Executor: Finished task 136.0 in stage 25.0 (TID 965). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 140.0 in stage 25.0 (TID 969, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 140.0 in stage 25.0 (TID 969)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 135.0 in stage 25.0 (TID 964) in 37 ms on localhost (executor driver) (134/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 133.0 in stage 25.0 (TID 962) in 45 ms on localhost (executor driver) (135/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 136.0 in stage 25.0 (TID 965) in 21 ms on localhost (executor driver) (136/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 132.0 in stage 25.0 (TID 961) in 47 ms on localhost (executor driver) (137/200)
26/06/26 13:26:41 INFO Executor: Running task 137.0 in stage 25.0 (TID 966)
26/06/26 13:26:41 INFO Executor: Finished task 140.0 in stage 25.0 (TID 969). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 138.0 in stage 25.0 (TID 967)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 141.0 in stage 25.0 (TID 970, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 140.0 in stage 25.0 (TID 969) in 12 ms on localhost (executor driver) (138/200)
26/06/26 13:26:41 INFO Executor: Running task 141.0 in stage 25.0 (TID 970)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 137.0 in stage 25.0 (TID 966). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 139.0 in stage 25.0 (TID 968)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 142.0 in stage 25.0 (TID 971, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 142.0 in stage 25.0 (TID 971)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 137.0 in stage 25.0 (TID 966) in 45 ms on localhost (executor driver) (139/200)
26/06/26 13:26:41 INFO Executor: Finished task 138.0 in stage 25.0 (TID 967). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 143.0 in stage 25.0 (TID 972, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 143.0 in stage 25.0 (TID 972)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 138.0 in stage 25.0 (TID 967) in 39 ms on localhost (executor driver) (140/200)
26/06/26 13:26:41 INFO Executor: Finished task 141.0 in stage 25.0 (TID 970). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 142.0 in stage 25.0 (TID 971). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 144.0 in stage 25.0 (TID 973, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 145.0 in stage 25.0 (TID 974, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 144.0 in stage 25.0 (TID 973)
26/06/26 13:26:41 INFO Executor: Finished task 139.0 in stage 25.0 (TID 968). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 141.0 in stage 25.0 (TID 970) in 34 ms on localhost (executor driver) (141/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 146.0 in stage 25.0 (TID 975, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 139.0 in stage 25.0 (TID 968) in 48 ms on localhost (executor driver) (142/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 142.0 in stage 25.0 (TID 971) in 21 ms on localhost (executor driver) (143/200)
26/06/26 13:26:41 INFO Executor: Running task 146.0 in stage 25.0 (TID 975)
26/06/26 13:26:41 INFO Executor: Running task 145.0 in stage 25.0 (TID 974)
26/06/26 13:26:41 INFO Executor: Finished task 143.0 in stage 25.0 (TID 972). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 147.0 in stage 25.0 (TID 976, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 146.0 in stage 25.0 (TID 975). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 145.0 in stage 25.0 (TID 974). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 148.0 in stage 25.0 (TID 977, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 149.0 in stage 25.0 (TID 978, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 148.0 in stage 25.0 (TID 977)
26/06/26 13:26:41 INFO Executor: Finished task 144.0 in stage 25.0 (TID 973). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 143.0 in stage 25.0 (TID 972) in 28 ms on localhost (executor driver) (144/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 146.0 in stage 25.0 (TID 975) in 14 ms on localhost (executor driver) (145/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 145.0 in stage 25.0 (TID 974) in 15 ms on localhost (executor driver) (146/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 150.0 in stage 25.0 (TID 979, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 144.0 in stage 25.0 (TID 973) in 20 ms on localhost (executor driver) (147/200)
26/06/26 13:26:41 INFO Executor: Running task 147.0 in stage 25.0 (TID 976)
26/06/26 13:26:41 INFO Executor: Running task 150.0 in stage 25.0 (TID 979)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO Executor: Running task 149.0 in stage 25.0 (TID 978)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 149.0 in stage 25.0 (TID 978). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 151.0 in stage 25.0 (TID 980, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 149.0 in stage 25.0 (TID 978) in 22 ms on localhost (executor driver) (148/200)
26/06/26 13:26:41 INFO Executor: Finished task 148.0 in stage 25.0 (TID 977). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 152.0 in stage 25.0 (TID 981, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 152.0 in stage 25.0 (TID 981)
26/06/26 13:26:41 INFO Executor: Finished task 150.0 in stage 25.0 (TID 979). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 153.0 in stage 25.0 (TID 982, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 153.0 in stage 25.0 (TID 982)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 148.0 in stage 25.0 (TID 977) in 31 ms on localhost (executor driver) (149/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 150.0 in stage 25.0 (TID 979) in 27 ms on localhost (executor driver) (150/200)
26/06/26 13:26:41 INFO Executor: Finished task 153.0 in stage 25.0 (TID 982). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 154.0 in stage 25.0 (TID 983, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 153.0 in stage 25.0 (TID 982) in 9 ms on localhost (executor driver) (151/200)
26/06/26 13:26:41 INFO Executor: Running task 154.0 in stage 25.0 (TID 983)
26/06/26 13:26:41 INFO Executor: Running task 151.0 in stage 25.0 (TID 980)
26/06/26 13:26:41 INFO Executor: Finished task 147.0 in stage 25.0 (TID 976). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 155.0 in stage 25.0 (TID 984, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 155.0 in stage 25.0 (TID 984)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 147.0 in stage 25.0 (TID 976) in 44 ms on localhost (executor driver) (152/200)
26/06/26 13:26:41 INFO Executor: Finished task 152.0 in stage 25.0 (TID 981). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 156.0 in stage 25.0 (TID 985, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 152.0 in stage 25.0 (TID 981) in 21 ms on localhost (executor driver) (153/200)
26/06/26 13:26:41 INFO Executor: Finished task 154.0 in stage 25.0 (TID 983). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 155.0 in stage 25.0 (TID 984). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 156.0 in stage 25.0 (TID 985)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 157.0 in stage 25.0 (TID 986, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 158.0 in stage 25.0 (TID 987, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 157.0 in stage 25.0 (TID 986)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 154.0 in stage 25.0 (TID 983) in 23 ms on localhost (executor driver) (154/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 155.0 in stage 25.0 (TID 984) in 19 ms on localhost (executor driver) (155/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 151.0 in stage 25.0 (TID 980). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 156.0 in stage 25.0 (TID 985). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 158.0 in stage 25.0 (TID 987)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 159.0 in stage 25.0 (TID 988, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 160.0 in stage 25.0 (TID 989, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 151.0 in stage 25.0 (TID 980) in 50 ms on localhost (executor driver) (156/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 156.0 in stage 25.0 (TID 985) in 28 ms on localhost (executor driver) (157/200)
26/06/26 13:26:41 INFO Executor: Finished task 157.0 in stage 25.0 (TID 986). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 160.0 in stage 25.0 (TID 989)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 161.0 in stage 25.0 (TID 990, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 157.0 in stage 25.0 (TID 986) in 26 ms on localhost (executor driver) (158/200)
26/06/26 13:26:41 INFO Executor: Finished task 158.0 in stage 25.0 (TID 987). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 160.0 in stage 25.0 (TID 989). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 162.0 in stage 25.0 (TID 991, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 159.0 in stage 25.0 (TID 988)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 163.0 in stage 25.0 (TID 992, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 158.0 in stage 25.0 (TID 987) in 32 ms on localhost (executor driver) (159/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO Executor: Running task 163.0 in stage 25.0 (TID 992)
26/06/26 13:26:41 INFO Executor: Running task 161.0 in stage 25.0 (TID 990)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 160.0 in stage 25.0 (TID 989) in 18 ms on localhost (executor driver) (160/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 161.0 in stage 25.0 (TID 990). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 159.0 in stage 25.0 (TID 988). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 164.0 in stage 25.0 (TID 993, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 165.0 in stage 25.0 (TID 994, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 161.0 in stage 25.0 (TID 990) in 22 ms on localhost (executor driver) (161/200)
26/06/26 13:26:41 INFO Executor: Running task 165.0 in stage 25.0 (TID 994)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 159.0 in stage 25.0 (TID 988) in 31 ms on localhost (executor driver) (162/200)
26/06/26 13:26:41 INFO Executor: Running task 162.0 in stage 25.0 (TID 991)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 165.0 in stage 25.0 (TID 994). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 166.0 in stage 25.0 (TID 995, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 162.0 in stage 25.0 (TID 991). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 164.0 in stage 25.0 (TID 993)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 167.0 in stage 25.0 (TID 996, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 162.0 in stage 25.0 (TID 991) in 32 ms on localhost (executor driver) (163/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 167.0 in stage 25.0 (TID 996)
26/06/26 13:26:41 INFO Executor: Finished task 163.0 in stage 25.0 (TID 992). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 164.0 in stage 25.0 (TID 993). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 168.0 in stage 25.0 (TID 997, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 169.0 in stage 25.0 (TID 998, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 165.0 in stage 25.0 (TID 994) in 22 ms on localhost (executor driver) (164/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 163.0 in stage 25.0 (TID 992) in 37 ms on localhost (executor driver) (165/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 164.0 in stage 25.0 (TID 993) in 24 ms on localhost (executor driver) (166/200)
26/06/26 13:26:41 INFO Executor: Running task 168.0 in stage 25.0 (TID 997)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:41 INFO Executor: Running task 169.0 in stage 25.0 (TID 998)
26/06/26 13:26:41 INFO Executor: Running task 166.0 in stage 25.0 (TID 995)
26/06/26 13:26:41 INFO Executor: Finished task 168.0 in stage 25.0 (TID 997). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 170.0 in stage 25.0 (TID 999, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 168.0 in stage 25.0 (TID 997) in 10 ms on localhost (executor driver) (167/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 170.0 in stage 25.0 (TID 999)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO Executor: Finished task 167.0 in stage 25.0 (TID 996). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 170.0 in stage 25.0 (TID 999). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 171.0 in stage 25.0 (TID 1000, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 172.0 in stage 25.0 (TID 1001, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 167.0 in stage 25.0 (TID 996) in 27 ms on localhost (executor driver) (168/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 170.0 in stage 25.0 (TID 999) in 12 ms on localhost (executor driver) (169/200)
26/06/26 13:26:41 INFO Executor: Running task 171.0 in stage 25.0 (TID 1000)
26/06/26 13:26:41 INFO Executor: Finished task 166.0 in stage 25.0 (TID 995). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 172.0 in stage 25.0 (TID 1001)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 171.0 in stage 25.0 (TID 1000). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 173.0 in stage 25.0 (TID 1002, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 174.0 in stage 25.0 (TID 1003, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 166.0 in stage 25.0 (TID 995) in 37 ms on localhost (executor driver) (170/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 171.0 in stage 25.0 (TID 1000) in 9 ms on localhost (executor driver) (171/200)
26/06/26 13:26:41 INFO Executor: Running task 173.0 in stage 25.0 (TID 1002)
26/06/26 13:26:41 INFO Executor: Running task 174.0 in stage 25.0 (TID 1003)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Finished task 172.0 in stage 25.0 (TID 1001). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 175.0 in stage 25.0 (TID 1004, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 172.0 in stage 25.0 (TID 1001) in 20 ms on localhost (executor driver) (172/200)
26/06/26 13:26:41 INFO Executor: Finished task 173.0 in stage 25.0 (TID 1002). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 176.0 in stage 25.0 (TID 1005, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 169.0 in stage 25.0 (TID 998). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 174.0 in stage 25.0 (TID 1003). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 173.0 in stage 25.0 (TID 1002) in 13 ms on localhost (executor driver) (173/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 177.0 in stage 25.0 (TID 1006, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 178.0 in stage 25.0 (TID 1007, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 177.0 in stage 25.0 (TID 1006)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 169.0 in stage 25.0 (TID 998) in 40 ms on localhost (executor driver) (174/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 174.0 in stage 25.0 (TID 1003) in 13 ms on localhost (executor driver) (175/200)
26/06/26 13:26:41 INFO Executor: Running task 176.0 in stage 25.0 (TID 1005)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 175.0 in stage 25.0 (TID 1004)
26/06/26 13:26:41 INFO Executor: Running task 178.0 in stage 25.0 (TID 1007)
26/06/26 13:26:41 INFO Executor: Finished task 176.0 in stage 25.0 (TID 1005). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 179.0 in stage 25.0 (TID 1008, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 179.0 in stage 25.0 (TID 1008)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 176.0 in stage 25.0 (TID 1005) in 9 ms on localhost (executor driver) (176/200)
26/06/26 13:26:41 INFO Executor: Finished task 177.0 in stage 25.0 (TID 1006). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 5 ms
26/06/26 13:26:41 INFO Executor: Finished task 178.0 in stage 25.0 (TID 1007). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 180.0 in stage 25.0 (TID 1009, localhost, executor driver, partition 180, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 181.0 in stage 25.0 (TID 1010, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 181.0 in stage 25.0 (TID 1010)
26/06/26 13:26:41 INFO Executor: Finished task 179.0 in stage 25.0 (TID 1008). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Finished task 177.0 in stage 25.0 (TID 1006) in 14 ms on localhost (executor driver) (177/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 178.0 in stage 25.0 (TID 1007) in 14 ms on localhost (executor driver) (178/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 182.0 in stage 25.0 (TID 1011, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 179.0 in stage 25.0 (TID 1008) in 9 ms on localhost (executor driver) (179/200)
26/06/26 13:26:41 INFO Executor: Finished task 175.0 in stage 25.0 (TID 1004). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 183.0 in stage 25.0 (TID 1012, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 175.0 in stage 25.0 (TID 1004) in 18 ms on localhost (executor driver) (180/200)
26/06/26 13:26:41 INFO Executor: Running task 182.0 in stage 25.0 (TID 1011)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 183.0 in stage 25.0 (TID 1012)
26/06/26 13:26:41 INFO Executor: Finished task 181.0 in stage 25.0 (TID 1010). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Finished task 182.0 in stage 25.0 (TID 1011). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 184.0 in stage 25.0 (TID 1013, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 185.0 in stage 25.0 (TID 1014, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 180.0 in stage 25.0 (TID 1009)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 181.0 in stage 25.0 (TID 1010) in 12 ms on localhost (executor driver) (181/200)
26/06/26 13:26:41 INFO Executor: Finished task 183.0 in stage 25.0 (TID 1012). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 186.0 in stage 25.0 (TID 1015, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 183.0 in stage 25.0 (TID 1012) in 11 ms on localhost (executor driver) (182/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 182.0 in stage 25.0 (TID 1011) in 12 ms on localhost (executor driver) (183/200)
26/06/26 13:26:41 INFO Executor: Running task 184.0 in stage 25.0 (TID 1013)
26/06/26 13:26:41 INFO Executor: Running task 185.0 in stage 25.0 (TID 1014)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO Executor: Running task 186.0 in stage 25.0 (TID 1015)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 184.0 in stage 25.0 (TID 1013). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Starting task 187.0 in stage 25.0 (TID 1016, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 184.0 in stage 25.0 (TID 1013) in 14 ms on localhost (executor driver) (184/200)
26/06/26 13:26:41 INFO Executor: Running task 187.0 in stage 25.0 (TID 1016)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 180.0 in stage 25.0 (TID 1009). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 188.0 in stage 25.0 (TID 1017, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 188.0 in stage 25.0 (TID 1017)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 180.0 in stage 25.0 (TID 1009) in 63 ms on localhost (executor driver) (185/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 186.0 in stage 25.0 (TID 1015). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 188.0 in stage 25.0 (TID 1017). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 187.0 in stage 25.0 (TID 1016). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 185.0 in stage 25.0 (TID 1014). 3672 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 189.0 in stage 25.0 (TID 1018, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 190.0 in stage 25.0 (TID 1019, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 191.0 in stage 25.0 (TID 1020, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 192.0 in stage 25.0 (TID 1021, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 186.0 in stage 25.0 (TID 1015) in 66 ms on localhost (executor driver) (186/200)
26/06/26 13:26:41 INFO Executor: Running task 191.0 in stage 25.0 (TID 1020)
26/06/26 13:26:41 INFO Executor: Running task 190.0 in stage 25.0 (TID 1019)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 188.0 in stage 25.0 (TID 1017) in 18 ms on localhost (executor driver) (187/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 187.0 in stage 25.0 (TID 1016) in 55 ms on localhost (executor driver) (188/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 185.0 in stage 25.0 (TID 1014) in 67 ms on localhost (executor driver) (189/200)
26/06/26 13:26:41 INFO Executor: Running task 189.0 in stage 25.0 (TID 1018)
26/06/26 13:26:41 INFO Executor: Running task 192.0 in stage 25.0 (TID 1021)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:41 INFO Executor: Finished task 189.0 in stage 25.0 (TID 1018). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 193.0 in stage 25.0 (TID 1022, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 193.0 in stage 25.0 (TID 1022)
26/06/26 13:26:41 INFO Executor: Finished task 190.0 in stage 25.0 (TID 1019). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 191.0 in stage 25.0 (TID 1020). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Finished task 192.0 in stage 25.0 (TID 1021). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO TaskSetManager: Finished task 189.0 in stage 25.0 (TID 1018) in 26 ms on localhost (executor driver) (190/200)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 194.0 in stage 25.0 (TID 1023, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 195.0 in stage 25.0 (TID 1024, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 195.0 in stage 25.0 (TID 1024)
26/06/26 13:26:41 INFO TaskSetManager: Starting task 196.0 in stage 25.0 (TID 1025, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 194.0 in stage 25.0 (TID 1023)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 190.0 in stage 25.0 (TID 1019) in 41 ms on localhost (executor driver) (191/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 191.0 in stage 25.0 (TID 1020) in 42 ms on localhost (executor driver) (192/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 192.0 in stage 25.0 (TID 1021) in 42 ms on localhost (executor driver) (193/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 196.0 in stage 25.0 (TID 1025)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Finished task 194.0 in stage 25.0 (TID 1023). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 197.0 in stage 25.0 (TID 1026, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Finished task 195.0 in stage 25.0 (TID 1024). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 198.0 in stage 25.0 (TID 1027, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 195.0 in stage 25.0 (TID 1024) in 39 ms on localhost (executor driver) (194/200)
26/06/26 13:26:41 INFO Executor: Finished task 196.0 in stage 25.0 (TID 1025). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO TaskSetManager: Starting task 199.0 in stage 25.0 (TID 1028, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:41 INFO Executor: Running task 199.0 in stage 25.0 (TID 1028)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 196.0 in stage 25.0 (TID 1025) in 42 ms on localhost (executor driver) (195/200)
26/06/26 13:26:41 INFO TaskSetManager: Finished task 194.0 in stage 25.0 (TID 1023) in 45 ms on localhost (executor driver) (196/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:41 INFO Executor: Running task 198.0 in stage 25.0 (TID 1027)
26/06/26 13:26:41 INFO Executor: Finished task 199.0 in stage 25.0 (TID 1028). 3672 bytes result sent to driver
26/06/26 13:26:42 INFO Executor: Finished task 193.0 in stage 25.0 (TID 1022). 3629 bytes result sent to driver
26/06/26 13:26:41 INFO Executor: Running task 197.0 in stage 25.0 (TID 1026)
26/06/26 13:26:42 INFO TaskSetManager: Finished task 199.0 in stage 25.0 (TID 1028) in 28 ms on localhost (executor driver) (197/200)
26/06/26 13:26:42 INFO TaskSetManager: Finished task 193.0 in stage 25.0 (TID 1022) in 91 ms on localhost (executor driver) (198/200)
26/06/26 13:26:41 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:42 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 18 ms
26/06/26 13:26:42 INFO Executor: Finished task 198.0 in stage 25.0 (TID 1027). 3629 bytes result sent to driver
26/06/26 13:26:42 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:42 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:42 INFO TaskSetManager: Finished task 198.0 in stage 25.0 (TID 1027) in 53 ms on localhost (executor driver) (199/200)
26/06/26 13:26:42 INFO Executor: Finished task 197.0 in stage 25.0 (TID 1026). 3629 bytes result sent to driver
26/06/26 13:26:42 INFO TaskSetManager: Finished task 197.0 in stage 25.0 (TID 1026) in 69 ms on localhost (executor driver) (200/200)
26/06/26 13:26:42 INFO TaskSchedulerImpl: Removed TaskSet 25.0, whose tasks have all completed, from pool 
26/06/26 13:26:42 INFO DAGScheduler: ShuffleMapStage 25 (showString at NativeMethodAccessorImpl.java:0) finished in 1.462 s
26/06/26 13:26:42 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:42 INFO DAGScheduler: running: Set()
26/06/26 13:26:42 INFO DAGScheduler: waiting: Set(ResultStage 26)
26/06/26 13:26:42 INFO DAGScheduler: failed: Set()
26/06/26 13:26:42 INFO DAGScheduler: Submitting ResultStage 26 (MapPartitionsRDD[100] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:42 INFO MemoryStore: Block broadcast_29 stored as values in memory (estimated size 9.1 KB, free 364.7 MB)
26/06/26 13:26:42 INFO MemoryStore: Block broadcast_29_piece0 stored as bytes in memory (estimated size 4.3 KB, free 364.7 MB)
26/06/26 13:26:42 INFO BlockManagerInfo: Added broadcast_29_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 4.3 KB, free: 366.1 MB)
26/06/26 13:26:42 INFO SparkContext: Created broadcast 29 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:42 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 26 (MapPartitionsRDD[100] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:42 INFO TaskSchedulerImpl: Adding task set 26.0 with 1 tasks
26/06/26 13:26:42 INFO TaskSetManager: Starting task 0.0 in stage 26.0 (TID 1029, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:42 INFO Executor: Running task 0.0 in stage 26.0 (TID 1029)
26/06/26 13:26:42 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:42 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:42 INFO Executor: Finished task 0.0 in stage 26.0 (TID 1029). 1625 bytes result sent to driver
26/06/26 13:26:42 INFO TaskSetManager: Finished task 0.0 in stage 26.0 (TID 1029) in 88 ms on localhost (executor driver) (1/1)
26/06/26 13:26:42 INFO TaskSchedulerImpl: Removed TaskSet 26.0, whose tasks have all completed, from pool 
26/06/26 13:26:42 INFO DAGScheduler: ResultStage 26 (showString at NativeMethodAccessorImpl.java:0) finished in 0.104 s
26/06/26 13:26:42 INFO DAGScheduler: Job 13 finished: showString at NativeMethodAccessorImpl.java:0, took 3.390259 s
+-------+--------+------+---------+
|user_id|movie_id|rating|timestamp|
+-------+--------+------+---------+
|      0|       0|     0|        0|
+-------+--------+------+---------+

26/06/26 13:26:43 WARN Utils: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by setting 'spark.debug.maxToStringFields' in SparkEnv.conf.
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 20.00857 ms
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 30.447753 ms
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 27.183428 ms
26/06/26 13:26:43 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
26/06/26 13:26:43 INFO DAGScheduler: Registering RDD 104 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:43 INFO DAGScheduler: Registering RDD 109 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:43 INFO DAGScheduler: Got job 14 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
26/06/26 13:26:43 INFO DAGScheduler: Final stage: ResultStage 29 (showString at NativeMethodAccessorImpl.java:0)
26/06/26 13:26:43 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 28)
26/06/26 13:26:43 INFO DAGScheduler: Missing parents: List(ShuffleMapStage 28)
26/06/26 13:26:43 INFO DAGScheduler: Submitting ShuffleMapStage 27 (MapPartitionsRDD[104] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:43 INFO MemoryStore: Block broadcast_30 stored as values in memory (estimated size 43.1 KB, free 364.7 MB)
26/06/26 13:26:43 INFO MemoryStore: Block broadcast_30_piece0 stored as bytes in memory (estimated size 20.5 KB, free 364.7 MB)
26/06/26 13:26:43 INFO BlockManagerInfo: Added broadcast_30_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 20.5 KB, free: 366.0 MB)
26/06/26 13:26:43 INFO SparkContext: Created broadcast 30 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:43 INFO DAGScheduler: Submitting 2 missing tasks from ShuffleMapStage 27 (MapPartitionsRDD[104] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1))
26/06/26 13:26:43 INFO TaskSchedulerImpl: Adding task set 27.0 with 2 tasks
26/06/26 13:26:43 INFO TaskSetManager: Starting task 0.0 in stage 27.0 (TID 1030, localhost, executor driver, partition 0, ANY, 7911 bytes)
26/06/26 13:26:43 INFO TaskSetManager: Starting task 1.0 in stage 27.0 (TID 1031, localhost, executor driver, partition 1, ANY, 7911 bytes)
26/06/26 13:26:43 INFO Executor: Running task 1.0 in stage 27.0 (TID 1031)
26/06/26 13:26:43 INFO Executor: Running task 0.0 in stage 27.0 (TID 1030)
26/06/26 13:26:43 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:0+118172
26/06/26 13:26:43 INFO HadoopRDD: Input split: hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/movielens100k/u.item:118172+118172
26/06/26 13:26:43 INFO PythonRunner: Times: total = 84, boot = -3344, init = 3356, finish = 72
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 15.658785 ms
26/06/26 13:26:43 INFO PythonRunner: Times: total = 109, boot = -3432, init = 3501, finish = 40
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 37.712955 ms
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 19.468902 ms
26/06/26 13:26:43 INFO Executor: Finished task 1.0 in stage 27.0 (TID 1031). 2598 bytes result sent to driver
26/06/26 13:26:43 INFO TaskSetManager: Finished task 1.0 in stage 27.0 (TID 1031) in 548 ms on localhost (executor driver) (1/2)
26/06/26 13:26:43 INFO Executor: Finished task 0.0 in stage 27.0 (TID 1030). 2555 bytes result sent to driver
26/06/26 13:26:43 INFO TaskSetManager: Finished task 0.0 in stage 27.0 (TID 1030) in 568 ms on localhost (executor driver) (2/2)
26/06/26 13:26:43 INFO TaskSchedulerImpl: Removed TaskSet 27.0, whose tasks have all completed, from pool 
26/06/26 13:26:43 INFO DAGScheduler: ShuffleMapStage 27 (showString at NativeMethodAccessorImpl.java:0) finished in 0.580 s
26/06/26 13:26:43 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:43 INFO DAGScheduler: running: Set()
26/06/26 13:26:43 INFO DAGScheduler: waiting: Set(ShuffleMapStage 28, ResultStage 29)
26/06/26 13:26:43 INFO DAGScheduler: failed: Set()
26/06/26 13:26:43 INFO DAGScheduler: Submitting ShuffleMapStage 28 (MapPartitionsRDD[109] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:43 INFO MemoryStore: Block broadcast_31 stored as values in memory (estimated size 80.7 KB, free 364.6 MB)
26/06/26 13:26:43 INFO MemoryStore: Block broadcast_31_piece0 stored as bytes in memory (estimated size 32.3 KB, free 364.6 MB)
26/06/26 13:26:43 INFO BlockManagerInfo: Added broadcast_31_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 32.3 KB, free: 366.0 MB)
26/06/26 13:26:43 INFO SparkContext: Created broadcast 31 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:43 INFO DAGScheduler: Submitting 200 missing tasks from ShuffleMapStage 28 (MapPartitionsRDD[109] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
26/06/26 13:26:43 INFO TaskSchedulerImpl: Adding task set 28.0 with 200 tasks
26/06/26 13:26:43 INFO TaskSetManager: Starting task 0.0 in stage 28.0 (TID 1032, localhost, executor driver, partition 0, ANY, 7743 bytes)
26/06/26 13:26:43 INFO TaskSetManager: Starting task 1.0 in stage 28.0 (TID 1033, localhost, executor driver, partition 1, ANY, 7743 bytes)
26/06/26 13:26:43 INFO TaskSetManager: Starting task 2.0 in stage 28.0 (TID 1034, localhost, executor driver, partition 2, ANY, 7743 bytes)
26/06/26 13:26:43 INFO TaskSetManager: Starting task 3.0 in stage 28.0 (TID 1035, localhost, executor driver, partition 3, ANY, 7743 bytes)
26/06/26 13:26:43 INFO Executor: Running task 3.0 in stage 28.0 (TID 1035)
26/06/26 13:26:43 INFO Executor: Running task 2.0 in stage 28.0 (TID 1034)
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:43 INFO Executor: Running task 1.0 in stage 28.0 (TID 1033)
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:43 INFO Executor: Running task 0.0 in stage 28.0 (TID 1032)
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:43 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 48.670369 ms
26/06/26 13:26:43 INFO CodeGenerator: Code generated in 9.256572 ms
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_29_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 4.3 KB, free: 366.0 MB)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 866
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 867
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_30_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 20.5 KB, free: 366.0 MB)
26/06/26 13:26:44 INFO CodeGenerator: Code generated in 44.581169 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 248
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 738
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 719
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 253
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 488
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 1
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 610
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 395
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 356
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_16_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 17.0 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO Executor: Finished task 0.0 in stage 28.0 (TID 1032). 3292 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Finished task 1.0 in stage 28.0 (TID 1033). 3292 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Finished task 3.0 in stage 28.0 (TID 1035). 3292 bytes result sent to driver
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 363
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 713
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 659
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 651
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 585
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 817
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 740
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 523
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 534
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 527
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 852
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 402
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 506
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 800
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 380
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 493
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 467
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 665
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 633
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 563
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 228
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 410
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 806
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 480
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 650
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 598
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 555
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 387
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 249
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 251
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 470
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 365
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 834
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 359
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 714
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 457
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 753
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 502
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 561
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 604
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 243
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 813
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 762
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 624
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 584
26/06/26 13:26:44 INFO TaskSetManager: Starting task 4.0 in stage 28.0 (TID 1036, localhost, executor driver, partition 4, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 5.0 in stage 28.0 (TID 1037, localhost, executor driver, partition 5, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 6.0 in stage 28.0 (TID 1038, localhost, executor driver, partition 6, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 5.0 in stage 28.0 (TID 1037)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 10
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 856
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 790
26/06/26 13:26:44 INFO TaskSetManager: Finished task 0.0 in stage 28.0 (TID 1032) in 720 ms on localhost (executor driver) (1/200)
26/06/26 13:26:44 INFO Executor: Running task 6.0 in stage 28.0 (TID 1038)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Finished task 3.0 in stage 28.0 (TID 1035) in 725 ms on localhost (executor driver) (2/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 1.0 in stage 28.0 (TID 1033) in 730 ms on localhost (executor driver) (3/200)
26/06/26 13:26:44 INFO Executor: Finished task 2.0 in stage 28.0 (TID 1034). 3292 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 7.0 in stage 28.0 (TID 1039, localhost, executor driver, partition 7, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 7.0 in stage 28.0 (TID 1039)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 2.0 in stage 28.0 (TID 1034) in 733 ms on localhost (executor driver) (4/200)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 7
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 632
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 374
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 468
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 627
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 504
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 505
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 754
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 551
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 463
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 725
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 570
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 687
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 401
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 609
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_11_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 12.2 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 7 ms
26/06/26 13:26:44 INFO Executor: Running task 4.0 in stage 28.0 (TID 1036)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Finished task 7.0 in stage 28.0 (TID 1039). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Finished task 6.0 in stage 28.0 (TID 1038). 3292 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 8.0 in stage 28.0 (TID 1040, localhost, executor driver, partition 8, ANY, 7743 bytes)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 701
26/06/26 13:26:44 INFO TaskSetManager: Starting task 9.0 in stage 28.0 (TID 1041, localhost, executor driver, partition 9, ANY, 7743 bytes)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 8
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 233
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 397
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 695
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 428
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 582
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 616
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 255
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 807
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 462
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 540
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 537
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 424
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 835
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 623
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 634
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 737
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 236
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 846
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 658
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 808
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 229
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 382
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 776
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 777
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 809
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 702
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 520
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 494
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 816
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 681
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 653
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 560
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 542
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 530
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 355
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 501
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 404
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 801
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 824
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 360
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 848
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 535
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 419
26/06/26 13:26:44 INFO TaskSetManager: Finished task 7.0 in stage 28.0 (TID 1039) in 77 ms on localhost (executor driver) (5/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 6.0 in stage 28.0 (TID 1038) in 96 ms on localhost (executor driver) (6/200)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 5
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 822
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 772
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 657
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 721
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 565
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 595
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 354
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 823
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 421
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 862
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 683
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 422
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 528
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 362
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 234
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 696
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 569
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 579
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 396
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 849
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 475
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 515
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 743
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 670
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 543
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 562
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 706
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 639
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 372
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 361
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 841
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 831
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 673
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 11
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 759
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 258
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 476
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 812
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 384
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 478
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 663
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 526
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 498
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 693
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 705
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 769
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 597
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_25_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 18.8 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO Executor: Running task 9.0 in stage 28.0 (TID 1041)
26/06/26 13:26:44 INFO Executor: Running task 8.0 in stage 28.0 (TID 1040)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 256
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 782
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 724
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 246
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 564
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 469
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 842
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 671
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 630
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 844
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 547
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 850
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 426
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 247
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 254
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 385
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 781
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 583
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 566
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 686
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 375
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 429
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 718
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 552
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 716
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 819
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 600
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 557
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 766
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 417
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 853
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 857
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 603
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 483
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 758
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 748
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 370
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 492
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 677
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 499
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 508
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 386
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 568
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 774
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 625
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 676
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 645
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 477
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 357
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 811
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 358
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 512
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 408
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 487
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 367
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 836
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 818
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 699
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 647
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 427
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 602
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 369
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 465
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 238
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 847
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 745
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 861
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 859
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 828
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 391
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 741
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 821
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 532
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 755
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 518
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 798
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 553
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 409
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 418
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 688
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 674
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 510
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 750
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 392
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 723
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 416
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 576
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 242
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 792
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 668
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 756
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 752
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 599
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 678
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 567
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 839
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 364
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 573
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 820
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 855
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 786
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 479
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 237
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 415
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 491
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 814
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 529
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 654
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 691
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 689
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 605
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 854
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 6
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 638
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 572
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 771
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 799
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 722
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 642
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 635
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 810
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 694
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 481
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 779
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 656
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 590
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 621
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 832
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 223
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 767
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 366
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 770
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 516
26/06/26 13:26:44 INFO Executor: Finished task 5.0 in stage 28.0 (TID 1037). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 10.0 in stage 28.0 (TID 1042, localhost, executor driver, partition 10, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 10.0 in stage 28.0 (TID 1042)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 9
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 596
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 761
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 608
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 250
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 550
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 403
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 863
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 644
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 795
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 838
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 731
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 414
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 747
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 373
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 546
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 525
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 496
26/06/26 13:26:44 INFO Executor: Finished task 8.0 in stage 28.0 (TID 1040). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 406
26/06/26 13:26:44 INFO TaskSetManager: Finished task 5.0 in stage 28.0 (TID 1037) in 153 ms on localhost (executor driver) (7/200)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Finished task 4.0 in stage 28.0 (TID 1036). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 11.0 in stage 28.0 (TID 1043, localhost, executor driver, partition 11, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 12.0 in stage 28.0 (TID 1044, localhost, executor driver, partition 12, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 11.0 in stage 28.0 (TID 1043)
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_18_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 14.2 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 843
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 710
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 780
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 734
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 669
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 503
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 376
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 829
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 637
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 851
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 649
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 513
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 840
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 495
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 672
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 259
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 511
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 611
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 244
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 389
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 815
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 664
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 709
26/06/26 13:26:44 INFO TaskSetManager: Finished task 8.0 in stage 28.0 (TID 1040) in 106 ms on localhost (executor driver) (8/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 4.0 in stage 28.0 (TID 1036) in 186 ms on localhost (executor driver) (9/200)
26/06/26 13:26:44 INFO Executor: Running task 12.0 in stage 28.0 (TID 1044)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
26/06/26 13:26:44 INFO Executor: Finished task 9.0 in stage 28.0 (TID 1041). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 4
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 226
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 711
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 545
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 837
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 631
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 690
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 785
26/06/26 13:26:44 INFO TaskSetManager: Starting task 13.0 in stage 28.0 (TID 1045, localhost, executor driver, partition 13, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 9.0 in stage 28.0 (TID 1041) in 119 ms on localhost (executor driver) (10/200)
26/06/26 13:26:44 INFO Executor: Running task 13.0 in stage 28.0 (TID 1045)
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_22_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 21.8 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Finished task 11.0 in stage 28.0 (TID 1043). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 14.0 in stage 28.0 (TID 1046, localhost, executor driver, partition 14, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 14.0 in stage 28.0 (TID 1046)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 381
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 860
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Finished task 11.0 in stage 28.0 (TID 1043) in 70 ms on localhost (executor driver) (11/200)
26/06/26 13:26:44 INFO Executor: Finished task 12.0 in stage 28.0 (TID 1044). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 15.0 in stage 28.0 (TID 1047, localhost, executor driver, partition 15, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 12.0 in stage 28.0 (TID 1044) in 71 ms on localhost (executor driver) (12/200)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 3
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 626
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 739
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 536
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 390
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 648
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 707
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 698
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 500
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 578
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 394
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 760
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 791
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 591
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 629
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 549
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 587
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 680
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 802
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 704
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 684
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 413
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 636
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 612
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 717
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 474
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 471
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 460
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 715
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 458
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 377
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 588
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 830
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 728
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 607
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 641
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 461
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 252
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 371
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 379
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 388
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 825
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 423
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 617
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 241
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 751
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 655
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 720
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 224
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 732
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 796
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 466
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 805
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 393
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 230
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 640
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 486
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 784
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 643
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 742
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 727
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 729
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 826
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 472
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 227
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 524
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 733
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 864
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 231
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 260
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 405
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 400
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 235
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 517
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 787
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 539
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 378
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 497
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 833
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 593
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 240
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 485
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 519
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 533
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_28_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 20.7 KB, free: 366.1 MB)
26/06/26 13:26:44 INFO Executor: Finished task 14.0 in stage 28.0 (TID 1046). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 16.0 in stage 28.0 (TID 1048, localhost, executor driver, partition 16, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 14.0 in stage 28.0 (TID 1046) in 26 ms on localhost (executor driver) (13/200)
26/06/26 13:26:44 INFO Executor: Running task 16.0 in stage 28.0 (TID 1048)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Running task 15.0 in stage 28.0 (TID 1047)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 804
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 575
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 757
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 685
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 586
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 712
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 577
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 489
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 398
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 383
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 858
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 768
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 484
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 257
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_21_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 19.2 KB, free: 366.2 MB)
26/06/26 13:26:44 INFO Executor: Finished task 10.0 in stage 28.0 (TID 1042). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 17.0 in stage 28.0 (TID 1049, localhost, executor driver, partition 17, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 10.0 in stage 28.0 (TID 1042) in 155 ms on localhost (executor driver) (14/200)
26/06/26 13:26:44 INFO Executor: Finished task 13.0 in stage 28.0 (TID 1045). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Running task 17.0 in stage 28.0 (TID 1049)
26/06/26 13:26:44 INFO Executor: Finished task 15.0 in stage 28.0 (TID 1047). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 18.0 in stage 28.0 (TID 1050, localhost, executor driver, partition 18, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 19.0 in stage 28.0 (TID 1051, localhost, executor driver, partition 19, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 19.0 in stage 28.0 (TID 1051)
26/06/26 13:26:44 INFO Executor: Finished task 16.0 in stage 28.0 (TID 1048). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Running task 18.0 in stage 28.0 (TID 1050)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Starting task 20.0 in stage 28.0 (TID 1052, localhost, executor driver, partition 20, ANY, 7743 bytes)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 865
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 797
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 574
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 521
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 803
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 407
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 619
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 730
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 420
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 746
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 531
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 225
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 708
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 425
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 726
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 789
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 368
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 775
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 412
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 601
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 571
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 736
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 735
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 682
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 679
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 613
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 614
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 618
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 232
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 509
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 622
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 245
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 773
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 778
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 765
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 675
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 660
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 490
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 594
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 522
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 580
26/06/26 13:26:44 INFO BlockManagerInfo: Removed broadcast_19_piece0 on sandbox-hdp.hortonworks.com:33329 in memory (size: 16.9 KB, free: 366.2 MB)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 13.0 in stage 28.0 (TID 1045) in 104 ms on localhost (executor driver) (15/200)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 697
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 749
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 514
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 652
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 538
26/06/26 13:26:44 INFO TaskSetManager: Finished task 16.0 in stage 28.0 (TID 1048) in 58 ms on localhost (executor driver) (16/200)
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 793
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 544
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 692
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 507
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 788
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 592
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 703
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 700
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 548
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 827
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 646
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 615
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 581
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 239
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 556
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 399
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 554
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 666
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 845
26/06/26 13:26:44 INFO TaskSetManager: Finished task 15.0 in stage 28.0 (TID 1047) in 76 ms on localhost (executor driver) (17/200)
26/06/26 13:26:44 INFO Executor: Running task 20.0 in stage 28.0 (TID 1052)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ContextCleaner: Cleaned shuffle 12
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 482
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 411
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 261
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 606
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 541
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 783
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 473
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 794
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 620
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 589
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 744
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 459
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 628
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 667
26/06/26 13:26:44 INFO ContextCleaner: Cleaned accumulator 464
26/06/26 13:26:44 INFO Executor: Finished task 19.0 in stage 28.0 (TID 1051). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 21.0 in stage 28.0 (TID 1053, localhost, executor driver, partition 21, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 21.0 in stage 28.0 (TID 1053)
26/06/26 13:26:44 INFO Executor: Finished task 20.0 in stage 28.0 (TID 1052). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Finished task 18.0 in stage 28.0 (TID 1050). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Finished task 19.0 in stage 28.0 (TID 1051) in 42 ms on localhost (executor driver) (18/200)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 22.0 in stage 28.0 (TID 1054, localhost, executor driver, partition 22, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 23.0 in stage 28.0 (TID 1055, localhost, executor driver, partition 23, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 18.0 in stage 28.0 (TID 1050) in 58 ms on localhost (executor driver) (19/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 20.0 in stage 28.0 (TID 1052) in 52 ms on localhost (executor driver) (20/200)
26/06/26 13:26:44 INFO Executor: Running task 22.0 in stage 28.0 (TID 1054)
26/06/26 13:26:44 INFO Executor: Finished task 17.0 in stage 28.0 (TID 1049). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 24.0 in stage 28.0 (TID 1056, localhost, executor driver, partition 24, ANY, 7743 bytes)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 13 ms
26/06/26 13:26:44 INFO TaskSetManager: Finished task 17.0 in stage 28.0 (TID 1049) in 63 ms on localhost (executor driver) (21/200)
26/06/26 13:26:44 INFO Executor: Running task 24.0 in stage 28.0 (TID 1056)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:44 INFO Executor: Running task 23.0 in stage 28.0 (TID 1055)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Finished task 24.0 in stage 28.0 (TID 1056). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 25.0 in stage 28.0 (TID 1057, localhost, executor driver, partition 25, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Finished task 21.0 in stage 28.0 (TID 1053). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO Executor: Running task 25.0 in stage 28.0 (TID 1057)
26/06/26 13:26:44 INFO Executor: Finished task 22.0 in stage 28.0 (TID 1054). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 26.0 in stage 28.0 (TID 1058, localhost, executor driver, partition 26, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Starting task 27.0 in stage 28.0 (TID 1059, localhost, executor driver, partition 27, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 24.0 in stage 28.0 (TID 1056) in 38 ms on localhost (executor driver) (22/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 21.0 in stage 28.0 (TID 1053) in 57 ms on localhost (executor driver) (23/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 22.0 in stage 28.0 (TID 1054) in 41 ms on localhost (executor driver) (24/200)
26/06/26 13:26:44 INFO Executor: Running task 26.0 in stage 28.0 (TID 1058)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Running task 27.0 in stage 28.0 (TID 1059)
26/06/26 13:26:44 INFO Executor: Finished task 23.0 in stage 28.0 (TID 1055). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Starting task 28.0 in stage 28.0 (TID 1060, localhost, executor driver, partition 28, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 28.0 in stage 28.0 (TID 1060)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Finished task 23.0 in stage 28.0 (TID 1055) in 67 ms on localhost (executor driver) (25/200)
26/06/26 13:26:44 INFO Executor: Finished task 26.0 in stage 28.0 (TID 1058). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 29.0 in stage 28.0 (TID 1061, localhost, executor driver, partition 29, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 26.0 in stage 28.0 (TID 1058) in 33 ms on localhost (executor driver) (26/200)
26/06/26 13:26:44 INFO Executor: Running task 29.0 in stage 28.0 (TID 1061)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO Executor: Finished task 25.0 in stage 28.0 (TID 1057). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 30.0 in stage 28.0 (TID 1062, localhost, executor driver, partition 30, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Finished task 27.0 in stage 28.0 (TID 1059). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 31.0 in stage 28.0 (TID 1063, localhost, executor driver, partition 31, ANY, 7743 bytes)
26/06/26 13:26:44 INFO Executor: Running task 31.0 in stage 28.0 (TID 1063)
26/06/26 13:26:44 INFO Executor: Running task 30.0 in stage 28.0 (TID 1062)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:44 INFO TaskSetManager: Finished task 25.0 in stage 28.0 (TID 1057) in 61 ms on localhost (executor driver) (27/200)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 27.0 in stage 28.0 (TID 1059) in 56 ms on localhost (executor driver) (28/200)
26/06/26 13:26:44 INFO Executor: Finished task 28.0 in stage 28.0 (TID 1060). 3249 bytes result sent to driver
26/06/26 13:26:44 INFO TaskSetManager: Starting task 32.0 in stage 28.0 (TID 1064, localhost, executor driver, partition 32, ANY, 7743 bytes)
26/06/26 13:26:44 INFO TaskSetManager: Finished task 28.0 in stage 28.0 (TID 1060) in 38 ms on localhost (executor driver) (29/200)
26/06/26 13:26:44 INFO Executor: Running task 32.0 in stage 28.0 (TID 1064)
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:44 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 31.0 in stage 28.0 (TID 1063). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 33.0 in stage 28.0 (TID 1065, localhost, executor driver, partition 33, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 31.0 in stage 28.0 (TID 1063) in 46 ms on localhost (executor driver) (30/200)
26/06/26 13:26:45 INFO Executor: Running task 33.0 in stage 28.0 (TID 1065)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 29.0 in stage 28.0 (TID 1061). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 30.0 in stage 28.0 (TID 1062). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 32.0 in stage 28.0 (TID 1064). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 34.0 in stage 28.0 (TID 1066, localhost, executor driver, partition 34, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 35.0 in stage 28.0 (TID 1067, localhost, executor driver, partition 35, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 36.0 in stage 28.0 (TID 1068, localhost, executor driver, partition 36, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 29.0 in stage 28.0 (TID 1061) in 72 ms on localhost (executor driver) (31/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 30.0 in stage 28.0 (TID 1062) in 59 ms on localhost (executor driver) (32/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 32.0 in stage 28.0 (TID 1064) in 45 ms on localhost (executor driver) (33/200)
26/06/26 13:26:45 INFO Executor: Running task 34.0 in stage 28.0 (TID 1066)
26/06/26 13:26:45 INFO Executor: Running task 36.0 in stage 28.0 (TID 1068)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 33.0 in stage 28.0 (TID 1065). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 37.0 in stage 28.0 (TID 1069, localhost, executor driver, partition 37, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 33.0 in stage 28.0 (TID 1065) in 52 ms on localhost (executor driver) (34/200)
26/06/26 13:26:45 INFO Executor: Running task 37.0 in stage 28.0 (TID 1069)
26/06/26 13:26:45 INFO Executor: Finished task 36.0 in stage 28.0 (TID 1068). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 38.0 in stage 28.0 (TID 1070, localhost, executor driver, partition 38, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 34.0 in stage 28.0 (TID 1066). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 38.0 in stage 28.0 (TID 1070)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 39.0 in stage 28.0 (TID 1071, localhost, executor driver, partition 39, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 37.0 in stage 28.0 (TID 1069). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 39.0 in stage 28.0 (TID 1071)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 36.0 in stage 28.0 (TID 1068) in 63 ms on localhost (executor driver) (35/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 34.0 in stage 28.0 (TID 1066) in 63 ms on localhost (executor driver) (36/200)
26/06/26 13:26:45 INFO Executor: Running task 35.0 in stage 28.0 (TID 1067)
26/06/26 13:26:45 INFO Executor: Finished task 38.0 in stage 28.0 (TID 1070). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 40.0 in stage 28.0 (TID 1072, localhost, executor driver, partition 40, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 41.0 in stage 28.0 (TID 1073, localhost, executor driver, partition 41, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 40.0 in stage 28.0 (TID 1072)
26/06/26 13:26:45 INFO Executor: Running task 41.0 in stage 28.0 (TID 1073)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 37.0 in stage 28.0 (TID 1069) in 47 ms on localhost (executor driver) (37/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 38.0 in stage 28.0 (TID 1070) in 41 ms on localhost (executor driver) (38/200)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 35.0 in stage 28.0 (TID 1067). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 42.0 in stage 28.0 (TID 1074, localhost, executor driver, partition 42, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 35.0 in stage 28.0 (TID 1067) in 102 ms on localhost (executor driver) (39/200)
26/06/26 13:26:45 INFO Executor: Finished task 41.0 in stage 28.0 (TID 1073). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 39.0 in stage 28.0 (TID 1071). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 42.0 in stage 28.0 (TID 1074)
26/06/26 13:26:45 INFO Executor: Finished task 40.0 in stage 28.0 (TID 1072). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 43.0 in stage 28.0 (TID 1075, localhost, executor driver, partition 43, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 44.0 in stage 28.0 (TID 1076, localhost, executor driver, partition 44, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 45.0 in stage 28.0 (TID 1077, localhost, executor driver, partition 45, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 41.0 in stage 28.0 (TID 1073) in 40 ms on localhost (executor driver) (40/200)
26/06/26 13:26:45 INFO Executor: Running task 44.0 in stage 28.0 (TID 1076)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 39.0 in stage 28.0 (TID 1071) in 64 ms on localhost (executor driver) (41/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 40.0 in stage 28.0 (TID 1072) in 41 ms on localhost (executor driver) (42/200)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 43.0 in stage 28.0 (TID 1075)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 45.0 in stage 28.0 (TID 1077)
26/06/26 13:26:45 INFO Executor: Finished task 42.0 in stage 28.0 (TID 1074). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 46.0 in stage 28.0 (TID 1078, localhost, executor driver, partition 46, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 46.0 in stage 28.0 (TID 1078)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 43.0 in stage 28.0 (TID 1075). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Finished task 42.0 in stage 28.0 (TID 1074) in 56 ms on localhost (executor driver) (43/200)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 47.0 in stage 28.0 (TID 1079, localhost, executor driver, partition 47, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 47.0 in stage 28.0 (TID 1079)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Finished task 43.0 in stage 28.0 (TID 1075) in 44 ms on localhost (executor driver) (44/200)
26/06/26 13:26:45 INFO Executor: Finished task 47.0 in stage 28.0 (TID 1079). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 48.0 in stage 28.0 (TID 1080, localhost, executor driver, partition 48, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 44.0 in stage 28.0 (TID 1076). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 49.0 in stage 28.0 (TID 1081, localhost, executor driver, partition 49, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 49.0 in stage 28.0 (TID 1081)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 47.0 in stage 28.0 (TID 1079) in 22 ms on localhost (executor driver) (45/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 44.0 in stage 28.0 (TID 1076) in 53 ms on localhost (executor driver) (46/200)
26/06/26 13:26:45 INFO Executor: Finished task 45.0 in stage 28.0 (TID 1077). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 48.0 in stage 28.0 (TID 1080)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 46.0 in stage 28.0 (TID 1078). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 50.0 in stage 28.0 (TID 1082, localhost, executor driver, partition 50, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 51.0 in stage 28.0 (TID 1083, localhost, executor driver, partition 51, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 51.0 in stage 28.0 (TID 1083)
26/06/26 13:26:45 INFO Executor: Finished task 49.0 in stage 28.0 (TID 1081). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Finished task 45.0 in stage 28.0 (TID 1077) in 77 ms on localhost (executor driver) (47/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 46.0 in stage 28.0 (TID 1078) in 52 ms on localhost (executor driver) (48/200)
26/06/26 13:26:45 INFO Executor: Running task 50.0 in stage 28.0 (TID 1082)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 52.0 in stage 28.0 (TID 1084, localhost, executor driver, partition 52, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 49.0 in stage 28.0 (TID 1081) in 47 ms on localhost (executor driver) (49/200)
26/06/26 13:26:45 INFO Executor: Running task 52.0 in stage 28.0 (TID 1084)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 50.0 in stage 28.0 (TID 1082). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 53.0 in stage 28.0 (TID 1085, localhost, executor driver, partition 53, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 50.0 in stage 28.0 (TID 1082) in 45 ms on localhost (executor driver) (50/200)
26/06/26 13:26:45 INFO Executor: Running task 53.0 in stage 28.0 (TID 1085)
26/06/26 13:26:45 INFO Executor: Finished task 51.0 in stage 28.0 (TID 1083). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 54.0 in stage 28.0 (TID 1086, localhost, executor driver, partition 54, ANY, 7743 bytes)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 54.0 in stage 28.0 (TID 1086)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Finished task 51.0 in stage 28.0 (TID 1083) in 74 ms on localhost (executor driver) (51/200)
26/06/26 13:26:45 INFO Executor: Finished task 48.0 in stage 28.0 (TID 1080). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 52.0 in stage 28.0 (TID 1084). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 55.0 in stage 28.0 (TID 1087, localhost, executor driver, partition 55, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 56.0 in stage 28.0 (TID 1088, localhost, executor driver, partition 56, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 55.0 in stage 28.0 (TID 1087)
26/06/26 13:26:45 INFO Executor: Finished task 53.0 in stage 28.0 (TID 1085). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 56.0 in stage 28.0 (TID 1088)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Finished task 48.0 in stage 28.0 (TID 1080) in 118 ms on localhost (executor driver) (52/200)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 57.0 in stage 28.0 (TID 1089, localhost, executor driver, partition 57, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 52.0 in stage 28.0 (TID 1084) in 73 ms on localhost (executor driver) (53/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 53.0 in stage 28.0 (TID 1085) in 54 ms on localhost (executor driver) (54/200)
26/06/26 13:26:45 INFO Executor: Running task 57.0 in stage 28.0 (TID 1089)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 54.0 in stage 28.0 (TID 1086). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 58.0 in stage 28.0 (TID 1090, localhost, executor driver, partition 58, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 54.0 in stage 28.0 (TID 1086) in 66 ms on localhost (executor driver) (55/200)
26/06/26 13:26:45 INFO Executor: Finished task 56.0 in stage 28.0 (TID 1088). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 59.0 in stage 28.0 (TID 1091, localhost, executor driver, partition 59, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 56.0 in stage 28.0 (TID 1088) in 42 ms on localhost (executor driver) (56/200)
26/06/26 13:26:45 INFO Executor: Running task 59.0 in stage 28.0 (TID 1091)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 58.0 in stage 28.0 (TID 1090)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 57.0 in stage 28.0 (TID 1089). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 55.0 in stage 28.0 (TID 1087). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 60.0 in stage 28.0 (TID 1092, localhost, executor driver, partition 60, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 61.0 in stage 28.0 (TID 1093, localhost, executor driver, partition 61, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 60.0 in stage 28.0 (TID 1092)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 57.0 in stage 28.0 (TID 1089) in 58 ms on localhost (executor driver) (57/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 55.0 in stage 28.0 (TID 1087) in 73 ms on localhost (executor driver) (58/200)
26/06/26 13:26:45 INFO Executor: Finished task 59.0 in stage 28.0 (TID 1091). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 58.0 in stage 28.0 (TID 1090). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 61.0 in stage 28.0 (TID 1093)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 62.0 in stage 28.0 (TID 1094, localhost, executor driver, partition 62, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 63.0 in stage 28.0 (TID 1095, localhost, executor driver, partition 63, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 59.0 in stage 28.0 (TID 1091) in 46 ms on localhost (executor driver) (59/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 58.0 in stage 28.0 (TID 1090) in 53 ms on localhost (executor driver) (60/200)
26/06/26 13:26:45 INFO Executor: Running task 63.0 in stage 28.0 (TID 1095)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 60.0 in stage 28.0 (TID 1092). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 62.0 in stage 28.0 (TID 1094)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 64.0 in stage 28.0 (TID 1096, localhost, executor driver, partition 64, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 60.0 in stage 28.0 (TID 1092) in 37 ms on localhost (executor driver) (61/200)
26/06/26 13:26:45 INFO Executor: Running task 64.0 in stage 28.0 (TID 1096)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 62.0 in stage 28.0 (TID 1094). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 64.0 in stage 28.0 (TID 1096). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 65.0 in stage 28.0 (TID 1097, localhost, executor driver, partition 65, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 66.0 in stage 28.0 (TID 1098, localhost, executor driver, partition 66, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 62.0 in stage 28.0 (TID 1094) in 66 ms on localhost (executor driver) (62/200)
26/06/26 13:26:45 INFO Executor: Running task 66.0 in stage 28.0 (TID 1098)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 64.0 in stage 28.0 (TID 1096) in 44 ms on localhost (executor driver) (63/200)
26/06/26 13:26:45 INFO Executor: Finished task 61.0 in stage 28.0 (TID 1093). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 65.0 in stage 28.0 (TID 1097)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 67.0 in stage 28.0 (TID 1099, localhost, executor driver, partition 67, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 61.0 in stage 28.0 (TID 1093) in 121 ms on localhost (executor driver) (64/200)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 67.0 in stage 28.0 (TID 1099)
26/06/26 13:26:45 INFO Executor: Finished task 63.0 in stage 28.0 (TID 1095). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 66.0 in stage 28.0 (TID 1098). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 65.0 in stage 28.0 (TID 1097). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 67.0 in stage 28.0 (TID 1099). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 68.0 in stage 28.0 (TID 1100, localhost, executor driver, partition 68, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 69.0 in stage 28.0 (TID 1101, localhost, executor driver, partition 69, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 70.0 in stage 28.0 (TID 1102, localhost, executor driver, partition 70, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 71.0 in stage 28.0 (TID 1103, localhost, executor driver, partition 71, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 68.0 in stage 28.0 (TID 1100)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 63.0 in stage 28.0 (TID 1095) in 169 ms on localhost (executor driver) (65/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 66.0 in stage 28.0 (TID 1098) in 103 ms on localhost (executor driver) (66/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 65.0 in stage 28.0 (TID 1097) in 104 ms on localhost (executor driver) (67/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 67.0 in stage 28.0 (TID 1099) in 99 ms on localhost (executor driver) (68/200)
26/06/26 13:26:45 INFO Executor: Running task 70.0 in stage 28.0 (TID 1102)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 69.0 in stage 28.0 (TID 1101)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 71.0 in stage 28.0 (TID 1103)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 69.0 in stage 28.0 (TID 1101). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 72.0 in stage 28.0 (TID 1104, localhost, executor driver, partition 72, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 69.0 in stage 28.0 (TID 1101) in 45 ms on localhost (executor driver) (69/200)
26/06/26 13:26:45 INFO Executor: Finished task 70.0 in stage 28.0 (TID 1102). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 72.0 in stage 28.0 (TID 1104)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 68.0 in stage 28.0 (TID 1100). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 73.0 in stage 28.0 (TID 1105, localhost, executor driver, partition 73, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 74.0 in stage 28.0 (TID 1106, localhost, executor driver, partition 74, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 70.0 in stage 28.0 (TID 1102) in 53 ms on localhost (executor driver) (70/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 68.0 in stage 28.0 (TID 1100) in 54 ms on localhost (executor driver) (71/200)
26/06/26 13:26:45 INFO Executor: Running task 74.0 in stage 28.0 (TID 1106)
26/06/26 13:26:45 INFO Executor: Running task 73.0 in stage 28.0 (TID 1105)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 71.0 in stage 28.0 (TID 1103). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 72.0 in stage 28.0 (TID 1104). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 75.0 in stage 28.0 (TID 1107, localhost, executor driver, partition 75, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 76.0 in stage 28.0 (TID 1108, localhost, executor driver, partition 76, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 71.0 in stage 28.0 (TID 1103) in 76 ms on localhost (executor driver) (72/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 72.0 in stage 28.0 (TID 1104) in 31 ms on localhost (executor driver) (73/200)
26/06/26 13:26:45 INFO Executor: Running task 76.0 in stage 28.0 (TID 1108)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 75.0 in stage 28.0 (TID 1107)
26/06/26 13:26:45 INFO Executor: Finished task 74.0 in stage 28.0 (TID 1106). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 77.0 in stage 28.0 (TID 1109, localhost, executor driver, partition 77, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 76.0 in stage 28.0 (TID 1108). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 78.0 in stage 28.0 (TID 1110, localhost, executor driver, partition 78, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 74.0 in stage 28.0 (TID 1106) in 46 ms on localhost (executor driver) (74/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 76.0 in stage 28.0 (TID 1108) in 24 ms on localhost (executor driver) (75/200)
26/06/26 13:26:45 INFO Executor: Running task 77.0 in stage 28.0 (TID 1109)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 75.0 in stage 28.0 (TID 1107). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 79.0 in stage 28.0 (TID 1111, localhost, executor driver, partition 79, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 75.0 in stage 28.0 (TID 1107) in 33 ms on localhost (executor driver) (76/200)
26/06/26 13:26:45 INFO Executor: Finished task 73.0 in stage 28.0 (TID 1105). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 80.0 in stage 28.0 (TID 1112, localhost, executor driver, partition 80, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 73.0 in stage 28.0 (TID 1105) in 60 ms on localhost (executor driver) (77/200)
26/06/26 13:26:45 INFO Executor: Running task 79.0 in stage 28.0 (TID 1111)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 77.0 in stage 28.0 (TID 1109). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 81.0 in stage 28.0 (TID 1113, localhost, executor driver, partition 81, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 77.0 in stage 28.0 (TID 1109) in 34 ms on localhost (executor driver) (78/200)
26/06/26 13:26:45 INFO Executor: Running task 80.0 in stage 28.0 (TID 1112)
26/06/26 13:26:45 INFO Executor: Running task 78.0 in stage 28.0 (TID 1110)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 81.0 in stage 28.0 (TID 1113)
26/06/26 13:26:45 INFO Executor: Finished task 79.0 in stage 28.0 (TID 1111). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 82.0 in stage 28.0 (TID 1114, localhost, executor driver, partition 82, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 79.0 in stage 28.0 (TID 1111) in 34 ms on localhost (executor driver) (79/200)
26/06/26 13:26:45 INFO Executor: Running task 82.0 in stage 28.0 (TID 1114)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 78.0 in stage 28.0 (TID 1110). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 83.0 in stage 28.0 (TID 1115, localhost, executor driver, partition 83, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 78.0 in stage 28.0 (TID 1110) in 50 ms on localhost (executor driver) (80/200)
26/06/26 13:26:45 INFO Executor: Finished task 81.0 in stage 28.0 (TID 1113). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 83.0 in stage 28.0 (TID 1115)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 84.0 in stage 28.0 (TID 1116, localhost, executor driver, partition 84, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 80.0 in stage 28.0 (TID 1112). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Finished task 81.0 in stage 28.0 (TID 1113) in 35 ms on localhost (executor driver) (81/200)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 82.0 in stage 28.0 (TID 1114). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 85.0 in stage 28.0 (TID 1117, localhost, executor driver, partition 85, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 86.0 in stage 28.0 (TID 1118, localhost, executor driver, partition 86, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 80.0 in stage 28.0 (TID 1112) in 55 ms on localhost (executor driver) (82/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 82.0 in stage 28.0 (TID 1114) in 25 ms on localhost (executor driver) (83/200)
26/06/26 13:26:45 INFO Executor: Running task 84.0 in stage 28.0 (TID 1116)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 85.0 in stage 28.0 (TID 1117)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 86.0 in stage 28.0 (TID 1118)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 86.0 in stage 28.0 (TID 1118). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 87.0 in stage 28.0 (TID 1119, localhost, executor driver, partition 87, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 86.0 in stage 28.0 (TID 1118) in 32 ms on localhost (executor driver) (84/200)
26/06/26 13:26:45 INFO Executor: Finished task 85.0 in stage 28.0 (TID 1117). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 88.0 in stage 28.0 (TID 1120, localhost, executor driver, partition 88, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 85.0 in stage 28.0 (TID 1117) in 34 ms on localhost (executor driver) (85/200)
26/06/26 13:26:45 INFO Executor: Running task 88.0 in stage 28.0 (TID 1120)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 87.0 in stage 28.0 (TID 1119)
26/06/26 13:26:45 INFO Executor: Finished task 83.0 in stage 28.0 (TID 1115). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 84.0 in stage 28.0 (TID 1116). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 89.0 in stage 28.0 (TID 1121, localhost, executor driver, partition 89, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 90.0 in stage 28.0 (TID 1122, localhost, executor driver, partition 90, ANY, 7743 bytes)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO Executor: Running task 90.0 in stage 28.0 (TID 1122)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Finished task 83.0 in stage 28.0 (TID 1115) in 73 ms on localhost (executor driver) (86/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 84.0 in stage 28.0 (TID 1116) in 62 ms on localhost (executor driver) (87/200)
26/06/26 13:26:45 INFO Executor: Finished task 88.0 in stage 28.0 (TID 1120). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 89.0 in stage 28.0 (TID 1121)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 91.0 in stage 28.0 (TID 1123, localhost, executor driver, partition 91, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 88.0 in stage 28.0 (TID 1120) in 24 ms on localhost (executor driver) (88/200)
26/06/26 13:26:45 INFO Executor: Running task 91.0 in stage 28.0 (TID 1123)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 87.0 in stage 28.0 (TID 1119). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 90.0 in stage 28.0 (TID 1122). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 91.0 in stage 28.0 (TID 1123). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 92.0 in stage 28.0 (TID 1124, localhost, executor driver, partition 92, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 93.0 in stage 28.0 (TID 1125, localhost, executor driver, partition 93, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 94.0 in stage 28.0 (TID 1126, localhost, executor driver, partition 94, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 87.0 in stage 28.0 (TID 1119) in 40 ms on localhost (executor driver) (89/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 90.0 in stage 28.0 (TID 1122) in 25 ms on localhost (executor driver) (90/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 91.0 in stage 28.0 (TID 1123) in 15 ms on localhost (executor driver) (91/200)
26/06/26 13:26:45 INFO Executor: Running task 92.0 in stage 28.0 (TID 1124)
26/06/26 13:26:45 INFO Executor: Running task 94.0 in stage 28.0 (TID 1126)
26/06/26 13:26:45 INFO Executor: Finished task 89.0 in stage 28.0 (TID 1121). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 93.0 in stage 28.0 (TID 1125)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 95.0 in stage 28.0 (TID 1127, localhost, executor driver, partition 95, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 89.0 in stage 28.0 (TID 1121) in 35 ms on localhost (executor driver) (92/200)
26/06/26 13:26:45 INFO Executor: Finished task 92.0 in stage 28.0 (TID 1124). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 96.0 in stage 28.0 (TID 1128, localhost, executor driver, partition 96, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 94.0 in stage 28.0 (TID 1126). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Finished task 92.0 in stage 28.0 (TID 1124) in 17 ms on localhost (executor driver) (93/200)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 97.0 in stage 28.0 (TID 1129, localhost, executor driver, partition 97, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 94.0 in stage 28.0 (TID 1126) in 18 ms on localhost (executor driver) (94/200)
26/06/26 13:26:45 INFO Executor: Running task 96.0 in stage 28.0 (TID 1128)
26/06/26 13:26:45 INFO Executor: Running task 95.0 in stage 28.0 (TID 1127)
26/06/26 13:26:45 INFO Executor: Running task 97.0 in stage 28.0 (TID 1129)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Finished task 96.0 in stage 28.0 (TID 1128). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 98.0 in stage 28.0 (TID 1130, localhost, executor driver, partition 98, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 96.0 in stage 28.0 (TID 1128) in 32 ms on localhost (executor driver) (95/200)
26/06/26 13:26:45 INFO Executor: Running task 98.0 in stage 28.0 (TID 1130)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 97.0 in stage 28.0 (TID 1129). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 93.0 in stage 28.0 (TID 1125). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 99.0 in stage 28.0 (TID 1131, localhost, executor driver, partition 99, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 97.0 in stage 28.0 (TID 1129) in 44 ms on localhost (executor driver) (96/200)
26/06/26 13:26:45 INFO Executor: Finished task 95.0 in stage 28.0 (TID 1127). 3292 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 100.0 in stage 28.0 (TID 1132, localhost, executor driver, partition 100, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 101.0 in stage 28.0 (TID 1133, localhost, executor driver, partition 101, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 93.0 in stage 28.0 (TID 1125) in 64 ms on localhost (executor driver) (97/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 95.0 in stage 28.0 (TID 1127) in 53 ms on localhost (executor driver) (98/200)
26/06/26 13:26:45 INFO Executor: Running task 99.0 in stage 28.0 (TID 1131)
26/06/26 13:26:45 INFO Executor: Finished task 98.0 in stage 28.0 (TID 1130). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 102.0 in stage 28.0 (TID 1134, localhost, executor driver, partition 102, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 98.0 in stage 28.0 (TID 1130) in 21 ms on localhost (executor driver) (99/200)
26/06/26 13:26:45 INFO Executor: Running task 102.0 in stage 28.0 (TID 1134)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 100.0 in stage 28.0 (TID 1132)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 102.0 in stage 28.0 (TID 1134). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 103.0 in stage 28.0 (TID 1135, localhost, executor driver, partition 103, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 101.0 in stage 28.0 (TID 1133)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 102.0 in stage 28.0 (TID 1134) in 15 ms on localhost (executor driver) (100/200)
26/06/26 13:26:45 INFO Executor: Running task 103.0 in stage 28.0 (TID 1135)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 99.0 in stage 28.0 (TID 1131). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 104.0 in stage 28.0 (TID 1136, localhost, executor driver, partition 104, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 99.0 in stage 28.0 (TID 1131) in 33 ms on localhost (executor driver) (101/200)
26/06/26 13:26:45 INFO Executor: Finished task 100.0 in stage 28.0 (TID 1132). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 8 ms
26/06/26 13:26:45 INFO Executor: Finished task 103.0 in stage 28.0 (TID 1135). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 105.0 in stage 28.0 (TID 1137, localhost, executor driver, partition 105, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 106.0 in stage 28.0 (TID 1138, localhost, executor driver, partition 106, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 100.0 in stage 28.0 (TID 1132) in 36 ms on localhost (executor driver) (102/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 103.0 in stage 28.0 (TID 1135) in 16 ms on localhost (executor driver) (103/200)
26/06/26 13:26:45 INFO Executor: Running task 105.0 in stage 28.0 (TID 1137)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Running task 106.0 in stage 28.0 (TID 1138)
26/06/26 13:26:45 INFO Executor: Finished task 101.0 in stage 28.0 (TID 1133). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Running task 104.0 in stage 28.0 (TID 1136)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO TaskSetManager: Starting task 107.0 in stage 28.0 (TID 1139, localhost, executor driver, partition 107, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 101.0 in stage 28.0 (TID 1133) in 61 ms on localhost (executor driver) (104/200)
26/06/26 13:26:45 INFO Executor: Finished task 105.0 in stage 28.0 (TID 1137). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 108.0 in stage 28.0 (TID 1140, localhost, executor driver, partition 108, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 105.0 in stage 28.0 (TID 1137) in 26 ms on localhost (executor driver) (105/200)
26/06/26 13:26:45 INFO Executor: Running task 108.0 in stage 28.0 (TID 1140)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:45 INFO Executor: Running task 107.0 in stage 28.0 (TID 1139)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 104.0 in stage 28.0 (TID 1136). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 109.0 in stage 28.0 (TID 1141, localhost, executor driver, partition 109, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 109.0 in stage 28.0 (TID 1141)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 104.0 in stage 28.0 (TID 1136) in 60 ms on localhost (executor driver) (106/200)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 106.0 in stage 28.0 (TID 1138). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO Executor: Finished task 107.0 in stage 28.0 (TID 1139). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 110.0 in stage 28.0 (TID 1142, localhost, executor driver, partition 110, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Finished task 109.0 in stage 28.0 (TID 1141). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 111.0 in stage 28.0 (TID 1143, localhost, executor driver, partition 111, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 111.0 in stage 28.0 (TID 1143)
26/06/26 13:26:45 INFO Executor: Finished task 108.0 in stage 28.0 (TID 1140). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 112.0 in stage 28.0 (TID 1144, localhost, executor driver, partition 112, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Starting task 113.0 in stage 28.0 (TID 1145, localhost, executor driver, partition 113, ANY, 7743 bytes)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 108.0 in stage 28.0 (TID 1140) in 46 ms on localhost (executor driver) (107/200)
26/06/26 13:26:45 INFO Executor: Running task 113.0 in stage 28.0 (TID 1145)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Running task 110.0 in stage 28.0 (TID 1142)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO TaskSetManager: Finished task 107.0 in stage 28.0 (TID 1139) in 63 ms on localhost (executor driver) (108/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 106.0 in stage 28.0 (TID 1138) in 88 ms on localhost (executor driver) (109/200)
26/06/26 13:26:45 INFO TaskSetManager: Finished task 109.0 in stage 28.0 (TID 1141) in 34 ms on localhost (executor driver) (110/200)
26/06/26 13:26:45 INFO Executor: Running task 112.0 in stage 28.0 (TID 1144)
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:45 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:45 INFO Executor: Finished task 113.0 in stage 28.0 (TID 1145). 3249 bytes result sent to driver
26/06/26 13:26:45 INFO TaskSetManager: Starting task 114.0 in stage 28.0 (TID 1146, localhost, executor driver, partition 114, ANY, 7743 bytes)
26/06/26 13:26:45 INFO Executor: Running task 114.0 in stage 28.0 (TID 1146)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 113.0 in stage 28.0 (TID 1145) in 42 ms on localhost (executor driver) (111/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 111.0 in stage 28.0 (TID 1143). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 115.0 in stage 28.0 (TID 1147, localhost, executor driver, partition 115, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 115.0 in stage 28.0 (TID 1147)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 111.0 in stage 28.0 (TID 1143) in 66 ms on localhost (executor driver) (112/200)
26/06/26 13:26:46 INFO Executor: Finished task 112.0 in stage 28.0 (TID 1144). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 110.0 in stage 28.0 (TID 1142). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 116.0 in stage 28.0 (TID 1148, localhost, executor driver, partition 116, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 117.0 in stage 28.0 (TID 1149, localhost, executor driver, partition 117, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 112.0 in stage 28.0 (TID 1144) in 70 ms on localhost (executor driver) (113/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 110.0 in stage 28.0 (TID 1142) in 70 ms on localhost (executor driver) (114/200)
26/06/26 13:26:46 INFO Executor: Running task 116.0 in stage 28.0 (TID 1148)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 117.0 in stage 28.0 (TID 1149)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 114.0 in stage 28.0 (TID 1146). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 115.0 in stage 28.0 (TID 1147). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 118.0 in stage 28.0 (TID 1150, localhost, executor driver, partition 118, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 119.0 in stage 28.0 (TID 1151, localhost, executor driver, partition 119, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 118.0 in stage 28.0 (TID 1150)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 114.0 in stage 28.0 (TID 1146) in 79 ms on localhost (executor driver) (115/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 115.0 in stage 28.0 (TID 1147) in 59 ms on localhost (executor driver) (116/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO Executor: Finished task 117.0 in stage 28.0 (TID 1149). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 120.0 in stage 28.0 (TID 1152, localhost, executor driver, partition 120, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 117.0 in stage 28.0 (TID 1149) in 58 ms on localhost (executor driver) (117/200)
26/06/26 13:26:46 INFO Executor: Finished task 116.0 in stage 28.0 (TID 1148). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 121.0 in stage 28.0 (TID 1153, localhost, executor driver, partition 121, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 116.0 in stage 28.0 (TID 1148) in 59 ms on localhost (executor driver) (118/200)
26/06/26 13:26:46 INFO Executor: Running task 121.0 in stage 28.0 (TID 1153)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 119.0 in stage 28.0 (TID 1151)
26/06/26 13:26:46 INFO Executor: Running task 120.0 in stage 28.0 (TID 1152)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 121.0 in stage 28.0 (TID 1153). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 118.0 in stage 28.0 (TID 1150). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 122.0 in stage 28.0 (TID 1154, localhost, executor driver, partition 122, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 123.0 in stage 28.0 (TID 1155, localhost, executor driver, partition 123, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 118.0 in stage 28.0 (TID 1150) in 56 ms on localhost (executor driver) (119/200)
26/06/26 13:26:46 INFO Executor: Running task 122.0 in stage 28.0 (TID 1154)
26/06/26 13:26:46 INFO Executor: Finished task 120.0 in stage 28.0 (TID 1152). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 119.0 in stage 28.0 (TID 1151). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 124.0 in stage 28.0 (TID 1156, localhost, executor driver, partition 124, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 125.0 in stage 28.0 (TID 1157, localhost, executor driver, partition 125, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 124.0 in stage 28.0 (TID 1156)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 119.0 in stage 28.0 (TID 1151) in 59 ms on localhost (executor driver) (120/200)
26/06/26 13:26:46 INFO Executor: Running task 123.0 in stage 28.0 (TID 1155)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 121.0 in stage 28.0 (TID 1153) in 47 ms on localhost (executor driver) (121/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 120.0 in stage 28.0 (TID 1152) in 49 ms on localhost (executor driver) (122/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 125.0 in stage 28.0 (TID 1157)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 122.0 in stage 28.0 (TID 1154). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 126.0 in stage 28.0 (TID 1158, localhost, executor driver, partition 126, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 122.0 in stage 28.0 (TID 1154) in 30 ms on localhost (executor driver) (123/200)
26/06/26 13:26:46 INFO Executor: Running task 126.0 in stage 28.0 (TID 1158)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 124.0 in stage 28.0 (TID 1156). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 127.0 in stage 28.0 (TID 1159, localhost, executor driver, partition 127, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 124.0 in stage 28.0 (TID 1156) in 51 ms on localhost (executor driver) (124/200)
26/06/26 13:26:46 INFO Executor: Running task 127.0 in stage 28.0 (TID 1159)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 125.0 in stage 28.0 (TID 1157). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 128.0 in stage 28.0 (TID 1160, localhost, executor driver, partition 128, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 126.0 in stage 28.0 (TID 1158). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 129.0 in stage 28.0 (TID 1161, localhost, executor driver, partition 129, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 128.0 in stage 28.0 (TID 1160)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 125.0 in stage 28.0 (TID 1157) in 71 ms on localhost (executor driver) (125/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 126.0 in stage 28.0 (TID 1158) in 45 ms on localhost (executor driver) (126/200)
26/06/26 13:26:46 INFO Executor: Finished task 123.0 in stage 28.0 (TID 1155). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 130.0 in stage 28.0 (TID 1162, localhost, executor driver, partition 130, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 130.0 in stage 28.0 (TID 1162)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 127.0 in stage 28.0 (TID 1159). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 131.0 in stage 28.0 (TID 1163, localhost, executor driver, partition 131, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 129.0 in stage 28.0 (TID 1161)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 131.0 in stage 28.0 (TID 1163)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 123.0 in stage 28.0 (TID 1155) in 126 ms on localhost (executor driver) (127/200)
26/06/26 13:26:46 INFO Executor: Finished task 128.0 in stage 28.0 (TID 1160). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Finished task 127.0 in stage 28.0 (TID 1159) in 80 ms on localhost (executor driver) (128/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 132.0 in stage 28.0 (TID 1164, localhost, executor driver, partition 132, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 132.0 in stage 28.0 (TID 1164)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 128.0 in stage 28.0 (TID 1160) in 65 ms on localhost (executor driver) (129/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 130.0 in stage 28.0 (TID 1162). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 133.0 in stage 28.0 (TID 1165, localhost, executor driver, partition 133, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 130.0 in stage 28.0 (TID 1162) in 56 ms on localhost (executor driver) (130/200)
26/06/26 13:26:46 INFO Executor: Finished task 129.0 in stage 28.0 (TID 1161). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 134.0 in stage 28.0 (TID 1166, localhost, executor driver, partition 134, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 133.0 in stage 28.0 (TID 1165)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 129.0 in stage 28.0 (TID 1161) in 104 ms on localhost (executor driver) (131/200)
26/06/26 13:26:46 INFO Executor: Finished task 131.0 in stage 28.0 (TID 1163). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 132.0 in stage 28.0 (TID 1164). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 135.0 in stage 28.0 (TID 1167, localhost, executor driver, partition 135, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 136.0 in stage 28.0 (TID 1168, localhost, executor driver, partition 136, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 132.0 in stage 28.0 (TID 1164) in 42 ms on localhost (executor driver) (132/200)
26/06/26 13:26:46 INFO Executor: Running task 134.0 in stage 28.0 (TID 1166)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 131.0 in stage 28.0 (TID 1163) in 69 ms on localhost (executor driver) (133/200)
26/06/26 13:26:46 INFO Executor: Running task 136.0 in stage 28.0 (TID 1168)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 135.0 in stage 28.0 (TID 1167)
26/06/26 13:26:46 INFO Executor: Finished task 134.0 in stage 28.0 (TID 1166). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 137.0 in stage 28.0 (TID 1169, localhost, executor driver, partition 137, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 137.0 in stage 28.0 (TID 1169)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 134.0 in stage 28.0 (TID 1166) in 41 ms on localhost (executor driver) (134/200)
26/06/26 13:26:46 INFO Executor: Finished task 136.0 in stage 28.0 (TID 1168). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 138.0 in stage 28.0 (TID 1170, localhost, executor driver, partition 138, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 136.0 in stage 28.0 (TID 1168) in 40 ms on localhost (executor driver) (135/200)
26/06/26 13:26:46 INFO Executor: Running task 138.0 in stage 28.0 (TID 1170)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 133.0 in stage 28.0 (TID 1165). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 139.0 in stage 28.0 (TID 1171, localhost, executor driver, partition 139, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 133.0 in stage 28.0 (TID 1165) in 117 ms on localhost (executor driver) (136/200)
26/06/26 13:26:46 INFO Executor: Running task 139.0 in stage 28.0 (TID 1171)
26/06/26 13:26:46 INFO Executor: Finished task 138.0 in stage 28.0 (TID 1170). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 135.0 in stage 28.0 (TID 1167). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 137.0 in stage 28.0 (TID 1169). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 140.0 in stage 28.0 (TID 1172, localhost, executor driver, partition 140, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 141.0 in stage 28.0 (TID 1173, localhost, executor driver, partition 141, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 142.0 in stage 28.0 (TID 1174, localhost, executor driver, partition 142, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 135.0 in stage 28.0 (TID 1167) in 95 ms on localhost (executor driver) (137/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 137.0 in stage 28.0 (TID 1169) in 68 ms on localhost (executor driver) (138/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 138.0 in stage 28.0 (TID 1170) in 57 ms on localhost (executor driver) (139/200)
26/06/26 13:26:46 INFO Executor: Running task 142.0 in stage 28.0 (TID 1174)
26/06/26 13:26:46 INFO Executor: Running task 140.0 in stage 28.0 (TID 1172)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 141.0 in stage 28.0 (TID 1173)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 139.0 in stage 28.0 (TID 1171). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 142.0 in stage 28.0 (TID 1174). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 140.0 in stage 28.0 (TID 1172). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 143.0 in stage 28.0 (TID 1175, localhost, executor driver, partition 143, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 143.0 in stage 28.0 (TID 1175)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 144.0 in stage 28.0 (TID 1176, localhost, executor driver, partition 144, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 145.0 in stage 28.0 (TID 1177, localhost, executor driver, partition 145, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 144.0 in stage 28.0 (TID 1176)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 140.0 in stage 28.0 (TID 1172) in 28 ms on localhost (executor driver) (140/200)
26/06/26 13:26:46 INFO Executor: Running task 145.0 in stage 28.0 (TID 1177)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 139.0 in stage 28.0 (TID 1171) in 39 ms on localhost (executor driver) (141/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 142.0 in stage 28.0 (TID 1174) in 31 ms on localhost (executor driver) (142/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 18 ms
26/06/26 13:26:46 INFO Executor: Finished task 144.0 in stage 28.0 (TID 1176). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 141.0 in stage 28.0 (TID 1173). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 146.0 in stage 28.0 (TID 1178, localhost, executor driver, partition 146, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 147.0 in stage 28.0 (TID 1179, localhost, executor driver, partition 147, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 146.0 in stage 28.0 (TID 1178)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 144.0 in stage 28.0 (TID 1176) in 33 ms on localhost (executor driver) (143/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 141.0 in stage 28.0 (TID 1173) in 60 ms on localhost (executor driver) (144/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 147.0 in stage 28.0 (TID 1179)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 145.0 in stage 28.0 (TID 1177). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 148.0 in stage 28.0 (TID 1180, localhost, executor driver, partition 148, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 148.0 in stage 28.0 (TID 1180)
26/06/26 13:26:46 INFO Executor: Finished task 143.0 in stage 28.0 (TID 1175). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 145.0 in stage 28.0 (TID 1177) in 69 ms on localhost (executor driver) (145/200)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 149.0 in stage 28.0 (TID 1181, localhost, executor driver, partition 149, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 149.0 in stage 28.0 (TID 1181)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 143.0 in stage 28.0 (TID 1175) in 73 ms on localhost (executor driver) (146/200)
26/06/26 13:26:46 INFO Executor: Finished task 147.0 in stage 28.0 (TID 1179). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 146.0 in stage 28.0 (TID 1178). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 150.0 in stage 28.0 (TID 1182, localhost, executor driver, partition 150, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 150.0 in stage 28.0 (TID 1182)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 151.0 in stage 28.0 (TID 1183, localhost, executor driver, partition 151, ANY, 7743 bytes)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 147.0 in stage 28.0 (TID 1179) in 52 ms on localhost (executor driver) (147/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 146.0 in stage 28.0 (TID 1178) in 53 ms on localhost (executor driver) (148/200)
26/06/26 13:26:46 INFO Executor: Finished task 148.0 in stage 28.0 (TID 1180). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Running task 151.0 in stage 28.0 (TID 1183)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 152.0 in stage 28.0 (TID 1184, localhost, executor driver, partition 152, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 148.0 in stage 28.0 (TID 1180) in 48 ms on localhost (executor driver) (149/200)
26/06/26 13:26:46 INFO Executor: Running task 152.0 in stage 28.0 (TID 1184)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 149.0 in stage 28.0 (TID 1181). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 153.0 in stage 28.0 (TID 1185, localhost, executor driver, partition 153, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 149.0 in stage 28.0 (TID 1181) in 49 ms on localhost (executor driver) (150/200)
26/06/26 13:26:46 INFO Executor: Running task 153.0 in stage 28.0 (TID 1185)
26/06/26 13:26:46 INFO Executor: Finished task 151.0 in stage 28.0 (TID 1183). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 154.0 in stage 28.0 (TID 1186, localhost, executor driver, partition 154, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 150.0 in stage 28.0 (TID 1182). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 155.0 in stage 28.0 (TID 1187, localhost, executor driver, partition 155, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 150.0 in stage 28.0 (TID 1182) in 65 ms on localhost (executor driver) (151/200)
26/06/26 13:26:46 INFO Executor: Running task 155.0 in stage 28.0 (TID 1187)
26/06/26 13:26:46 INFO Executor: Running task 154.0 in stage 28.0 (TID 1186)
26/06/26 13:26:46 INFO Executor: Finished task 152.0 in stage 28.0 (TID 1184). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Finished task 151.0 in stage 28.0 (TID 1183) in 67 ms on localhost (executor driver) (152/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 156.0 in stage 28.0 (TID 1188, localhost, executor driver, partition 156, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 152.0 in stage 28.0 (TID 1184) in 73 ms on localhost (executor driver) (153/200)
26/06/26 13:26:46 INFO Executor: Finished task 153.0 in stage 28.0 (TID 1185). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 157.0 in stage 28.0 (TID 1189, localhost, executor driver, partition 157, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 157.0 in stage 28.0 (TID 1189)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 153.0 in stage 28.0 (TID 1185) in 59 ms on localhost (executor driver) (154/200)
26/06/26 13:26:46 INFO Executor: Running task 156.0 in stage 28.0 (TID 1188)
26/06/26 13:26:46 INFO Executor: Finished task 155.0 in stage 28.0 (TID 1187). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 158.0 in stage 28.0 (TID 1190, localhost, executor driver, partition 158, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 155.0 in stage 28.0 (TID 1187) in 53 ms on localhost (executor driver) (155/200)
26/06/26 13:26:46 INFO Executor: Running task 158.0 in stage 28.0 (TID 1190)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO Executor: Finished task 157.0 in stage 28.0 (TID 1189). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 159.0 in stage 28.0 (TID 1191, localhost, executor driver, partition 159, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 159.0 in stage 28.0 (TID 1191)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 157.0 in stage 28.0 (TID 1189) in 47 ms on localhost (executor driver) (156/200)
26/06/26 13:26:46 INFO Executor: Finished task 156.0 in stage 28.0 (TID 1188). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 154.0 in stage 28.0 (TID 1186). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 160.0 in stage 28.0 (TID 1192, localhost, executor driver, partition 160, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 161.0 in stage 28.0 (TID 1193, localhost, executor driver, partition 161, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 156.0 in stage 28.0 (TID 1188) in 82 ms on localhost (executor driver) (157/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 154.0 in stage 28.0 (TID 1186) in 109 ms on localhost (executor driver) (158/200)
26/06/26 13:26:46 INFO Executor: Running task 160.0 in stage 28.0 (TID 1192)
26/06/26 13:26:46 INFO Executor: Running task 161.0 in stage 28.0 (TID 1193)
26/06/26 13:26:46 INFO Executor: Finished task 158.0 in stage 28.0 (TID 1190). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 162.0 in stage 28.0 (TID 1194, localhost, executor driver, partition 162, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 162.0 in stage 28.0 (TID 1194)
26/06/26 13:26:46 INFO Executor: Finished task 159.0 in stage 28.0 (TID 1191). 3292 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Finished task 158.0 in stage 28.0 (TID 1190) in 70 ms on localhost (executor driver) (159/200)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 163.0 in stage 28.0 (TID 1195, localhost, executor driver, partition 163, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 163.0 in stage 28.0 (TID 1195)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 159.0 in stage 28.0 (TID 1191) in 60 ms on localhost (executor driver) (160/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 163.0 in stage 28.0 (TID 1195). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 164.0 in stage 28.0 (TID 1196, localhost, executor driver, partition 164, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 160.0 in stage 28.0 (TID 1192). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Finished task 163.0 in stage 28.0 (TID 1195) in 58 ms on localhost (executor driver) (161/200)
26/06/26 13:26:46 INFO Executor: Running task 164.0 in stage 28.0 (TID 1196)
26/06/26 13:26:46 INFO Executor: Finished task 161.0 in stage 28.0 (TID 1193). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 165.0 in stage 28.0 (TID 1197, localhost, executor driver, partition 165, ANY, 7743 bytes)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 166.0 in stage 28.0 (TID 1198, localhost, executor driver, partition 166, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 165.0 in stage 28.0 (TID 1197)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 160.0 in stage 28.0 (TID 1192) in 88 ms on localhost (executor driver) (162/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 161.0 in stage 28.0 (TID 1193) in 89 ms on localhost (executor driver) (163/200)
26/06/26 13:26:46 INFO Executor: Running task 166.0 in stage 28.0 (TID 1198)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 162.0 in stage 28.0 (TID 1194). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 167.0 in stage 28.0 (TID 1199, localhost, executor driver, partition 167, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 162.0 in stage 28.0 (TID 1194) in 92 ms on localhost (executor driver) (164/200)
26/06/26 13:26:46 INFO Executor: Finished task 164.0 in stage 28.0 (TID 1196). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 168.0 in stage 28.0 (TID 1200, localhost, executor driver, partition 168, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 165.0 in stage 28.0 (TID 1197). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Finished task 164.0 in stage 28.0 (TID 1196) in 39 ms on localhost (executor driver) (165/200)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 169.0 in stage 28.0 (TID 1201, localhost, executor driver, partition 169, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 169.0 in stage 28.0 (TID 1201)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 165.0 in stage 28.0 (TID 1197) in 40 ms on localhost (executor driver) (166/200)
26/06/26 13:26:46 INFO Executor: Running task 168.0 in stage 28.0 (TID 1200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 166.0 in stage 28.0 (TID 1198). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Running task 167.0 in stage 28.0 (TID 1199)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 170.0 in stage 28.0 (TID 1202, localhost, executor driver, partition 170, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 166.0 in stage 28.0 (TID 1198) in 62 ms on localhost (executor driver) (167/200)
26/06/26 13:26:46 INFO Executor: Running task 170.0 in stage 28.0 (TID 1202)
26/06/26 13:26:46 INFO Executor: Finished task 168.0 in stage 28.0 (TID 1200). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 171.0 in stage 28.0 (TID 1203, localhost, executor driver, partition 171, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 168.0 in stage 28.0 (TID 1200) in 40 ms on localhost (executor driver) (168/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 169.0 in stage 28.0 (TID 1201). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 167.0 in stage 28.0 (TID 1199). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 172.0 in stage 28.0 (TID 1204, localhost, executor driver, partition 172, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 172.0 in stage 28.0 (TID 1204)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 169.0 in stage 28.0 (TID 1201) in 50 ms on localhost (executor driver) (169/200)
26/06/26 13:26:46 INFO Executor: Running task 171.0 in stage 28.0 (TID 1203)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 173.0 in stage 28.0 (TID 1205, localhost, executor driver, partition 173, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 170.0 in stage 28.0 (TID 1202). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Running task 173.0 in stage 28.0 (TID 1205)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 174.0 in stage 28.0 (TID 1206, localhost, executor driver, partition 174, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 174.0 in stage 28.0 (TID 1206)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 167.0 in stage 28.0 (TID 1199) in 90 ms on localhost (executor driver) (170/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 170.0 in stage 28.0 (TID 1202) in 58 ms on localhost (executor driver) (171/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 172.0 in stage 28.0 (TID 1204). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 175.0 in stage 28.0 (TID 1207, localhost, executor driver, partition 175, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 172.0 in stage 28.0 (TID 1204) in 54 ms on localhost (executor driver) (172/200)
26/06/26 13:26:46 INFO Executor: Running task 175.0 in stage 28.0 (TID 1207)
26/06/26 13:26:46 INFO Executor: Finished task 171.0 in stage 28.0 (TID 1203). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 176.0 in stage 28.0 (TID 1208, localhost, executor driver, partition 176, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 171.0 in stage 28.0 (TID 1203) in 68 ms on localhost (executor driver) (173/200)
26/06/26 13:26:46 INFO Executor: Running task 176.0 in stage 28.0 (TID 1208)
26/06/26 13:26:46 INFO Executor: Finished task 173.0 in stage 28.0 (TID 1205). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 177.0 in stage 28.0 (TID 1209, localhost, executor driver, partition 177, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 174.0 in stage 28.0 (TID 1206). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 178.0 in stage 28.0 (TID 1210, localhost, executor driver, partition 178, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 178.0 in stage 28.0 (TID 1210)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 173.0 in stage 28.0 (TID 1205) in 37 ms on localhost (executor driver) (174/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 174.0 in stage 28.0 (TID 1206) in 35 ms on localhost (executor driver) (175/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Running task 177.0 in stage 28.0 (TID 1209)
26/06/26 13:26:46 INFO Executor: Finished task 176.0 in stage 28.0 (TID 1208). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 179.0 in stage 28.0 (TID 1211, localhost, executor driver, partition 179, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 179.0 in stage 28.0 (TID 1211)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 176.0 in stage 28.0 (TID 1208) in 22 ms on localhost (executor driver) (176/200)
26/06/26 13:26:46 INFO Executor: Finished task 175.0 in stage 28.0 (TID 1207). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 180.0 in stage 28.0 (TID 1212, localhost, executor driver, partition 180, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 175.0 in stage 28.0 (TID 1207) in 29 ms on localhost (executor driver) (177/200)
26/06/26 13:26:46 INFO Executor: Finished task 178.0 in stage 28.0 (TID 1210). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 181.0 in stage 28.0 (TID 1213, localhost, executor driver, partition 181, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 177.0 in stage 28.0 (TID 1209). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 182.0 in stage 28.0 (TID 1214, localhost, executor driver, partition 182, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 182.0 in stage 28.0 (TID 1214)
26/06/26 13:26:46 INFO Executor: Running task 180.0 in stage 28.0 (TID 1212)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO Executor: Finished task 179.0 in stage 28.0 (TID 1211). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 178.0 in stage 28.0 (TID 1210) in 51 ms on localhost (executor driver) (178/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 177.0 in stage 28.0 (TID 1209) in 53 ms on localhost (executor driver) (179/200)
26/06/26 13:26:46 INFO Executor: Running task 181.0 in stage 28.0 (TID 1213)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Starting task 183.0 in stage 28.0 (TID 1215, localhost, executor driver, partition 183, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 183.0 in stage 28.0 (TID 1215)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 179.0 in stage 28.0 (TID 1211) in 48 ms on localhost (executor driver) (180/200)
26/06/26 13:26:46 INFO Executor: Finished task 182.0 in stage 28.0 (TID 1214). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO Executor: Finished task 180.0 in stage 28.0 (TID 1212). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 184.0 in stage 28.0 (TID 1216, localhost, executor driver, partition 184, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Starting task 185.0 in stage 28.0 (TID 1217, localhost, executor driver, partition 185, ANY, 7743 bytes)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 182.0 in stage 28.0 (TID 1214) in 33 ms on localhost (executor driver) (181/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 180.0 in stage 28.0 (TID 1212) in 47 ms on localhost (executor driver) (182/200)
26/06/26 13:26:46 INFO Executor: Running task 185.0 in stage 28.0 (TID 1217)
26/06/26 13:26:46 INFO Executor: Running task 184.0 in stage 28.0 (TID 1216)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO Executor: Finished task 181.0 in stage 28.0 (TID 1213). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 186.0 in stage 28.0 (TID 1218, localhost, executor driver, partition 186, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Finished task 185.0 in stage 28.0 (TID 1217). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 187.0 in stage 28.0 (TID 1219, localhost, executor driver, partition 187, ANY, 7743 bytes)
26/06/26 13:26:46 INFO Executor: Running task 187.0 in stage 28.0 (TID 1219)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 181.0 in stage 28.0 (TID 1213) in 62 ms on localhost (executor driver) (183/200)
26/06/26 13:26:46 INFO TaskSetManager: Finished task 185.0 in stage 28.0 (TID 1217) in 29 ms on localhost (executor driver) (184/200)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:46 INFO Executor: Running task 186.0 in stage 28.0 (TID 1218)
26/06/26 13:26:46 INFO Executor: Finished task 184.0 in stage 28.0 (TID 1216). 3249 bytes result sent to driver
26/06/26 13:26:46 INFO TaskSetManager: Starting task 188.0 in stage 28.0 (TID 1220, localhost, executor driver, partition 188, ANY, 7743 bytes)
26/06/26 13:26:46 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:46 INFO TaskSetManager: Finished task 184.0 in stage 28.0 (TID 1216) in 33 ms on localhost (executor driver) (185/200)
26/06/26 13:26:47 INFO Executor: Running task 188.0 in stage 28.0 (TID 1220)
26/06/26 13:26:47 INFO Executor: Finished task 183.0 in stage 28.0 (TID 1215). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO TaskSetManager: Starting task 189.0 in stage 28.0 (TID 1221, localhost, executor driver, partition 189, ANY, 7743 bytes)
26/06/26 13:26:47 INFO Executor: Running task 189.0 in stage 28.0 (TID 1221)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 183.0 in stage 28.0 (TID 1215) in 66 ms on localhost (executor driver) (186/200)
26/06/26 13:26:47 INFO Executor: Finished task 187.0 in stage 28.0 (TID 1219). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 190.0 in stage 28.0 (TID 1222, localhost, executor driver, partition 190, ANY, 7743 bytes)
26/06/26 13:26:47 INFO Executor: Running task 190.0 in stage 28.0 (TID 1222)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO TaskSetManager: Finished task 187.0 in stage 28.0 (TID 1219) in 40 ms on localhost (executor driver) (187/200)
26/06/26 13:26:47 INFO Executor: Finished task 188.0 in stage 28.0 (TID 1220). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 191.0 in stage 28.0 (TID 1223, localhost, executor driver, partition 191, ANY, 7743 bytes)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 188.0 in stage 28.0 (TID 1220) in 64 ms on localhost (executor driver) (188/200)
26/06/26 13:26:47 INFO Executor: Finished task 190.0 in stage 28.0 (TID 1222). 3292 bytes result sent to driver
26/06/26 13:26:47 INFO Executor: Finished task 189.0 in stage 28.0 (TID 1221). 3292 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 192.0 in stage 28.0 (TID 1224, localhost, executor driver, partition 192, ANY, 7743 bytes)
26/06/26 13:26:47 INFO TaskSetManager: Starting task 193.0 in stage 28.0 (TID 1225, localhost, executor driver, partition 193, ANY, 7743 bytes)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 190.0 in stage 28.0 (TID 1222) in 41 ms on localhost (executor driver) (189/200)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 189.0 in stage 28.0 (TID 1221) in 51 ms on localhost (executor driver) (190/200)
26/06/26 13:26:47 INFO Executor: Finished task 186.0 in stage 28.0 (TID 1218). 3292 bytes result sent to driver
26/06/26 13:26:47 INFO Executor: Running task 192.0 in stage 28.0 (TID 1224)
26/06/26 13:26:47 INFO TaskSetManager: Starting task 194.0 in stage 28.0 (TID 1226, localhost, executor driver, partition 194, ANY, 7743 bytes)
26/06/26 13:26:47 INFO Executor: Running task 194.0 in stage 28.0 (TID 1226)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO TaskSetManager: Finished task 186.0 in stage 28.0 (TID 1218) in 85 ms on localhost (executor driver) (191/200)
26/06/26 13:26:47 INFO Executor: Running task 191.0 in stage 28.0 (TID 1223)
26/06/26 13:26:47 INFO Executor: Running task 193.0 in stage 28.0 (TID 1225)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO Executor: Finished task 194.0 in stage 28.0 (TID 1226). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 195.0 in stage 28.0 (TID 1227, localhost, executor driver, partition 195, ANY, 7743 bytes)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 194.0 in stage 28.0 (TID 1226) in 19 ms on localhost (executor driver) (192/200)
26/06/26 13:26:47 INFO Executor: Running task 195.0 in stage 28.0 (TID 1227)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO Executor: Finished task 192.0 in stage 28.0 (TID 1224). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 196.0 in stage 28.0 (TID 1228, localhost, executor driver, partition 196, ANY, 7743 bytes)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 19 ms
26/06/26 13:26:47 INFO TaskSetManager: Finished task 192.0 in stage 28.0 (TID 1224) in 34 ms on localhost (executor driver) (193/200)
26/06/26 13:26:47 INFO Executor: Finished task 191.0 in stage 28.0 (TID 1223). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO Executor: Running task 196.0 in stage 28.0 (TID 1228)
26/06/26 13:26:47 INFO Executor: Finished task 195.0 in stage 28.0 (TID 1227). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 197.0 in stage 28.0 (TID 1229, localhost, executor driver, partition 197, ANY, 7743 bytes)
26/06/26 13:26:47 INFO TaskSetManager: Starting task 198.0 in stage 28.0 (TID 1230, localhost, executor driver, partition 198, ANY, 7743 bytes)
26/06/26 13:26:47 INFO Executor: Running task 197.0 in stage 28.0 (TID 1229)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 1 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:47 INFO TaskSetManager: Finished task 191.0 in stage 28.0 (TID 1223) in 51 ms on localhost (executor driver) (194/200)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 195.0 in stage 28.0 (TID 1227) in 28 ms on localhost (executor driver) (195/200)
26/06/26 13:26:47 INFO Executor: Finished task 193.0 in stage 28.0 (TID 1225). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Starting task 199.0 in stage 28.0 (TID 1231, localhost, executor driver, partition 199, ANY, 7743 bytes)
26/06/26 13:26:47 INFO Executor: Running task 199.0 in stage 28.0 (TID 1231)
26/06/26 13:26:47 INFO Executor: Running task 198.0 in stage 28.0 (TID 1230)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 193.0 in stage 28.0 (TID 1225) in 60 ms on localhost (executor driver) (196/200)
26/06/26 13:26:47 INFO Executor: Finished task 196.0 in stage 28.0 (TID 1228). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO Executor: Finished task 197.0 in stage 28.0 (TID 1229). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
26/06/26 13:26:47 INFO TaskSetManager: Finished task 196.0 in stage 28.0 (TID 1228) in 31 ms on localhost (executor driver) (197/200)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 197.0 in stage 28.0 (TID 1229) in 25 ms on localhost (executor driver) (198/200)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
26/06/26 13:26:47 INFO Executor: Finished task 198.0 in stage 28.0 (TID 1230). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO Executor: Finished task 199.0 in stage 28.0 (TID 1231). 3249 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Finished task 198.0 in stage 28.0 (TID 1230) in 45 ms on localhost (executor driver) (199/200)
26/06/26 13:26:47 INFO TaskSetManager: Finished task 199.0 in stage 28.0 (TID 1231) in 26 ms on localhost (executor driver) (200/200)
26/06/26 13:26:47 INFO TaskSchedulerImpl: Removed TaskSet 28.0, whose tasks have all completed, from pool 
26/06/26 13:26:47 INFO DAGScheduler: ShuffleMapStage 28 (showString at NativeMethodAccessorImpl.java:0) finished in 3.348 s
26/06/26 13:26:47 INFO DAGScheduler: looking for newly runnable stages
26/06/26 13:26:47 INFO DAGScheduler: running: Set()
26/06/26 13:26:47 INFO DAGScheduler: waiting: Set(ResultStage 29)
26/06/26 13:26:47 INFO DAGScheduler: failed: Set()
26/06/26 13:26:47 INFO DAGScheduler: Submitting ResultStage 29 (MapPartitionsRDD[113] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
26/06/26 13:26:47 INFO MemoryStore: Block broadcast_32 stored as values in memory (estimated size 22.3 KB, free 365.0 MB)
26/06/26 13:26:47 INFO MemoryStore: Block broadcast_32_piece0 stored as bytes in memory (estimated size 7.3 KB, free 365.0 MB)
26/06/26 13:26:47 INFO BlockManagerInfo: Added broadcast_32_piece0 in memory on sandbox-hdp.hortonworks.com:33329 (size: 7.3 KB, free: 366.2 MB)
26/06/26 13:26:47 INFO SparkContext: Created broadcast 32 from broadcast at DAGScheduler.scala:1039
26/06/26 13:26:47 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 29 (MapPartitionsRDD[113] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
26/06/26 13:26:47 INFO TaskSchedulerImpl: Adding task set 29.0 with 1 tasks
26/06/26 13:26:47 INFO TaskSetManager: Starting task 0.0 in stage 29.0 (TID 1232, localhost, executor driver, partition 0, ANY, 7754 bytes)
26/06/26 13:26:47 INFO Executor: Running task 0.0 in stage 29.0 (TID 1232)
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Getting 200 non-empty blocks out of 200 blocks
26/06/26 13:26:47 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 2 ms
26/06/26 13:26:47 INFO Executor: Finished task 0.0 in stage 29.0 (TID 1232). 1702 bytes result sent to driver
26/06/26 13:26:47 INFO TaskSetManager: Finished task 0.0 in stage 29.0 (TID 1232) in 39 ms on localhost (executor driver) (1/1)
26/06/26 13:26:47 INFO TaskSchedulerImpl: Removed TaskSet 29.0, whose tasks have all completed, from pool 
26/06/26 13:26:47 INFO DAGScheduler: ResultStage 29 (showString at NativeMethodAccessorImpl.java:0) finished in 0.050 s
26/06/26 13:26:47 INFO DAGScheduler: Job 14 finished: showString at NativeMethodAccessorImpl.java:0, took 3.990564 s
+--------+-----------+------------+------------------+--------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+
|movie_id|movie_title|release_date|video_release_date|imdb_url|unknown|action|adventure|animation|children|comedy|crime|documentary|drama|fantasy|film_noir|horror|musical|mystery|romance|sci_fi|thriller|war|western|
+--------+-----------+------------+------------------+--------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+
|       0|          0|           0|                 0|       0|      0|     0|        0|        0|       0|     0|    0|          0|    0|      0|        0|     0|      0|      0|      0|     0|       0|  0|      0|
+--------+-----------+------------+------------------+--------+-------+------+---------+---------+--------+------+-----+-----------+-----+-------+---------+------+-------+-------+-------+------+--------+---+-------+


Spark SQL Views Created
26/06/26 13:26:48 INFO CodeGenerator: Code generated in 8.378812 ms
26/06/26 13:26:48 INFO CodeGenerator: Code generated in 5.607847 ms
+--------+---------+-----------+
|database|tableName|isTemporary|
+--------+---------+-----------+
|        |   movies|       true|
|        |  ratings|       true|
|        |    users|       true|
+--------+---------+-----------+


Module 1 Completed Successfully
26/06/26 13:26:48 INFO AbstractConnector: Stopped Spark@775dd60d{HTTP/1.1,[http/1.1]}{0.0.0.0:4040}
26/06/26 13:26:48 INFO SparkUI: Stopped Spark web UI at http://sandbox-hdp.hortonworks.com:4040
26/06/26 13:26:49 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
26/06/26 13:26:50 INFO MemoryStore: MemoryStore cleared
26/06/26 13:26:50 INFO BlockManager: BlockManager stopped
26/06/26 13:26:50 INFO BlockManagerMaster: BlockManagerMaster stopped
26/06/26 13:26:50 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
26/06/26 13:26:50 INFO SparkContext: Successfully stopped SparkContext
26/06/26 13:26:51 INFO ShutdownHookManager: Shutdown hook called
26/06/26 13:26:51 INFO ShutdownHookManager: Deleting directory /tmp/spark-622bed24-d735-468b-b7b9-750ec55e59f4/pyspark-d3e48dce-0b4f-4e8d-94b9-5a997a0224f3
26/06/26 13:26:51 INFO ShutdownHookManager: Deleting directory /tmp/spark-1807f1f5-9ce4-4205-9412-42b487eedb64
26/06/26 13:26:51 INFO ShutdownHookManager: Deleting directory /tmp/spark-622bed24-d735-468b-b7b9-750ec55e59f4

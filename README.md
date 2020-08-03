# GD5-11 模块介绍
###便携式启动
1 · 第一次执行需要开启 `MYSQL`、`SSDB`服务器

**运行ssdb：**

    cd /usr/local/ssdb
    ./ssdb-server -d ./ssdb.conf -s restart//重启
    # 启动主库, 此命令会阻塞住命令行
    ./ssdb-server ssdb.conf
    # 或者启动为后台进程(不阻塞命令行)
    ./ssdb-server -d ssdb.conf
    # 停止 ssdb-server
    ./ssdb-server ssdb.conf -s stop
    # 对于旧版本
    
    kill `cat ./var/ssdb.pid`
    # 重启
    ./ssdb-server ssdb.conf -s restart

----

2 · 开启`Proxy`服务器，目录在`proxy_pool-master/cli/proxyPool.py`

    **执行第一条命令**
    **# # 启动调度程序**
    python proxyPool.py schedule（中端运行，退出中断）
    nohup python proxyPool.py schedule & （nohup运行，退出不中断）本次运行PID：13788
    
    **# # 启动webApi服务**
    python proxyPool.py webserver （中端运行，退出中断）
    nohup python proxyPool.py webserver & （nohup运行，退出不中断）本次运行PID：13800
    
    **# # 如选择的不中断运行会在目录下生成"nohup.out"文件，用于监视进程**
    查看 nohup.out的日志 最后几行的日志
    tail -fn 50 nohup.out
    
3 · 运行项目主程序
在`GD5-11`根目录下 运行 `Timed_task.py`

    **执行命令**
    **## 启动主程序**
    python Timed_task.py （或者以 nohup 运行）nohup python Timed_task.py &
    
----
    
###模块介绍
1 · **`requestGD511.py`**:蜘蛛模块，负责爬取指定的网页，传入参数"page"设定爬行几页。

2 · **`REGD.py`**: 正则清洗模块，用于对蜘蛛爬取的网页进行正则数据清洗，提取出需要的数据。

3 · **`conmitdb.py`**：连接数据库模块

4 · **`Write_Excel.py`**： 将最后需要的数据写入EXCEL

5 · **`Send_mail.py`**： 邮件报警模块

6 · **`get_dwanum.py`**： 获取最新一期抽奖号

7 · **`Get_Big_Data.py`**： 处理抽取数据的模块

8 · **`proxy_pool-master`**： 代理池主程序

----

### **ModuLe**目录
目录存放所有计算公式 `Run_Algebra.py` 为在用的计算模块主程序

----

### STATIC 目录
`requestGD511.txt`： 此文件为蜘蛛爬取暂存文件

----

### Excel目录
`excel`: 此目录存放着计算公式所写入的文件
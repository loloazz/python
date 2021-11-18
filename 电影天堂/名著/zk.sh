#!/bin/bash 
 #该脚本是用来对zookeeper脚本进行启动/关闭/查看状态
if [ $# -lt 1 ] 
then 
    echo "没有参数输入。。。。。。。" 
    exit ; 
fi 
 
zkpath='/opt/share/zookeeper-3.4.10'  #配置zookeeper的安装目录
hostlist="master node1 node2" # 配置主机名队列
 
case $1 in 
"start") 
        echo " =================== 启动 zk 集群 ===================" 
		for  host in $hostlist
		do
			ssh $host $zkpath'/bin/zkServer.sh start' 
			echo $host "zookeeper已经启动" 
		done
		
;; 
"stop") 
        echo " ===================关闭 zk 集群 ===================" 
		for  host in $hostlist
		do
			ssh $host $zkpath'/bin/zkServer.sh stop' 
			echo $host "zookeeper已经关闭" 
		done
        
;; 

"status") 
        echo " =================== zk 集群状态 ===================" 
		for  host in $hostlist
		do
			ssh $host $zkpath'/bin/zkServer.sh status' 
		done
        
;; 




*) 
    echo "参数为 [start|stop|status]" 
;; 
esac 
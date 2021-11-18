
#!/bin/bash
#该脚本是用来显示集群的所有java进程状态


# 1. 安装chrony

echo "正在安装chrony服务"
echo
	yum install chrony

# 2. 启用
echo "正在启动chrony服务"
	systemctl start chronyd
	systemctl enable chronyd

# 3. 设置亚洲时区

echo "正在设置亚洲时区"
	timedatectl set-timezone Asia/Shanghai
echo

#4. 启用NTP同步

echo "启动NTP同步"
	timedatectl set-ntp yes
echo "当前日期为：检查是否同步成功"
#5. 通过date来查询时间是否进行同步
	date
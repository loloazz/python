#！/bin/bash
#一键安装mysql


# 卸载原来的mysql，或者清除mysql的数据。
set -e

if [ $# -lt 1 ] 
then 
    echo "没有参数输入。。。。。。。" 
    exit ; 
fi 
 
 case $1 in 
"remove") 
 
 
		rpm -qa |grep -i mysql
		yum remove mysql-community mysql-community-server mysql-community-libs mysql-community-common
		rm -rf | find / -name mysql 
		echo "清除mysql成功！"
;;

"install")  
		echo 
		echo "开始安装mysql"
		wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
		yum -y install mysql57-community-release-el7-10.noarch.rpm
		yum -y install mysql-community-server

		echo "正在安装mysql服务"
		systemctl enable mysqld.service
		systemctl start mysqld.service
		systemctl status mysqld.service
		echo "mysql安装成功"

		echo "正在关闭yum的自动更新"
		yum -y remove mysql57-community-release-el7-10.noarch

		echo
		echo "你的临时密码为" 
		grep "password" /var/log/mysqld.log
	;;
	
	*) 
    echo "参数为 [install|remove]"
esac 	
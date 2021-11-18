
import pymysql
import requests
import time
import hashlib
import json
from get_user_agent import getheaders

from request_SQL import request_html_sql


# 提取订单
"""
    orderId:提取订单号
    secret:用户密钥
    num:提取IP个数
    pid:省份
    cid:城市
    type：请求类型，1=http/https,2=socks5
    unbindTime:使用时长，秒/s为单位
    noDuplicate:去重，0=不去重，1=去重
    lineSeparator:分隔符
    singleIp:切换,0=切换，1=不切换
"""

orderId = "O21061420521619352922"
secret = "a0637b6b98694456a0a321da29cbfe0f"
num = "20"
pid = "-1"
cid = ""
type = "1"
unbindTime = "60"
noDuplicate = "0"
lineSeparator = "0"
singleIp = "0"
time = str(int(time.time())) #时间戳

# 计算sign
txt = "orderId=" + orderId + "&" + "secret=" + secret + "&" + "time=" + time
sign = hashlib.md5(txt.encode()).hexdigest()
# 访问URL获取IP
url = "http://api.hailiangip.com:8422/api/getIp?type=1" + "&num=" + num + "&pid=" + pid + "&unbindTime=" + unbindTime + "&cid=" + cid +  "&orderId=" + orderId + "&time=" + time + "&sign=" + sign + "&dataType=0" + "&lineSeparator=" + lineSeparator + "&noDuplicate=" + noDuplicate + "&singleIp=" + singleIp
my_response = requests.get(url).content
js_res = json.loads(my_response)




# 连接database
conn = pymysql.connect(host="hadoop100", port=3306, user='root', password='123456', database='蜀山区房源租房信息',charset='utf8')
# 得到一个可以执行SQL语句并且将结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)




urls = []
for i in range(69, 70):
    str = 'https://nj.58.com/pukouqu/chuzu/pn' + format(
        i)
    urls.append(str)



header= {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': getheaders()
        }
for dic ,url in zip( js_res["data"],urls):
    ip = dic["ip"]
    port = dic["port"]

    proxyUrl = "http://" + ip + ":" + format(port)
    proxy = {'http': proxyUrl,"https": proxyUrl}

    sqls = request_html_sql(url,headers=header,proxies=proxy)
    print(f"============正在爬取第{url}数据=============")



    for sql in sqls:
        cursor.execute(sql)
        print('插入成功数据库成功！\n' + sql + '\n')
        cursor.connection.commit()
# 关闭数据库连接
conn.close()















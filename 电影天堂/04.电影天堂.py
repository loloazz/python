import requests
import re
import csv

rootUrl = "https://www.dy2018.com"
# resp = requests.get(rootUrl, verify=False)  # verify=False 跳过协议中的安全验证
headers = {
 "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
               "AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/91.0.4472.124 Safari/537.36 "
               "OPR/77.0.4054.203"
}
resp = requests.get(rootUrl,headers=headers)
resp.encoding = 'gbk'
# print(resp.text)

obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<childUrl>.*?)'", re.S)
obj3 = re.compile(r'<div class="title_all"><h1>(?P<Name>.*?)'
                  r'</h1></div>.*?<td style="WORD-WRAP: break'
                  r'-word" bgcolor="#fdfddf"><a href="(?P<bt>.*?)">magnet', re.S)

result1 = obj1.finditer(resp.text)
childUrl_list = []

f = open("dytt89.csv", "w", encoding="utf-8")
for it in result1:
    ul = it.group('ul').strip()
    result2 = obj2.finditer(ul)
    for itt in result2:
        # childUrl = itt.group('childUrl')
        # print(itt.group('childUrl'))
        childUrl = rootUrl + itt.group('childUrl')
        # childUrl_list = (childUrl)
        childUrl_list.append(childUrl)
        # print(childUrl_list)
for childUrl in childUrl_list:
    child_resp = requests.get(childUrl, headers=headers)
    child_resp.encoding = 'gbk'
    result3 = obj3.finditer(child_resp.text)
    # print(child_resp.text)

    for ittt in result3:
         data= ittt.group('Name')+","+ittt.group('bt')+"\n"
         f.write(data)
         f.flush()
         print(data)

f.close()
    # print("ok")


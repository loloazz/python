import requests
from lxml import etree


def request_html_sql(url,headers,proxies):

    pagetext=requests.get(url,headers=headers,proxies=proxies)
    print("status Code : " ,pagetext.status_code)

    parse=etree.HTML(pagetext.text)
    titles=parse.xpath('/html/body/div[6]/div[2]/ul//div[2]/h2/a/text()')

    #  面积大小，房间大小
    area_roomtypes=parse.xpath("/html/body/div[6]/div[2]/ul//div[2]/p[1]/text()[1]")

    addresses1 =parse.xpath("/html/body/div[6]/div[2]/ul//div[2]/p[2]/a[1]//text()")
    addresses2 = parse.xpath("/html/body/div[6]/div[2]/ul//div[2]/p[2]/a[2]//text()")
    addresses=[]
    for x,y in zip(addresses1,addresses2):
          addresses.append(x+' '+y)
    prices_parse= parse.xpath("/html/body/div[6]/div[2]/ul//div[3]/div[2]/b/text()")
    prices = []
    for i in prices_parse:
        prices.append(i)

    urls =parse.xpath("/html/body/div[6]/div[2]/ul//div[2]/h2//@href")
    #  转成sql
    sqls=[]
    for title,area_roomtype,address,price,url in zip(titles,area_roomtypes,addresses,prices,urls):
        sql="insert into  南京浦口区租房信息  values ('%s','%s','%s','%s','%s')" %(title,area_roomtype,address,price,url)
        sqls.append(sql)
        print(sql+'转换成功')
    return  sqls

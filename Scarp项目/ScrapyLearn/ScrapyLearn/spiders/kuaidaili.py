import scrapy

# 创建爬虫类 并继承自scrapy.Spider   爬虫的基类

class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'   # 爬虫名字  不能重名
    allowed_domains = ['kuaidaili.com'] #允许采集的域名
    start_urls = [f'https://www.kuaidaili.com/free/']#开始第一次采集的网站

    # 解析响应数据，提取网址  ，或者数据
    def parse(self, response):    #response 就是得到的网页源码直接用就行
        selectors= response.xpath("//tr")  #得到所有的tr标签的值
        for selector in selectors :
            ip=selector.xpath('./td[1]/text()')  #具体解析td标签得到ip
            port=selector.xpath("./td[2]/text()")#具体解析td标签得到port
            print(ip.get(),port.get())

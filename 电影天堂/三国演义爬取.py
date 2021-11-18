import requests
from bs4 import BeautifulSoup
import os
import time
if __name__ == '__main__':
    if not  os.path.exists('/名著'):
        os.mkdir('/名著')
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    headers={
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
    }
    page_text = requests.get(url=url, headers=headers,timeout=(3,7)).text
    page_title =BeautifulSoup(page_text,"lxml")
    li_list=page_title.select('.book-mulu > ul > li ')
    fp= open('名著/sangou.txt', 'w', encoding='utf-8')
    for title in li_list:
        detail_titile=title.text
        url = 'https://www.shicimingju.com'
        detail_url = url + title.a['href']
        detail_txt=requests.get(url=detail_url,headers=headers,timeout=(3,7)).text
        time.sleep(1)
        detail_text=BeautifulSoup(detail_txt,'lxml')
        detail_finalltext=detail_text.find('div',class_="chapter_content").text
        fp.write(detail_titile+':'+detail_finalltext+'\n')
        print(detail_titile+'     '+'下载成功！')




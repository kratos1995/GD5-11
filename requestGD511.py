## -*- coding: utf-8 -*-
import requests
import os
import random
import REGD
import conmitdb
import re
import time
import platform

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def page_url(page):
    pages = page
    for index in range(pages):
        index =1 +index
        proxy = get_proxy().get("proxy")
        url = 'http://www.caipiaow.com/index.php?m=kaijiang&a=index&cz=gd11x5&type=11x5&p=%s' %index
        headers = {
            'Host': 'www.caipiaow.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/67.0.3396.99 '
                          'Safari/537.36',
            'proxies':"http://{}".format(proxy),
            'Referer': "http://www.caipiaow.com",
        }
        list = []
        html = requests.get(url, headers=headers)
        html = html.text
        # if __name__ == '__main__':
        sys = platform.system()
        if sys == "Windows":
            print("OS is Windows")
            path = '\GD5-11\static\\requestGD511.txt'
            with open('\GD5-11\static\\requestGD511.txt', 'wb') as f:
                f.truncate()
                f.write(html.encode('utf8'))
                f.close()
        elif sys == "Linux":
            print("OS is Linux!!!")
            path = '/GD5-11/static/requestGD511.txt'
            with open('\GD5-11\static\\requestGD511.txt', 'wb') as f:
                f.truncate()
                f.write(html.encode('utf8'))
                f.close()
        else:
            print("==============无法识别的操作系统================")
            pass
        # path = '\GD5-11\static\\requestGD511.txt'
        # with open('\GD5-11\static\\requestGD511.txt', 'wb') as f:
        #     f.truncate()
        #     f.write(html.encode('utf8'))
        #     f.close()
        regds = REGD.regd()
        regds
        print(url) # 输出当前爬取网址
        time.sleep(3) # 爬虫爬取的间隔时间
        if index >=page:
            print('执行完毕')
            break

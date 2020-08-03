## -*- coding: utf-8 -*-
import requests
import os
import random
import REGD
import conmitdb
import re
import time
import platform
import Send_mail

# 获取代理
def get_proxy():
    try:
        proxys = requests.get("http://127.0.0.1:5010/get/").json()
    except (requests.exceptions.ConnectionError, requests.exceptions.ConnectionError, requests.exceptions.BaseHTTPError) as e:
        # 异常执行邮件警报
        Send_mail.send_mail(subject="警报：‘requestGD511’ 模块错误，Spider 执行失败！本次爬取不成功",
                            content_text=e,attachments=None)
    return proxys

# print(get_proxy())

# 爬取函数，传入参数让函数爬行N次
def page_url(page):
    pages = page # 声明实例化变量 PAGE
    for index in range(pages): # 循环迭代 PAGES，如果需要爬取10页则从1-10开始迭代
        index =1 +index
        proxy = get_proxy().get("proxy") # 声明实例化代理
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
        regds = REGD.regd() # 声明实例化清洗模块
        regds
        print(url) # 输出当前爬取网址
        time.sleep(3) # 爬虫爬取的间隔时间
        if index >=page: # 如果 index 大于等于用户输入的页数则执行完毕 跳出循环
            print('执行完毕')
            break
# page_url(1)
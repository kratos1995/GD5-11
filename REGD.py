## -*- coding: utf-8 -*-
import re
import numpy as np
import pymysql
import pandas as pd
from conmitdb import DatabaseAccess
from collections import Counter
import csv
import os
import time
import platform


# dir = os.path.abspath('.')#.split('\\ModuLe')[0]
# print(dir)
# dir = dir+"\static\excel\\差异统计.xls"
# sheeet_name='差异统计'



__draw__list = []
def regd():
    data_list = []
    # 读取原始数据
    sys = platform.system()
    if sys == "Windows":
        with open('\GD5-11\static\\requestGD511.txt', encoding='utf8') as f:
            data_list = f.read()
            f.close()
    elif sys == "Linux":
        with open('\GD5-11\static\\requestGD511.txt', encoding='utf8') as f:
            data_list = f.read()
            f.close()
    else:
        print("==============无法识别的操作系统================")
        pass
    # with open('\GD5-11\static\\requestGD511.txt',encoding='utf8') as f:
    #     data_list = f.read()
    #     f.close()
    # 正则清洗（redata原始数据）
    redata = re.findall('>([0-9]\d*)<', data_list)
    fetal1= len(redata)# 获取清洗数据的长度
    del redata[:fetal1:7]# 步调对不需要的ID参数进行删除（二次清洗）

    # 创建用于存储期号数据
    draw_number = []
    draw_number.append(redata[:len(redata):6])# 写入期号数据到draw_number
    dra_num = draw_number[0] # 提取的list为数组，且会多出一个空格 dra_num对其清理
    dra_num=[[i for i in ii.split(',')] for ii in dra_num]# 将数组转为list，dra_num为期号

    new_list = [redata[i:i + 6] for i in range(0, len(redata), 6)]

    #用原始数据删除期号，保留中奖号码
    del redata[:len(redata):6]
    len_redata=len(redata)# 获取中奖号码长度
    len_redata=len_redata/5 # 用总长度除以5，得到纵向长度
    arr_data = np.array(redata).reshape(int(len_redata),5)# 对中将号码进行数组排列，如总长度为75 则横向数组为5，纵向为15
    arr_data2 = arr_data.copy() # 复制arr_data 用于计算纵向最高概率的前两位
    arr_data = arr_data.tolist()#将 arr_data转换为list
    #arr_data = [''.join(i) for i in arr_data]# 列表生成式，保留数字

    for n in new_list:
        post_sql = "INSERT INTO GD511 VALUES (%s,%s,%s,%s,%s,%s);"
        print(n)
        db = DatabaseAccess()
        db.linesinsert(post_sql,n)

        if len(__draw__list) <= 0:
            __draw__list.append(n)
        elif len(__draw__list) >= 1:
            pass
    time.sleep(5)


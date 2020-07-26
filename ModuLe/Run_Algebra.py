# -*- coding: utf-8 -*-
# Time: 2020/07/20 09:00:30
# File Name: Run_Algebra.py

# from ModuLe import Algebra01
# from ModuLe import Algebra02
# from ModuLe import Algebra03
# from ModuLe import Algebra04
# from ModuLe import Algebra05
# from ModuLe import Algebra06
# from ModuLe import Algebra07
import sys
sys.path.append("..") #把上级目录加入到变量中
import re
import numpy as np
from requestGD511 import page_url
page_url(1)
# from update_db import run_spyde
# from REGD import __Draw__List
from Write_Excel import write_excel
import get_dwanum
from Get_Big_Data import get_big_data,arry_big_data,Get_Alg
from ModuLe import Algebra301
from collections import Counter
import time

data = []
big_data=[]


count_dwa = Algebra301.Count_DWA()

# count1 = Algebra01.run()
# count2 = Algebra02.run()
# count3 = Algebra03.run()
# count4 = Algebra04.run()
# count5 = Algebra05.run()
# count6 = Algebra06.run()
# count7 = Algebra07.run()

count8 = Algebra301.run() # 调用实例化 Algebra301
big_data.append(count8)   # 创建 big_data 将 count8公式写入

get_big_datas =[]  # 创建 get_big_datas 循环迭代出count8所有元素,并append进get_big_datas
for list1 in count8:
    get_big_datas.append(list1)
get_big_datas.pop(0)  # 删除空格
get_big_datas.pop(0)  # 删除“301公式：出现2~4个”


count_sum = ("统计数据共计%s条：" % len(count_dwa),'\n',"所有展示如下：",'\n',count_dwa)
print("统计数据共计%s条：" % len(count_dwa),'\n',"所有展示如下：",'\n',count_dwa)

# for i in count1:-
#     data.append(i)
# for k in count2:
#     data.append(k)
# for j in count3:
#     data.append(j)
# for v in count4:
#     data.append(v)
# for q in count5:
#     data.append(q)
# for w in count6:
#     data.append(w)
# for e in count7:

# 正则表达式合并所有List,并对元素进行频率排序
def Get_Alg():
    # print("Get_dwanum")
    b = str(get_big_datas)
    Alg = re.findall('[\d]*[\d]', b)
    Alg_int = [int(i) for i in Alg]

    return Alg_int

re_data = np.array(Get_Alg())

b=0
__Draw__List = str(get_dwanum.Get_dwanum())
c = __Draw__List+str(Counter(re_data))
write_excel(b,c,list(count_sum)+get_big_datas)
datas = str(data)
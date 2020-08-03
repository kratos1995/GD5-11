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
import os
sys.path.append("..") #把上级目录加入到变量中
import re
import numpy as np
from requestGD511 import page_url
# page_url(1)
# from update_db import run_spyde
# from REGD import __Draw__List
from Write_Excel import write_excel
import get_dwanum
from Get_Big_Data import get_big_data,arry_big_data
from ModuLe import Algebra301
from collections import Counter
import time
import platform


# 将N个list转为一整条 arry数组，便于执行count统计
def list_to_arry(List_data): # 接收一组List_data
    List_data_str = str(List_data) # 将传入的参数转化为 str，不转换会报错
    Alg = re.findall('[\d]*[\d]', List_data_str) # 正则表达式抽取N个List里的所有数字并保存到Alg
    Alg_int = [int(i) for i in Alg] # 循环Alg 将 Alg里的list全部转换回int类型，转换为int类型之后才能使用 Count 函数进行统计
    return Alg_int # 返回 arry类型的Alg_int



def run_algebra():
    # data = []
    big_data=[]

    # 实例化 Algebra301.Count_DWA 打印输出所有的开奖号
    count_dwa = Algebra301.Count_DWA()
    count_sum = ("统计数据共计%s条：" % len(count_dwa),'\n',"所有展示如下：",'\n',count_dwa)
    print("统计数据共计%s条：" % len(count_dwa),'\n',"所有展示如下：",'\n',count_dwa)

    # 增加抽奖数据arr，不做301匹配，只做统计计算
    no_301_list = list_to_arry(count_dwa)

# 实例化所有公式函数
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



# for 循环将所有公式一并写入到 变量“data”
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

    # 将所有抽奖公式（list_to_arry）转为 arry
    re_data = np.array(list_to_arry(get_big_datas))

    # 未做301统计的数据
    no_301arr = np.array(no_301_list)
    no_301count  = [["未做301统计的数据："],[str(Counter(no_301arr))]]



    local=0 # Excel 的位置参数 代表第一列第一行开始
    __Draw__List = str(get_dwanum.Get_dwanum()) # get_dwanum.Get_dwanum()本期最新中奖号码实例化，并将元素转为str类型
    c = __Draw__List+str(Counter(re_data)) # 本期最新中奖号码，加Count 所有公式数据
    write_excel(local,c,no_301count+list(count_sum)+get_big_datas)# 写入 Excel ，local(位置参数)，c(最新中奖号码，加公式统计结果)，no_301count+list(count_sum)+get_big_datas（未经过301统计的结果和所有公式迭代写入）
    # datas = str(data)

    # 实例化 platform.system() 用于对系统进行命令操作
    sys = platform.system()
    if sys == "Linux": # 如果系统为 Linux 则执行下方命令
        val = os.system("cp /var/www/html/GD5-11/static/excel/配码表.xls /home/yy/gd511.xls")
        print("已将文件复制到FTP目录:")
        vall = os.system("ls /home/yy/")
    elif sys == "Windows":# 如果系统为 Windows 则执行下方命令
        vall = os.system("del C:\\Users\\tesla\AppData\Roaming\WeTool\\users\wxid_zxcil65t7kox21\wtpdata\WPPageChatBot\\res\keybot\\1\配码表.xls")
        val = os.system("copy G:\GD5-11\static\excel\配码表.xls C:\\Users\\tesla\AppData\Roaming\WeTool\\users\wxid_zxcil65t7kox21\wtpdata\WPPageChatBot\\res\keybot\\1\配码表.xls")
        print("EXCEL    寫入成功")
    else: # 如果Linux Windows都不属于则PASS
        pass
if __name__ == "__main__":
    run_algebra
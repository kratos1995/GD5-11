import pandas as pd
import numpy as np
import pymysql
from conmitdb import DatabaseAccess
# import matplotlib.pyplot as plt
# %matplotlib inline


db = DatabaseAccess() # 实例化数据库链接
post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
read =db.database_check(post_sql)

read1 = list(read)
# dataFrame = pd.DataFrame(read1)



sum_list = ['1','2','3','4','5','6','7','8','9','10','11'] # 所有号码集合
arr_data2 = [['4','9','8','3','2'],
 ['5','11','7','8','4'],
 ['1','7','5','9','11'],
 ['6','8','9','1','10'],
 ['11','5','3','7','10'],
 ['1','8','5','7','9'],
 ['8','7','3','5','4'],
 ['10','11','2','8','5'],
 ['1','9','4','5','3'],
 ['1','8','7','2','4'],
 ['1','11','10','2','3'],
 ['5','7','8','11','4'],
 ['11','2','10','5','8'],
 ['2','6','9','4','8'],
 ['11','4','6','5','2']]

dataFrame = pd.DataFrame(arr_data2)
cols_name = dataFrame.values.tolist()

arr_data2 = np.array(arr_data2)
a = arr_data2[:,0]
a = [int(x) for x in a]


def step_statistics(lists):
    b = 1
    zeros = 0
    total = 1
    statistics = []
    tp = []
    for j in lists:
        if int(j) == int(b):
            # print('+',j)
            zeros= zeros+1
            tp.append(zeros)
            # print(tp,'*****************')
        elif int(j) != int(b):
            # print("-", j)
            statistics.append(len(tp))
            # print(statistics,'--------------------')
            tp.clear()
            # print('clear:', tp)
            zeros = 0
    newEmails = list(filter(lambda x : x !=0, statistics))
    print(newEmails)
step_statistics(a)







# def index_lenList():
#     for index in range(len(cols_name)):
#         index = None
#         return ++index
# index_lenList()

# distance_data = []
# class Rec_list(object):
#     def __init__(self,sum_list,list1_name):
#         self.sum_list = sum_list # 所有的号码1-11
#         self.list1_name = list1_name # 第N*N期数据
#         count = len(list1_name) # 获取N*N期数据长度
#         zero_count = 0 # 初始化一个zero_count 0
#         temporary_list = [] # 用于存放临时数据
#         Flase_list=[] # 用于存放本期没有的号码
#         stepCount_list = [] # 步数
#         for i in self.list1_name: # 用 i 迭代 所有奖号 n*n
#             if isinstance(i,list):
#                 sum_list_set = set(self.sum_list)
#                 print(i,'这是arr')
#                 # 创建两条list
#                 for k in self.sum_list: # k 迭代所有数字 1-11
#                     if k in i:
#                         print(k[0])
#                         pass # print(k,": 存在，距离重置：%s。"%zero_count)
#                     else:
#                         temporary_list.append(k) # 写入 i 不存在的数字k (i为所有开奖号，k为所有数字)
#                         # print('查看临时数据',temporary_list)
#                         if not Flase_list:
#                             print("列表为空，执行第一次写入",k)
#                             Flase_list.append(k)
#
#
#                         # elif (len(temporary_list)>=7): # 如果 temporary_list 超过7，代表数据异常
#                         #     print('数据写入异常：')
#                         else: # 数据无异常时执行
#                             for y in temporary_list:# y是临时数据
#                                 if y not in Flase_list: # 如果y不存在于 Flase_list则写入k
#                                     Flase_list.append(k)
#                                     print(Flase_list,'========',k)
#                                     print(Flase_list,"++++++++++++++++++++")
#                                     temporary_list.clear()
#                                 else:
#                                     for x in Flase_list:
#                                         if x not in i:
#                                             print('hahhahaha')
#                                 # elif i in Flase_list: # 如果y and Flase_list 都存在，则写入
#                                 #         Flase_list.append(k)
#                                 #         print(Flase_list)
#                                 #         print(temporary_list,'------------------------------')
#                                 #         temporary_list.clear()
#                                 # else:
#                                 #     #if x not
#                                 #     c =[x for x in Flase_list if x not in temporary_list]
#                                 #     print('Flase_list需要取出%s'%c)
#                                 #     temporary_list.clear()
#
#                                     # temporary_list.clear()
#                         # print('检查Flase_list',Flase_list,len(Flase_list))
#                         # print(k,": 不存在，最大距离是：%s。"%zero_count)
#                         # print('看看i',len(i))
# #                        c = [y for y in Flase_list if y not in temporary_list] # 在Flase_list列表中而不在temporary_list列表中
#                         '''
#                         当Flase_list中存在，而temporary_list不存在时，应当取出Flase_list存在的数，从temporary_list写入Flase_list不存在的数
#                         '''
#                         # stepCount_list.append(c)
# #                     elif k in i:
# #                         print(k,":存在，距离是%s。"%zero_count)
# Rec_list(sum_list,cols_name)
# clear_data=[]
# diff=[]
# for i in cols_name:
#     clear_data.append(i)
#     diff=list(clear_data.difference(i))
#     print(diff)
#     diff.clear()
# print(type(cols_name[0]))
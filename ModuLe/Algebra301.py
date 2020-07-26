import os
# from conmitdb import DatabaseAccess
import xlwt
# from Get_Big_Data import get_big_data
import Get_Big_Data
# from Get_Big_Data import get_big_data
# from requestGD511 import get_proxy
# from requestGD511 import page_url
#
# get_proxy()
# page_url(1)
# 从数据库获取上期中奖号

get_big_datas = Get_Big_Data.get_big_data()

count_number = []
count_value = []
count_number_rset = []
count_dwa = []

count_a = [1,2,3,4]
count_b = [2,3,4,5]
count_c = [3,4,5,6]
count_d = [4,5,6,7]
count_e = [5,6,7,8]
count_f = [6,7,8,9]
count_g = [7,8,9,10]
count_h = [8,9,10,11]

# 301公式：出现2~4个
class algebra1_8(object):
    def __init__(self,draw_list,count_list):
        self.draw_list = draw_list
        self.count_list = count_list
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
        for j in self.count_list:
            if j in self.draw_list:
                count_error.append(j)
            elif j not in self.draw_list:
                # print(j,'不在',a)
                pass
        len_count_error = len(count_error)
        if len(count_error)<=0:
            pass
            #print("公式成立0：", self.count_list)
        elif len(count_error)>=2 and len(count_error)<=4:
            # print("公式成立：", self.count_list)
            # print("出现的数字%s个："%len_count_error,count_error)
            count_number.append(self.count_list,)
            count_value.append(count_error)
            count_value.append(count_errors)



class run1(object):
    def __init__(self,a):
        self.a =a
        algebra1_8(a,count_a)
        algebra1_8(a,count_b)
        algebra1_8(a,count_c)
        algebra1_8(a,count_d)
        algebra1_8(a,count_e)
        algebra1_8(a,count_f)
        algebra1_8(a,count_g)
        algebra1_8(a,count_h)


for a in get_big_datas:
    run1(a)
    count_dwa.append(a)

def Count_DWA(): # 用户输入的抽取条数，用于返回抽取的N条期号
    return count_dwa

def run():
    count_number_rset.append('  ')
    count_number_rset.append("301公式：出现2~4个")
    count1 = count_number
    for i in count1:
        count_number_rset.append(i)
    return count_number_rset
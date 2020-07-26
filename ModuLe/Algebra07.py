import os
from conmitdb import DatabaseAccess
import xlwt
from get_dwanum import Get_dwanum

# 从数据库获取上期中奖号
a = Get_dwanum()
count_number = []
count_value = []
count_number_rset = []
# db = DatabaseAccess() # 实例化数据库链接
# post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
# read_data =db.database_check(post_sql)
# read_data = list(read_data)

count1_14_a = [[1,2],[3,4,5]]
count1_14_b = [[2,3],[4,5,6]]
count1_14_c = [[3,4],[5,6,7]]
count1_14_d = [[4,5],[6,7,8]]
count1_14_e = [[5,6],[7,8,9]]
count1_14_f = [[6,7],[8,9,10]]
count1_14_g = [[7,8],[9,10,11]]
count1_14_h = [[8,9],[9,10,11]]
count1_14_i = [[9,10],[6,7,8]]
count1_14_j = [[10,11],[7,8,9]]

count1_14_k = [[8,9],[5,6,7]]
count1_14_l = [[7,8],[4,5,6]]
count1_14_n = [[6,7],[3,4,5]]
count1_14_m = [[5,6],[2,3,4]]
count1_14_o = [[4,5],[1,2,3]]

# 286公式：前面出现1~2个，后面出现1~3个
class algebra1_14(object):
    def __init__(self,draw_list,count_list): # 接受兩個參數，draw開獎號，count_list公式
        self.draw_list = draw_list
        self.count_list = count_list
        lencount_list = len(self.count_list)# 获取公式长度，公式数据类型为嵌套list，[[3,4],[1,2,3]]
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
        # for k in range(lencount_list):
        for j in self.count_list[0]:
            if j in a:
                # print(j,'在',a)
                count_error.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass
        for j in self.count_list[1]:
            if j in a:
                # print(j,'在',a)
                count_errors.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass
        if len(count_error)>=1 and len(count_error)<=2:
            if len(count_errors)>=1 and len(count_errors)<=3:
                # print("=======",count_error,len(count_error),"=========",count_errors,len(count_errors),"=======")
                # print("公式成立：",self.count_list,len(count_error),len(count_error))
                count_number.append(self.count_list)
                count_value.append(count_error)
                count_value.append(count_errors)
            else:
                pass
        else:
            pass

def run1():
    algebra1_14(a,count1_14_a)
    algebra1_14(a,count1_14_b)
    algebra1_14(a,count1_14_c)
    algebra1_14(a,count1_14_d)
    algebra1_14(a,count1_14_e)
    algebra1_14(a,count1_14_f)
    algebra1_14(a,count1_14_g)
    algebra1_14(a,count1_14_h)
    algebra1_14(a,count1_14_i)
    algebra1_14(a,count1_14_j)
    algebra1_14(a,count1_14_k)
    algebra1_14(a,count1_14_l)
    algebra1_14(a,count1_14_n)
    algebra1_14(a,count1_14_m)
    algebra1_14(a,count1_14_o)
    return count_number

def run():
    # count_number_rset.append("   ")
    # count_number_rset.append("286公式: 前面2~3个，后面2~3个")
    count1 = run1()
    for i in count1:
        count_number_rset.append(i)
    return count_number_rset
if __name__ == "__main__":
    run()
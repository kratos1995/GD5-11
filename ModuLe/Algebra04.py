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

count_a = [1,2,3,4]
count_b = [2,3,4,5]
count_c = [3,4,5,6]
count_d = [4,5,6,7]
count_e = [5,6,7,8]
count_f = [6,7,8,9]
count_g = [7,8,9,10]
count_h = [8,9,10,11]

count9_15_a = [[1,2],[2,3,4]]
count9_15_b = [[2,3],[3,4,5]]
count9_15_c = [[3,4],[4,5,6]]
count9_15_d = [[4,5],[5,6,7]]
count9_15_e = [[5,6],[6,7,8]]
count9_15_f = [[6,7],[7,8,9]]
count9_15_g = [[7,8],[8,9,10]]
count9_15_h = [[8,9],[9,10,11]]

count9_15_i = [[10,11],[8,9,10]]
count9_15_j = [[9,10],[7,8,9]]
count9_15_k = [[8,9],[6,7,8]]
count9_15_l = [[7,8],[5,6,7]]
count9_15_n = [[6,7],[4,5,6]]
count9_15_m = [[5,6],[3,4,5]]
count9_15_o = [[4,5],[2,3,4]]
count9_15_p = [[3,4],[1,2,3]]

# 301公式：出现2~4个
class algebra1_8(object):
    def __init__(self,draw_list,count_list):
        self.draw_list = draw_list
        self.count_list = count_list
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
        for j in self.count_list:
            if j in a:
                count_error.append(j)
            elif j not in a:
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

class algebra_294(object):
    def __init__(self,draw_list,count_list):
        self.draw_list = draw_list
        self.count_list = count_list
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
        for j in self.count_list:
            if j in a:
                count_error.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass
        len_count_error = len(count_error)
        if len(count_error)<=0:
            pass
            #print("公式成立0：", self.count_list)
        elif len(count_error)>=2 and len(count_error)<=3:
            # print("公式成立：", self.count_list)
            # print("出现的数字%s个："%len_count_error,count_error)
            count_number.append(self.count_list,)
            count_value.append(count_error)
            count_value.append(count_errors)

# 301公式：前面出现1~2个，后面出现1~3个
class algebra9_15(object):
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
            if len(count_errors)>=1and len(count_errors)<=3:
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
    algebra1_8(a,count_a)
    algebra1_8(a,count_b)
    algebra1_8(a,count_c)
    algebra1_8(a,count_d)
    algebra1_8(a,count_e)
    algebra1_8(a,count_f)
    algebra1_8(a,count_g)
    algebra1_8(a,count_h)
    return count_number

def run2():
    algebra9_15(a,count9_15_a)
    algebra9_15(a,count9_15_b)
    algebra9_15(a,count9_15_c)
    algebra9_15(a,count9_15_d)
    algebra9_15(a,count9_15_e)
    algebra9_15(a,count9_15_f)
    algebra9_15(a,count9_15_g)
    algebra9_15(a,count9_15_h)
    algebra9_15(a,count9_15_i)
    algebra9_15(a,count9_15_j)
    algebra9_15(a,count9_15_k)
    algebra9_15(a,count9_15_l)
    algebra9_15(a,count9_15_n)
    algebra9_15(a,count9_15_m)
    algebra9_15(a,count9_15_o)
    algebra9_15(a,count9_15_p)
    return count_number

def run294():
    algebra_294(a,count_a)
    algebra_294(a,count_b)
    algebra_294(a,count_c)
    algebra_294(a,count_d)
    algebra_294(a,count_e)
    algebra_294(a,count_f)
    algebra_294(a,count_g)
    algebra_294(a,count_h)
    return count_number

def run():
    count_number_rset.append('  ')
    count_number_rset.append("301公式：出现2~4个")
    count1 = run1()
    for i in count1:
        count_number_rset.append(i)
    count_number.clear()

    count_number_rset.append('  ')
    count_number_rset.append("294公式：出现2~3个")
    count294 = run294()
    for i in count294:
        count_number_rset.append(i)
    count_number.clear()

    # count_number_rset.append("   ")
    # count_number_rset.append("301公式：前面出现1~2个，后面出现1~3个")
    count2 = run2()
    for i in count2:
        count_number_rset.append(i)
    return count_number_rset
if __name__ == "__main__":
    run()
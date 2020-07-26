import os
from conmitdb import DatabaseAccess
import xlwt
from get_dwanum import Get_dwanum

# 从数据库获取上期中奖号
a = Get_dwanum()
count_number = []
count_value = []
count_number_rset = []

algebra1_21_a = [[1,2,3,4,5],[4,5,6]]
algebra1_21_b = [[2,3,4,5,6],[5,6,7]]
algebra1_21_c = [[3,4,5,6,7],[6,7,8]]
algebra1_21_d = [[4,5,6,7,8],[7,8,9]]
algebra1_21_e = [[5,6,7,8,9],[8,9,10]]
algebra1_21_f = [[6,7,8,9,10],[9,10,11]]

algebra1_21_g = [[7,8,9,10,11],[6,7,8]]
algebra1_21_h = [[6,7,8,9,10],[5,6,7]]
algebra1_21_i = [[5,6,7,8,9],[4,5,6]]
algebra1_21_j = [[4,5,6,7,8],[3,4,5]]
algebra1_21_k = [[3,4,5,6,7],[2,3,4]]
algebra1_21_l = [[2,3,4,5,6],[1,2,3]]

algebra1_21_aa = [[1,2,3,4,5],[5,6,7]]
algebra1_21_bb = [[2,3,4,5,6],[6,7,8]]
algebra1_21_cc = [[3,4,5,6,7],[7,8,9]]
algebra1_21_dd = [[4,5,6,7,8],[8,9,10]]
algebra1_21_ee = [[5,6,7,8,9],[9,10,11]]
algebra1_21_ff = [[6,7,8,9,10],[4,5,6]]
algebra1_21_hh = [[7,8,9,10,11],[5,6,7]]
algebra1_21_ii = [[5,6,7,8,9],[3,4,5]]
algebra1_21_jj = [[4,5,6,7,8],[2,3,4]]
algebra1_21_kk = [[3,4,5,6,7],[1,2,3]]

# db = DatabaseAccess() # 实例化数据库链接
# post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
# read_data =db.database_check(post_sql)
# read_data = list(read_data)

# 前面2~3，后面1~2
class algebra1_21(object):
    def __init__(self,draw_list,count_list):
        self.draw_list = draw_list
        self.count_list = count_list
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
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
        if len(count_error)>=2 and len(count_error)<=3:
            if len(count_errors)>=1and len(count_errors)<=2:
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
    algebra1_21(a, algebra1_21_a)
    algebra1_21(a, algebra1_21_b)
    algebra1_21(a, algebra1_21_c)
    algebra1_21(a, algebra1_21_d)
    algebra1_21(a, algebra1_21_e)
    algebra1_21(a, algebra1_21_f)
    algebra1_21(a, algebra1_21_g)
    algebra1_21(a, algebra1_21_h)
    algebra1_21(a, algebra1_21_i)
    algebra1_21(a, algebra1_21_j)
    algebra1_21(a, algebra1_21_k)
    algebra1_21(a, algebra1_21_l)
    algebra1_21(a, algebra1_21_aa)
    algebra1_21(a, algebra1_21_bb)
    algebra1_21(a, algebra1_21_cc)
    algebra1_21(a, algebra1_21_dd)
    algebra1_21(a, algebra1_21_ee)
    algebra1_21(a, algebra1_21_ff)
    algebra1_21(a, algebra1_21_hh)
    algebra1_21(a, algebra1_21_ii)
    algebra1_21(a, algebra1_21_jj)
    algebra1_21(a, algebra1_21_kk)
    return count_number

def run():
    # count_number_rset.append("   ")
    # count_number_rset.append("285公式: 前面出现2~3，后面出现1~2")
    count5 = run1()
    for i in count5:
        count_number_rset.append(i)
    return count_number_rset
if __name__ == "__main__":
    run()
import os
from conmitdb import DatabaseAccess
from Write_Excel import write_excel
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

algebra1_6_a = [[1,2,3,4,5],[2,3,4,5,6]]
algebra1_6_b = [[2,3,4,5,6],[3,4,5,6,7]]
algebra1_6_c = [[3,4,5,6,7],[4,5,6,7,8]]
algebra1_6_d = [[4,5,6,7,8],[5,6,7,8,9]]
algebra1_6_e = [[5,6,7,8,9],[6,7,8,9,10]]
algebra1_6_f = [[6,7,8,9,10],[7,8,9,10,11]]

# 290 前面2~3个，后面2~3个
class algebra1_6(object):
    def __init__(self,draw_list,count_list):
        self.count_ = count_ = []
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
            if len(count_errors)>=2and len(count_errors)<=3:
                # print("=======",count_error,len(count_error),"=========",count_errors,len(count_errors),"=======")
                # print("公式成立：",self.count_list,len(count_error),len(count_error))
                count_number.append(self.count_list)
                count_value.append(count_error)
                count_value.append(count_errors)
            else:
                pass
        else:
            pass


def run0():
    algebra1_6(a,algebra1_6_a)
    algebra1_6(a,algebra1_6_b)
    algebra1_6(a,algebra1_6_c)
    algebra1_6(a,algebra1_6_d)
    algebra1_6(a,algebra1_6_e)
    algebra1_6(a,algebra1_6_f)
    return count_number

def run():
    count_number_rset.append("   ")
    count_number_rset.append("290公式: 前面2~3个，后面2~3个")
    count5 = run0()
    if len(count5) == 0:
        count_number_rset.append("290公式不成立，未达到要求！！！！！数值为空")
    elif len(count5) >=1:
        for i in count5:
            count_number_rset.append(i)
    return count_number_rset

if __name__ == "__main__":
    run()
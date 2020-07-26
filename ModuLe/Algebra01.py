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

# 公式1，list中出现1~2个
count_a = [[1,2,3],[2,3,4]]
count_b = [[2,3,4],[3,4,5]]
count_c = [[3,4,5],[4,5,6]]
count_d = [[4,5,6],[5,6,7]]
count_e = [[5,6,7],[6,7,8]]
count_es= [[6,7,8],[7,8,9]]
count_f = [[7,8,9],[8,9,10]]
count_g = [[8,9,10],[9,10,11]]

# 公式2，list中出现1~3个
count_aa = [[1,2],[2,3,4]]
count_bb = [[2,3],[3,4,5]]
count_cc = [[3,4],[4,5,6]]
count_dd = [[4,5],[5,6,7]]
count_ee = [[5,6],[6,7,8]]
count_ff = [[6,7],[7,8,9]]
count_gg = [[7,8],[8,9,10]]
count_hh = [[8,9],[9,10,11]]

# 公式3，出现1~3个
count_aaa = [[10,11],[8,9,10]]
count_bbb = [[9,10],[7,8,9]]
count_ccc = [[8,9],[6,7,8]]
count_ddd = [[7,8],[5,6,7]]
count_eee = [[6,7],[4,5,6]]
count_fff = [[5,6],[3,4,5]]
count_ggg = [[4,5],[2,3,4]]
count_hhh = [[3,4],[1,2,3]]

# 公式4，出现0~4个
count_aaaa = [1,2,3,4]
count_bbbb = [2,3,4,5]
count_cccc = [3,4,5,6]
count_dddd = [4,5,6,7]
count_eeee = [5,6,7,8]
count_ffff = [6,7,8,9]
count_gggg = [7,8,9,10]
count_hhhh = [8,9,10,11]

# 322 前面1~2个，后面1~2个
class algebra1_8(object):
    def __init__(self,draw_list,count_list): # 接受兩個參數，draw開獎號，count_list公式
        self.draw_list = draw_list
        self.count_list = count_list
        lencount_list = len(self.count_list)# 获取公式长度，公式数据类型为嵌套list，[[3,4],[1,2,3]]
        count_error = []    # 用于存储 count_list[0]
        count_errors = []    # 用于存储 count_list[1]
        for j in self.count_list[0]:
            if j in a:
                # print(j,'在',a)
                count_error.append(j)
            elif j not in a:
                pass
        for j in self.count_list[1]:
            if j in a:
                # print(j,'在',a)
                count_errors.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass

        if len(count_error)>=1and len(count_error)<=2:
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

# 322 前面出现0~1个，后面出现1~3个
class algebra9_24(object):
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
                pass
        for j in self.count_list[1]:
            if j in a:
                # print(j,'在',a)
                count_errors.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass
        if len(count_error)>=0and len(count_error)<=1:
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


# 322公式：出现0,2,3,4
class algebra31_38(object):
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
            # print("公式成立0：", self.count_list)
            count_number.append(self.count_list)
        elif len(count_error)==1:
            pass
        elif len(count_error)>=2 and len(count_error)<=4:
            # print("公式成立：", self.count_list)
            # print("出现的数字%s个："%len_count_error,count_error)
            count_number.append(self.count_list)
            count_value.append(count_error)
            count_value.append(count_errors)

def run1():
    algebra1_8(a,count_a)
    algebra1_8(a,count_b)
    algebra1_8(a,count_c)
    algebra1_8(a,count_d)
    algebra1_8(a,count_e)
    algebra1_8(a,count_f)
    algebra1_8(a,count_g)
    return count_number
def run2():
    algebra9_24(a,count_aa)
    algebra9_24(a,count_bb)
    algebra9_24(a,count_cc)
    algebra9_24(a,count_dd)
    algebra9_24(a,count_ee)
    algebra9_24(a,count_ff)
    algebra9_24(a,count_gg)
    algebra9_24(a,count_hh)

    algebra9_24(a,count_aaa)
    algebra9_24(a,count_bbb)
    algebra9_24(a,count_ccc)
    algebra9_24(a,count_ddd)
    algebra9_24(a,count_eee)
    algebra9_24(a,count_fff)
    algebra9_24(a,count_ggg)
    algebra9_24(a,count_hhh)
    return count_number

def run3():
    algebra31_38(a,count_aaaa)
    algebra31_38(a,count_bbbb)
    algebra31_38(a,count_cccc)
    algebra31_38(a,count_dddd)
    algebra31_38(a,count_eeee)
    algebra31_38(a,count_ffff)
    algebra31_38(a,count_gggg)
    algebra31_38(a,count_hhhh)
    return count_number


def run():
    # count_number_rset.append("322公式：前面1~2个，后面1~2个")
    count1 = run1()
    for i in count1:
        count_number_rset.append(i)
    count_number.clear()

    # count_number_rset.append('  ')
    # count_number_rset.append("322公式：前面出现0~1个，后面出现1~3个")
    count2 = run2()
    for n in count2:
        count_number_rset.append(n)
    count_number.clear()

    # count_number_rset.append('  ')
    # count_number_rset.append("322公式：出现0个、2个、3个、4个")
    count3 = run3()
    for k in count3:
        count_number_rset.append(k)

    return count_number_rset
if __name__ == "__main__":
    run()
# count_number.clear()
# count_value.clear()




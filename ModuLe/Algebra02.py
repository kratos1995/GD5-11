import os
from conmitdb import DatabaseAccess
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

# 公式1，前面1~2个，后面1~2个
count_a = [[1,2,3],[4,5,6]]
count_b = [[2,3,4],[5,6,7]]
count_c = [[3,4,5],[6,7,8]]
count_d = [[4,5,6],[7,8,9]]
count_e = [[5,6,7],[8,9,10]]
count_f = [[6,7,8],[9,10,11]]

# 公式2，前面2~3个，后面1~2个
count_aa = [[1,2,3,4,5],[1,2,3]]
count_bb = [[1,2,3,4,5],[2,3,4]]
count_cc = [[1,2,3,4,5],[3,4,5]]
count_dd = [[1,2,3,4,5],[4,5,6]]
count_ee = [[1,2,3,4,5],[5,6,7]]
count_ff = [[1,2,3,4,5],[6,7,8]]
count_gg = [[1,2,3,4,5],[7,8,9]]
count_hh = [[1,2,3,4,5],[8,9,10]]
count_ii = [[1,2,3,4,5],[9,10,11]]

# 公式3，前面2~3个，后面1~2个
count_aaa = [[2,3,4,5,6],[1,2,3]]
count_bbb = [[2,3,4,5,6],[2,3,4]]
count_ccc = [[2,3,4,5,6],[3,4,5]]
count_ddd = [[2,3,4,5,6],[4,5,6]]
count_eee = [[2,3,4,5,6],[5,6,7]]
count_fff = [[2,3,4,5,6],[6,7,8]]
count_ggg = [[2,3,4,5,6],[7,8,9]]
count_hhh = [[2,3,4,5,6],[8,9,10]]
count_iii = [[2,3,4,5,6],[9,10,11]]

# 公式3，前面2~3个，后面1~2个
count_aaaa = [[3,4,5,6,7],[1,2,3]]
count_bbbb = [[3,4,5,6,7],[2,3,4]]
count_cccc = [[3,4,5,6,7],[3,4,5]]
count_dddd = [[3,4,5,6,7],[4,5,6]]
count_eeee = [[3,4,5,6,7],[5,6,7]]
count_ffff = [[3,4,5,6,7],[6,7,8]]
count_gggg = [[3,4,5,6,7],[7,8,9]]
count_hhhh = [[3,4,5,6,7],[8,9,10]]
count_iiii = [[3,4,5,6,7],[9,10,11]]

count_aaaaa = [[4,5,6,7,8],[1,2,3]]
count_bbbbb = [[4,5,6,7,8],[2,3,4]]
count_ccccc = [[4,5,6,7,8],[3,4,5]]
count_ddddd = [[4,5,6,7,8],[4,5,6]]
count_eeeee = [[4,5,6,7,8],[5,6,7]]
count_fffff = [[4,5,6,7,8],[6,7,8]]
count_ggggg = [[4,5,6,7,8],[7,8,9]]
count_hhhhh = [[4,5,6,7,8],[8,9,10]]
count_iiiii = [[4,5,6,7,8],[9,10,11]]

count_aaaaaa = [[5,6,7,8,9],[1,2,3]]
count_bbbbbb = [[5,6,7,8,9],[2,3,4]]
count_cccccc = [[5,6,7,8,9],[3,4,5]]
count_dddddd = [[5,6,7,8,9],[4,5,6]]
count_eeeeee = [[5,6,7,8,9],[5,6,7]]
count_ffffff = [[5,6,7,8,9],[6,7,8]]
count_gggggg = [[5,6,7,8,9],[7,8,9]]
count_hhhhhh = [[5,6,7,8,9],[8,9,10]]
count_iiiiii = [[5,6,7,8,9],[9,10,11]]

count_aaaaaaa = [[5,6,7,8,9],[1,2,3]]
count_bbbbbbb = [[5,6,7,8,9],[2,3,4]]
count_ccccccc = [[5,6,7,8,9],[3,4,5]]
count_ddddddd = [[5,6,7,8,9],[4,5,6]]
count_eeeeeee = [[5,6,7,8,9],[5,6,7]]
count_fffffff = [[5,6,7,8,9],[6,7,8]]
count_ggggggg = [[5,6,7,8,9],[7,8,9]]
count_hhhhhhh = [[5,6,7,8,9],[8,9,10]]
count_iiiiiii = [[5,6,7,8,9],[9,10,11]]

count_aaaaaaaa = [[6,7,8,9,10],[1,2,3]]
count_bbbbbbbb = [[6,7,8,9,10],[2,3,4]]
count_cccccccc = [[6,7,8,9,10],[3,4,5]]
count_dddddddd = [[6,7,8,9,10],[4,5,6]]
count_eeeeeeee = [[6,7,8,9,10],[5,6,7]]
count_ffffffff = [[6,7,8,9,10],[6,7,8]]
count_gggggggg = [[6,7,8,9,10],[7,8,9]]
count_hhhhhhhh = [[6,7,8,9,10],[8,9,10]]
count_iiiiiiii = [[6,7,8,9,10],[9,10,11]]

count_aaaaaaaaa = [[7,8,9,10,11],[1,2,3]]
count_bbbbbbbbb = [[7,8,9,10,11],[2,3,4]]
count_ccccccccc = [[7,8,9,10,11],[3,4,5]]
count_ddddddddd = [[7,8,9,10,11],[4,5,6]]
count_eeeeeeeee = [[7,8,9,10,11],[5,6,7]]
count_fffffffff = [[7,8,9,10,11],[6,7,8]]
count_ggggggggg = [[7,8,9,10,11],[7,8,9]]
count_hhhhhhhhh = [[7,8,9,10,11],[8,9,10]]
count_iiiiiiiii = [[7,8,9,10,11],[9,10,11]]

# 前面0~1个，后面1~2个
count42_52a = [[1,2],[3,4,5]]
count42_52b = [[2,3],[4,5,6]]
count42_52c = [[3,4],[5,6,7]]
count42_52d = [[4,5],[6,7,8]]
count42_52e = [[5,6],[7,8,9]]
count42_52f = [[6,7],[8,9,10]]
count42_52g = [[7,8],[9,10,11]]

count42_52h = [[10,11],[7,8,9]]
count42_52i = [[9,10],[6,7,8]]
count42_52j = [[8,9],[5,6,7]]
count42_52k = [[7,8],[4,5,6]]
count42_52l = [[6,7],[3,4,5]]
count42_52n = [[5,6],[2,3,4]]
count42_52m = [[4,5],[1,2,3]]

# 315公式：前面1~2個，後面1~2個
class algebra1_6(object):
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


# 315公式：前面2~3個，後面1~2個
class algebra7_41(object):
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
        if len(count_error)>=2and len(count_error)<=3:
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

# 315公式：前面0~1个，后面1~2个
class algebra42_52(object):
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
                # print(j,'不在',a)
        for j in self.count_list[1]:
            if j in a:
                # print(j,'在',a)
                count_errors.append(j)
            elif j not in a:
                # print(j,'不在',a)
                pass
        if len(count_error)>=0 and len(count_error)<=1:
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
    algebra1_6(a,count_a)
    algebra1_6(a,count_b)
    algebra1_6(a,count_c)
    algebra1_6(a,count_d)
    algebra1_6(a,count_e)
    algebra1_6(a,count_f)
    return count_number

def run2():
    algebra7_41(a,count_aa)
    algebra7_41(a,count_bb)
    algebra7_41(a,count_cc)
    algebra7_41(a,count_dd)
    algebra7_41(a,count_ee)
    algebra7_41(a,count_ff)
    algebra7_41(a,count_gg)
    algebra7_41(a,count_hh)
    algebra7_41(a,count_ii)
    algebra7_41(a,count_aaa)
    algebra7_41(a,count_bbb)
    algebra7_41(a,count_ccc)
    algebra7_41(a,count_ddd)
    algebra7_41(a,count_eee)
    algebra7_41(a,count_fff)
    algebra7_41(a,count_ggg)
    algebra7_41(a,count_hhh)
    algebra7_41(a,count_iii)
    algebra7_41(a,count_aaaa)
    algebra7_41(a,count_bbbb)
    algebra7_41(a,count_cccc)
    algebra7_41(a,count_dddd)
    algebra7_41(a,count_eeee)
    algebra7_41(a,count_ffff)
    algebra7_41(a,count_gggg)
    algebra7_41(a,count_hhhh)
    algebra7_41(a,count_iiii)
    algebra7_41(a,count_aaaaa)
    algebra7_41(a,count_bbbbb)
    algebra7_41(a,count_ccccc)
    algebra7_41(a,count_ddddd)
    algebra7_41(a,count_eeeee)
    algebra7_41(a,count_fffff)
    algebra7_41(a,count_ggggg)
    algebra7_41(a,count_hhhhh)
    algebra7_41(a,count_iiiii)
    algebra7_41(a,count_aaaaaa)
    algebra7_41(a,count_bbbbbb)
    algebra7_41(a,count_cccccc)
    algebra7_41(a,count_dddddd)
    algebra7_41(a,count_eeeeee)
    algebra7_41(a,count_ffffff)
    algebra7_41(a,count_gggggg)
    algebra7_41(a,count_hhhhhh)
    algebra7_41(a,count_iiiiii)
    algebra7_41(a,count_aaaaaaa)
    algebra7_41(a,count_bbbbbbb)
    algebra7_41(a,count_ccccccc)
    algebra7_41(a,count_ddddddd)
    algebra7_41(a,count_eeeeeee)
    algebra7_41(a,count_fffffff)
    algebra7_41(a,count_ggggggg)
    algebra7_41(a,count_hhhhhhh)
    algebra7_41(a,count_iiiiiii)
    algebra7_41(a,count_aaaaaaaa)
    algebra7_41(a,count_bbbbbbbb)
    algebra7_41(a,count_cccccccc)
    algebra7_41(a,count_dddddddd)
    algebra7_41(a,count_eeeeeeee)
    algebra7_41(a,count_ffffffff)
    algebra7_41(a,count_gggggggg)
    algebra7_41(a,count_hhhhhhhh)
    algebra7_41(a,count_iiiiiiii)
    algebra7_41(a,count_aaaaaaaaa)
    algebra7_41(a,count_bbbbbbbbb)
    algebra7_41(a,count_ccccccccc)
    algebra7_41(a,count_ddddddddd)
    algebra7_41(a,count_eeeeeeeee)
    algebra7_41(a,count_fffffffff)
    algebra7_41(a,count_ggggggggg)
    algebra7_41(a,count_hhhhhhhhh)
    algebra7_41(a,count_iiiiiiiii)
    return count_number

def run3():
    algebra42_52(a,count42_52a)
    algebra42_52(a,count42_52b)
    algebra42_52(a,count42_52c)
    algebra42_52(a,count42_52d)
    algebra42_52(a,count42_52e)
    algebra42_52(a,count42_52f)
    algebra42_52(a,count42_52g)
    algebra42_52(a,count42_52h)
    algebra42_52(a,count42_52i)
    algebra42_52(a,count42_52j)
    algebra42_52(a,count42_52k)
    algebra42_52(a,count42_52l)
    algebra42_52(a,count42_52n)
    algebra42_52(a,count42_52m)
    return count_number

def run():
    # count_number_rset.append('  ')
    # count_number_rset.append("315公式：前面1~2個，後面1~2個")
    count1 = run1()
    for i in count1:
        count_number_rset.append(i)
    count_number.clear()

    # count_number_rset.append('  ')
    # count_number_rset.append("315公式：前面2~3個，後面1~2個")
    count2 = run2()
    for n in count2:
        count_number_rset.append(n)
    count_number.clear()

    # count_number_rset.append('  ')
    # count_number_rset.append("315公式：前面0~1个，后面1~2个")
    count3 = run3()
    for k in count3:
        count_number_rset.append(k)

    return count_number_rset

if __name__ == "__main__":
    run()
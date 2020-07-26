from conmitdb import DatabaseAccess
import re
import time

def Get_dwanum():

    db = DatabaseAccess()  # 实例化数据库链接
    # post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
    post_sql = "select draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 FROM GD511 ORDER BY pashe DESC LIMIT 0,1;"
    read_data = db.database_check(post_sql)
    # read_data = list(read_data)
    a = read_data

    b = str(a)
    dwa = re.findall('[\d]*[\d]', b)
    dwa_int = [int(i) for i in dwa]
    dwa_ints = [2,5,3,4,9] # 测试用
    print("最新一期数据为：%s" % dwa_int)
    #print(type(dwa_int[0]),dwa_int)
    return dwa_int
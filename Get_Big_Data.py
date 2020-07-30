from conmitdb import DatabaseAccess
import re
import time



__Extract_number__ = []#创建 Extract_list 用于存储用户需要抽取几条数据的信息
__getdb_list__ = []  # 用于存储所有抽奖号

def Extract_data(): # 用户输入抽取数量
    while True:
        __input__ = input("请输入需要抽取的数据：")
        if __input__.isdigit():
            __Extract_number__.append(__input__)
            break
        else:
            print("数据类型错误！！ 请输入整数")
            continue
Extract_data()


# 根据用户输入的数量获取数据库
def get_dbquantity():
    db = DatabaseAccess()  # 实例化数据库链接
    # post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
    # 获取最新10期的数据
    post_sql = "select draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 FROM GD511 ORDER BY pashe DESC LIMIT 0, %s;" % __Extract_number__[0]
    read_data = db.database_check(post_sql)  # 执行SQL命令
    a = read_data
    return read_data


a = [[1,2,3,4,5],[2,3,4,5,6]]
# 清洗所有公式为Array
def Get_Alg(count_number_rset):
    b = str(count_number_rset)
    Alg = re.findall('[\d]*[\d]', b)
    Alg_int = [int(i) for i in Alg]
    return Alg_int



arry_big_data_list = []
get_big_data_list = []
def arry_big_data():
    a = __getdb_list__
    for i in __getdb_list__:
        for k in i:
            arry_big_data_list.append(k)
    return arry_big_data_list


# 获取所有开奖号码
def get_big_data():
    a = get_dbquantity()
    for i in a:
        get_big_data_list.append(i)
    return get_big_data_list

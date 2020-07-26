import pandas as pd
import numpy as np
import pymysql
from conmitdb import DatabaseAccess


db = DatabaseAccess() # 实例化数据库链接
post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
read =db.database_check(post_sql)

read1 = list(read)
dataFrame = pd.DataFrame(read1)

for i in range(5):
    col = dataFrame.iloc[:, i]
    col_max = col.value_counts().iloc[:12]
    col_list = []
    col_list.append(col_max)
    col_lists = pd.DataFrame(col_list)
    cont = i+1
    print("第%s列为"%cont,'\n',col_max,"\n","================")
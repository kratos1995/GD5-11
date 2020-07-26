import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from conmitdb import DatabaseAccess
from openpyxl import workbook
from openpyxl import load_workbook
import os
import xlwt
# import matplotlib.pyplot as plt
# %matplotlib inline


db = DatabaseAccess() # 实例化数据库链接
post_sql = "SELECT draw_number_01,draw_number_02,draw_number_03,draw_number_04,draw_number_05 from GD511;"
read_data =db.database_check(post_sql)
read_data = list(read_data)

sum_list = ['1','2','3','4','5','6','7','8','9','10','11'] # 所有号码集合
sum_list = list(map(int, sum_list))# 将sum_list里的元素转换为 int 类型

dataFrame = pd.DataFrame(read_data)
cols_name = dataFrame.values.tolist()

dir = os.path.abspath('.').split('\\ModuLe')[0]
dir = dir+"\static\excel\\差异统计.xls"
sheeet_name='差异统计'





distance_data = []
class Rec_list(object):
    def __init__(self,sum_list,list1_name):
        self.sum_list = sum_list
        self.list1_name = list1_name
        for i in self.list1_name:
            if isinstance(i,list):
                sum_list_set = set(self.sum_list)
                print(i,'这是arr')
                for k in self.sum_list:
                    if k in i:
                        print(k,": 存在。")
                        distance_data.append(k)
                        pass
                    else:
                        distance_data.append("0")
                        print(k, ":不存在。")

def write_excel():
    #distance_data = list(map(str, distance_data))# 将sum_list里的元素转换为 str 类型
    len_distance_data = len(distance_data)  # 获取中奖号码长度
    len_distance_data = len_distance_data / 11  # 用总长度除以5，得到纵向长度
    print(len(distance_data))
    arr_data = np.array(distance_data).reshape(int(len_distance_data), 11)

    # excel表头
    table_head= ["期号占位",'1','2','3','4','5','6','7','8','9','10','11']
    f = xlwt.Workbook()
    # 字体样式
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = True  # 黑体
    # font.underline = True  # 下划线
    # font.italic = True  # 斜体字
    style.font = font  # 设定样式
    # 颜色
    pattern = xlwt.Pattern()  # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 5  # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    colours = xlwt.XFStyle()  # Create the Pattern
    colours.pattern = pattern  # Add Pattern to Style

    # 边框
    borders = xlwt.Borders()  # Create Borders
    borders.left = xlwt.Borders.THIN
    '''
    DASHED虚线
    NO_LINE没有
    THIN实线
    '''
    # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    borders.right = xlwt.Borders.DASHED
    borders.top = xlwt.Borders.DASHED
    borders.bottom = xlwt.Borders.DASHED
    borders.left_colour = 0x40
    borders.right_colour = 0x40
    borders.top_colour = 0x40
    borders.bottom_colour = 0x40
    frames = xlwt.XFStyle()  # Create Style
    frames.borders = borders  # Add Borders to Style

    # 设置sheet标题
    sheet1 = f.add_sheet('差异统计', cell_overwrite_ok=True)  # 创建sheet
    for i in range(len(table_head)):
        sheet1.write(0,i,table_head[i],style)
        sheet1.col(0).width = 6666# 设置单元格宽度
    f.save(dir)  # 保存文件

    # 迭代写入arr_data
    for row in range(len(arr_data)):
        for col in range(0,len(arr_data[row])):
            if arr_data[row][col] == "0":
                sheet1.write(row + 1, col + 1, arr_data[row][col])
            # print(row+1,col,arr_data[row][col])
            else:
                sheet1.write(row+1,col+1,arr_data[row][col],colours)
    f.save(dir)  # 保存文件

if __name__ =="__main__":


    Rec_list(sum_list, cols_name)
    write_excel()
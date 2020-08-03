# -*- coding: utf-8 -*-
import os
import xlwt
import time
from openpyxl import workbook
from openpyxl import load_workbook
import platform


a = ["haha","hahah","wodjwda"]
b = 1
c = "公式成立"
# dir = os.path.abspath('.').split('\\ModuLe')[0]
#dir = dir+"\static\excel\\配码表.xls"
dir
sys = platform.system()
if sys == "Windows":
    dir = os.path.abspath('.').split('\\ModuLe')[0]
    dir = dir + "\static\excel\\配码表.xls"
elif sys == "Linux":
    # linux_path = "/home/yy"
    # linux_filename = '配码表.xls'
    # dir = os.path.join(linux_path,linux_filename)
    dir = os.path.abspath('.').split('/ModuLe')[0]
    dir = dir + "/static/excel/配码表.xls"
else:
    pass
# if not os.path.exists(dir):
#     os.makedirs(dir)
table_head = ["公式成立",'相同的号码']


class write_excel(object):
    def __init__(self,local,table_headd,list_data):
        self.local = local
        self.table_headd = table_headd
        self.list_data = list_data
        f = xlwt.Workbook('utf-8')
        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN # 实线
        sheet1 = f.add_sheet('配码表', cell_overwrite_ok=True)  # 创建sheet
        sheet1.col(0).width = 6666  # 列  宽度
        i=0
        sheet1.write(i,i,self.table_headd)
        for j in range(len(list_data)):
            # list_data_str = str(self.list_data[j])
            # list_data_str.strip("\\[\\]")
            sheet1.write(j+i+1,self.local,str(self.list_data[j]))
        f.save(dir)  # 保存文件

# write_excel(b,c,a)


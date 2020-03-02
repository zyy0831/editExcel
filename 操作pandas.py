# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xlrd,os,xlwt
from openpyxl import load_workbook

def getTable(fileName_Path):
    f = pd.ExcelFile(fileName_Path) #读取excel文件
    table=f.sheet_names[0]  # 获取所有工作表sheet名称 f.sheet_names[0]

def getExcelName(data_path):
    for fileName in os.listdir(data_path):
        if ".xls" in fileName:
            #print(fileName)
            fileName_Path = os.path.join(data_path, fileName)#拼接路径
            #print(fileName_Path)
            getTable(fileName_Path)



if __name__=="__main__":
    path = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\新建文件夹'
    # path = input("请输入待处理文件\n")
    pathout = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\out'
    # pathout = input("请输入输出文件\n")
    getExcelName(path) 
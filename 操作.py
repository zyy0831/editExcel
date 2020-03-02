# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:05:34 2020

@author: 张吉智
"""

import os
# from sklearn import linear_model
import xlrd
import xlwt
import numpy as np
import pandas as pd

def getExcelName(path):
    # path = r'F:\张敏\大气表格数据\城市_20190101-20191231-xlsx'
    filenames = os.listdir(path)    
    for filename in filenames:
        # excel_path = 'F:\张敏\大气表格数据\城市_20190101-20191231-xlsx\\' + filename
        excel_path = os.path.join(path, filename)#拼接路径
        excel = xlrd.open_workbook(excel_path) #循环读取文件夹下所有excel文件
        deal(filename,excel,pathout)

def outPut(pathout,filename,result):
    data = pd.DataFrame(result)
    filename_head = filename.split('.')[0]
    exportName=filename_head+'Deal.xlsx'
    excel_pathout = os.path.join(pathout, exportName)#拼接路径
    writer = pd.ExcelWriter(excel_pathout)		# 写入Excel文件
    data.to_excel(writer, 'AQI', float_format='%.5f')		# ‘AQI’是写入excel的sheet名
    writer.save()
    writer.close()

def deal(filename,excel,pathout):
        table = excel.sheets()[0]#通过索引获取sheet
        rows=table.nrows #获取行数361
        cols=table.ncols #有效列数556 实际370
        sum = np.zeros((17,cols))
        #result = np.zeros(380)
        result = np.zeros((17,cols))

        for i in range(3, cols): #遍历列 
            for j in range(2, 17): #遍历行 
                for k in range(0,23):
                    ctype =table.cell(j+k*15,i).ctype#判断数据类型
                    if ctype == 0: # python读取excel中单元格的内容返回的有5种类型,0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                        data=0.0
                    elif ctype == 2:#数字一律按浮点型输出
                        data = table.cell(j+k*15,i).value #获取当前行列的内容,从第一行第一列是从0开始的
                    sum[j][i] += data
                result[j][i] = sum[j][i]/24
        
        outPut(pathout,filename,result)

if __name__=="__main__":
    path = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\新建文件夹'
    # path = input("请输入待处理文件\n")
    pathout = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\out'
    # pathout = input("请输入输出文件\n")
    getExcelName(path)        

#Row_values=table.row_values(i)   #获取整行内容

#Col_values=table.col_values(i)   #获取整列内容
  
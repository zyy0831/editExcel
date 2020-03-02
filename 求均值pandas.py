# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xlrd,os,xlwt
from openpyxl import load_workbook

def getLabel(labels,labelFin):
    ex1 = 'Unnamed'
    for label in labels:
        if (ex1 in label) or ('o' in label) or ('e' in label):
            result= label
        else:
            labelFin.append(label)
    return labelFin

def Deal(fileName,fileName_Path,sheetNameAll):
    filename_head = fileName.split('.')[0]
    date_filename=filename_head.split('_')[2]
    exportName=filename_head+'Deal.xlsx'
    outPath = os.path.join(pathout, exportName)#拼接路径
    writer = pd.ExcelWriter(outPath)	# 写入Excel文件
    for i in sheetNameAll:
        df = pd.read_excel(fileName_Path,sheet_name=i)   
        Types=['AQI','PM2.5','PM2.5_24h','PM10','PM10_24h','SO2','SO2_24h','NO2','NO2_24h','O3','O3_24h','O3_8h','O3_8h_24h','CO','CO_24h']
        for Type in Types: 
            outfile = df[(df['type']==Type)]
            labels = list(outfile.columns.values)
            labelFin=[]
            getLabel(labels,labelFin)
            # print(labelFin)
            col_mean = outfile[labelFin].mean()
            col_mean["type"] = "Avg"
            col_mean["date"] = date_filename
            outfile = outfile.append(col_mean,ignore_index=True)
            # outfile.loc[Type+'Row_sum'] = outfile.apply(lambda x: x.sum()) #求和
            outfile = outfile[outfile['type'].isin(['Avg'])]
            outfile.to_excel(writer, Type)		# ‘Type’是写入excel的sheet名
    writer.save()
    writer.close()

def getTable(fileName,fileName_Path):
    f = pd.ExcelFile(fileName_Path) #读取excel文件
    sheetNameAll=f.sheet_names  # 获取所有工作表sheet名称
    Deal(fileName,fileName_Path,sheetNameAll)

def getExcelName(data_path):
    for fileName in os.listdir(data_path):
        # if ".xls" in fileName:
        #print(fileName)
        fileName_Path = os.path.join(data_path, fileName)#拼接路径
        #print(fileName_Path)
        getTable(fileName,fileName_Path)

if __name__=="__main__":
    path = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\城市_20190101-20191231-xlsx'
    # path = input("请输入待处理文件\n")
    pathout = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\out'
    # pathout = input("请输入输出文件\n")
    getExcelName(path) 
    print('处理完成')
    
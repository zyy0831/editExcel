import pandas as pd
import numpy as np
import xlrd,os,xlwt
#from openpyxl import *
from openpyxl import load_workbook

orderCity=['北京市','蓟州区','邯郸市','呼和浩特市','上海市','苏州市','常州市','南通市','扬州市','杭州市','金华市','湖州市','淮南市','蚌埠市','淮北市','福州市','泉州市','济南市','青岛市','临沂市','泰安市','郑州市','许昌市','洛阳市','商丘市','长沙市','广州市','深圳市','东莞市','南宁市','柳州市','重庆市','成都市','玉溪市','西安市']
#fileRefer = '城市顺序表.xlsx'

def auto_fill_merge_cell(df):
    #合并单元格 填充完毕
    cols=[
        c
        for c in df.columns
        if pd.api.types.is_string_dtype(df[c])
    ]
    df[cols]=df[cols].ffill()
    return df

def order(f_n,sheetNameAll,export): 
    #对每个sheet表，按照城市顺序进行排序       
    for i in sheetNameAll:
        df = pd.read_excel(f_n,sheet_name=i)
        if i=='存量排查' or i=='领导小组':
            df = auto_fill_merge_cell(df)
        df['城市顺序']=pd.Categorical(df['城市'],orderCity) #Categorical 实例化指定顺序
        #print(df.columns) #读取df文件的列名
        if i=='领导小组':
            finishDf=df.sort_values(by = ['城市顺序','成员岗位'], ascending = [True,True])
        else:
            finishDf=df.sort_values(by = ['城市顺序','发布时间'], ascending = True)
        #print('1')
        df2 = pd.read_excel(fileRefer)
        finishDf=pd.merge(finishDf,df2)
        finishDf.to_excel(export, i)  #将finishDf的内容写入export文件的 i 表中
    export.save()#文件保存
    export.close()#文件关闭

def adjust(f_n,sheetNameAll):

  #获取所有sheet的最大行数与最大列数
    fileNameAd_rd = xlrd.open_workbook(f_n)
    rowMaxNum=[]
    colMaxNum=[]
    for i in range(fileNameAd_rd.nsheets):
        adSheet = fileNameAd_rd.sheet_by_index(i)
        rowMaxNum.append(adSheet.nrows) #最大行数
        colMaxNum.append(adSheet.ncols) #最大列数
    rowMaxNum_Arr=np.array(rowMaxNum)
    colMaxNum_Arr=np.array(colMaxNum)  # 列表转数组
    # print(rowMaxNum_Arr[0])

  # 基于最大行数与最大列数，将最后一列数值 =》赋值到第二列
    fileNameAd_pyxl = load_workbook(f_n)
    num=0
    for i in sheetNameAll:
        ws = fileNameAd_pyxl[i]
        b=[]
        shRowMax=rowMaxNum_Arr[num]
        shColMax=colMaxNum_Arr[num]
        j=1
        while j < shRowMax:
            j = j+1
            b.insert(j, ws.cell (j,shColMax).value)
            ws.cell (j,2).value = b[j-2]
        num=num+1
        # 删除第一列与最后两列
        ws.delete_cols(shColMax-1,2)
        ws.delete_cols(1)

    fileNameAd_pyxl.save(f_n) 

def auto_order_monthData(fileName):
    #print('Loading')
    f = pd.ExcelFile(fileName) #读取excel文件
    sheetNameAll=f.sheet_names  # 获取所有工作表sheet名称
    filename_head = fileName.split('.')[0]
    exportName=filename_head+'Order.xlsx'
    export = pd.ExcelWriter(exportName)#创建数据存放路径
    
    order(fileName,sheetNameAll,export)
    
    #print(exportName)
    
    adjust(exportName,sheetNameAll)
    print('恭喜！已完成处理')

def getExcelName(data_path):
    
    for fileName in os.listdir(data_path):
        if ".xls" in fileName:
            #print(fileName)
            fileName_Path = os.path.join(data_path, fileName)#拼接路径
            #print(fileName_Path)
            auto_order_monthData(fileName_Path)

def main():
    flag_f=input('是否以文件夹形式上传，请输入：y或n\n')
    if flag_f=='y' :
        data_path = input("请拖动上传待处理文件夹\n")
        getExcelName(data_path)
    else:
        fileName=input("请拖动上传待处理xls文件\n")
        auto_order_monthData(fileName)
    flag_main=input('是否继续处理，请输入：y或n\n')
    if flag_main=='y' :
        return main()
    else:
        print('祝生活愉快')
#========================================================================================================    
if __name__=="__main__":
    fileRefer = input("请输入城市顺序表.xls文件\n")
    main()
        



 

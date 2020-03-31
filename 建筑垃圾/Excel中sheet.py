import os,xlrd
 
#data_path = os.path.join(r'C:\Users\zyy\Desktop\建筑垃圾\试点城市总结报告上报情况','data')
#os.path.join()函数：连接两个或更多的路径名
data_path = r'C:\Users\zyy\Desktop\建筑垃圾\试点城市总结报告上报情况'
print(data_path)
 
#获取目录下所有Excel中sheet
def getTables():
    print(os.listdir(data_path))
    for excel in os.listdir(data_path):#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        print(excel)
        if ".xls" in excel:
            excelPath = os.path.join(data_path, excel)#拼接路径
            print(excelPath)
            excels = xlrd.open_workbook(excelPath)
            sheetNames = excels.sheet_names()#获取目录下所有sheet的名字，sheetNames为list类型
            print('sheetNames:',sheetNames)
            # 循环从sheetNames中读取sheet表，返回的是sheet的内存地址
            for sheet in sheetNames:
                table = excels.sheet_by_name(sheet)
            print('table:',table)
            data=[]
            for i in range(2, table.nrows):
                data.append(dict(zip(table.row_values(1), table.row_values(i))))
            print('读取出的data:',data)
#从getTables()中返回的table中提取数据，sheet中的数据组成一个列表，Excel中的表头和数据分别组成key:value的格式
 
getTables()

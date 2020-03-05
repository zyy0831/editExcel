import pandas as pd
import os

def getLabel(labels,labelFin):
    ex1 = 'Unnamed'
    for label in labels:
        if (ex1 in label) or ('y' in label)or ('h' in label):
            a=1
        else:
            labelFin.append(label)
    return labelFin

def delNull(fileName_Path,fileName,pathout):
    f = pd.ExcelFile(fileName_Path) #读取excel文件
    sheetNameAll=f.sheet_names  # 获取所有工作表sheet名称
    filename_head = fileName.split('.')[0]
    exportName=filename_head+'.xlsx'
    outPath = os.path.join(pathout, exportName)#拼接路径
    writer = pd.ExcelWriter(outPath)	# 写入Excel文件
    num = 1
    for i in sheetNameAll:
        df = pd.read_excel(fileName_Path,sheet_name=i)
        labels = list(df.columns.values) 
        labelFin=[]
        getLabel(labels,labelFin)
        _df = df[labelFin]
        print(labelFin)
        _df.to_excel(writer, i)
        print(i + "  保存成功！共%d个，第%d个。" % (len(sheetNameAll),num))
        num += 1
    writer.save()
    writer.close()


def getExcelName(data_path,pathout):
    for fileName in os.listdir(data_path):
        if '.xlsx' in fileName:
            fileName_Path = os.path.join(data_path, fileName)#拼接路径
            delNull(fileName_Path,fileName,pathout)

if __name__=="__main__":
    path = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\finn'
    # path = input("请输入待处理文件\n")
    pathout = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\a'
    getExcelName(path,pathout)

import pandas as pd
 
def main(fileName):
    df = pd.read_excel(fileName)
    print(df)
    df1 = pd.read_excel(fileName,sheet_name='Sheet1')
    print(df1)
    df1 = pd.read_excel(fileName,sheet_name='Sheet1', index_col=0)
    print(df1)
    df = pd.read_excel(fileName, sheet_name='Sheet1', header=None, skiprows=1, usecols='B,D')
    print(df1)
 
if __name__=="__main__":
    fileName = input("请输入excel文件\n")
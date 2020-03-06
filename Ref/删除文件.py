'''
@Author: zyy
@Date: 2020-03-02 09:15:43
@LastEditTime: 2020-03-06 16:18:09
@LastEditors: Please set LastEditors
@Description: 删除指定文件夹内包含233关键词的文件
'''

import os

def delFile(folderPath):
    for fileName in os.listdir(folderPath):
        if "233" in fileName:
            fileName_Path = os.path.join(folderPath, fileName) #拼接路径
            print(fileName_Path)
            os.remove(fileName_Path)   # 删除文件
    print("已删除")

if __name__=="__main__":
    folderPath = input("请输入待处理文件夹\n")
    delFile(folderPath)



# path = "D:\\hello.py"
# if(os.path.exists(path)):   # 判断文件是否存在
#     os.remove(path)   # 删除文件
    
# path = "D:\\hello"
# if(os.path.exists(path)):   # 判断文件夹是否存在  
#     os.removedirs(path)   # 删除文件夹
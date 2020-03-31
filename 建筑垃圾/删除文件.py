import os

# path = "D:\\hello.py"
# if(os.path.exists(path)):   # 判断文件是否存在
#     os.remove(path)   # 删除文件
    
# path = "D:\\hello"
# if(os.path.exists(path)):   # 判断文件夹是否存在  
#     os.removedirs(path)   # 删除文件夹

data_path = r'C:\Users\zyy\Desktop\1'
for fileName in os.listdir(data_path):
    if "Order" in fileName:
        fileName_Path = os.path.join(data_path, fileName)#拼接路径
        fileName_Path2 = os.path.join(data_path, '11')#拼接路径,形成新文件夹
        print(fileName_Path,fileName_Path2)
        os.remove(fileName_Path)   # 删除文件

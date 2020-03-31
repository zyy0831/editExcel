# -*- coding: utf-8 -*-
import pandas as pd
from openpyxl import load_workbook
import os,shutil
import threading

def main(folderPath,pathout,newFileName):
    t1 = threading.Thread(target=duo,args=(folderPath,pathout,newFileName))
    t1.start()

def duo(folderPath,pathout,newFileName):
    # 获取excel文件路径
    xlsx_names=[]
    for fileName in os.listdir(folderPath):
        fileName = os.path.join(folderPath, fileName)#拼接路径
        xlsx_names.append(fileName)
    # 将excel中的sheet名称放入列表
    sheet_names = ['AQI','PM2.5','PM2.5_24h','PM10','PM10_24h','SO2','SO2_24h','NO2','NO2_24h','O3','O3_24h','O3_8h','O3_8h_24h','CO','CO_24h']
    sheet_cols=['date','北京', '天津', '石家庄', '唐山', '秦皇岛', '邯郸', '保定', '张家口', '承德', '廊坊', '沧州', '衡水', '邢台', '太原', '呼和浩特', '沈阳', '大连', '长春', '哈尔滨', '上海', '南京', '苏州', '南通', '连云港', '徐州', '扬州', '无锡', '常州', '镇江', '泰州', '淮安', '盐城', '宿迁', '杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '台州', '舟山', '金华', '衢州', '丽水', '合肥', '福州', '厦门', '南昌', '济南', '青岛', '郑州', '武汉', '长沙', '广州', '深圳', '珠海', '佛山', '中山', '江门', '东莞', '惠州', '肇庆', '南宁', '海口', '重庆', '成都', '贵阳', '昆明', '拉萨', '西安', '兰州', '西宁', '银川', '乌鲁木齐', '湘潭', '株洲', '包头', '鄂尔多斯', '营口', '盘锦', '泉州', '莱芜', '临沂', '德州', '聊城', '滨州', '淄博', '枣庄', '烟台', '潍坊', '济宁', '泰安', '日照', '威海', '东营', '韶关', '汕头', '湛江', '茂名', '梅州', '汕尾', '阳江', '清远', '潮州', '云浮', '玉溪', '菏泽', '大同', '长治', '临汾', '阳泉', '赤峰', '鞍山', '抚顺', '本溪', '锦州', '吉林', '齐齐哈尔', '牡丹江', '大庆', '芜湖', '马鞍山', '九江', '洛阳', '安阳', '开封', '焦作', '平顶山', '三门峡', '宜昌', '荆州', '岳阳', '常德', '张家界', '桂林', '北海', '柳州', '三亚', '绵阳', '宜宾', '攀枝花', '泸州', '自贡', '德阳', '南充', '遵义', '曲靖', '咸阳', '铜川', '延安', '宝鸡', '渭南', '金昌', '嘉峪关', '石嘴山', '克拉玛依', '库尔勒', '寿光', '章丘', '即墨', '胶南', '胶州', '莱西', '平度', '蓬莱', '招远', '莱州', '荣成', '文登', '乳山', '吴江', '昆山', '常熟', '张家港', '太仓', '句容', '江阴', '宜兴', '金坛', '溧阳', '海门', '临安', '富阳', '义乌', '诸暨', '瓦房店', '信阳', '周口', '漳州', '晋城', '朔州', '晋中', '运城', '忻州', '吕梁', '乌海', '通辽', '呼伦贝尔', '巴彦淖尔', '乌兰察布', '兴安盟', '锡林郭勒盟', '阿拉善盟', '阜新', '铁岭', '四平', '辽源', '通化', '白山', '松原', '白城', '延边州', '鸡西', '鹤岗', '双鸭山', '伊春', '佳木斯', '七台河', '黑河', '绥化', '大兴安岭地区', '蚌埠', '淮南', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '六安', '亳州', '池州', '宣城', '莆田', '三明', '南平', '龙岩', '宁德', '景德镇', '萍乡', '新余', '鹰潭', '赣州', '吉安', '宜春', '抚州', '上饶', '鹤壁', '新乡', '濮阳', '许昌', '漯河', '南阳', '商丘', '驻马店', '黄石', '十堰', '鄂州', '荆门', '孝感', '黄冈', '咸宁', '随州', '恩施州', '衡阳', '邵阳', '益阳', '郴州', '永州', '怀化', '娄底', '湘西州', '梧州', '防城港', '钦州', '贵港', '玉林', '百色', '贺州', '河池', '来宾', '崇左', '广元', '遂宁', '内江', '乐山', '眉山', '广安', '达州', '雅安', '巴中', '资阳', '阿坝州', '甘孜州', '凉山州', '六盘水', '安顺', '铜仁地区', '毕节', '黔西南州', '黔东南州', '黔南州', '保山', '昭通', '丽江', '临沧', '楚雄州', '红河州', '文山州', '西双版纳州', '大理州', '德宏州', '怒江州', '迪庆州', '昌都地区', '山南地区', '日喀则地区', '那曲地区', '阿里地区', '林芝地区', '汉中', '榆林', '安康', '商洛', '白银', '天水', '武威', '张掖', '平凉', '酒泉', '庆阳', '定西', '陇南', '临夏州', '甘南州', '海东地区', '海北州', '黄南州', '海南州', '果洛州', '玉树州', '海西州', '吴忠', '中卫', '固原', '吐鲁番地区', '哈密地区', '昌吉州', '博州', '阿克苏地区', '喀什地区', '和田地区', '伊犁哈萨克州', '塔城地区', '阿勒泰地区', '石河子', '五家渠', '克州', '普洱', '襄阳', '葫芦岛', '河源', '揭阳', '辽阳', '朝阳', '丹东']
    # 设置excel输出路径
    outPath = os.path.join(pathout, newFileName + '.xlsx')#拼接路径
    writer = pd.ExcelWriter(outPath,engine='openpyxl')
    num = 1
    for sheet_name in sheet_names:
        df = None
        for xlsx_name in xlsx_names:
            print('1')
            _df = pd.read_excel(xlsx_name, sheet_name=sheet_name, usecols=sheet_cols)
            # _df = _df[_df['type'].isin(['Avg'])]
            # print(rowVal)
            if df is None:
                df = _df
            else:
                df = pd.concat([df, _df], ignore_index=True)
        # 下面的保存文件处填写writer，结果会不断地新增sheet，避免循环时被覆盖
        df.to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="utf-8", index=False)
        print(sheet_name + "  保存成功！共%d个，第%d个。" % (len(sheet_names),num))
        num += 1
    writer.save()
    writer.close()

def Deal(folderPathArr):
    for folderpath in folderPathArr:
        folderPath = folderpath
        newFileName = folderpath[-6:] #截取倒数第三位到结尾
        main(folderPath,pathout,newFileName)
        

def mkdir(file):
    folder = os.path.exists(file)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(file)            #makedirs 创建文件时如果路径不存在会创建这个路径
        # print("---  new folder...  ---")
    else:
        a = 0
        # print( "---  There is this folder!  ---")

def moveFile(path):
    # 这个是文件和文件夹所在目录
    for folderName, subfolders, filenames in os.walk(path):
        for subfolder in subfolders:
            for filename in filenames:
                #这个是用来对比文件和文件夹的前20个字符，如果一样，就移动
                if subfolder in filename:
                    #这个try一定要有的，因为不加的话，一旦出错了，就不继续执行了
                    try:
                        shutil.move(folderName + '\\'+ filename, folderName + '\\'+ subfolder) #shutil.move("oldpos","newpos")   
                    except OSError:
                        pass

if __name__=="__main__":
    n = 0
    path = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\out'
    pathout = r'c:\Users\zyy\Desktop\气象\城市_20190101-20191231-xlsx\fin'
    #创建文件夹
    dateArr=['201901','201902','201903','201904','201905','201906','201907','201908','201909','201910','201911','201912']
    folderPathArr=[]
    for i in dateArr:
        file = os.path.join(path, i)
        folderPathArr.append(file)
        mkdir(file)   
    moveFile(path)
    Deal(folderPathArr)
    print('处理完成')
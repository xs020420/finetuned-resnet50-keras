import cv2
from glob import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy
import xlrd

def read_excel(path):
    # 打开文件
    workbook = xlrd.open_workbook(path)
    # 获取所有sheet
    print(workbook.sheet_names())

def img_distribution(path,data):
    print("Distribution is being calculated ...")
    height_global = []
    width_global = []
    height_shape = 0
    width_shape =0
    error_number = 0
    for item in data:
        try:
            img = cv2.imread(item)
            height_shape = img.shape[0]
            width_shape = img.shape[1]
            height_global.append(height_shape)
            width_global.append(width_shape)
        except:
            print(item)
            cv2.imwrite("./1.jpg",img)
            error_number=error_number+1

    print(" Calculation  End")

    height_bins = np.linspace(min(height_global), max(width_global), 20)
    width_bins = np.linspace(min(height_global), max(width_global), 20)

    plt.figure(1)
    plt.hist(height_global,height_bins)
    plt.xlabel('Number of value')
    plt.ylabel('Number of occurences')
    plt.title('Frequency distribution of height of '+dataset_name)

    plt.figure(2)
    plt.hist(width_global, width_bins)
    plt.xlabel('Number of value')
    plt.ylabel('Number of occurences')
    plt.title('Frequency distribution of width of '+dataset_name)

    plt.show()

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self,path_scr,path_dst):
        self.path_scr = path_scr  #表示需要命名处理的文件夹
        self.path_dst = path_dst
    def rename(self):
        filelist = os.listdir(self.path_scr) #获取文件路径
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            #if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
            src = os.path.join(os.path.abspath(self.path_scr), item)
            dst = os.path.join(os.path.abspath(self.path_dst), ''+str(i) + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
            #dst = os.path.join(os.path.abspath(self.path), '0000' + format(str(i), '0>3s') + '.jpg')    这种情况下的命名格式为0000000.jpg形式，可以自主定义想要的格式
            # try:
            os.rename(src, dst)
            print('converting %s to %s ...' % (src, dst))
            i = i + 1

            # except:
            #     continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    beforerename = "D:\ly\DCGAN-tensorflow-master\data\street"
    afterrename = r"D:\ly\DCGAN-tensorflow-master\data\rename"
    #demo = BatchRename(beforerename,afterrename)
    #demo.rename()







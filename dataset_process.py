"""
for fashionstyle14 dataset process
according to the excel, spit the dataset to
"""
import cv2
from glob import glob
import os
import matplotlib.pyplot as plt
import numpy as np
from  utils import *
import pandas as pd
import pandas


#list out all catagories of  dataset

catagories_list = []
for root, dirs, files in os.walk("../../fashionDataset/FashionStyle14_v1/dataset", topdown=False):
    for name in dirs:
        path = os.path.join(root, name)
        catagories_list.append(path)
print(catagories_list)

# split dataset according into train,valid,test
csv_raw = pd.read_csv("../../fashionDataset/FashionStyle14_v1/val.csv",header=None, names=['val'])
csv_output = csv_raw.applymap(lambda x: "../../"+x)

catagories_dict={}
for item in csv_output['val']:
    try:
        path_split,file_split = os.path.split(item)
    except:
        print("error")
        continue
    print(path_split,file_split)
    if path_split not in catagories_dict.keys():
        catagories_dict[path_split] = 1
    else:
        catagories_dict[path_split] = catagories_dict[path_split]+1
print(catagories_dict)




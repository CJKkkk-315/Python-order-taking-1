# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:06:40 2022

@author: Lenovo
"""
from osgeo import gdal, ogr, gdal_array # 读取数据
import numpy as np # 数组处理
import matplotlib.pyplot as plt # 显示图像
from sklearn.ensemble import RandomForestClassifier # 引入随机森林模型
import pandas as pd 
import cv2
from sklearn.metrics import classification_report, accuracy_score,confusion_matrix  # 精度评价
import seaborn as sn #seaborn是在matplotlib基础上面的封装，方便直接传参数调用
import datetime#获取时间和日期
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
np.set_printoptions(threshold=np.inf)

def get_data(in_file):
    #让GDAL抛出Python异常，并注册所有驱动程序
    gdal.UseExceptions()
    gdal.AllRegister()
    dataset = gdal.Open(in_file)
    im_proj = dataset.GetProjection()
    im_geotrans = dataset.GetGeoTransform()
    im_data = dataset.ReadAsArray()
    im_width = dataset.RasterXSize
    im_height = dataset.RasterYSize
    im_bands = dataset.RasterCount
    band = dataset.GetRasterBand(1)
    datatype = band.DataType
    
    return im_proj,im_geotrans, im_data,im_width,im_height,im_bands,datatype

def save_data(out_file,im_width,im_height,im_bands,datatype,im_proj,im_geotrans):
    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(out_file,im_width,im_height,im_bands,datatype)
    dataset.SetProjection(im_proj)
    dataset.SetGeoTransform(im_geotrans)
    if im_bands == 1:
        dataset.GetRasterBand(1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i + 1).WriteArray(im_data[i])
    del dataset
if __name__ == '__main__':
    in_file = 'E:\我的下载毕设\RFC\GF_2.tif'
    
    [im_proj,im_geotrans, im_data,im_width,im_height,im_bands,datatype] = get_data(in_file)
    
    b = im_data[0,:, :]
    g = im_data[1,:, :]
    r = im_data[2,:, :]
    img_rgb = cv2.merge([r,g,b])
    plt.imshow(img_rgb)
    plt.title('原始图像')
    out_file = 'E:\\我的下载毕设\\RFC\\results\\result1_GF2.tif'
    print('ok')

    
    
    
    
    
    
    
    
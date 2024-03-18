# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:53:34 2021

@author: Lenovo
"""
#需要的库
import numpy as np
from sklearn import cluster
1
from osgeo import gdal, gdal_array
import matplotlib.pyplot as plt
#import sys
def main(argv1, argv2):
# 解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 让GDAL抛出Python异常，并注册所有驱动程序
    gdal.UseExceptions()
    gdal.AllRegister()
    # In[1]:
    # 单一波段分类 
    
    # 栅格文件读取，使用高分二遥感影像
    
    img_rs = argv1
    img_result = argv2
    ## 打开原始图像栅格数据集
    img_ds = gdal.Open(img_rs, gdal.GA_ReadOnly)
    # 获取图像的高度（y方向上的像素个数），宽度（x方向上的像素个数），波段数
    img_dss = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
    # 将波段数据写入数组
                   gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
    for b in range(img_dss.shape[2]):
        img_dss[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
    row = img_ds.RasterYSize #行
    col = img_ds.RasterXSize #列
    band_number = img_ds.RasterCount #波段数
    # 输出图像尺寸大小（行*列）
#    print('图像大小: {} x {} (行 x 列)'.format(row, col))
#    # 输出波段数
#    print('波段数: {}'.format(band_number))
    # 获取第一个波段数据   
    band = img_ds.GetRasterBand(1)
    # 将img_ds转化为一个numpy数组
    img = band.ReadAsArray()
    #print(img.shape)
    # 将数据展平为行（未知长度），并将列的值保持为1
    X = img.reshape((-1,1))
    print(X.shape)
    # 对数据运行k-means分类器
    # 选择6个分类集群
    # 拟合到定义的数据X中
    # 此分类过程耗时比较长
    k_means = cluster.KMeans(n_clusters=6)#生成的聚类数
    k_means.fit(X)
    #print("轮廓系数：",metrics.silhouette_score(X,labels,metric='euclidean'))
    # 给拟合的结果分配一个新变量X_Cluster
    X_cluster = k_means.labels_
    #metrics.silhouette_score(X, X_cluster, metric='euclidean')
    # 重新调整原始图像的尺寸
    X_cluster = X_cluster.reshape(img.shape)
#    print('分类结果显示')
     # 可视化数据 
     #plt.figure (figsize =(5,5) )#窗口大小
    plt.subplot(121)
    plt.imshow(img_dss[:, :, 0], cmap="Greys_r")#灰色显示
    plt.title('原始图像')
    
    plt.subplot(122)
    plt.imshow(X_cluster,cmap = "rainbow")#颜色
    plt.title('分类结果')
    plt.show()
    #print("轮廓系数：",metrics.silhouette_score(X,labels,metric='euclidean'))
     ###########################################
    
    #from sklearn.cluster import KMeans
    #kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
    #labels = kmeans_model.labels_
    
    
    
    
    
    
    
    
    
    
    # In[2]:
    # 多波段分类
    # 栅格文件读取
    #img_ds = gdal.Open('E:/我的下载毕设/RFC/GF_2.tif', gdal.GA_ReadOnly)
    #
    ## 将多波段图像加载到numpy中(最快的方法)
    #img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
    #               gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
    #
    #for b in range(img.shape[2]):
    #    img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
    #
    #new_shape =(img.shape [0] * img.shape [1],img.shape [2])
    #
    ## GF2有4个波段，将列重塑保持为4
    #X = img[:, :, :4].reshape(new_shape)
    #
    #k_means = cluster.KMeans(n_clusters=4)
    #k_means.fit(X)
    #X_cluster = k_means.labels_
    #X_cluster = X_cluster.reshape(img[:, :, 0].shape)
    #
    #plt.figure(figsize=(10,10))
    #plt.imshow(X_cluster, cmap="rainbow")
    #plt.show()
    
    
#     In[3]
#    图像保存
    ds = gdal.Open(img_rs)
    band = ds.GetRasterBand(1)
    arr = band.ReadAsArray()
    [cols, rows] = arr.shape
    
    format = "gtiff"
    driver = gdal.GetDriverByName(format)
    
    #创建图层（结果，行，列，波段，存储类型）
    outDataRaster = driver.Create(img_result, rows, cols, 1, gdal.GDT_UInt16)
    #写入仿射变换参数
    outDataRaster.SetGeoTransform(ds.GetGeoTransform()) 
    #写入投影
    outDataRaster.SetProjection(ds.GetProjection()) 
    #写入数组数据
    outDataRaster.GetRasterBand(1).WriteArray(X_cluster)
    outDataRaster.FlushCache()
    del outDataRaster

if __name__ == "__main__":

    img_rs = 'E:\\我的下载毕设\\RFC\\GF_2.tif'#原始数据
    img_result = "E:\\我的下载毕设\\RFC\\results\\k_means6.tif"#分类结果
    main(img_rs,img_result)












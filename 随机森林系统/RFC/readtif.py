# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:58:44 2022

@author: Lenovo
"""
def read_data():
    # packages
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
    #让GDAL抛出Python异常，并注册所有驱动程序
    gdal.UseExceptions()
    gdal.AllRegister()
    
    
    # - 输入数据 
    
    # In[3]:
    
    
    # 定义树（默认值=500） 
    est = 500
    n_cores = -1 #拟合和预测过程中并行运用的作业数量。如果为-1，则作业数设置为处理器的core数。
    # 待分类影像
    img_RS = 'E:\\我的下载毕设\\RFC\\GF_2.tif'
    # 训练样本
    training = 'E:\\我的下载毕设\\RFC\\train1.shp'
    # 验证样本
    validation = 'E:\\我的下载毕设\\RFC\\validation1.shp'
    # 属性表类别字段名
    attribute = 'class'
    # 图像结果保存路径
    classification_image = 'E:\\我的下载毕设\\RFC\\results\\result2_GF2.tif'
    # 文本结果保存路径
    results_txt = 'E:\\我的下载毕设\\RFC\\results\\result2_GF2.txt'
    
    
    # In[4]:
    
    
    # 加载训练样本，显示所有属性字段
    # 读取训练样本矢量数据
    shape_dataset = ogr.Open(training)
    # 获取图层对象
    shape_layer = shape_dataset.GetLayer()
    # 提取图层中所有属性字段
    attributes = []
    ldefn = shape_layer.GetLayerDefn()
    for n in range(ldefn.GetFieldCount()):
        fdefn = ldefn.GetFieldDefn(n)
        attributes.append(fdefn.name)
        
    # 输出所有属性
    #print('Available attributes in the shape file are: {}'.format(attributes)) #format:格式化函数，该函数把字符串当一个模板，通过传入的参数进行格式化，并且使用大括号“{}”作为特殊字符代替“%”
    
    
    # -数据获取
    
    # In[5]:
    
    
    # 输出文本文件
    # 标题
    print('随机森林分类', file=open(results_txt, "a"))
    # 创建时间
    print('创建时间: {}'.format(datetime.datetime.now()), file=open(results_txt, "a"))
    # 下划线
    print('-------------------------------------------------', file=open(results_txt, "a"))
    # 数据输入输出路径
    print('路径:', file=open(results_txt, "a"))
    # 待分类tif路径
    print('影像: {}'.format(img_RS), file=open(results_txt, "a"))
    # 训练样本矢量路径
    print('训练样本: {}'.format(training) , file=open(results_txt, "a"))
    # 验证样本矢量路径
    print('验证样本: {}'.format(validation) , file=open(results_txt, "a"))
    # 属性表中的字段名称
    print('属性字段名称: {}'.format(attribute) , file=open(results_txt, "a"))
    # 分类结果生成tif文件路径
    print('分类结果: {}'.format(classification_image) , file=open(results_txt, "a"))
    # 分类结果生成文本文件路径
    print('结果文件: {}'.format(results_txt) , file=open(results_txt, "a"))
    # 下划线
    print('-------------------------------------------------', file=open(results_txt, "a"))
    
    
    # In[6]:
    
    # 加载影像
    
    # 打开原始图像栅格数据集
    img_ds = gdal.Open(img_RS, gdal.GA_ReadOnly)
    # 获取图像的高度（y方向上的像素个数），宽度（x方向上的像素个数），波段数
    img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),
    # 将波段数据写入数组
    gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))
    for b in range(img.shape[2]):
        img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
    
    
    # In[7]:
    
    
    row = img_ds.RasterYSize #行
    col = img_ds.RasterXSize #列
    band_number = img_ds.RasterCount #波段数
    # 输出图像尺寸大小（行*列）
    print('图像大小: {} x {} (行 x 列)'.format(row, col))
    # 输出波段数
    print('波段数: {}'.format(band_number))
    # 文本中输出图像尺寸大小（行*列）
    print('图像大小: {} x {} (行 x 列)'.format(row, col), file=open(results_txt, "a"))
    # 文本中输出波段数
    print('波段数: {}'.format(band_number), file=open(results_txt, "a"))
    # 下划线
    print('---------------------------------------', file=open(results_txt, "a"))
    # 训练样本设置参数
    print('训练样本', file=open(results_txt, "a"))
    # 树的数量
    print('决策树的数量: {}'.format(est), file=open(results_txt, "a"))
    
    
    # In[8]:
    
    
    # 加载训练样本
    
    # 打开训练样本矢量文件
    shape_dataset = ogr.Open(training)
    # 获取图层对象
    shape_layer = shape_dataset.GetLayer()
    # 存的数据格式（GDAL库中提供了一种内存文件格式——MEM，MEM文件支持几乎所有的空间数据信息，包括投影，坐标，GCP，元数据等信息）
    mem_drv = gdal.GetDriverByName('MEM')
    # 获取图像宽，高，波段，定义格式
    mem_raster = mem_drv.Create('',img_ds.RasterXSize,img_ds.RasterYSize,1,gdal.GDT_UInt16)
    # 写入投影
    mem_raster.SetProjection(img_ds.GetProjection())
    # 写入仿射变换参数
    mem_raster.SetGeoTransform(img_ds.GetGeoTransform())
    # 写入数组数据
    mem_band = mem_raster.GetRasterBand(1)
    mem_band.Fill(0)
    mem_band.SetNoDataValue(0)
    # 字段名你
    att_ = 'ATTRIBUTE='+attribute
    # 创建栅格图层
    err = gdal.RasterizeLayer(mem_raster, [1], shape_layer, None, None, [1],  [att_,"ALL_TOUCHED=TRUE"])
    # assert断言函数，判断是否创建成功，成功则继续执行程序；否则抛出异常
    assert err == gdal.CE_None
    # 读取的栅格数据集
    roi = mem_raster.ReadAsArray()
    
    
    # In[9]:
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]
    img_rgb = cv2.merge([r,g,b])
    plt.imshow(img_rgb)
    plt.title('原始图像')
    
    
read_data()
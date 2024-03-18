# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:27:53 2022

@author: Lenovo
"""






import pickle  # 存放数据的模块
import tkinter as tk
import tkinter.messagebox
import os
#
import shutil
#
import tkinter as tk
#
from tkinter import *
#
from tkinter.filedialog import askopenfilename
#
from PIL import Image, ImageTk
def system():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Oct  7 09:58:58 2021

    @author: Lenovo
    """

    # - 需要的库和包

    # packages
    from osgeo import gdal, ogr, gdal_array  # 读取数据
    import numpy as np  # 数组处理
    import matplotlib.pyplot as plt  # 显示图像
    from sklearn.ensemble import RandomForestClassifier  # 引入随机森林模型
    import pandas as pd
    import cv2
    from sklearn.metrics import classification_report, accuracy_score, confusion_matrix  # 精度评价

    # import seaborn as sn #seaborn是在matplotlib基础上面的封装，方便直接传参数调用

    import datetime  # 获取时间和日期
    span_score = 0

    #
    def choosepic2():
        global span_score

        # 解决中文显示问题
        plt.rcParams['font.sans-serif'] = ['SimHei']

        plt.rcParams['axes.unicode_minus'] = False
        # 让GDAL抛出Python异常，并注册所有驱动程序
        gdal.UseExceptions()

        gdal.AllRegister()

        # - 输入数据

        # In[3]:

        # 定义树（默认值=500）
        est = 500
        n_cores = -1  # 拟合和预测过程中并行运用的作业数量。如果为-1，则作业数设置为处理器的core数。
        # 待分类影像
        global img_RS
        # 训练样本
        training = 'train1.shp'
        # 验证样本
        validation = 'validation1.shp'
        # 属性表类别字段名
        attribute = 'class'
        # 图像结果保存路径
        classification_image = 'result_GF2.tif'
        # 文本结果保存路径
        results_txt = 'result_GF2.txt'

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
        # print('Available attributes in the shape file are: {}'.format(attributes)) #format:格式化函数，该函数把字符串当一个模板，通过传入的参数进行格式化，并且使用大括号“{}”作为特殊字符代替“%”

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
        print('训练样本: {}'.format(training), file=open(results_txt, "a"))

        # 验证样本矢量路径
        print('验证样本: {}'.format(validation), file=open(results_txt, "a"))

        # 属性表中的字段名称
        print('属性字段名称: {}'.format(attribute), file=open(results_txt, "a"))

        # 分类结果生成tif文件路径
        print('分类结果: {}'.format(classification_image), file=open(results_txt, "a"))

        # 分类结果生成文本文件路径
        print('结果文件: {}'.format(results_txt), file=open(results_txt, "a"))

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
        b = img[:, :, 0]

        g = img[:, :, 1]

        r = img[:, :, 2]

        img_rgb = cv2.merge([r, g, b])

        # plt.imshow(img_rgb, cmap=plt.cm.Greys_r)
        # plt.savefig('1.png')
        # plt.title('原始图像')
        # plt.show()
        row = img_ds.RasterYSize  # 行

        col = img_ds.RasterXSize  # 列

        band_number = img_ds.RasterCount  # 波段数

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
        mem_raster = mem_drv.Create('', img_ds.RasterXSize, img_ds.RasterYSize, 1, gdal.GDT_UInt16)

        # 写入投影
        mem_raster.SetProjection(img_ds.GetProjection())

        # 写入仿射变换参数
        mem_raster.SetGeoTransform(img_ds.GetGeoTransform())

        # 写入数组数据
        mem_band = mem_raster.GetRasterBand(1)

        mem_band.Fill(0)

        mem_band.SetNoDataValue(0)

        # 字段名你
        att_ = 'ATTRIBUTE=' + attribute

        # 创建栅格图层
        err = gdal.RasterizeLayer(mem_raster, [1], shape_layer, None, None, [1], [att_, "ALL_TOUCHED=TRUE"])

        # assert断言函数，判断是否创建成功，成功则继续执行程序；否则抛出异常
        assert err == gdal.CE_None

        # 读取的栅格数据集
        roi = mem_raster.ReadAsArray()

        # In[9]:

        ## 显示图像
        ## 1代表行，2代表列，所以一共有2个图，1代表此时绘制第一个图
        # plt.subplot(121)
        ## 显示第一波段图片，并调用颜色函数这里用灰色显示
        # plt.imshow(img[:, :, 0], cmap=plt.cm.Greys_r)
        ## 标题
        # plt.title('原始图像')
        ## 1代表行，2代表列，所以一共有2个图，2代表此时绘制第二个图
        # plt.subplot(122)
        ## 显示栅格图像，彩色显示
        plt.imshow(roi, cmap=plt.cm.Spectral)

        # 标题
        plt.title('训练样本')

        plt.savefig('2.png')

        # plt.show()
        #
        # 训练样本像元数目
        n_samples = (roi > 0).sum()

        # 输出训练样本像元
        print('{n} 个训练样本像元'.format(n=n_samples))

        # 输出到文本
        print('{n} 个训练样本像元'.format(n=n_samples), file=open(results_txt, "a"))

        # 分类标签
        labels = np.unique(roi[roi > 0])

        # 输出标签
        print('训练数据包括 {n} 类: {classes}'.format(n=labels.size, classes=labels))

        # 输出到文本
        print('训练数据包括 {n} 类: {classes}'.format(n=labels.size, classes=labels), file=open(results_txt, "a"))

        # 训练图像数据集 = X
        # 训练样本的标签 = y
        X = img[roi > 0, :]

        y = roi[roi > 0]

        ## 输出X Y
        # print('X 矩阵的大小: {sz}'.format(sz=X.shape))
        # print('y 数组的大小: {sz}'.format(sz=y.shape))

        # - 训练随机森林模型

        # In[10]:

        # 随机森林模型参数（n_estimators=est：决策树的个数，oob_score=True：是否采用袋外样本来评估模型的好坏；袋外分数，事实上每次对有放回抽样，那么肯定存在一些样本没有被抽到，那么没有被抽到的样本称为袋外样本，用训练好的模型预测袋外样本所得到的分数
        # verbose ：控制构建数过程的冗长度，就是每隔多少输出一次信息；n_jobs ：设定fit和predict阶段并列执行的任务个数,如果设置为-1表示并行执行的任务数等于计算级核数;）
        rf = RandomForestClassifier(n_estimators=est, oob_score=True, verbose=1, n_jobs=n_cores)

        # verbose = 2 -> prints out every tree progression
        # rf = RandomForestClassifier(n_estimators=est, oob_score=True, verbose=2, n_jobs=n_cores)

        # 获取训练数据集
        X = np.nan_to_num(X)
        # 训练
        rf2 = rf.fit(X, y)

        # - 模型诊断

        # In[11]:

        # 通过模型拟合，可以查看 "Out-of-Bag" (OOB)预测分数：

        # 输出结果到文本
        print('--------------------------------', file=open(results_txt, "a"))

        print('模型训练和模型诊断:', file=open(results_txt, "a"))

        # 输出模型诊断精度指数
        print('预测的精度指数: {oob}%'.format(oob=rf.oob_score_ * 100))

        print('预测的精度指数: {oob}%'.format(oob=rf.oob_score_ * 100), file=open(results_txt, "a"))

        #  band importance:（波段特征重要性）
        bands = range(1, img_ds.RasterCount + 1)

        #  调用模型中特征重要性函数，输出每个波段的特征重要性
        for b, imp in zip(bands, rf2.feature_importances_):
            print('波段 {b} 特征重要性: {imp}'.format(b=b, imp=imp))
            print('波段 {b} 特征重要性: {imp}'.format(b=b, imp=imp), file=open(results_txt, "a"))

        #  建立交叉表（混淆矩阵）.
        #  导入Pandas库
        #  异常处理：可能存在的内存错误

        try:
            df = pd.DataFrame()  # 定义一个交叉表
            df['truth'] = y  # 表格y方向标题
            df['predict'] = rf.predict(X)  # x方向标题

        except MemoryError:
            print('不可用 ')

        else:
            # 交叉表预测
            #    print(pd.crosstab(df['truth'], df['predict'], margins=True))
            print(pd.crosstab(df['truth'], df['predict'], margins=True), file=open(results_txt, "a"))

        # In[12]:

        cm = confusion_matrix(y, rf.predict(X))  # 混淆矩阵（真实值，预测值）

        new_shape = (img.shape[0] * img.shape[1], img.shape[2])  # 高 宽 波段

        img_as_array = img[:, :, :np.int(img.shape[2])].reshape(new_shape)  # 三维转二维

        # 输出转化后的结果
        print('Reshaped from {o} to {n}'.format(o=img.shape, n=img_as_array.shape))

        # 获取转化后的图像数据集
        img_as_array = np.nan_to_num(img_as_array)

        # In[14]:

        # 预测每个像元
        # 在整个图像上尝试第一次预测
        # 如果内存不足，数据集将被切片处理
        try:
            class_prediction = rf.predict(img_as_array)
        except MemoryError:
            slices = int(round(len(img_as_array) // 2))

            test = True

            while test == True:
                try:
                    class_preds = list()

                    temp = rf.predict(img_as_array[0:slices + 1, :])
                    class_preds.append(temp)

                    for i in range(slices, len(img_as_array), slices):
                        print('{} %, derzeit: {}'.format((i * 100) // (len(img_as_array)), i))
                        temp = rf.predict(img_as_array[i + 1:i + (slices + 1), :])
                        class_preds.append(temp)

                except MemoryError as error:
                    slices = slices // 2
                    print('Not enought RAM, new slices = {}'.format(slices))

                else:
                    test = False
        else:
            print('Class prediction was successful without slicing!')

        try:
            class_prediction = np.concatenate(class_preds, axis=0)
        except NameError:
            #    print('No slicing was necessary!')

            class_prediction = class_prediction.reshape(img[:, :, 0].shape)

        print('Reshaped back to {}'.format(class_prediction.shape))

        # - 掩膜处理(背景值 = 0)
        #
        #

        # In[16]:
        # 设置掩膜

        # 在第一波段图像上生成掩膜图像
        mask = np.copy(img[:, :, 0])  # 获取数据

        mask[mask > 0.0] = 1.0  # 所有实际像素的值均为1.0

        # 绘制掩膜
        print('绘制掩膜')

        plt.imshow(mask)

        # In[17]:

        # 显示图像
        # 类型转换
        class_prediction.astype(np.float16)

        class_prediction_ = class_prediction * mask

        # 显示未掩膜图像

        #    plt.subplot(121)
        #
        #    plt.imshow(class_prediction, cmap=plt.cm.Spectral)

        #    plt.title('未掩膜')

        #    # 显示掩膜图像

        #    plt.subplot(122)

        #    plt.imshow(class_prediction_, cmap=plt.cm.Spectral)

        #    plt.title('掩膜')

        # plt.show()

        # - 将分类图像保存到磁盘

        # In[18]:

        cols = img.shape[1]  # 高

        rows = img.shape[0]  # 宽

        class_prediction_.astype(np.float16)

        # 保存格式为gtiff
        driver = gdal.GetDriverByName("gtiff")

        # 获取图像宽，高，波段，定义格式
        outdata = driver.Create(classification_image, cols, rows, 1, gdal.GDT_UInt16)

        # 写入仿射变换参数
        outdata.SetGeoTransform(img_ds.GetGeoTransform())

        # 写入投影
        outdata.SetProjection(img_ds.GetProjection())

        # 写入数组数据
        outdata.GetRasterBand(1).WriteArray(class_prediction_)

        # 保存到磁盘
        outdata.FlushCache()

        # 输出结果
        print('图像保存到: {}'.format(classification_image))

        print('分类结果显示')

        # - 精度评价

        # In[19]:

        # 输出到文本中的标题

        print('------------------------------------', file=open(results_txt, "a"))

        print('验证', file=open(results_txt, "a"))  # 验证样本

        # 打开验证样本矢量
        shape_dataset_v = ogr.Open(validation)

        # 获取验证样本图层对象
        shape_layer_v = shape_dataset_v.GetLayer()

        # 存的数据格式设置为MEM
        mem_drv_v = gdal.GetDriverByName('MEM')

        # 获取图像宽，高，波段，定义格式
        mem_raster_v = mem_drv_v.Create('', img_ds.RasterXSize, img_ds.RasterYSize, 1, gdal.GDT_UInt16)

        # 写入投影
        mem_raster_v.SetProjection(img_ds.GetProjection())

        # 写入仿射变换参数
        mem_raster_v.SetGeoTransform(img_ds.GetGeoTransform())

        # 写入数组数据
        mem_band_v = mem_raster_v.GetRasterBand(1)

        mem_band_v.Fill(0)

        mem_band_v.SetNoDataValue(0)

        # 创建栅格图层
        err_v = gdal.RasterizeLayer(mem_raster_v, [1], shape_layer_v, None, None, [1], [att_, "ALL_TOUCHED=TRUE"])

        assert err_v == gdal.CE_None
        # 读取的栅格数据
        roi_v = mem_raster_v.ReadAsArray()

        # 显示图像2行2列，第一个图像，原始数据
        # plt.subplot(121)
        plt.imshow(img[:, :, :], cmap=plt.cm.Spectral)  # 灰色显示

        plt.title('原始图像')
        # 第二个图像，分类结果
        plt.subplot(111)

        plt.imshow(class_prediction, cmap=plt.cm.Spectral)

        plt.title('分类后图像')

        plt.savefig('3.png')
        # plt.show()

        # 获取验证样本像元，并输出
        n_val = (roi_v > 0).sum()

        print('{n} 个验证样本像元'.format(n=n_val))

        print('{n} 个验证样本像元'.format(n=n_val), file=open(results_txt, "a"))

        # 验证样本标签
        labels_v = np.unique(roi_v[roi_v > 0])

        # 输出标签
        print('验证数据包括 {n} 类: {classes}'.format(n=labels_v.size, classes=labels_v))

        print('验证数据包括 {n} 类: {classes}'.format(n=labels_v.size, classes=labels_v), file=open(results_txt, "a"))
        # 混淆矩阵
        X_v = class_prediction[roi_v > 0]  # 验证样本像元数

        y_v = roi_v[roi_v > 0]  # 类别标签
        # 输出X_v，y_v
        # print('x矩阵大小: {sz_v}'.format(sz_v=X_v.shape))
        # print('y数组大小: {sz_v}'.format(sz_v=y_v.shape))

        # 交叉表预测
        convolution_mat = pd.crosstab(y_v, X_v, margins=True)
        # 输出预测结果
        # print(convolution_mat)
        print(convolution_mat, file=open(results_txt, "a"))

        # information about precision, recall, f1_score, and support:
        # sklearn.metrics.precision_recall_fscore_support
        target_names = list()

        for name in range(1, (labels.size) + 1):
            target_names.append(str(name))
        sum_mat = classification_report(y_v, X_v, target_names=target_names)  # 真实值 预测值 标签
        print(sum_mat)
        print(sum_mat, file=open(results_txt, "a"))

        # Overall Accuracy (OAA)
        print('精度指数 = {} %'.format(accuracy_score(y_v, X_v) * 100))
        span_score = accuracy_score(y_v, X_v) * 100
        print('精度指数 = {} %'.format(accuracy_score(y_v, X_v) * 100), file=open(results_txt, "a"))
        img_open = Image.open('2.png')
        img = ImageTk.PhotoImage(img_open)
        l1.config(image=img)
        l1.image = img  # keep a reference

    def choosepic1():
        global img_RS

        path_ = askopenfilename()

        path.set(path_)

        img_RS = e1.get()

        print(img_RS)
        # 解决中文显示问题
        plt.rcParams['font.sans-serif'] = ['SimHei']

        plt.rcParams['axes.unicode_minus'] = False
        # 让GDAL抛出Python异常，并注册所有驱动程序
        gdal.UseExceptions()

        gdal.AllRegister()

        est = 500

        n_cores = -1  # 拟合和预测过程中并行运用的作业数量。如果为-1，则作业数设置为处理器的core数。

        # 训练样本
        training = 'train1.shp'

        # 验证样本
        validation = 'validation1.shp'

        # 属性表类别字段名
        attribute = 'class'

        # 图像结果保存路径
        classification_image = 'result5_GF2.tif'

        # 文本结果保存路径
        results_txt = 'result5_GF2.txt'

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
        # print('Available attributes in the shape file are: {}'.format(attributes)) #format:格式化函数，该函数把字符串当一个模板，通过传入的参数进行格式化，并且使用大括号“{}”作为特殊字符代替“%”

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
        print('训练样本: {}'.format(training), file=open(results_txt, "a"))

        # 验证样本矢量路径
        print('验证样本: {}'.format(validation), file=open(results_txt, "a"))

        # 属性表中的字段名称
        print('属性字段名称: {}'.format(attribute), file=open(results_txt, "a"))

        # 分类结果生成tif文件路径
        print('分类结果: {}'.format(classification_image), file=open(results_txt, "a"))

        # 分类结果生成文本文件路径
        print('结果文件: {}'.format(results_txt), file=open(results_txt, "a"))

        # 下划线
        print('-------------------------------------------------', file=open(results_txt, "a"))

        print(img_RS)

        #
        #
        #
        #
        #
        #
        #
        #
        ##########可视化界面########################################################################
        #
        #
        #
        # 打开图像 样本

        img_ds = gdal.Open(img_RS, gdal.GA_ReadOnly)

        # 获取图像的高度（y方向上的像素个数），宽度（x方向上的像素个数），波段数
        img = np.zeros((img_ds.RasterYSize, img_ds.RasterXSize, img_ds.RasterCount),

                       # 将波段数据写入数组
                       gdal_array.GDALTypeCodeToNumericTypeCode(img_ds.GetRasterBand(1).DataType))

        for b in range(img.shape[2]):
            img[:, :, b] = img_ds.GetRasterBand(b + 1).ReadAsArray()
        b = img[:, :, 0]

        g = img[:, :, 1]

        r = img[:, :, 2]

        img_rgb = cv2.merge([r, g, b])  # RGB真彩色

        plt.subplot(111)

        plt.imshow(img_rgb, cmap=plt.cm.Greys_r)

        plt.savefig('1.png')

        plt.title('原始图像')

        img_open = Image.open('1.png')

        img = ImageTk.PhotoImage(img_open)

        l1.config(image=img)

        l1.image = img  # keep a reference

    # 分类
    def choosepic3():

        img_open = Image.open('3.png')

        img = ImageTk.PhotoImage(img_open)

        print(type(img))

        l1.config(image=img)

        l1.image = img  # keep a reference

    # 精度指数
    def choosepic4():

        global span_score

        result = tk.messagebox.askokcancel(title='精度评价', message='精度指数：' + str(span_score) + '%')

    # 保存
    def choosepic5():

        filelist = os.listdir(os.getcwd())

        path1 = os.getcwd()

        path2 = os.getcwd() + '\保存图片\保存图片'
        print(path1)

        for files in filelist:
            filename1 = os.path.splitext(files)[1]

            filename0 = os.path.splitext(files)[0]

            print(filename1)

            m = filename1 == '.png'

            print(m)

            if m:
                full_path = os.path.join(path1, files)

                despath = path2 + filename0 + '.png'

                shutil.move(full_path, despath)

            else:
                continue
        result = tk.messagebox.askokcancel(title='保存图片', message='保存成功')

    #    主函数

    #

    #
    img_RS = 0
    # 待分类影像

    root = Tk()
    root.title('基于随机森林的城市信息提取系统')
    root.geometry('600x350')
    path = StringVar()

    Button(root, width=13, height=2, text='打开图像', command=choosepic1).place(x=30, y=23)
    #
    Button(root, width=13, height=2, text='显示样本', command=choosepic2).place(x=30, y=83)
    #
    Button(root, width=13, height=2, text='图像分类', command=choosepic3).place(x=30, y=143)
    #
    Button(root, width=13, height=2, text='精度评价', command=choosepic4).place(x=30, y=203)
    #
    Button(root, width=13, height=2, text='保存结果', command=choosepic5).place(x=30, y=263)
    #
    e1 = Entry(root, state='readonly', text=path)

    l1 = Label(root)

    l1.place(x=150, y=20)

    root.mainloop()

    file_name = os.getcwd()

    for root, dirs, files in os.walk(file_name):
        for name in files:
            if name.endswith(".png"):  # 填写规则
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))
    # print(img_RS)
    # 训练样本
    training = 'train1.shp'
    # 验证样本
    validation = 'validation1.shp'
    # 图像结果保存路径
    classification_image = 'result_GF2.tif'
    # main(img_RS, training, validation, classification_image)

#     main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


window = tk.Tk()
window.title("my window")
window.geometry("450x300")
 
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file="welcome.gif")
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')
 
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password name:').place(x=50, y=190)
 
var_usr_name = tk.StringVar()
var_usr_name.set('温德')
 
var_usr_pwd = tk.StringVar()
 
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)
 
 
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
 
    try:
        with open("usrs_info.pickle", "rb") as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open("usrs_info.pickle", "wb") as usr_file:  # with open with语句可以自动关闭资源
            usrs_info = {"admin": "admin"}  # 以字典的形式保存账户和密码
            pickle.dump(usrs_info, usr_file)
 
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title="Welcome", message="How are you! " + usr_name)
            window.destroy()
            system()
        else:
            tk.messagebox.showerror(message="Error,your password is wrong,try again")
    else:
        is_sign_up = tk.messagebox.askyesno("Welcome", "You have not sign up yet.Sign up today?")
        if is_sign_up:
            usr_sign_up()
 
 
def usr_sign_up():
    def sign_to_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open("usrs_info.pickle", "rb") as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror("Error", "Password and confirm password must be the same!")
        elif nn in exist_usr_info:
            tk.messagebox.showerror("Error", "The user has already signed up! ")
        else:
            exist_usr_info[nn] = np
            with open("usrs_info.pickle", "wb") as usr_file:
                pickle.dump(exist_usr_info, usr_file)
 
            tk.messagebox.showinfo("Welcome", "You have successfully signed up!")
            # close window
            window_sign_up.destroy()
 
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry("350x200")
    window_sign_up.title("sign up window")
 
    new_name = tk.StringVar()
    new_name.set("example@python.com")
    tk.Label(window_sign_up, text="User name:").place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)
 
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text="Password:").place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)
 
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password:").place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)
 
    btn_confirm_sign_up = tk.Button(window_sign_up, text="Sign up", command=sign_to_Python)
    btn_confirm_sign_up.place(x=150, y=130)
 
 
# login and sign up
btn_login = tk.Button(window, text="Login", command=usr_login)
btn_login.place(x=170, y=230)
 
btn_sign_up = tk.Button(window, text="Sign up", command=usr_sign_up)
btn_sign_up.place(x=270, y=230)
 
window.mainloop()

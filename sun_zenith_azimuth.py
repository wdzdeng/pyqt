import cv2
import numpy as np
import math
import os
import gdal
from osgeo import gdal
from osgeo import osr
from sun_angle import sun_angle
def getSRSPair(dataset):
    '''
    获得给定数据的投影参考系和地理参考系
    :param dataset: GDAL地理数据
    :return: 投影参考系和地理参考系
    '''
    prosrs = osr.SpatialReference()
    prosrs.ImportFromWkt(dataset.GetProjection())
    geosrs = prosrs.CloneGeogCS()
    return prosrs, geosrs

def geo2lonlat(dataset, x, y):
    '''
    将投影坐标转为经纬度坐标（具体的投影坐标系由给定数据确定）
    :param dataset: GDAL地理数据
    :param x: 投影坐标x
    :param y: 投影坐标y
    :return: 投影坐标(x, y)对应的经纬度坐标(lon, lat)
    '''
    prosrs, geosrs = getSRSPair(dataset)
    ct = osr.CoordinateTransformation(prosrs, geosrs)
    coords = ct.TransformPoint(x, y)
    return coords[:2]

def geo2lonlat2(prosrs,geosrs, x, y):#改写，换参数
    '''
    将投影坐标转为经纬度坐标（具体的投影坐标系由给定数据确定）
    :param dataset: GDAL地理数据
    :param x: 投影坐标x
    :param y: 投影坐标y
    :return: 投影坐标(x, y)对应的经纬度坐标(lon, lat)
    '''
    ct = osr.CoordinateTransformation(prosrs, geosrs)
    coords = ct.TransformPoint(x, y)
    return coords[:2]


def lonlat2geo(dataset, lon, lat):
    '''
    将经纬度坐标转为投影坐标（具体的投影坐标系由给定数据确定）
    :param dataset: GDAL地理数据
    :param lon: 地理坐标lon经度
    :param lat: 地理坐标lat纬度
    :return: 经纬度坐标(lon, lat)对应的投影坐标
    '''
    prosrs, geosrs = getSRSPair(dataset)
    ct = osr.CoordinateTransformation(geosrs, prosrs)
    coords = ct.TransformPoint(lon, lat)
    return coords[:2]

def imagexy2geo(dataset, row, col):
    '''
    根据GDAL的六参数模型将影像图上坐标（行列号）转为投影坐标或地理坐标（根据具体数据的坐标系统转换）
    :param dataset: GDAL地理数据
    :param row: 像素的行号
    :param col: 像素的列号
    :return: 行列号(row, col)对应的投影坐标或地理坐标(x, y)
    '''
    trans = dataset.GetGeoTransform()
    px = trans[0] + row * trans[1] + col * trans[2]
    py = trans[3] + row * trans[4] + col * trans[5]
    return px, py


def geo2imagexy(dataset, x, y):
    '''
    根据GDAL的六 参数模型将给定的投影或地理坐标转为影像图上坐标（行列号）
    :param dataset: GDAL地理数据
    :param x: 投影或地理坐标x
    :param y: 投影或地理坐标y
    :return: 影坐标或地理坐标(x, y)对应的影像图上行列号(row, col)
    '''
    trans = dataset.GetGeoTransform()
    a = np.array([[trans[1], trans[2]], [trans[4], trans[5]]])
    b = np.array([x - trans[0], y - trans[3]])
    return np.linalg.solve(a, b)  # 使用numpy的linalg.solve进行二元一次方程的求解







def get_Sun_Zenith_Azimuth(child,utc,col,row):#首先要知道求经纬度是根据头文件里的6个数据来求得，这六个数据可以百度‘tfw头文件’
    #这里用的计算方法，求个像元的地理坐标，仅仅适用于aster卫星，嘿嘿，原因我也不知道！！！
    #print(filename)
    gdal.AllRegister()
    #filePath = child
    dataset = gdal.Open(child)
    adfGeoTransform = dataset.GetGeoTransform()
    #print(adfGeoTransform)
    zhuanjiao=np.array([[adfGeoTransform[1],-adfGeoTransform[2]],[adfGeoTransform[4],-adfGeoTransform[5]]])
    #print('zhuan',zhuanjiao)
    u = math.sqrt(zhuanjiao[0, 0]** 2 + zhuanjiao[0, 1]**2)
    #print(u)
    xuanzhuan=zhuanjiao/u
    #print(xuanzhuan)
    # 左上角地理坐标
    #print(adfGeoTransform[0])
    #print(adfGeoTransform[3])
    #col = dataset.RasterXSize  # 列数
    #row = dataset.RasterYSize  # 行数
    Zenith_Azimuth= np.zeros((row, col, 2))
    prosrs, geosrs = getSRSPair(dataset)
    #print('col',col,'row',row)
    for i in range(col):
        #print(i)
        for j in range(row):
            x=xuanzhuan[0,0]*(15*i)+xuanzhuan[0,1]*(-15*j)+adfGeoTransform[0]
            y=xuanzhuan[1,0]*(15*i)+xuanzhuan[1,1]*(-15*j)+adfGeoTransform[3]
            # px = adfGeoTransform[0] + i * adfGeoTransform[1] + j * adfGeoTransform[2]
            # py = adfGeoTransform[3] + i * adfGeoTransform[4] + j * adfGeoTransform[5]
            lon,lat=geo2lonlat2(prosrs, geosrs, x, y)#根据地理坐标求经纬度，这个方法在任何地方通用
            sun_zenith, sun_azimuth = sun_angle(lon,lat,utc)
            #return sun_zenith,sun_azimuth
            Zenith_Azimuth[j, i, 0] = sun_zenith
            Zenith_Azimuth[j, i, 1] = sun_azimuth
            print(sun_azimuth,sun_zenith)
    return Zenith_Azimuth

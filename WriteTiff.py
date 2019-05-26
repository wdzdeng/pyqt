import gdal,osr
import numpy as np
def writeTiff(im_data,top_left_lon,top_left_lat,pixelWidth, pixelHeight,path):
    '''

    :param im_data: 要存入tiff文件的数据
    :param im_relatedfilepath: 和这个数据相关的tiff文件，为了获取其头文件，以便保存时，输入头文件信息
    :param path: 要输出保存tiff文件的路径
    :return:
    '''
    geotransform = [top_left_lon,pixelWidth,0,top_left_lat,0,pixelHeight]
    #related=gdal.Open(im_relatedfilepath)
    #im_geotrans=related.GetGeoTransform()
    #im_proj=related.GetProjection()
    datatype=gdal.GDT_Float64
    im_height, im_width=im_data.shape
    driver=gdal.GetDriverByName('GTiff')
    dataset=driver.Create(path, im_width, im_height,1,datatype)
    dataset.SetGeoTransform(geotransform)
    outRasterSRS = osr.SpatialReference()
    #dataset.SetProjection(im_proj)
    outRasterSRS.ImportFromEPSG(4326)
    dataset.SetProjection(outRasterSRS.ExportToWkt())
    dataset.GetRasterBand(1).WriteArray(im_data)

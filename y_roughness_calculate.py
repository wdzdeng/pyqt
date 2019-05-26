import cv2
import numpy as np
import os
import WriteTiff
def get_roughness(image1_zenith,image1_azimuth,image2_zenith,image2_azimuth,zenith_azimuth,image1,image2,outpath,lr1,la1,lr2,la2):
    #注意：这里全部角度全部采用的弧度制，前面计算卫星角度时就是用弧度制存储的，而太阳角度不是按照弧度制存储的，所以这里太阳的角度需要转化一下
    #1、读取卫星角度
    #angle_3N=np.load(file_3N_angle)
    #angle_3B=np.load(file_3B_angle)
    #2、读取太阳角度
    sun_zenith_azimuth=np.load(zenith_azimuth)
    sun_zenith=sun_zenith_azimuth[:,:,0]*(np.pi/180.0)
    sun_azimuth=sun_zenith_azimuth[:,:,1]*(np.pi/180.0)
    del sun_zenith_azimuth

    scatterAngle_3N = 0.5 * np.arccos(np.cos(image1_zenith)*np.cos(sun_zenith[:, :])+np.sin(image1_zenith)*np.sin(sun_zenith[:,:]) \
                    *np.cos(image1_azimuth-sun_azimuth[:,:]))#2.1入射角
    tiltedAngle_3N=np.arccos(0.5*(np.cos(image1_zenith)+np.cos(sun_zenith[:,:]))/np.cos(scatterAngle_3N))#波面倾斜角
    Nr=1.341
    refractionAngle_3N=np.arcsin(np.sin(scatterAngle_3N)/Nr)#2-7，折射角
    SinTerm_3N = np.sin(scatterAngle_3N - refractionAngle_3N)/np.sin(scatterAngle_3N + refractionAngle_3N)
    TanTerm_3N = np.tan(scatterAngle_3N - refractionAngle_3N)/np.tan(scatterAngle_3N + refractionAngle_3N)
    Ref_3N=0.5*(SinTerm_3N**2+TanTerm_3N**2)#列尔反射率

    del SinTerm_3N
    del TanTerm_3N
    del refractionAngle_3N
    del scatterAngle_3N

    scatterAngle_3B = 0.5 * np.arccos(np.cos(image2_zenith)*np.cos(sun_zenith[:, :]) \
                    + np.sin(image2_zenith)*np.sin(sun_zenith[:, :])*np.cos(image2_azimuth-sun_azimuth[:,:]))
    tiltedAngle_3B = np.arccos(0.5 * (np.cos(image2_zenith) \
                    +np.cos(sun_zenith[:, :])) / np.cos(scatterAngle_3B))
    refractionAngle_3B = np.arcsin(np.sin(scatterAngle_3B) / Nr)
    SinTerm_3B = np.sin(scatterAngle_3B - refractionAngle_3B) \
                    / np.sin(scatterAngle_3B + refractionAngle_3B)
    TanTerm_3B = np.tan(scatterAngle_3B - refractionAngle_3B) \
                    / np.tan(scatterAngle_3B + refractionAngle_3B)
    Ref_3B = 0.5 * (SinTerm_3B**2 + TanTerm_3B**2)

    del SinTerm_3B
    del TanTerm_3B
    del refractionAngle_3B
    del scatterAngle_3B
    del sun_zenith
    del sun_azimuth

    s1 = (Ref_3N * np.cos(image2_zenith) * (np.cos(tiltedAngle_3B))**4) \
        / (Ref_3B * np.cos(image1_zenith) * (np.cos(tiltedAngle_3N))**4)

    del image1_zenith
    del image1_azimuth
    del image2_zenith
    del image2_azimuth
    del Ref_3B
    del Ref_3N

    s2 = np.tan(tiltedAngle_3B)**2 - np.tan(tiltedAngle_3N)**2
    del tiltedAngle_3B
    del tiltedAngle_3N

    aster_3N=cv2.imread(image1, -1)
    aster_3B=cv2.imread(image2, -1)

    #做了大气校正（瑞利散射和气溶胶散射）
    aster_3N=aster_3N-(lr1+la1)
    aster_3B=aster_3B-(lr2*1+la2)
    law,col=aster_3N.shape

    s3=np.zeros((law,col))
    roughness=np.zeros((law,col))
    for i in range(law):
        for j in range(col):
            if aster_3N[i,j]>=0 and aster_3B[i,j]>=0:
                s3[i, j] = (aster_3N[i, j]) / (aster_3B[i, j])
                roughness[i, j] = s2[i, j] / np.log(s3[i, j] / s1[i, j])
            else:
                roughness[i, j] = 0
    del aster_3N
    del aster_3B
    WriteTiff.writeTiff(roughness, image1, outpath)
    return roughness


def y_roughness_calculate(filepath):
    outpath=filepath+'\SSR'
    if os.path.exists(outpath)==False:
        os.makedirs(outpath)
    count=0
    lr=np.loadtxt(filepath+r'\lr.txt')
    print(lr.shape)
    la=np.loadtxt(filepath+r'\la.txt')
    print(la.shape)
    pathDir = os.listdir(filepath + r'\storage_image\3N')
    for Dir in pathDir:
        sufix = os.path.splitext(Dir)
        print(Dir)
        if (sufix[1] == '.tif'):
            filename = Dir[:-7]
            file_3N_angle = filepath + r'\satellite_point\3N' + '\\' + filename + r'_3N_angle.npy'
            file_3B_angle = filepath + r'\satellite_point\3B' + '\\' + filename + r'_3B_angle.npy'
            zenith_azimuth = filepath + r'\sun_angle' + '\\' + filename + r'_Zenith_Azimuth.npy'
            file_3N=filepath+r'\storage_image\3N'+'\\'+filename+'_3N.tif'
            file_3B = filepath + r'\storage_image\3B' + '\\' + filename + '_3B.tif'
            out_R=outpath+'\\'+filename+r'.tif'
            if(len(lr.shape)==1):
                roughness=get_roughness(file_3N_angle,file_3B_angle,zenith_azimuth,file_3N,file_3B,lr,la)
            else:
                roughness = get_roughness(file_3N_angle, file_3B_angle, zenith_azimuth, file_3N, file_3B, lr[count,:], la[count,:])
            WriteTiff.writeTiff(roughness,file_3N,out_R)
            count+=1

import numpy as np

def glintToroughness(N_zenith,N_azimuth,B_zenith,B_azimuth,Sun_zenith,Sun_azimuth,N_glint,B_glint):
    '''
    耀光亮度转粗糙度
    根据提供的前后视 视场角、方位角，太阳高度角和方位角，前后视太阳耀光归一化亮度，计算粗糙度
    :param N_zenith:
    :param N_azimuth:
    :param B_zenith:
    :param B_azimuth:
    :param Sun_zenith:
    :param Sun_azimuth:
    :param N_glint:
    :param B_glint:
    :return:roughness
    '''
    #计算前视相关参数
    N_zenith=N_zenith*np.pi/180
    N_azimuth=N_azimuth*np.pi/180
    B_zenith=B_zenith*np.pi/180
    B_azimuth=B_azimuth*np.pi/180
    Sun_zenith=Sun_zenith*np.pi/180
    Sun_azimuth=Sun_azimuth*np.pi/180
    scatterAngle_3N = 0.5 * np.arccos(np.cos(N_zenith) * np.cos(Sun_zenith) + np.sin(N_zenith) * np.sin(Sun_zenith) \
        * np.cos(N_azimuth - Sun_azimuth))  # 2.1入射角
    tiltedAngle_3N = np.arccos(0.5 * (np.cos(N_zenith) + np.cos(Sun_zenith)) / np.cos(scatterAngle_3N))  # 波面倾斜角
    Nr = 1.341
    refractionAngle_3N = np.arcsin(np.sin(scatterAngle_3N) / Nr)  # 2-7，折射角
    SinTerm_3N = np.sin(scatterAngle_3N - refractionAngle_3N) / np.sin(scatterAngle_3N + refractionAngle_3N)
    TanTerm_3N = np.tan(scatterAngle_3N - refractionAngle_3N) / np.tan(scatterAngle_3N + refractionAngle_3N)
    Ref_3N = 0.5 * (SinTerm_3N ** 2 + TanTerm_3N ** 2)
    del SinTerm_3N
    del TanTerm_3N


    ##计算后视相关参数
    scatterAngle_3B = 0.5 * np.arccos(np.cos(B_zenith) * np.cos(Sun_zenith) + np.sin(B_zenith) * np.sin(Sun_zenith) \
            * np.cos(B_azimuth - Sun_azimuth))
    tiltedAngle_3B = np.arccos(0.5 * (np.cos(B_zenith) + np.cos(Sun_zenith)) / np.cos(scatterAngle_3B))
    refractionAngle_3B = np.arcsin(np.sin(scatterAngle_3B) / Nr)
    #print(scatterAngle_3B,refractionAngle_3B,scatterAngle_3B + refractionAngle_3B )
    SinTerm_3B = np.sin(scatterAngle_3B - refractionAngle_3B) \
                 / np.sin(scatterAngle_3B + refractionAngle_3B)
    TanTerm_3B = np.tan(scatterAngle_3B - refractionAngle_3B) \
                 / np.tan(scatterAngle_3B + refractionAngle_3B)
    Ref_3B = 0.5 * (SinTerm_3B ** 2 + TanTerm_3B ** 2)
    del SinTerm_3B
    del TanTerm_3B

    s1 = (Ref_3N * np.cos(B_zenith) * (np.cos(tiltedAngle_3B)) ** 4) \
         / (Ref_3B * np.cos(N_zenith) * (np.cos(tiltedAngle_3N)) ** 4)

    s2 = np.tan(tiltedAngle_3B) ** 2 - np.tan(tiltedAngle_3N) ** 2
    #print("后视倾斜角tiltedAngle_3B:",tiltedAngle_3B)
    #print("前视倾斜角tiltedAngle_3N:",tiltedAngle_3N)
    s3=N_glint / B_glint

    roughness = s2 / np.log(s3 / s1)
    #print("分子:",s2)
    #print("分母:",s3/s1)
    m=s3/s1
    return roughness,m
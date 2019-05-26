import numpy as np
def  roughnessToglint(valueMap):
    '''
    粗糙度转耀光亮度
    根据传感器视场角、方位角，太阳高度角、方位角，风速（相当于提供粗糙度），计算归一化的太阳耀光亮度
    所有的角度都先转化为弧度制
    '''

    Satellite_zenith=valueMap["satellite_zenith"]*np.pi/180
    Satellite_azimuth=valueMap["satellite_azimuth"]*np.pi/180
    Sun_zenith=valueMap["sun_zenith"]*np.pi/180
    Sun_azimuth=valueMap["sun_azimuth"]*np.pi/180
    feng = valueMap["feng"]
    scatterAngle_a = np.arccos(np.cos(Sun_zenith) * np.cos(Satellite_zenith) + np.sin(Satellite_zenith) \
                               * np.sin(Sun_zenith) * np.cos(Satellite_azimuth-Sun_azimuth))  # 公式2.1
    reflectionAngle_a = 0.5 * scatterAngle_a  # 入射角W
    tiltedAngle_a = np.arccos(
        0.5 * (np.cos(Satellite_zenith) + np.cos(Sun_zenith)) / np.cos(reflectionAngle_a))  # 波面倾角
    Nr = 1.341  # 海水折射率
    refractionAngle_a = np.arcsin(np.sin(reflectionAngle_a)/ Nr)  # 2—7反射角,求出折射角
    #print(reflectionAngle_a,refractionAngle_a,reflectionAngle_a + refractionAngle_a,"toglint")
    #print(reflectionAngle_a)
    #print(refractionAngle_a)
    #print(reflectionAngle_a + refractionAngle_a)
    SinTerm_a = np.sin(reflectionAngle_a - refractionAngle_a) / np.sin(reflectionAngle_a + refractionAngle_a)
    TanTerm_a = np.tan(reflectionAngle_a - refractionAngle_a) / np.tan(reflectionAngle_a + refractionAngle_a)
    Ref_a = 0.5 * (SinTerm_a ** 2 + TanTerm_a ** 2)  # 菲涅尔反射率equation(2 - 6)
    roughness = 0.003 + 0.00512 * feng
    I1 = Ref_a * np.exp(-np.tan(tiltedAngle_a) * np.tan(tiltedAngle_a) / roughness) / (
                4 * np.pi * roughness * np.cos(Satellite_zenith) * (np.cos(tiltedAngle_a)) ** 4)

    #print(I1)
    return I1#返回归一化耀光强度

def  roughnessToglintByMatrix(Satellite_zenith,Satellite_azimuth,Sun_zenith,Sun_azimuth,feng):
    '''
    粗糙度转耀光亮度
    根据传感器视场角、方位角，太阳高度角、方位角，风速（相当于提供粗糙度），计算归一化的太阳耀光亮度
    所有的角度都先转化为弧度制
    '''

    Satellite_zenith=Satellite_zenith*np.pi/180
    Satellite_azimuth=Satellite_azimuth*np.pi/180
    Sun_zenith=Sun_zenith*np.pi/180
    Sun_azimuth=Sun_azimuth*np.pi/180

    scatterAngle_a = np.arccos(np.cos(Sun_zenith) * np.cos(Satellite_zenith) + np.sin(Satellite_zenith) \
                               * np.sin(Sun_zenith) * np.cos(Satellite_azimuth-Sun_azimuth))  # 公式2.1
    reflectionAngle_a = 0.5 * scatterAngle_a  # 入射角W
    tiltedAngle_a = np.arccos(
        0.5 * (np.cos(Satellite_zenith) + np.cos(Sun_zenith)) / np.cos(reflectionAngle_a))  # 波面倾角
    Nr = 1.341  # 海水折射率
    refractionAngle_a = np.arcsin(np.sin(reflectionAngle_a)/ Nr)  # 2—7反射角,求出折射角
    #print(reflectionAngle_a,refractionAngle_a,reflectionAngle_a + refractionAngle_a,"toglint")
    #print(reflectionAngle_a)
    #print(refractionAngle_a)
    #print(reflectionAngle_a + refractionAngle_a)
    SinTerm_a = np.sin(reflectionAngle_a - refractionAngle_a) / np.sin(reflectionAngle_a + refractionAngle_a)
    TanTerm_a = np.tan(reflectionAngle_a - refractionAngle_a) / np.tan(reflectionAngle_a + refractionAngle_a)
    Ref_a = 0.5 * (SinTerm_a ** 2 + TanTerm_a ** 2)  # 菲涅尔反射率equation(2 - 6)
    roughness = 0.003 + 0.00512 * feng
    I1 = Ref_a * np.exp(-np.tan(tiltedAngle_a) * np.tan(tiltedAngle_a) / roughness) / (
                4 * np.pi * roughness * np.cos(Satellite_zenith) * (np.cos(tiltedAngle_a)) ** 4)

    #print(I1)
    return I1#返回归一化耀光强度
#print(roughnessToglint(0,270,20,200,5))
#print(roughnessToglint(0,270,20,180,5))
#print(roughnessToglint(0,270,20,100,5))
# print(roughnessToglint(20,180,20,200,5))
# # print(roughnessToglint(10,180,20,200,5))
# # print(roughnessToglint(2,270,20,200,5))
#print(roughnessToglint(0,180,20,60,5))
#print(roughnessToglint(30,180,30,180,5))
#print(roughnessToglint(10,180,20,60,5))
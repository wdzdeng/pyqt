import RoughnessToGlintForPSO
import GlintToRoughness
import numpy as np
import random
def compare2(N_zenith,N_azimuth,B_zenith,B_azimuth,Sun_zenith,Sun_azimuth,feng,N_deviation,B_deviation,add_deviation):
    # N_zenith = np.random.randint(N_zenith-5,N_zenith+5,size=(100,100))
    # N_azimuth = np.random.randint(N_azimuth-10,N_azimuth+10,size=(100,100))
    # B_zenith = np.random.randint(B_zenith-5,B_zenith+5,size=(100,100))
    # B_azimuth = np.random.randint(B_azimuth-10,B_azimuth+10,size=(100,100))
    '''
    特定角度下，后视视场角对耀光误差的敏感性
    :param N_zenith:
    :param N_azimuth:
    :param B_zenith:
    :param B_azimuth:
    :param Sun_zenith:
    :param Sun_azimuth:
    :param feng:
    :param N_deviation: 前视误差
    :param B_deviation: 后视误差
    :return:
    '''
    roughness1= 0.003 + 0.00512 * feng
    N_glint=RoughnessToGlintForPSO.roughnessToglint(N_zenith, N_azimuth, Sun_zenith, Sun_azimuth, feng)
    B_glint=RoughnessToGlintForPSO.roughnessToglint(B_zenith, B_azimuth, Sun_zenith, Sun_azimuth, feng)


    N_glint=N_glint*(1+N_deviation/100)+add_deviation#*random.random()
    B_glint=B_glint*(1+B_deviation/100)+add_deviation#*random.random()
    roughness2,m=GlintToRoughness.glintToroughness(N_zenith,N_azimuth,B_zenith,B_azimuth,Sun_zenith,Sun_azimuth,N_glint,B_glint)
    # result=roughness2-roughness1
    # print("前视视场角：",N_zenith*180/np.pi,"   ","前视方位角：",N_azimuth*180/np.pi,'\n',
    #       "后视视场角：",B_zenith*180/np.pi,"   ","后视方位角：",B_azimuth*180/np.pi,'\n',
    #       "太阳天顶角：",Sun_zenith*180/np.pi,"   ","太阳方位角：",Sun_azimuth*180/np.pi,'\n',
    #       "用于仿真的风速：",feng)
    # print("用于仿真耀光风速对应的粗糙度：",roughness1)
    # print("反演得到的粗糙度：",roughness2)
    #print("反演得到粗糙度，相对误差：",np.abs(roughness2-roughness1)/roughness1)
    #print(np.abs(roughness2-roughness1)/roughness1)
    return np.abs(roughness2-roughness1)/roughness1
def compare3(N_zenith,N_azimuth,B_zenith,B_azimuth,Sun_zenith,Sun_azimuth,feng,N_deviation,B_deviation,add_deviation):
    N_zenith = np.random.uniform(N_zenith-5,N_zenith+5,size=(1000,1000))
    N_azimuth = np.random.uniform(N_azimuth-10,N_azimuth+10,size=(1000,1000))
    B_zenith = np.random.uniform(B_zenith-5,B_zenith+5,size=(1000,1000))
    B_azimuth = np.random.uniform(B_azimuth-10,B_azimuth+10,size=(1000,1000))
    '''
    特定角度下，后视视场角对耀光误差的敏感性
    :param N_zenith:
    :param N_azimuth:
    :param B_zenith:
    :param B_azimuth:
    :param Sun_zenith:
    :param Sun_azimuth:
    :param feng:
    :param N_deviation: 前视误差
    :param B_deviation: 后视误差
    :return:
    '''
    roughness1= 0.003 + 0.00512 * feng
    N_glint=RoughnessToGlintForPSO.roughnessToglint(N_zenith, N_azimuth, Sun_zenith, Sun_azimuth, feng)
    B_glint=RoughnessToGlintForPSO.roughnessToglint(B_zenith, B_azimuth, Sun_zenith, Sun_azimuth, feng)


    N_glint=N_glint*(1+N_deviation/100)+add_deviation#*random.random()
    B_glint=B_glint*(1+B_deviation/100)+add_deviation#*random.random()
    roughness2,m=GlintToRoughness.glintToroughness(N_zenith,N_azimuth,B_zenith,B_azimuth,Sun_zenith,Sun_azimuth,N_glint,B_glint)
    # result=roughness2-roughness1
    # print("前视视场角：",N_zenith*180/np.pi,"   ","前视方位角：",N_azimuth*180/np.pi,'\n',
    #       "后视视场角：",B_zenith*180/np.pi,"   ","后视方位角：",B_azimuth*180/np.pi,'\n',
    #       "太阳天顶角：",Sun_zenith*180/np.pi,"   ","太阳方位角：",Sun_azimuth*180/np.pi,'\n',
    #       "用于仿真的风速：",feng)
    # print("用于仿真耀光风速对应的粗糙度：",roughness1)
    # print("反演得到的粗糙度：",roughness2)
    #print("反演得到粗糙度，相对误差：",np.abs(roughness2-roughness1)/roughness1)
    #print(np.abs(roughness2-roughness1)/roughness1)
    error_matrix = (np.abs(roughness2-roughness1)/roughness1)*100
    return np.max(error_matrix),np.mean(error_matrix)
#print(compare2(10, 0.0, 20, 229,20,90,5,4,7,0.0005))




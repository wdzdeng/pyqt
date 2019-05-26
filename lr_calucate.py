import numpy as np
import os
import datetime
def julday(st):
    dt = datetime.datetime.strptime(st, r'%Y.%m.%d')
    tt = dt.timetuple()
    return tt.tm_year*1000+tt.tm_yday


def get_lr(angle,zenith_azimuth,time):
    dayth=julday(str(time[0])+'.'+str(time[1])+'.'+str(time[2]))-julday(str(time[0])+'.'+str(1)+'.'+str(1))+1
    FirAverage=1101.0
    Fir=FirAverage*(1+0.0167*np.cos(2*np.pi*(dayth-3)/365.0))**2
    OpticalThickness = 0.021
    angle_3N=np.load(angle)
    sun_zenith_azimuth=np.load(zenith_azimuth)
    sun_zenith=sun_zenith_azimuth[:,:,0]*(np.pi/180.0)
    sun_azimuth=sun_zenith_azimuth[:,:,1]*(np.pi/180.0)

    p_aplus=(3/4.0)*(1+(np.cos(sun_zenith)*np.cos(angle_3N[:,:,0])+np.sin(sun_zenith)* np.sin(angle_3N[:, :, 0]) * np.cos(sun_azimuth - angle_3N[:, :, 1]))**2)

    p_aminus = (3 / 4.0) * (1 + (-np.cos(sun_zenith) * np.cos(angle_3N[:, :, 0]) + np.sin(sun_zenith) * np.sin(angle_3N[:, :, 0]) * np.cos(sun_azimuth - angle_3N[:, :, 1]))**2)

    refractionAngle_sun = np.arcsin(np.sin(sun_zenith) / 1.34)
    SinTerm_sun = np.sin(sun_zenith - refractionAngle_sun)/np.sin(sun_zenith+refractionAngle_sun)
    TanTerm_sun = np.tan(sun_zenith - refractionAngle_sun)/np.tan(sun_zenith+refractionAngle_sun)
    Ref_sun = 0.5 * (SinTerm_sun**2 + TanTerm_sun**2)

    refractionAngle_3N = np.arcsin(np.sin(angle_3N[:, :, 0]) / 1.34)
    SinTerm_3N = np.sin(angle_3N[:, :, 0]-refractionAngle_3N)/np.sin(angle_3N[:,:,0]+refractionAngle_3N)
    TanTerm_3N = np.tan(angle_3N[:, :, 0]-refractionAngle_3N)/np.tan(angle_3N[:,:,0]+refractionAngle_3N)
    Ref_3N = 0.5 * (SinTerm_3N**2 + TanTerm_3N**2)

    Lr = (Fir * OpticalThickness * (p_aminus + (Ref_sun + Ref_3N) * p_aplus)) / (4 *np.pi * np.cos(angle_3N[:,:, 0]))

    return np.mean(Lr)

def lr_calucate(filepath):
    fp = open(filepath + "\\" + r'lr.txt', 'a')
    time=np.loadtxt(filepath+r'\utc.txt',int)
    count=0
    pathDir = os.listdir(filepath + r'\storage_image\3N')
    for Dir in pathDir:
        sufix = os.path.splitext(Dir)
        print(Dir)
        if (sufix[1] == '.tif'):
            filename=Dir[:-7]
            file_3N_angle=filepath+r'\satellite_point\3N'+'\\'+filename+r'_3N_angle.npy'
            file_3B_angle = filepath + r'\satellite_point\3B' + '\\' + filename + r'_3B_angle.npy'
            zenith_azimuth=filepath+r'\sun_angle'+'\\'+filename+r'_Zenith_Azimuth.npy'
            if(len(time.shape)==1):
                Lr_3N=get_lr(file_3N_angle,zenith_azimuth,time[1:4])
                Lr_3B=get_lr(file_3B_angle,zenith_azimuth,time[1:4])
            else:
                Lr_3N = get_lr(file_3N_angle, zenith_azimuth, time[count, 1:4])
                Lr_3B = get_lr(file_3B_angle, zenith_azimuth, time[count, 1:4])
            fp.write(str(Lr_3N)+'   '+str(Lr_3B)+'\n')
            count += 1
            print(Lr_3N)
            print(Lr_3B)

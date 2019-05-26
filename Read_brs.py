#实现从头文件信息中读取UTC时间和PS数据
import os
def readFile(filename):
    name=filename.split('\\')[-1].split('.')[0]
    if(name[:4]=='prbr'):
        number=name[4:]
    else:
        number=name
    #number=filename.split('\\')[-1].split('.')[0][4:]
    #if(number.strip()==''):
        #number=filename.split('\\')[-1].split('.')[0]

    readlines=open(filename,'rb').readlines()
    t_time=1
    t_p=1
    t_s=1
    for i in range(len(readlines)):
        if readlines[i].strip()==b"OBJECT                 = SETTINGTIMEOFPOINTING" and t_time==1:
            utc=readlines[i+3].strip().decode('utf-8').split('=')[1].strip()
            t_time=0
            utc_line=utc[1:5]+'-'+utc[6:8]+'-'+utc[9:11]+'-'+utc[12:14]+'-'+utc[15:17]+'-'+utc[18:20]
        if readlines[i].strip()==b"OBJECT                 = POINTINGANGLE" and t_p==1:
            p=readlines[i+3].strip().decode('utf-8').split('=')[1].strip()
            t_p=0
        if readlines[i].strip() == b"OBJECT                 = SCENEORIENTATIONANGLE" and t_s == 1:
            s = readlines[i + 2].strip().decode('utf-8').split('=')[1].strip()
            t_s = 0
        if t_time==0 and t_p==0 and t_s==0:
            break
    return utc_line,number,p,s


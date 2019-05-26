import numpy as np
import math
def calculate(row,col,p,s,zenith1,zenith2,ifov,H,M):
    pi = math.pi / 180.0
    P=p*pi
    zenith1 = zenith1*pi
    zenith2 = zenith2*pi
    M = M/1000

    image1_zenith_onecol = np.zeros(col)
    image1_azimuth_onecol = np.zeros(col)
    image2_zenith_onecol = np.zeros(col)
    image2_azimuth_onecol = np.zeros(col)
    for i in range(col):
        image1_zenith_onecol[i] = math.atan(math.sqrt((H * math.tan(P) + M * (i + 1 - col / 2))**2 + (H *math. tan(zenith1) /math. cos(P))**2) / H)
        image2_zenith_onecol[i] = math.atan(math.sqrt((H * math.tan(P) + M * (i + 1 - col / 2)) ** 2 + (H * math.tan(zenith2) / math.cos(P)) ** 2) / H)
        if P+(i+1-col/2)*ifov >= 0:
            image1_azimuth_onecol[i] = 270 * pi - math.atan(np.tan(-1*zenith1) / math.tan(P + (i + 1 - col / 2) * ifov)) + s * pi
            image2_azimuth_onecol[i] = 270 * pi - math.atan(np.tan(-1 * zenith2) / math.tan(P + (i + 1 - col / 2) * ifov)) + s * pi
        else:
            image1_azimuth_onecol[i] = 90 * pi - math.atan(np.tan(-1*zenith1) / math.tan(P + (i + 1 - col / 2) * ifov)) + s * pi
            image2_azimuth_onecol[i] = 90 * pi - math.atan(np.tan(-1 * zenith2) / math.tan(P + (i + 1 - col / 2) * ifov)) + s * pi

    image1_zenith = np.zeros((row, col))
    image1_azimuth = np.zeros((row, col))

    image2_zenith = np.zeros((row, col))
    image2_azimuth = np.zeros((row, col))

    for i in range(row):
        image1_zenith[i,:] = image1_zenith_onecol
        image1_azimuth[i,:] = image1_azimuth_onecol
        image2_zenith[i,:] = image2_zenith_onecol
        image2_azimuth[i,:] = image2_azimuth_onecol

    del(image1_zenith_onecol)
    del(image1_azimuth_onecol)
    del(image2_zenith_onecol)
    del(image2_azimuth_onecol)
    return  image1_zenith,image1_azimuth,image2_zenith,image2_azimuth

def point_calculate(p1,s1,v1,p2,s2,v2,h1,h2):
    pi = math.pi / 180.0
    P1=p1*pi
    H1 = h1/1000
    H2 = h2/1000
    V1 = v1*pi
    S1 = s1*pi
    P2 = p2*pi
    V2 = v2*pi
    S2 = s2*pi
    zenith1 = math.atan(math.sqrt((H1 * math.tan(P1) )**2 + (H1 *math. tan(V1) /math. cos(P1))**2) / H1)
    azimuth1 = 270 * pi - math.atan(np.tan(-1*V1) / math.tan(P1 )) + S1

    zenith2 = math.atan(math.sqrt((H2 * math.tan(P2)) ** 2 + (H2 * math.tan(V2) / math.cos(P2)) ** 2) / H2)
    azimuth2 = 270 * pi - math.atan(np.tan(-1 * V2) / math.tan(P2)) + S2

    return  zenith1*180/np.pi,(azimuth1*180/np.pi)%360,zenith2*180/np.pi,(azimuth2*180/np.pi)%360

#print(point_calculate(9.999999999986715, 0, 0, 19.999999999992994, 0, 0,200))
#[9.999999999986715, 0, 0, 19.999999999992994, 0, 0] 190.0000000000203 [9.999999999986715, 270.0, 19.999999999992994, 270.0]
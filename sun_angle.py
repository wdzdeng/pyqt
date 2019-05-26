import cv2
import numpy as np
import math
import os
import gdal
class Topocentric_sun_position():
    pass
class Nutation():
    pass
class Sun_geocentric_position():
    pass
class Earth_heliocentric_position():
    pass

class JuLian():
    day=0
    ephemeris_day=0
    century=0
    ephemeris_century=0
    ephemeris_millenium=0
    def __init__(self,day,ephemeris_day,century,ephemeris_century,ephemeris_millenium):
        self.day=day
        self.ephemeris_day=ephemeris_day
        self.century=century
        self.ephemeris_century=ephemeris_century
        self.ephemeris_millenium=ephemeris_millenium



class Sun():
    pass

class location():
    longitude=0
    latitude=0
    altitude=0
    def __init__(self,lon,lat,altitude):
        self.longitude=lon
        self.latitude=lat
        self.altitude=altitude
class time():
    year=0
    month=0
    day=0
    hour=0
    min=0
    sec=0
    UTC=0
    def __init__(self,year,month,day,hour,min,sec,UTC):
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour
        self.min=min
        self.sec=sec
        self.UTC=UTC






def julian_calculation(time):#1
    if (time.month == 1 and time.month == 2):
        Y = time.year - 1
        M = time.month + 12
    else:
        Y = time.year
        M = time.month
    ut_time = ((time.hour - time.UTC) / 24) + (time.min / (60 * 24)) + (time.sec/(60 * 60 * 24))
    D = time.day + ut_time
    if (time.year == 1582):
        if (time.month == 10):
            if (time.day <= 4):
                B = 0
            if(time.day >= 15):
                A = Y // 100
                B = 2 - A + (A // 4)
            else:
                time.month = 10
                time.day = 4
                B = 0
        if time.month<10:
            B = 0
        else:
            A = Y // 100
            B = 2 - A + A // 4
    if (time.year < 1582):
        B=0
    else:
        A = Y // 100
        B = 2 - A + A // 4
    day=math.floor(365.25*(Y+4716))+math.floor(30.6001*(M+1))+ D + B - 1524.5
    delta_t = 0# 33.184
    ephemeris_day = day + (delta_t / 86400)
    century = (day - 2451545) / 36525
    ephemeris_century = (ephemeris_day - 2451545) / 36525
    ephemeris_millenium = ephemeris_century / 10
    jl=JuLian(day,ephemeris_day,century,ephemeris_century,ephemeris_millenium)
    return jl



def earth_heliocentric_position_calculation(julian):#2
    L0_terms=np.array([[1.75347046e+08, 0.00000000e+00, 0.00000000e+00],
       [3.34165600e+06, 4.66925680e+00, 6.28307585e+03],
       [3.48940000e+04, 4.62610000e+00, 1.25661517e+04],
       [3.49700000e+03, 2.74410000e+00, 5.75338490e+03],
       [3.41800000e+03, 2.82890000e+00, 3.52310000e+00],
       [3.13600000e+03, 3.62770000e+00, 7.77137715e+04],
       [2.67600000e+03, 4.41810000e+00, 7.86041940e+03],
       [2.34300000e+03, 6.13520000e+00, 3.93020970e+03],
       [1.32400000e+03, 7.42500000e-01, 1.15067698e+04],
       [1.27300000e+03, 2.03710000e+00, 5.29691000e+02],
       [1.19900000e+03, 1.10960000e+00, 1.57734350e+03],
       [9.90000000e+02, 5.23300000e+00, 5.88492700e+03],
       [9.02000000e+02, 2.04500000e+00, 2.62980000e+01],
       [8.57000000e+02, 3.50800000e+00, 3.98149000e+02],
       [7.80000000e+02, 1.17900000e+00, 5.22369400e+03],
       [7.53000000e+02, 2.53300000e+00, 5.50755300e+03],
       [5.05000000e+02, 4.58300000e+00, 1.88492280e+04],
       [4.92000000e+02, 4.20500000e+00, 7.75523000e+02],
       [3.57000000e+02, 2.92000000e+00, 6.70000000e-02],
       [3.17000000e+02, 5.84900000e+00, 1.17906290e+04],
       [2.84000000e+02, 1.89900000e+00, 7.96298000e+02],
       [2.71000000e+02, 3.15000000e-01, 1.09770790e+04],
       [2.43000000e+02, 3.45000000e-01, 5.48677800e+03],
       [2.06000000e+02, 4.80600000e+00, 2.54431400e+03],
       [2.05000000e+02, 1.86900000e+00, 5.57314300e+03],
       [2.02000000e+02, 2.44580000e+00, 6.06977700e+03],
       [1.56000000e+02, 8.33000000e-01, 2.13299000e+02],
       [1.32000000e+02, 3.41100000e+00, 2.94246300e+03],
       [1.26000000e+02, 1.08300000e+00, 2.07750000e+01],
       [1.15000000e+02, 6.45000000e-01, 9.80000000e-01],
       [1.03000000e+02, 6.36000000e-01, 4.69400300e+03],
       [1.02000000e+02, 9.76000000e-01, 1.57208390e+04],
       [1.02000000e+02, 4.26700000e+00, 7.11400000e+00],
       [9.90000000e+01, 6.21000000e+00, 2.14617000e+03],
       [9.80000000e+01, 6.80000000e-01, 1.55420000e+02],
       [8.60000000e+01, 5.98000000e+00, 1.61000690e+05],
       [8.50000000e+01, 1.30000000e+00, 6.27596000e+03],
       [8.50000000e+01, 3.67000000e+00, 7.14307000e+04],
       [8.00000000e+01, 1.81000000e+00, 1.72601500e+04],
       [7.90000000e+01, 3.04000000e+00, 1.20364600e+04],
       [7.10000000e+01, 1.76000000e+00, 5.08863000e+03],
       [7.40000000e+01, 3.50000000e+00, 3.15469000e+03],
       [7.40000000e+01, 4.68000000e+00, 8.01820000e+02],
       [7.00000000e+01, 8.30000000e-01, 9.43776000e+03],
       [6.20000000e+01, 3.98000000e+00, 8.82739000e+03],
       [6.10000000e+01, 1.82000000e+00, 7.08490000e+03],
       [5.70000000e+01, 2.78000000e+00, 6.28660000e+03],
       [5.60000000e+01, 4.39000000e+00, 1.41435000e+04],
       [5.60000000e+01, 3.47000000e+00, 6.27955000e+03],
       [5.20000000e+01, 1.90000000e-01, 1.21395500e+04],
       [5.20000000e+01, 1.33000000e+00, 1.74802000e+03],
       [5.10000000e+01, 2.80000000e-01, 5.85648000e+03],
       [4.90000000e+01, 4.90000000e-01, 1.19445000e+03],
       [4.10000000e+01, 5.37000000e+00, 8.42924000e+03],
       [4.10000000e+01, 2.40000000e+00, 1.96510500e+04],
       [3.90000000e+01, 6.17000000e+00, 1.04473900e+04],
       [3.70000000e+01, 6.04000000e+00, 1.02132900e+04],
       [3.70000000e+01, 2.57000000e+00, 1.05938000e+03],
       [3.60000000e+01, 1.71000000e+00, 2.35287000e+03],
       [3.60000000e+01, 1.78000000e+00, 6.81277000e+03],
       [3.30000000e+01, 5.90000000e-01, 1.77898500e+04],
       [3.00000000e+01, 4.40000000e-01, 8.39968500e+04],
       [3.00000000e+01, 2.74000000e+00, 1.34987000e+03],
       [2.50000000e+01, 3.16000000e+00, 4.69048000e+03]])
    L1_terms=np.array([[6.28331967e+11, 0.00000000e+00, 0.00000000e+00],
       [2.06059000e+05, 2.67823500e+00, 6.28307585e+03],
       [4.30300000e+03, 2.63510000e+00, 1.25661517e+04],
       [4.25000000e+02, 1.59000000e+00, 3.52300000e+00],
       [1.19000000e+02, 5.79600000e+00, 2.62980000e+01],
       [1.09000000e+02, 2.96600000e+00, 1.57734400e+03],
       [9.30000000e+01, 2.59000000e+00, 1.88492300e+04],
       [7.20000000e+01, 1.14000000e+00, 5.29690000e+02],
       [6.80000000e+01, 1.87000000e+00, 3.98150000e+02],
       [6.70000000e+01, 4.41000000e+00, 5.50755000e+03],
       [5.90000000e+01, 2.89000000e+00, 5.22369000e+03],
       [5.60000000e+01, 2.17000000e+00, 1.55420000e+02],
       [4.50000000e+01, 4.00000000e-01, 7.96300000e+02],
       [3.60000000e+01, 4.70000000e-01, 7.75520000e+02],
       [2.90000000e+01, 2.65000000e+00, 7.11000000e+00],
       [2.10000000e+01, 5.34000000e+00, 9.80000000e-01],
       [1.90000000e+01, 1.85000000e+00, 5.48678000e+03],
       [1.90000000e+01, 4.97000000e+00, 2.13300000e+02],
       [1.70000000e+01, 2.99000000e+00, 6.27596000e+03],
       [1.60000000e+01, 3.00000000e-02, 2.54431000e+03],
       [1.60000000e+01, 1.43000000e+00, 2.14617000e+03],
       [1.50000000e+01, 1.21000000e+00, 1.09770800e+04],
       [1.20000000e+01, 2.83000000e+00, 1.74802000e+03],
       [1.20000000e+01, 3.26000000e+00, 5.08863000e+03],
       [1.20000000e+01, 5.27000000e+00, 1.19445000e+03],
       [1.20000000e+01, 2.08000000e+00, 4.69400000e+03],
       [1.10000000e+01, 7.70000000e-01, 5.53570000e+02],
       [1.00000000e+01, 1.30000000e+00, 3.28660000e+03],
       [1.00000000e+01, 4.24000000e+00, 1.34987000e+03],
       [9.00000000e+00, 2.70000000e+00, 2.42730000e+02],
       [9.00000000e+00, 5.64000000e+00, 9.51720000e+02],
       [8.00000000e+00, 5.30000000e+00, 2.35287000e+03],
       [6.00000000e+00, 2.65000000e+00, 9.43776000e+03],
       [6.00000000e+00, 4.67000000e+00, 4.69048000e+03]])
    L2_terms=np.array([[5.2919000e+04, 0.0000000e+00, 0.0000000e+00],
       [8.7200000e+03, 1.0721000e+00, 6.2830758e+03],
       [3.0900000e+02, 8.6700000e-01, 1.2566152e+04],
       [2.7000000e+01, 5.0000000e-02, 3.5200000e+00],
       [1.6000000e+01, 5.1900000e+00, 2.6300000e+01],
       [1.6000000e+01, 3.6800000e+00, 1.5542000e+02],
       [1.0000000e+01, 7.6000000e-01, 1.8849230e+04],
       [9.0000000e+00, 2.0600000e+00, 7.7713770e+04],
       [7.0000000e+00, 8.3000000e-01, 7.7552000e+02],
       [5.0000000e+00, 4.6600000e+00, 1.5773400e+03],
       [4.0000000e+00, 1.0300000e+00, 7.1100000e+00],
       [4.0000000e+00, 3.4400000e+00, 5.5731400e+03],
       [3.0000000e+00, 5.1400000e+00, 7.9630000e+02],
       [3.0000000e+00, 6.0500000e+00, 5.5075500e+03],
       [3.0000000e+00, 1.1900000e+00, 2.4273000e+02],
       [3.0000000e+00, 6.1200000e+00, 5.2969000e+02],
       [3.0000000e+00, 3.1000000e-01, 3.9815000e+02],
       [3.0000000e+00, 2.2800000e+00, 5.5357000e+02],
       [2.0000000e+00, 4.3800000e+00, 5.2236900e+03],
       [2.0000000e+00, 3.7500000e+00, 9.8000000e-01]])
    L3_terms=np.array([[2.890000e+02, 5.844000e+00, 6.283076e+03],
       [3.500000e+01, 0.000000e+00, 0.000000e+00],
       [1.700000e+01, 5.490000e+00, 1.256615e+04],
       [3.000000e+00, 5.200000e+00, 1.554200e+02],
       [1.000000e+00, 4.720000e+00, 3.520000e+00],
       [1.000000e+00, 5.300000e+00, 1.884923e+04],
       [1.000000e+00, 5.970000e+00, 2.427300e+02]])
    L4_terms=np.array([[1.140000e+02, 3.142000e+00, 0.000000e+00],
       [8.000000e+00, 4.130000e+00, 6.283080e+03],
       [1.000000e+00, 3.840000e+00, 1.256615e+04]])
    L5_terms =np.array([[1, 3.14, 0]])
    A0 = L0_terms[:, 0]
    B0 = L0_terms[:, 1]
    C0 = L0_terms[:, 2]

    A1 = L1_terms[:, 0]
    B1 = L1_terms[:, 1]
    C1 = L1_terms[:, 2]

    A2 = L2_terms[:, 0]
    B2 = L2_terms[:, 1]
    C2 = L2_terms[:, 2]

    A3 = L3_terms[:, 0]
    B3 = L3_terms[:, 1]
    C3 = L3_terms[:, 2]

    A4 = L4_terms[:, 0]
    B4 = L4_terms[:, 1]
    C4 = L4_terms[:, 2]

    A5 = L5_terms[:, 0]
    B5 = L5_terms[:, 1]
    C5 = L5_terms[:, 2]

    JME = julian.ephemeris_millenium

    L0 = np.sum(A0*np.cos(B0 + (C0 * JME)))
    L1 = np.sum(A1*np.cos(B1 + (C1 * JME)))
    L2 = np.sum(A2*np.cos(B2 + (C2 * JME)))
    L3 = np.sum(A3*np.cos(B3 + (C3 * JME)))
    L4 = np.sum(A4*np.cos(B4 + (C4 * JME)))
    L5 = np.sum(A5*np.cos(B5 + (C5 * JME)))

    earth_heliocentric_position=Earth_heliocentric_position()#创建该结构体

    earth_heliocentric_position.longitude = (L0 + (L1 * JME) + (L2 * JME **2) + (L3 * JME **3) + (L4 * JME **4) + (L5 * JME **5)) / 1e8
    earth_heliocentric_position.longitude = earth_heliocentric_position.longitude * 180 / math.pi
    earth_heliocentric_position.longitude = set_to_range(earth_heliocentric_position.longitude, 0, 360)

    B0_terms=np.array([[2.8000000e+02, 3.1990000e+00, 8.4334662e+04],
       [1.0200000e+02, 5.4220000e+00, 5.5075530e+03],
       [8.0000000e+01, 3.8800000e+00, 5.2236900e+03],
       [4.4000000e+01, 3.7000000e+00, 2.3528700e+03],
       [3.2000000e+01, 4.0000000e+00, 1.5773400e+03]])

    B1_terms=np.array([[9.00000e+00, 3.90000e+00, 5.50755e+03],
       [6.00000e+00, 1.73000e+00, 5.22369e+03]])

    A0 = B0_terms[:, 0]
    B0 = B0_terms[:, 1]
    C0 = B0_terms[:, 2]

    A1 = B1_terms[:, 0]
    B1 = B1_terms[:, 1]
    C1 = B1_terms[:, 2]

    L0 = np.sum(A0*np.cos(B0 + (C0 * JME)))
    L1 = np.sum(A1*np.cos(B1 + (C1 * JME)))

    earth_heliocentric_position.latitude = (L0 + (L1 * JME)) / 1e8
    earth_heliocentric_position.latitude = earth_heliocentric_position.latitude * 180 / np.pi
    earth_heliocentric_position.latitude = set_to_range(earth_heliocentric_position.latitude, 0, 360)

    R0_terms =np.array([[1.00013989e+08, 0.00000000e+00, 0.00000000e+00],
       [1.67070000e+06, 3.09846350e+00, 6.28307585e+03],
       [1.39560000e+04, 3.05525000e+00, 1.25661517e+04],
       [3.08400000e+03, 5.19850000e+00, 7.77137715e+04],
       [1.62800000e+03, 1.17390000e+00, 5.75338490e+03],
       [1.57600000e+03, 2.84690000e+00, 7.86041940e+03],
       [9.25000000e+02, 5.45300000e+00, 1.15067700e+04],
       [5.42000000e+02, 4.56400000e+00, 3.93021000e+03],
       [4.72000000e+02, 3.66100000e+00, 5.88492700e+03],
       [3.46000000e+02, 9.64000000e-01, 5.50755300e+03],
       [3.29000000e+02, 5.90000000e+00, 5.22369400e+03],
       [3.07000000e+02, 2.99000000e-01, 5.57314300e+03],
       [2.43000000e+02, 4.27300000e+00, 1.17906290e+04],
       [2.12000000e+02, 5.84700000e+00, 1.57734400e+03],
       [1.86000000e+02, 5.02200000e+00, 1.09770790e+04],
       [1.75000000e+02, 3.01200000e+00, 1.88492280e+04],
       [1.10000000e+02, 5.05500000e+00, 5.48677800e+03],
       [9.80000000e+01, 8.90000000e-01, 6.06978000e+03],
       [8.60000000e+01, 5.69000000e+00, 1.57208400e+04],
       [8.60000000e+01, 1.27000000e+00, 1.61000690e+05],
       [8.50000000e+01, 2.70000000e-01, 1.72601500e+04],
       [6.30000000e+01, 9.20000000e-01, 5.29690000e+02],
       [5.70000000e+01, 2.01000000e+00, 8.39968500e+04],
       [5.60000000e+01, 5.24000000e+00, 7.14307000e+04],
       [4.90000000e+01, 3.25000000e+00, 2.54431000e+03],
       [4.70000000e+01, 2.58000000e+00, 7.75520000e+02],
       [4.50000000e+01, 5.54000000e+00, 9.43776000e+03],
       [4.30000000e+01, 6.01000000e+00, 6.27596000e+03],
       [3.90000000e+01, 5.36000000e+00, 4.69400000e+03],
       [3.80000000e+01, 2.39000000e+00, 8.82739000e+03],
       [3.70000000e+01, 8.30000000e-01, 1.96510500e+04],
       [3.70000000e+01, 4.90000000e+00, 1.21395500e+04],
       [3.60000000e+01, 1.67000000e+00, 1.20364600e+04],
       [3.50000000e+01, 1.84000000e+00, 2.94246000e+03],
       [3.30000000e+01, 2.40000000e-01, 7.08490000e+03],
       [3.20000000e+01, 1.80000000e-01, 5.08863000e+03],
       [3.20000000e+01, 1.78000000e+00, 3.98150000e+02],
       [2.80000000e+01, 1.21000000e+00, 6.28660000e+03],
       [2.80000000e+01, 1.90000000e+00, 6.27955000e+03],
       [2.60000000e+01, 4.59000000e+00, 1.04473900e+04]])

    R1_terms =np.array([[1.03019000e+05, 1.10749000e+00, 6.28307585e+03],
       [1.72100000e+03, 1.06440000e+00, 1.25661517e+04],
       [7.02000000e+02, 3.14200000e+00, 0.00000000e+00],
       [3.20000000e+01, 1.02000000e+00, 1.88492300e+04],
       [3.10000000e+01, 2.84000000e+00, 5.50755000e+03],
       [2.50000000e+01, 1.32000000e+00, 5.22369000e+03],
       [1.80000000e+01, 1.42000000e+00, 1.57734000e+03],
       [1.00000000e+01, 5.91000000e+00, 1.09770800e+04],
       [9.00000000e+00, 1.42000000e+00, 6.27596000e+03],
       [9.00000000e+00, 2.70000000e-01, 5.48678000e+03]])

    R2_terms =np.array([[4.3590000e+03, 5.7846000e+00, 6.2830758e+03],
       [1.2400000e+02, 5.5790000e+00, 1.2566152e+04],
       [1.2000000e+01, 3.1400000e+00, 0.0000000e+00],
       [9.0000000e+00, 3.6300000e+00, 7.7713770e+04],
       [6.0000000e+00, 1.8700000e+00, 5.5731400e+03],
       [3.0000000e+00, 5.4700000e+00, 1.8849000e+04]])

    R3_terms =np.array([[1.450000e+02, 4.273000e+00, 6.283076e+03],
       [7.000000e+00, 3.920000e+00, 1.256615e+04]])

    R4_terms =np.array([4.00000e+00, 2.56000e+00, 6.28308e+03])

    A0 = R0_terms[:, 0]
    B0 = R0_terms[:, 1]
    C0 = R0_terms[:, 2]

    A1 = R1_terms[:, 0]
    B1 = R1_terms[:, 1]
    C1 = R1_terms[:, 2]

    A2 = R2_terms[:, 0]
    B2 = R2_terms[:, 1]
    C2 = R2_terms[:, 2]

    A3 = R3_terms[:, 0]
    B3 = R3_terms[:, 1]
    C3 = R3_terms[:, 2]

    A4 = R4_terms[0]
    B4 = R4_terms[1]
    C4 = R4_terms[2]

    L0 = np.sum(A0 * np.cos(B0 + (C0 * JME)))
    L1 = np.sum(A1 * np.cos(B1 + (C1 * JME)))
    L2 = np.sum(A2 * np.cos(B2 + (C2 * JME)))
    L3 = np.sum(A3 * np.cos(B3 + (C3 * JME)))
    L4 = np.sum(A4 * np.cos(B4 + (C4 * JME)))

    earth_heliocentric_position.radius = (L0 + (L1 * JME) + (L2 * JME **2) + (L3 * JME ** 3) + (L4 * JME ** 4)) / 1e8
    return  earth_heliocentric_position


def sun_geocentric_position_calculation(earth_heliocentric_position):
    sun_geocentric_position=Sun_geocentric_position()
    sun_geocentric_position.longitude = earth_heliocentric_position.longitude + 180
    sun_geocentric_position.longitude = set_to_range(sun_geocentric_position.longitude, 0, 360);
    sun_geocentric_position.latitude = -earth_heliocentric_position.latitude;
    sun_geocentric_position.latitude = set_to_range(sun_geocentric_position.latitude, 0, 360)
    return  sun_geocentric_position


def nutation_calculation(julian):
    JCE = julian.ephemeris_century
    p = np.array([(1 / 189474),- 0.0019142,445267.11148,297.85036])
    X0 = p[0] * JCE ** 3 + p[1] * JCE **2 + p[2] * JCE + p[3]

    p = np.array([-(1/300000),-0.0001603,35999.05034,357.52772])
    X1 = p[0] * JCE ** 3 + p[1] * JCE ** 2 + p[2] * JCE + p[3]

    p = np.array([(1/56250),0.0086972,477198.867398,134.96298])
    X2 = p[0] * JCE ** 3 + p[1] * JCE ** 2 + p[2] * JCE + p[3]

    p = np.array([(1/327270),-0.0036825,483202.017538,93.27191])
    X3 = p[0] * JCE ** 3 + p[1] * JCE ** 2 + p[2] * JCE + p[3]

    p = np.array([(1/450000),0.0020708,-1934.136261,125.04452])
    X4 = p[0] * JCE ** 3 + p[1] * JCE ** 2 + p[2] * JCE + p[3]

    Y_terms =np.array([[ 0.,  0.,  0.,  0.,  1.],
       [-2.,  0.,  0.,  2.,  2.],
       [ 0.,  0.,  0.,  2.,  2.],
       [ 0.,  0.,  0.,  0.,  2.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [-2.,  1.,  0.,  2.,  2.],
       [ 0.,  0.,  0.,  2.,  1.],
       [ 0.,  0.,  1.,  2.,  2.],
       [-2., -1.,  0.,  2.,  2.],
       [-2.,  0.,  1.,  0.,  0.],
       [-2.,  0.,  0.,  2.,  1.],
       [ 0.,  0., -1.,  2.,  2.],
       [ 2.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  1.],
       [ 2.,  0., -1.,  2.,  2.],
       [ 0.,  0., -1.,  0.,  1.],
       [ 0.,  0.,  1.,  2.,  1.],
       [-2.,  0.,  2.,  0.,  0.],
       [ 0.,  0., -2.,  2.,  1.],
       [ 2.,  0.,  0.,  2.,  2.],
       [ 0.,  0.,  2.,  2.,  2.],
       [ 0.,  0.,  2.,  0.,  0.],
       [-2.,  0.,  1.,  2.,  2.],
       [ 0.,  0.,  0.,  2.,  0.],
       [-2.,  0.,  0.,  2.,  0.],
       [ 0.,  0., -1.,  2.,  1.],
       [ 0.,  2.,  0.,  0.,  0.],
       [ 2.,  0., -1.,  0.,  1.],
       [-2.,  2.,  0.,  2.,  2.],
       [ 0.,  1.,  0.,  0.,  1.],
       [-2.,  0.,  1.,  0.,  1.],
       [ 0., -1.,  0.,  0.,  1.],
       [ 0.,  0.,  2., -2.,  0.],
       [ 2.,  0., -1.,  2.,  1.],
       [ 2.,  0.,  1.,  2.,  2.],
       [ 0.,  1.,  0.,  2.,  2.],
       [-2.,  1.,  1.,  0.,  0.],
       [ 0., -1.,  0.,  2.,  2.],
       [ 2.,  0.,  0.,  2.,  1.],
       [ 2.,  0.,  1.,  0.,  0.],
       [-2.,  0.,  2.,  2.,  2.],
       [-2.,  0.,  1.,  2.,  1.],
       [ 2.,  0., -2.,  0.,  1.],
       [ 2.,  0.,  0.,  0.,  1.],
       [ 0., -1.,  1.,  0.,  0.],
       [-2., -1.,  0.,  2.,  1.],
       [-2.,  0.,  0.,  0.,  1.],
       [ 0.,  0.,  2.,  2.,  1.],
       [-2.,  0.,  2.,  0.,  1.],
       [-2.,  1.,  0.,  2.,  1.],
       [ 0.,  0.,  1., -2.,  0.],
       [-1.,  0.,  1.,  0.,  0.],
       [-2.,  1.,  0.,  0.,  0.],
       [ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  2.,  0.],
       [ 0.,  0., -2.,  2.,  2.],
       [-1., -1.,  1.,  0.,  0.],
       [ 0.,  1.,  1.,  0.,  0.],
       [ 0., -1.,  1.,  2.,  2.],
       [ 2., -1., -1.,  2.,  2.],
       [ 0.,  0.,  3.,  2.,  2.],
       [ 2., -1.,  0.,  2.,  2.]])
    nutation_terms=np.array([[-1.71996e+05, -1.74200e+02,  9.20250e+04,  8.90000e+00],
       [-1.31870e+04, -1.60000e+00,  5.73600e+03, -3.10000e+00],
       [-2.27400e+03, -2.00000e-01,  9.77000e+02, -5.00000e-01],
       [ 2.06200e+03,  2.00000e-01, -8.95000e+02,  5.00000e-01],
       [ 1.42600e+03, -3.40000e+00,  5.40000e+01, -1.00000e-01],
       [ 7.12000e+02,  1.00000e-01, -7.00000e+00,  0.00000e+00],
       [-5.17000e+02,  1.20000e+00,  2.24000e+02, -6.00000e-01],
       [-3.86000e+02, -4.00000e-01,  2.00000e+02,  0.00000e+00],
       [-3.01000e+02,  0.00000e+00,  1.29000e+02, -1.00000e-01],
       [ 2.17000e+02, -5.00000e-01, -9.50000e+01,  3.00000e-01],
       [-1.58000e+02,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 1.29000e+02,  1.00000e-01, -7.00000e+01,  0.00000e+00],
       [ 1.23000e+02,  0.00000e+00, -5.30000e+01,  0.00000e+00],
       [ 6.30000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 6.30000e+01,  1.00000e-01, -3.30000e+01,  0.00000e+00],
       [-5.90000e+01,  0.00000e+00,  2.60000e+01,  0.00000e+00],
       [-5.80000e+01, -1.00000e-01,  3.20000e+01,  0.00000e+00],
       [-5.10000e+01,  0.00000e+00,  2.70000e+01,  0.00000e+00],
       [ 4.80000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 4.60000e+01,  0.00000e+00, -2.40000e+01,  0.00000e+00],
       [-3.80000e+01,  0.00000e+00,  1.60000e+01,  0.00000e+00],
       [-3.10000e+01,  0.00000e+00,  1.30000e+01,  0.00000e+00],
       [ 2.90000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 2.90000e+01,  0.00000e+00, -1.20000e+01,  0.00000e+00],
       [ 2.60000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-2.20000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 2.10000e+01,  0.00000e+00, -1.00000e+01,  0.00000e+00],
       [ 1.70000e+01, -1.00000e-01,  0.00000e+00,  0.00000e+00],
       [ 1.60000e+01,  0.00000e+00, -8.00000e+00,  0.00000e+00],
       [-1.60000e+01,  1.00000e-01,  7.00000e+00,  0.00000e+00],
       [-1.50000e+01,  0.00000e+00,  9.00000e+00,  0.00000e+00],
       [-1.30000e+01,  0.00000e+00,  7.00000e+00,  0.00000e+00],
       [-1.20000e+01,  0.00000e+00,  6.00000e+00,  0.00000e+00],
       [ 1.10000e+01,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-1.00000e+01,  0.00000e+00,  5.00000e+00,  0.00000e+00],
       [-8.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [ 7.00000e+00,  0.00000e+00, -3.00000e+00,  0.00000e+00],
       [-7.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-7.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [-7.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [ 6.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 6.00000e+00,  0.00000e+00, -3.00000e+00,  0.00000e+00],
       [ 6.00000e+00,  0.00000e+00, -3.00000e+00,  0.00000e+00],
       [-6.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [-6.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [ 5.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-5.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [-5.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [-5.00000e+00,  0.00000e+00,  3.00000e+00,  0.00000e+00],
       [ 4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-4.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [ 3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00],
       [-3.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00]])

    Xi=np.array([[X0],[X1],[X2],[X3],[X4]])
    tabulated_argument=np.matmul(Y_terms,Xi)*np.pi/180
    delta_longitude = ((nutation_terms[:, 0] + (nutation_terms[:, 1] * JCE)))*np.sin(tabulated_argument).T
    delta_obliquity = ((nutation_terms[:, 2] + (nutation_terms[:, 3] * JCE))) * np.sin(tabulated_argument).T
    nutation=Nutation()
    nutation.longitude = np.sum(delta_longitude) / 36000000
    nutation.obliquity = np.sum(delta_obliquity) / 36000000
    return nutation


def true_obliquity_calculation(julian, nutation):
    p = np.array([2.45,5.79,27.87,7.12,- 39.05,- 249.67,- 51.38,1999.25,- 1.55,- 4680.93,84381.448])
    U = julian.ephemeris_millenium / 10
    mean_obliquity = p[0] * U**10 + p[1] * U**9 + p[2] * U**8 + p[3] * U**7 + p[4] * U**6 + p[5] * U**5 + p[6] * U**4 + p[7] * U**3 + p[8] * U**2 + p[9] * U + p[10]
    true_obliquity = (mean_obliquity / 3600) + nutation.obliquity
    return true_obliquity

def abberation_correction_calculation(earth_heliocentric_position):
    aberration_correction = -20.4898 / (3600 * earth_heliocentric_position.radius)
    return aberration_correction


def apparent_sun_longitude_calculation(sun_geocentric_position, nutation,aberration_correction):
    apparent_sun_longitude = sun_geocentric_position.longitude + nutation.longitude + aberration_correction
    return apparent_sun_longitude


def apparent_stime_at_greenwich_calculation(julian, nutation, true_obliquity):
    JD = julian.day
    JC = julian.century
    mean_stime = 280.46061837 + (360.98564736629 * (JD - 2451545)) + (0.000387933 * JC **2) - (JC**3 / 38710000)
    mean_stime = set_to_range(mean_stime, 0, 360)
    apparent_stime_at_greenwich = mean_stime + (nutation.longitude * np.cos(true_obliquity * np.pi / 180))
    return  apparent_stime_at_greenwich


def sun_rigth_ascension_calculation(apparent_sun_longitude, true_obliquity,sun_geocentric_position):
    argument_numerator = (np.sin(apparent_sun_longitude * np.pi / 180) * np.cos(true_obliquity *np. pi / 180)) - \
                         (np.tan(sun_geocentric_position.latitude * np.pi / 180) * np.sin(true_obliquity * np.pi / 180))

    argument_denominator = np.cos(apparent_sun_longitude * np.pi / 180)
    sun_rigth_ascension = np.arctan2(argument_numerator, argument_denominator) * 180 / np.pi
    sun_rigth_ascension = set_to_range(sun_rigth_ascension, 0, 360)
    return sun_rigth_ascension

def sun_geocentric_declination_calculation(apparent_sun_longitude, true_obliquity,sun_geocentric_position):
    argument = (np.sin(sun_geocentric_position.latitude * np.pi/180) * np.cos(true_obliquity * np.pi/180)) + \
               (np.cos(sun_geocentric_position.latitude * np.pi/180) * np.sin(true_obliquity * np.pi/180) * np.sin(apparent_sun_longitude * np.pi / 180))
    sun_geocentric_declination = np.arcsin(argument) * 180/np.pi
    return sun_geocentric_declination


def observer_local_hour_calculation(apparent_stime_at_greenwich, location, sun_rigth_ascension):
    observer_local_hour = apparent_stime_at_greenwich + location.longitude - sun_rigth_ascension
    observer_local_hour = set_to_range(observer_local_hour, 0, 360)
    return observer_local_hour


def topocentric_sun_position_calculate(earth_heliocentric_position, location,observer_local_hour, sun_rigth_ascension,sun_geocentric_declination):
    eq_horizontal_parallax = 8.794 / (3600 * earth_heliocentric_position.radius)
    u = np.arctan(0.99664719 * np.tan(location.latitude * np.pi/180))
    x = np.cos(u) + ((location.altitude / 6378140) * np.cos(location.latitude * np.pi/180))
    y = (0.99664719 * np.sin(u)) + ((location.altitude/ 6378140) * np.sin(location.latitude * np.pi/180))
    nominator = -x * np.sin(eq_horizontal_parallax * np.pi/ 180) * np.sin(observer_local_hour * np.pi/180)
    denominator = np.cos(sun_geocentric_declination * np.pi/ 180) - ( \
                x * np.sin(eq_horizontal_parallax * np.pi/180) * np.cos(observer_local_hour * np.pi/180))
    sun_rigth_ascension_parallax = np.arctan2(nominator, denominator)
    topocentric_sun_position=Topocentric_sun_position()
    topocentric_sun_position.rigth_ascension_parallax = sun_rigth_ascension_parallax * 180 / np.pi
    topocentric_sun_position.rigth_ascension = sun_rigth_ascension + (sun_rigth_ascension_parallax * 180/np.pi)
    nominator = (np.sin(sun_geocentric_declination * np.pi / 180) - (y * np.sin(eq_horizontal_parallax * np.pi / 180))) * np.cos(sun_rigth_ascension_parallax)
    denominator = np.cos(sun_geocentric_declination * np.pi / 180) - (y * np.sin(eq_horizontal_parallax * np.pi / 180)) * np.cos(observer_local_hour * np.pi / 180)
    topocentric_sun_position.declination = np.arctan2(nominator, denominator) * 180 / np.pi
    return topocentric_sun_position

def topocentric_local_hour_calculate(observer_local_hour, topocentric_sun_position):
    topocentric_local_hour = observer_local_hour - topocentric_sun_position.rigth_ascension_parallax
    return topocentric_local_hour


def sun_topocentric_zenith_angle_calculate(location, topocentric_sun_position, topocentric_local_hour):
    argument = (np.sin(location.latitude * np.pi / 180) * np.sin(topocentric_sun_position.declination * np.pi / 180)) + \
                (np.cos(location.latitude * np.pi / 180) * np.cos(topocentric_sun_position.declination * np.pi / 180) * np.cos(topocentric_local_hour * np.pi / 180))
    true_elevation = np.arcsin(argument) * 180 / np.pi
    argument = true_elevation + (10.3 / (true_elevation + 5.11))
    refraction_corr = 1.02 / (60 * np.tan(argument * np.pi / 180))
    apparent_elevation = true_elevation + refraction_corr
    sun=Sun()
    sun.zenith = 90 - apparent_elevation
    nominator = np.sin(topocentric_local_hour * np.pi / 180)
    denominator = (np.cos(topocentric_local_hour * np.pi / 180) * np.sin(location.latitude * np.pi / 180)) - \
                (np.tan(topocentric_sun_position.declination * np.pi / 180) * np.cos(location.latitude * np.pi / 180))
    sun.azimuth = (np.arctan2(nominator, denominator) * 180 / np.pi) + 180
    sun.azimuth = set_to_range(sun.azimuth, 0, 360)
    return sun


def set_to_range(var, min_interval, max_interval):
    var = var - max_interval * np.floor(var / max_interval)
    if (var < min_interval):
        var = var + max_interval
    return var



def sun_position(time,location):
    #1
    julian=julian_calculation(time)
    #2
    earth_heliocentric_position = earth_heliocentric_position_calculation(julian)
    #3
    sun_geocentric_position = sun_geocentric_position_calculation(earth_heliocentric_position)
    #4
    nutation = nutation_calculation(julian)
    #5
    true_obliquity = true_obliquity_calculation(julian, nutation)
    #6
    aberration_correction = abberation_correction_calculation(earth_heliocentric_position)
    #7
    apparent_sun_longitude = apparent_sun_longitude_calculation(sun_geocentric_position, nutation,aberration_correction)
    #8
    apparent_stime_at_greenwich = apparent_stime_at_greenwich_calculation(julian, nutation, true_obliquity)
    #9
    sun_rigth_ascension = sun_rigth_ascension_calculation(apparent_sun_longitude, true_obliquity,sun_geocentric_position)
    #10
    sun_geocentric_declination = sun_geocentric_declination_calculation(apparent_sun_longitude, true_obliquity,sun_geocentric_position)
    #11
    observer_local_hour = observer_local_hour_calculation(apparent_stime_at_greenwich, location, sun_rigth_ascension)
    #12
    topocentric_sun_position = topocentric_sun_position_calculate(earth_heliocentric_position, location,observer_local_hour, sun_rigth_ascension,sun_geocentric_declination)
    #13
    topocentric_local_hour = topocentric_local_hour_calculate(observer_local_hour, topocentric_sun_position)
    #14
    sun = sun_topocentric_zenith_angle_calculate(location, topocentric_sun_position, topocentric_local_hour)
    return  sun



def sun_angle(lon,lat,utc):##哈哈，借鉴别人的方法，翻译了一下，完全不懂
    times =[int(i) for i in utc.strip().split("-")]
    T = time(times[0], times[1], times[2], times[3], times[4], times[5], 0)
    L=location(lon,lat,0)
    sun=sun_position(T,L)#zenith天顶角，azimuth方位角
    return sun.zenith,sun.azimuth

#sun_angle(r"E:\MyResearchWork\wdz")

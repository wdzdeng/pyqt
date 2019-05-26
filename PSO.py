"""
    Created by 壮壮 on 2019/4/26 0026
"""
__author__ = "wdz"

import random
from bird import getBird
import numpy as np
import Compare2

# class bird():
#     """
#     speed:速度
#     position:位置
#     fit:适应度
#     lbestposition:经历的最佳位置
#     lbestfit:经历的最佳的适应度值
#     """
#
#     def __init__(self, speed, position, fit, lBestPosition, lBestFit):
#         self.speed = speed
#         self.position = position
#         self.fit = fit
#         self.lBestFit = lBestPosition
#         self.lBestPosition = lBestFit


class PSO():
    """
    fitFunc:适应度函数
    birdNum:种群规模
    w:惯性权重
    c1,c2:个体学习因子，社会学习因子
    solutionSpace:解空间，列表类型：[最小值，最大值]
    """
    def __init__(self, fitFunc, birdNum, w, c1, c2, solutionSpace,sun_zenith,sun_azimuth,feng,N_deviation,B_deviation,add_deviation,target):
        #Sun_zenith,Sun_azimuth,feng,N_deviation,B_deviation,add_deviation

        self.fitFunc = fitFunc
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.solutionSpace = solutionSpace
        self.sun_zenith = sun_zenith
        self.sun_azimuth = sun_azimuth
        self.feng = feng
        self.N_deviation = N_deviation
        self.B_deviation = B_deviation
        self.add_deviation =add_deviation
        self.target = target
        self.birds, self.best = self.initbirds(birdNum, solutionSpace)


    def initbirds(self, size, solutionSpace):

        birds = []


        for i in range(size):
            position = [0,0,0,0]
            position[0] = random.uniform(solutionSpace[0][0],solutionSpace[0][1])
            position[1] = random.uniform(solutionSpace[1][0], solutionSpace[1][1])
            position[2] = random.uniform(solutionSpace[2][0], solutionSpace[2][1])
            position[3] = random.uniform(solutionSpace[3][0], solutionSpace[3][1])
            #position = random.uniform(solutionSpace[0], solutionSpace[1])
            speed = [0,0,0,0]
            fit = self.fitFunc(position,self.sun_zenith,self.sun_azimuth,self.feng,self.N_deviation,self.B_deviation,self.add_deviation,self.target)
            birds.append(getBird(speed,position,fit,position,fit))
        best = birds[0]
        for bird in birds:
            if bird.fit < best.fit:
                best = bird
        return birds, best

    def updateBirds(self):

        for bird in self.birds:
            # 更新速度
            bird.speed = list(self.w * np.array(bird.speed) + self.c1 * random.random() * (
                        np.array(bird.lBestPosition) - np.array(bird.position)) + self.c2 * random.random() * (
                                     np.array(self.best.position) - np.array(bird.position)))
            # 更新位置
            bird.position = list(np.array(bird.position) + np.array(bird.speed))
            # bird.position[0] = float(bird.position[0])
            # bird.position[1] = int(bird.position[1])
            # bird.position[2] = int(bird.position[2])
            # bird.position[3] = int(bird.position[3])
            # # 跟新适应度
            self.dealOutBounds(bird.position,self.solutionSpace)
            bird.fit = self.fitFunc(bird.position,self.sun_zenith,self.sun_azimuth,self.feng,self.N_deviation,self.B_deviation,self.add_deviation,self.target)
            # 查看是否需要更新经验最优
            if bird.fit < bird.lBestFit:
                bird.lBestFit = bird.fit
                bird.lBestPosition = bird.position
    def dealOutBounds(self,position,limit):
        position[0] = limit[0][0] if position[0]<limit[0][0] else position[0]
        position[0] = limit[0][1] if position[0] > limit[0][1] else position[0]

        position[1] = limit[1][0] if position[1] < limit[1][0] else position[1]
        position[1] = limit[1][1] if position[1] > limit[1][1] else position[1]

        position[2] = limit[2][0] if position[2] < limit[2][0] else position[2]
        position[2] = limit[2][1] if position[2] > limit[2][1] else position[2]

        position[3] = limit[3][0] if position[3] < limit[3][0] else position[3]
        position[3] = limit[3][1] if position[3] > limit[3][1] else position[3]

    def solve(self, maxIter):
        # 只考虑了最大迭代次数，如需考虑阈值，添加判断语句就好
        for i in range(maxIter):
            # 更新粒子
            print(i)
            self.updateBirds()
            for bird in self.birds:
                # 查看是否需要更新全局最优
                if bird.fit < self.best.fit:
                    self.best = bird

def a(x,sun_zenith,sun_azimuth,feng,N_deviation,B_deviation,add_deviation,target):
    if target == 0:
        error = Compare2.compare2(x[0], x[1], x[2], x[3], sun_zenith, sun_azimuth, feng, N_deviation, B_deviation,
                 add_deviation)
        return error*100
    if target == 1:
        error = Compare2.compare2(x[0], x[1], x[0], x[3], sun_zenith, sun_azimuth, feng, N_deviation, B_deviation,
                                  add_deviation)
        return error * 100
    if target == 2:
        error = Compare2.compare2(x[0], x[1], x[2], x[1], sun_zenith, sun_azimuth, feng, N_deviation, B_deviation,
                                  add_deviation)
        return error * 100
# b = PSO(a,1000,0.4,2,2,[[0,89],[0,360],[0,89],[0,360]],20,120,7,4,7,0.005)
# b.solve(100)
# print(b.best.position,b.best.fit)
def dealPSO(birdNum,update,solutionSpace,sun_zenith,sun_azimuth,feng,N_deviation,B_deviation,add_deviation,target):
    PSOobject = PSO(a,birdNum,0.4,2,2,solutionSpace,sun_zenith,sun_azimuth,feng,N_deviation,B_deviation,add_deviation,target)
    PSOobject.solve(update)
    if target == 1:
        PSOobject.best.position[2] =  PSOobject.best.position[0]
    if target == 2:
        PSOobject.best.position[3] = PSOobject.best.position[1]
    print(PSOobject.best.position,PSOobject.best.fit)
    return PSOobject.best.position,PSOobject.best.fit



#c = b.solve(100)
#print(c)
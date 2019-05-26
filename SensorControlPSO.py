"""
    Created by 壮壮 on 2019/4/26 0026
"""
__author__ = "wdz"

import random
#from bird import getBird
import numpy as np
import Compare2
from y_angle_calculate import point_calculate

class bird():
    """
    speed:速度
    position:位置
    fit:适应度
    lbestposition:经历的最佳位置
    lbestfit:经历的最佳的适应度值
    """

    def __init__(self, speed, position, fit, lBestPosition, lBestFit,result):
        self.speed = speed
        self.position = position
        self.fit = fit
        self.lBestFit = lBestFit
        self.lBestPosition = lBestPosition
        self.result = result
def getBird(speed, position, fit, lBestPosition, lBestFit,result):
    return bird(speed, position, fit, lBestPosition, lBestFit,result)



class PSO():
    """
    fitFunc:适应度函数
    birdNum:种群规模
    w:惯性权重
    c1,c2:个体学习因子，社会学习因子
    solutionSpace:解空间，列表类型：[最小值，最大值]
    """
    def __init__(self, fitFunc, birdNum, w, c1, c2, solutionSpace,h1,h2,optimal,target):
        #Sun_zenith,Sun_azimuth,feng,N_deviation,B_deviation,add_deviation

        self.fitFunc = fitFunc
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.solutionSpace = solutionSpace
        self.h1 = h1
        self.h2 = h2
        self.target = target
        self.optimal = optimal
        self.birds, self.best = self.initbirds(birdNum, solutionSpace)


    def initbirds(self, size, solutionSpace):

        birds = []


        for i in range(size):
            position = [0,0,0,0,0,0]
            position[0] = random.uniform(solutionSpace[0][0],solutionSpace[0][1])
            position[1] = random.uniform(solutionSpace[1][0], solutionSpace[1][1])
            position[2] = random.uniform(solutionSpace[2][0], solutionSpace[2][1])
            position[3] = random.uniform(solutionSpace[3][0], solutionSpace[3][1])
            position[4] = random.uniform(solutionSpace[4][0], solutionSpace[4][1])
            position[5] = random.uniform(solutionSpace[5][0], solutionSpace[5][1])
            #position = random.uniform(solutionSpace[0], solutionSpace[1])
            speed = [0,0,0,0,0,0]
            fit,result = self.fitFunc(position,self.h1,self.h2,self.target,self.optimal)
            birds.append(getBird(speed,position,fit,position,fit,result))
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
            bird.fit,bird.result = self.fitFunc(bird.position,self.h1,self.h2,self.target,self.optimal)
            # 查看是否需要更新经验最优
            if bird.fit < bird.lBestFit:
                bird.lBestFit = bird.fit
                bird.lBestPosition = bird.position
    def dealOutBounds(self,position,limit):
        position[0] = limit[0][0] if position[0] < limit[0][0] else position[0]
        position[0] = limit[0][1] if position[0] > limit[0][1] else position[0]

        position[1] = limit[1][0] if position[1] < limit[1][0] else position[1]
        position[1] = limit[1][1] if position[1] > limit[1][1] else position[1]

        position[2] = limit[2][0] if position[2] < limit[2][0] else position[2]
        position[2] = limit[2][1] if position[2] > limit[2][1] else position[2]

        position[3] = limit[3][0] if position[3] < limit[3][0] else position[3]
        position[3] = limit[3][1] if position[3] > limit[3][1] else position[3]

        position[4] = limit[4][0] if position[4] < limit[4][0] else position[4]
        position[4] = limit[4][1] if position[4] > limit[4][1] else position[4]

        position[5] = limit[5][0] if position[5] < limit[5][0] else position[5]
        position[5] = limit[5][1] if position[5] > limit[5][1] else position[5]

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

def a(x,h1,h2,target,optimal):
    if target == 0:
        combination = list(point_calculate(x[0], x[1],x[2], x[3], x[4], x[5],h1,h2))
        return np.sum(np.abs(np.array(combination)-optimal)),combination
    if target == 1:
        combination = list(point_calculate(x[0], x[1], x[2], x[0], x[4], x[5], h1,h2))
        return np.sum(np.abs(np.array(combination) - optimal)), combination
    if target == 2:
        combination = list(point_calculate(x[0], x[1], x[2], x[3], x[1], x[5], h1,h2))
        return np.sum(np.abs(np.array(combination) - optimal)), combination
    if target == 3:
        combination = list(point_calculate(x[0], x[1], x[2], x[3], x[4], x[2], h1,h2))
        return np.sum(np.abs(np.array(combination) - optimal)), combination
    if target == 4:
        combination = list(point_calculate(x[0], x[1], x[2], x[0], x[1], x[5], h1,h2))
        return np.sum(np.abs(np.array(combination) - optimal)), combination
    if target == 5:
        combination = list(point_calculate(x[0], x[1], x[2], x[0], x[4], x[2], h1,h2))
        return np.sum(np.abs(np.array(combination) - optimal)), combination
    if target == 6:
        combination = list(point_calculate(x[0], x[1],x[2], x[3], x[1], x[2],h1,h2))
        return np.sum(np.abs(np.array(combination)-optimal)),combination
# b = PSO(a,1000,0.4,2,2,[[0,89],[0,360],[0,89],[0,360]],20,120,7,4,7,0.005)
# b.solve(100)
# print(b.best.position,b.best.fit)
def dealPSO(birdNum,update,solutionSpace,h1,h2,optimal,target):
    PSOobject = PSO(a,birdNum,0.4,2,2,solutionSpace,h1,h2,optimal,target)
    PSOobject.solve(update)
    if target == 1:
        PSOobject.best.position[3] =  PSOobject.best.position[0]
    if target == 2:
        PSOobject.best.position[4] = PSOobject.best.position[1]
    if target == 3:
        PSOobject.best.position[5] = PSOobject.best.position[2]
    if target == 4:
        PSOobject.best.position[3] = PSOobject.best.position[0]
        PSOobject.best.position[4] = PSOobject.best.position[1]
    if target == 5:
        PSOobject.best.position[3] = PSOobject.best.position[0]
        PSOobject.best.position[5] = PSOobject.best.position[2]
    if target == 6:
        PSOobject.best.position[4] = PSOobject.best.position[1]
        PSOobject.best.position[5] = PSOobject.best.position[2]
    print(PSOobject.best.position,PSOobject.best.fit,PSOobject.best.result)
    return PSOobject.best.position,PSOobject.best.fit,PSOobject.best.result

#psv
#dealPSO(100000,10,[[-89,89],[0,360],[-89,89],[-89,89],[0,360],[-89,89]],120,120,np.array([10,120,20,120]),2)
#print(point_calculate(3, 0, -9, 7, 0, -19,200))
#c = b.solve(100)
#print(c)
"""
    Created by 壮壮 on 2019/4/26 0026
"""
__author__ = "wdz"
class bird:
    """
    speed:速度
    position:位置
    fit:适应度
    lbestposition:经历的最佳位置
    lbestfit:经历的最佳的适应度值
    """
    def __init__(self, speed, position, fit, lBestPosition, lBestFit):
        self.speed = speed
        self.position = position
        self.fit = fit
        self.lBestFit = lBestFit
        self.lBestPosition = lBestPosition
def getBird(speed, position, fit, lBestPosition, lBestFit):
    return bird(speed, position, fit, lBestPosition, lBestFit)
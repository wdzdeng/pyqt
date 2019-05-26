"""
    Created by 壮壮 on 2019/4/22 0022
"""
__author__ = "wdz"
import Ldaqi_calucate
import lr_calucate
def get_ld_lr(image_zenith,image_azimuth,sun_zenith_azimuth,utc,n_plus,n_minus):
    date = [int(i) for i in utc.split("-")][0:3]



 
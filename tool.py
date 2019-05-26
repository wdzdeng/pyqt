"""
    Created by 壮壮 on 2019/3/25 0025
"""
__author__ = "wdz"
import os
def transPyFile(uifile):
    pyfile = os.path.splitext(uifile)[0]+".py"
    print(pyfile)
    cmd = "pyuic5 -o {pyfile} {uifile}".format(pyfile=pyfile,uifile=uifile)
    os.system(cmd)
transPyFile("Distance.ui")
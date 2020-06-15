import sys

def Conver_min(min):
    if  min < 0:
        raise ValueError("min<0")
    else:
        print( "{} H, {} M".format(int(min / 60), min % 60))
Conver_min(910)
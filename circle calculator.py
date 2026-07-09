import math

def rrpi():
    r = float(input("enter the circle's radius:"))
    area = math.pi*r*r
    envi = r*2*math.pi
    volume = (4/3)*math.pi*r**3
    print("radius: ",r,  "area: ", area, "environment: ", envi, "volume: ", volume)

rrpi()
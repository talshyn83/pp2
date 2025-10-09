import math

n=int(input())
s=int(input())
area=(n*(s**2)/4*math.tan(math.pi/n))

print (round(area))
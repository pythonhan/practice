import math
from math import sqrt,cos,pi
x=input('输入两边长以及夹角：')
a,b,theta=map(float,x.split())
c=sqrt(a**2+b**2-2*a*b*cos(theta*pi/180))
print('C= ',c)
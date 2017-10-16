s=input('x,y,z=')
x,y,z=s.split(',')
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print('%s\n%s\n%s' % (x,y,z))
x,y,z=sorted([x,y,z])
print(x,y,z)
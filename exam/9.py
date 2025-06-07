
a,b,c = map(float,input().split(','))
d= b**2 - 4*a*c
x1= (-b + d**0.5) / (2 * a)
x2= (-b - d**0.5) / (2 * a)
print("%0.2f"%x1)
print("%0.2f"%x2)
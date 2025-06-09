

i = 1
s = 0
while 3 ** i < 10000:
    s+=3**i
    i+=1
s += 3 ** i
print(s)
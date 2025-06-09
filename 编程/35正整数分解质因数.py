x = input()
print(x)

for i in range(2,x+1):
    while x != i:
        if x % i == 0:
            print("%d*"%i,end=' ')
            x /=i
        else:
            break
print(x)
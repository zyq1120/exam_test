n = eval(input())
f1 = 1
f2 = 1
for i in range(3 , n+1):
    f = f1 + f2
    f1,f2 = f2 ,f
print(f)
n = eval(input())
for i in range(n):
    if (i % 7 != 0) and (i % 3 == 0):
        print(i, end=' ')
n = eval(input())
s = n
while n>=3:
    s += n // 3
    n = n//3+n % 3
print(s)

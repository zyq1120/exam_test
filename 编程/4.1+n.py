def sum_(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

print(sum_(int(input())))
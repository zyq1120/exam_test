num = input()

x  = eval(input())

s = 3000

if x < 88:
    s = x * 20
elif x > 176:
    s += 176*20 + (x -176) * 20 * 1.3
else:
    s += x * 20
print(s)
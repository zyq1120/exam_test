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











num = input()
a = 3000
h = 20
n = eval(input())


if n < 88:
    print(n * h)
elif 176 < n:
    print(176 * h + (n - 176) * h * 1.3+a)
else:
    print(a + n * h)
































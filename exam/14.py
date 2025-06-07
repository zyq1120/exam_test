"""
35.	正整数分解质因数 （分值：2.00）
【问题描述】将⼀个正整数分解质因数。如：输⼊90，输出90＝2*3*3*5。
【输⼊形式】正整数
【输出形式】质因数相乘
【样例输⼊】90
【样例输出】90＝2*3*3*5

"""

x = int(input())
print("%d="%x,end='')

for i in range(2,x+1):
    while x != i:
        if x % i == 0:
            print("%d*" % i, end='')
            x = x // i
        else:
            break
print("%d"%x)

x = int(input())
print("%d"%x,end='')
for i in range(2,x+1):
    while x != i:
        if x % i == 0:
            print("%d*"%i,end='')
            x = x // i
        else:
            break
print("%d"%x)
"""
14. 找出m,n间的所有素数
【问题描述】输出m,n之间的所有素数，每行输出10个。m,n由键盘输入。

【输入形式】m,n
【输出形式】一组素数（空格分隔）
【样例输入】10,30
【样例输出】11 13 17 19 23 29
"""
m,n = eval(input())
str1 = ""
for i in range(m , n):
    for j in range(m,n**0.5+1):
        if i % j == 0:
            str1 += i
print(str1)

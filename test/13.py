"""
【问题描述】请编程输出不大于n 的所有不能被 7 整除但能被 3 整除的自然数，其中n由键盘输入。

【输入形式】n=input("")，input里不要有任何提示语
【输出形式】输出的结果每个数中间用空格隔开，如2 3 4 6 7
【样例输入】7
【样例输出】3 6
"""

n = input("")
for i in range(int(n)):
    if i % 3 == 0 and i % 7 != 0:
        print(i,end=" ")


n = eval(input(""))
for i in range(n):
    if (i % 7 != 0) and i % 3 == 0:
        print(i,end=' ')
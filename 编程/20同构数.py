"""
同构数

（分值：
3.00
）
【问题描述】
具有下⾯性质的数
a
称为
&ldquo;
同构数
&rdquo;
：
设
b
是
a
的平⽅，
a
与
b
的低若⼲位相同。
例如，
5
是
25
的同构数
,25
是
625
的同构数
编程序满⾜如下要求
:
输⼊两个整数
a,b (0<=a, b<=99),
找出
a
、
b
之间全部的同构数。
【输⼊形式】
从键盘输⼊
0-99
之间的两个整数
a
和
b
，以空格隔开。
【输出形式】
在屏幕上按照由⼩到⼤的顺序输出所有同构数，每⼀个整数占⼀⾏。
【输⼊样例】
0 30
【输出样例】
0
 1
 5
 6
 25
【样例说明】
在
0-30
之间的同构数有
0, 1, 5, 6, 25.
【评分标准】
结果完全正确得
20
分，每个测试点
4
分
"""
from sys import int_info

a,b=map(int,input().split())
for i in range(a,b+1):
    if str(i*i).endswith(str(i)):
        print(i)












n,m = int(input())
for j in  range(n,m+1):
    if str(j*j).endswith(str(j)):
        print(j)


m,n = int(input())
for i in range(m,n+1):
    if str(i*i).endswith(str(i)):
        print(i)



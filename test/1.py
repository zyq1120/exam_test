"""
1. 找对应数
【问题描述】编写程序找到并输出一个特定的4位数，它的4倍正好是他数字的逆序，即4 X abcd = dcba（要求使用循环实现）

【输入形式】无
【输出形式】四位类型的整数
【样例输入】无
【样例输出】2178
【样例说明】4*2178=8712
"""

for i in range(1000,2500+1):
    z = int(str(i)[::-1])
    if z == i * 4:
        print(i)
        break

for i in range(1000,2501):
    z = int(str(i)[::-1])
    if z == i* 4:
        print(i)
        break

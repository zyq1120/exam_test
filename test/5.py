"""
5. 函数
【问题描述】请定义函数count(str,c)，检查字符串str中单个字符c出现的次数，返回这个次数。

【输入形式】输入字符串
【输出形式】输出字符串中指定字符出现的次数。
【样例输入】abcds  c

【样例输出】1
"""

def count(str,c):
    count = 0
    for i in range(len(str)):
        if str[i] == c:
            count += 1
    return count

n = input()
m = input()
print(count(n,m))
"""
10. 判断由键盘输入的一行字符中元音字母的个数。
【问题描述】判断由键盘输入的一行字符中元音字母的个数。
【输入形式】input不要任何提示语,元音字母包含a o e i u
【输出形式】输出数字
【样例输入】python
【样例输出】1
"""
n = input()
count = 0
for i in range(len(n)):
    if n[i] == 'a' or n[i] == 'o' or n[i] == 'e' or n[i] == 'i' or n[i]=='u':
        count +=1
print(count)
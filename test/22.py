"""
【问题描述】键盘输入一行字符串，请编程输出每个字符对应的Unicode值，一行输出，逗号分隔。

【样例输入】qaz
【样例输出】113,97,122
"""
print(','.join(str(ord(c))for c in input().strip()))
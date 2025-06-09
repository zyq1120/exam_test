"""
【问题描述】求s=a+aa+aaa+aaaa+aa·..a 的值，其中a是一个数字。例如2+22+222+2222+22222(个数相加)，求6个这样的数相加。

【输入形式】a=input('')，input中不要加任何提示内容
【输出形式】6个数的和
【样例输入】a这个数由键盘输入
【样例输出】直接打印结果，如print(result)
"""
a = int(input(''))
sum1 = 0
c = 0
for i in range(6):
    sum1 = sum1 * 10 + a
    c += sum1
print(c)

# n = 0
# m = 0
# a = int(input(''))
# for i in range(6):
#     n = n*10 + a
#     m = m +n
# print(m)
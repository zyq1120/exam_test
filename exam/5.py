"""
百分之转换
"""

n = int(input())

if n > 100 or n < 0 :
    print("wrong score")
elif n>=90:
    print("优")
elif n>=80:
    print("良")
elif n>=70:
    print("中")
elif n>=60:
    print("及格")
else:
    print("不及格")
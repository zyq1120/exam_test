"""
【问题描述】键盘输⼊圆柱体的底⾯半径和⾼，计算并输出圆柱体的表⾯积和体积。（⼩数点后保留2位⼩数）
【输⼊形式】底⾯半径，⾼
【输出形式】表⾯积 体积（中间留⼀空格）
【样例输⼊】2.0,3
【样例输出】62.83 37.70

"""

import math
r,h = map(float, input().split(','))
print("%0.2f %0.2f"%(2 * math.pi * r**2 + 2 * math.pi * r* h,math.pi* r**2 *h))

"""
有无重复元素
"""

n = list(eval(input()))
for i in n:
    if n.count(i) >= 2:
        print("yes")
        break
else:print('no')
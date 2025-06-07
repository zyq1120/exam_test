"""
判断有无重复元素
"""

list1 = list(eval(input()))
for e in list1:
    if list1.count(e)>= 2:
        print("yes")
        break;
else:
    print("no")

"""
16. 请编程判断一个列表中有无重复元素
【问题描述】请编程判断一个列表中有无重复元素，若有输出yes，没有输出no。

【输入形式】输入列表数据，用逗号分隔

【输出形式】yes或no
【样例输入】1,2,3,4,5,6,7,8,9,2,3

【样例输出】yes
【样例说明】
【评分标准】
"""
list1 = list(eval(input()))
for e in list1:
    if list1.count(e)>= 2:
        print("yes")
        break;
else:
    print("no")

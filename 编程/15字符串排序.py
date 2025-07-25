"""
【问题描述】编写⼀个程序，从键盘接收⼀个字符串，然后按照字符顺序从⼩到⼤进⾏排序，并删
除重复的字符。
【输⼊形式】⽤户在第⼀⾏输⼊⼀个字符串。
【输出形式】程序按照字符
(ASCII)
顺序从⼩到⼤排序字符串，并删除重复的字符进⾏输出。
【样例输⼊】
badacgegfacb
【样例输出】
abcdefg
【样例说明】⽤户输⼊字符串
badacgegfacb
，程序对其进⾏按从⼩到⼤
(ASCII)
顺序排序，并删除重
复的字符，最后输出为
abcdefg
【评分标准】结果完全正确得
20
分，每个测试点
4
分。
"""
from os import set_inheritable

print(''.join(sorted(set(input()))))


print(' '.join(sorted(set(input()))))

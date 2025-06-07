"""
【问题描述】请定义函数count(str,c)，检查字符串str中单个字符c出现的次数，返回这个次数。
【输⼊形式】输⼊字符串
【输出形式】输出字符串中指定字符出现的次数。
【样例输⼊】abcds  c
【样例输出】1
【样例说明】【评分标准】

"""

def count(str, c):
    count = 0
    for i in str:
        if i == c:
            count += 1
    return count

if __name__ == "__main__":
    i = input().split()
    print(count(i[0], i[1]))

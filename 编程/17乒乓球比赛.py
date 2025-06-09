# 固定匹配关系，满足题目条件
matches = {
    'a': 'z',
    'b': 'x',
    'c': 'y',
    'x': 'b',
    'y': 'c',
    'z': 'a'
}

# 输入选手代号
p = input().strip()

# 输出对应对手
print(matches.get(p))

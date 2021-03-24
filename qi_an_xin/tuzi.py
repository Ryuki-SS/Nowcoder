n = int(input())
m1, m2, m3, adu = 1, 0, 0, 0
for i in range(n - 1):
    m1, m2, m3, adu = adu, m1, m2, adu + m3
print(sum((m1, m2, m3, adu)))


"""
有一对兔子，从出生后的第五个月起每月生出一对小兔子（即满4月就开始生小兔），小兔子也会出生从第五个月起每月生一对小免子。假如兔子不会死，第n个月时，兔群有多少对兔子。

输入描述:
第n月（n为自然数，n<101）

输出描述:
第n个月时，兔子的对数（免群的兔子有多少对兔子）。

输入例子1:
5

输出例子1:
2

例子说明1:
第五个月时，有两对兔子
"""
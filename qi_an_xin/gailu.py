from math import factorial


def combination(m, n):
    son = factorial(n)
    mot = factorial(m) * factorial(n - m)
    return son / mot


n = int(input())
if n <= 990:
    res = 1 - combination(n, 990) / combination(n, 1000)
else:
    res = 1
print("{0:.6f}".format(res))

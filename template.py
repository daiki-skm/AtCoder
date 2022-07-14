import sys
from itertools import combinations, permutations, product, accumulate, groupby
from collections import defaultdict, deque, Counter
from functools import reduce
from operator import add, mul
import heapq
from bisect import bisect_left, bisect_right
from math import gcd, ceil, floor, sqrt, sin, cos, atan2, radians, pi
from math import log, log2, log10, exp, tan, asin, acos
from copy import deepcopy

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
MOD = 10 ** 9 + 7


# dfs, bfs, 全探索, 二分探索, 累積和, dp, ナップサック

def choose(n, a, mod):
    x = 1
    y = 1
    for i in range(min(n - a, a)):
        x *= n - i
        x %= mod
        y *= i + 1
        y %= mod
    # fermat's little theorem
    return x * pow(y, mod - 2, mod) % mod


# 表
# 左下から右上へ行く経路は何通りか
# →→↑↑↑↑
# choose(a+b, a, mod)

# 三角形の左下(右下)の角度求める
# atan2(y, x) (radians)
# (radians / 2pi) * 360 (degrees)

def rle(s):
    r = []
    for i in range(len(s)):
        if len(r) > 0 and r[-1][0] == s[i]:
            r[-1][1] += 1
        else:
            r.append([s[i], 1])
    return r


# オーダー的には枝刈より二分探索

# A, Bの公約数 = GCD(A, B)の約数

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# 2以上の公約数（1は含んでいないので、最後に足す）
def factorize(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i:
            continue
        res.append([i, 0])
        while n % i == 0:
            n //= i
            res[-1][1] += 1
    if n != 1:
        res.append([n, 1])
    return res

# A
# d, t, s = map(int, input().split())
# ans = d / s
# if ans <= t:
#     print('Yes')
# else:
#     print('No')

# B
# s = input()
# t = input()
# ans = 10 ** 9
# for si in range(len(s)):
#     if si + len(t) > len(s):
#         break
#     cnt = 0
#     for ti in range(len(t)):
#         if s[si + ti] != t[ti]:
#             cnt += 1
#     ans = min(ans, cnt)
# print(ans)

# C
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# x = 0
# mod = 10 ** 9 + 7
# for i in range(n):
#     ans = (ans + a[i] * x) % mod
#     x = (x + a[i]) % mod
# print(ans)

# D
# from collections import deque, defaultdict, Counter
# import itertools
# import math
# import bisect
# import heapq
# from functools import reduce
# from sys import setrecursionlimit
#
# setrecursionlimit(10 ** 6)
# N, M = map(int, input().split())
#
#
# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n
#
#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]
#
#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)
#
#         if x == y:
#             return
#
#         if self.parents[x] > self.parents[y]:
#             x, y = y, x
#
#         self.parents[x] += self.parents[y]
#         self.parents[y] = x
#
#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]
#
#     def group_count(self):
#         return len(self.roots())
#
#     def size(self, x):
#         return -self.parents[self.find(x)]
#
#
# uf = UnionFind(N)
#
# for i in range(M):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     uf.union(a, b)
# ans = 0
# for i in range(N):
#     ans = max(ans, uf.size(i))
# print(ans)

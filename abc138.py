# A
# a = int(input())
# s = input()
# if a >= 3200:
#     print(s)
#     exit()
# print('red')

# B
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     ans += 1 / a[i]
# print(1 / ans)

# C
# n = int(input())
# v = list(map(int, input().split()))
# v.sort()
# ans = v[0]
# for i in range(1, n):
#     ans = (ans + v[i]) / 2
# print(ans)

# D
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
# n, q = map(int, input().split())
# g = [[] for _ in range(n)]
# ans = [0] * n
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     g[a].append(b)
#     g[b].append(a)
# for _ in range(q):
#     p, x = map(int, input().split())
#     p -= 1
#     ans[p] += x
#
#
# def dfs(v, p):
#     for u in g[v]:
#         if u == p:
#             continue
#         ans[u] += ans[v]
#         dfs(u, v)
#
#
# dfs(0, -1)
# print(*ans)

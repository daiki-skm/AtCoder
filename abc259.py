# A
# n, m, x, t, d = map(int, input().split())
# if m >= x:
#     print(t)
# else:
#     print(t + (d * (m - x)))

# B
# from math import cos, sin, radians
#
# a, b, d = map(int, input().split())
# print(a * cos(radians(d)) - b * sin(radians(d)), a * sin(radians(d)) + b * cos(radians(d)))

# C
# s = list(input())
# t = list(input())
# ls = []
# num = 1
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         num += 1
#     else:
#         ls.append([s[i - 1], num])
#         num = 1
# ls.append([s[-1], num])
# lt = []
# num = 1
# for i in range(1, len(t)):
#     if t[i] == t[i - 1]:
#         num += 1
#     else:
#         lt.append([t[i - 1], num])
#         num = 1
# lt.append([t[-1], num])
# if len(ls) != len(lt):
#     print('No')
#     exit()
# for i in range(len(ls)):
#     if ls[i][0] != lt[i][0]:
#         print('No')
#         exit()
#     if ls[i][1] < lt[i][1] and ls[i][1] == 1:
#         print('No')
#         exit()
#     if ls[i][1] > lt[i][1]:
#         print('No')
#         exit()
# print('Yes')

# D
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# n = int(input())
# sx, sy, tx, ty = map(int, input().split())
# x = [0] * n
# y = [0] * n
# r = [0] * n
# for i in range(n):
#     x[i], y[i], r[i] = map(int, input().split())
# d = [[] for _ in range(n)]
# sc = 0
# sflg = True
# tc = 0
# tflg = True
# for i in range(n):
#     if sflg and (sx - x[i]) ** 2 + (sy - y[i]) ** 2 == r[i] ** 2:
#         sc = i
#         sflg = False
#     if tflg and (tx - x[i]) ** 2 + (ty - y[i]) ** 2 == r[i] ** 2:
#         tc = i
#         tflg = False
#     for j in range(i + 1, n):
#         if (r[i] - r[j]) ** 2 <= (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= (r[i] + r[j]) ** 2:
#             d[i].append(j)
#             d[j].append(i)
#             continue
# used = [False for _ in range(n)]
#
#
# def dfs(v):
#     used[v] = True
#     for i in d[v]:
#         if i == tc:
#             return True
#         if not used[i] and dfs(i):
#             return True
#     return False
#
#
# if sc == tc or dfs(sc):
#     print('Yes')
# else:
#     print('No')

# E
# n = int(input())
# ans = set()
# d = []
# for i in range(n):
#     m = int(input())
#     t = 1
#     for j in range(m):
#         pi, ei = map(int, input().split())
#         t *= pi ** ei
#     d.append(t)
#
# print(len(ans))

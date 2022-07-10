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
#
#
# def rle(s):
#     r = []
#     for i in range(len(s)):
#         if len(r) > 0 and r[-1][0] == s[i]:
#             r[-1][1] += 1
#         else:
#             r.append([s[i], 1])
#     return r
#
#
# ls = rle(s)
# lt = rle(t)
# if len(ls) != len(lt):
#     print('No')
#     exit()
# for i in range(len(ls)):
#     if ls[i][0] != lt[i][0]:
#         print('No')
#         exit()
#     if ls[i][1] == 1:
#         if lt[i][1] != 1:
#             print('No')
#             exit()
#     else:
#         if lt[i][1] < ls[i][1]:
#             print('No')
#             exit()
# print('Yes')

# D
# from collections import deque
#
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
#
# seen = set()
# seen.add(sc)
# q = deque()
# q.append(sc)
#
# while q:
#     v = q.popleft()
#     if v == tc:
#         print('Yes')
#         exit()
#     for i in d[v]:
#         if i not in seen:
#             seen.add(i)
#             q.append(i)
# print('No')

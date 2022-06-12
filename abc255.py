# A
# r, c = map(int, input().split())
# a11, a12 = map(int, input().split())
# a21, a22 = map(int, input().split())
# if r == 1 and c == 1:
#     print(a11)
# elif r == 1 and c == 2:
#     print(a12)
# elif r == 2 and c == 1:
#     print(a21)
# elif r == 2 and c == 2:
#     print(a22)

# B
# from math import sqrt
# from collections import defaultdict
#
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a = [i - 1 for i in a]
# x = [0] * n
# y = [0] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
# ans = defaultdict(list)
# for j in range(n):
#     for k_ in range(j + 1, n):
#         if not j in a and k_ in a or not k_ in a and j in a:
#             t = abs(x[j] - x[k_]) ** 2 + abs(y[j] - y[k_]) ** 2
#             ans[j].append(t)
#             ans[k_].append(t)
# t = 0
# for i in ans:
#     if i in a:
#         continue
#     t = max(t, min(ans[i]))
# print(sqrt(t))

# C
x, a, d, n = map(int, input().split())

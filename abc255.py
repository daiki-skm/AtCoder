# A
# r, c = map(int, input().split())
# a11, a12 = map(int, input().split())
# a21, a22 = map(int, input().split())
# ans = 0
# if r == 1 and c == 1:
#     ans = a11
# if r == 1 and c == 2:
#     ans = a12
# if r == 2 and c == 1:
#     ans = a21
# if r == 2 and c == 2:
#     ans = a22
# print(ans)

# B
# from math import sqrt
#
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# a = [i - 1 for i in a]
# x = [0] * n
# y = [0] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
# r = [0] * n
# for i in range(n):
#     r[i] = 10 ** 18
#     for j in range(k):
#         dist = sqrt((x[i] - x[a[j]]) ** 2 + (y[i] - y[a[j]]) ** 2)
#         r[i] = min(r[i], dist)
# ans = 0
# for i in range(n):
#     ans = max(ans, r[i])
# print(ans)

# C
# x, a, d, n = map(int, input().split())
# if d == 0:
#     print(abs(x - a))
#     exit()
# if d < 0:
#     a = a + d * (n - 1)
#     d = -d
# i = (x - a) // d
#
#
# def f(i):
#     if i < 0:
#         i = 0
#     if i >= n:
#         i = n - 1
#     return a + i * d
#
#
# ans = abs(x - f(i))
# ans = min(ans, abs(x - f(i + 1)))
# print(ans)

# D
# from bisect import bisect_left
#
# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# s = [0] * (n + 1)
# for i in range(n):
#     s[i + 1] = s[i] + a[i]
# for i in range(q):
#     x = int(input())
#     k = bisect_left(a, x)
#     ans = k * x - s[k]
#     ans += s[n] - s[k] - (n - k) * x
#     print(ans)

# A
# a = int(input())
# b = int(input())
# t = [-1] * 3
# t[a - 1] = 1
# t[b - 1] = 1
# print(t.index(-1) + 1)

# B
# n = int(input())
# s, t = input().split()
# for i in range(n):
#     print(s[i] + t[i], end="")
# print()

# C
# from math import gcd
#
# a, b = map(int, input().split())
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
#
# print(lcm(a, b))

# D
# n = int(input())
# a = list(map(int, input().split()))
# now = 1
# ans = 0
# for i in range(n):
#     if a[i] == now:
#         now += 1
#     else:
#         ans += 1
# if now > 1:
#     print(ans)
# else:
#     print(-1)

# E
# n = int(input())
#
#
# def g1(n, p):
#     if n == 0:
#         return 0
#     return n // p + g1(n // p, p)
#
#
# def g2(n, p):
#     if n % 2 == 1:
#         return g1(n, p) - g2(n - 1, p)
#     res = g1(n // 2, p)
#     if p == 2:
#         res += n // 2
#     return res
#
#
# ans = min(g2(n, 2), g2(n, 5))
# print(ans)

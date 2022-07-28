# A
# s = input()
# if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
#     print('Bad')
# else:
#     print('Good')

# B
# n, l = map(int, input().split())
# a = [0] * n
# for i in range(n):
#     a[i] = l + i
# s = sum(a)
# ans = 10 ** 18
# for i in range(n):
#     t = s - a[i]
#     if abs(t - s) < abs(ans - s):
#         ans = t
# print(ans)

# C
# from math import gcd
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
#
# def f(x, c, d):
#     res = x
#     res -= x // c
#     res -= x // d
#     res += x // lcm(c, d)
#     return res
#
#
# a, b, c, d = map(int, input().split())
# ans = f(b, c, d) - f(a - 1, c, d)
# print(ans)

# D
# n = int(input())
# ab = [list(map(int, input().split())) for _ in range(n)]
# ab.sort(key=lambda x: x[1])
# now = 0
# for i in range(n):
#     now += ab[i][0]
#     if now > ab[i][1]:
#         print('No')
#         exit()
# print('Yes')

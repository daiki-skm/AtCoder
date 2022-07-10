# A
# r = int(input())
# print(r ** 2)

# B
# n = int(input())
# s = input()
# if s[:n // 2] == s[n // 2:]:
#     print('Yes')
# else:
#     print('No')

# C
# from math import sqrt
#
# n = int(input())
# x = [0] * n
# y = [0] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
#
#
# def dist(i, j):
#     return sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
#
#
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         ans += dist(i, j)
# num = 2
# for i in range(1, n):
#     num *= i
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# ans = (ans * num) / fact
# print(ans)

# D
# x, y = map(int, input().split())
# if (x + y) % 3:
#     print(0)
#     exit()
# n = (x + y) // 3
# x -= n
# y -= n
# if x < 0 or y < 0:
#     print(0)
#     exit()
#
#
# def choose(n, a, mod):
#     x = 1
#     y = 1
#     for i in range(min(n - a, a)):
#         x *= n - i
#         x %= mod
#         y *= i + 1
#         y %= mod
#     # fermat's little theorem
#     return x * pow(y, mod - 2, mod) % mod
#
#
# print(choose(x + y, x, 10 ** 9 + 7))

# A
# from math import pi
#
# r = int(input())
# print(r * 2 * pi)

# B
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# ans = n - sum(a)
# if ans < 0:
#     ans = -1
# print(ans)

# C
# from collections import Counter
#
# n = int(input())
# a = list(map(int, input().split()))
# a = Counter(a)
# for i in range(1, n + 1):
#     print(a[i])

# D
# def sm(l, r):
#     return (l + r) * (r - l + 1) // 2
#
#
# mod = 10 ** 9 + 7
# n, k = map(int, input().split())
# ans = 0
# for i in range(k, n + 2):
#     l = sm(0, i - 1)
#     l %= mod
#     r = sm(n - i + 1, n)
#     r %= mod
#     ans += r - l + 1
#     ans %= mod
# print(ans)

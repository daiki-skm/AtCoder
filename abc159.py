# A
# def comb(n, r):
#     if n // 2 < r:
#         r = n - r
#     numerator = 1
#     denominator = 1
#     for i in range(n, n - r, -1):
#         numerator *= i
#     for i in range(1, r + 1):
#         denominator *= i
#     return numerator // denominator
#
#
# n, m = map(int, input().split())
# ans = 0
# if n >= 2:
#     ans += comb(n, 2)
# if m >= 2:
#     ans += comb(m, 2)
# print(ans)

# B
# s = input()
# flg = True
# t = s[::-1]
# if s != t:
#     flg = False
# s1 = s[:(len(s) // 2)]
# t1 = s1[::-1]
# if s1 != t1:
#     flg = False
# s2 = s[(len(s) // 2) + 1:]
# t2 = s2[::-1]
# if s2 != t2:
#     flg = False
# if flg:
#     print('Yes')
# else:
#     print('No')

# C
# l = int(input())
# print((l / 3) ** 3)

# D
# from collections import Counter
#
#
# def choose(n):
#     return n * (n - 1) // 2
#
#
# n = int(input())
# a = list(map(int, input().split()))
# for i in range(n):
#     a[i] -= 1
# cnt = Counter(a)
# total = 0
# for i in cnt.values():
#     total += choose(i)
# for i in range(n):
#     ans = total
#     ans -= choose(cnt[a[i]])
#     ans += choose(cnt[a[i]] - 1)
#     print(ans)

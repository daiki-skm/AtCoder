# A
# a, b = map(int, input().split())
# if a - b * 2 > 0:
#     print(a - b * 2)
# else:
#     print(0)

# B
# from itertools import combinations
#
# n = int(input())
# d = list(map(int, input().split()))
# ans = 0
# for v in combinations(d, 2):
#     ans += v[0] * v[1]
# print(ans)

# C
# n = int(input())
# s = input()
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
# print(len(ls))

# D
# from bisect import bisect_left
#
# n = int(input())
# l = list(map(int, input().split()))
# l.sort()
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         t = l[i] + l[j]
#         p = bisect_left(l[j + 1:], t)
#         ans += p
# print(ans)

# A
# n = int(input())
# if n % 1000 == 0:
#     print(0)
# else:
#     print(1000 - n % 1000)

# B
# from collections import defaultdict
#
# n = int(input())
# d = defaultdict(int)
# for i in range(n):
#     s = input()
#     d[s] += 1
# print('AC x {}'.format(d['AC']))
# print('WA x {}'.format(d['WA']))
# print('TLE x {}'.format(d['TLE']))
# print('RE x {}'.format(d['RE']))

# C
# h, w, k = map(int, input().split())
# s = [list(input()) for _ in range(h)]
# ans = 0
# for i in range(2 ** h):
#     for j in range(2 ** w):
#         cnt = 0
#         for i_ in range(h):
#             for j_ in range(w):
#                 if i >> i_ & 1:
#                     continue
#                 if j >> j_ & 1:
#                     continue
#                 if s[i_][j_] == '#':
#                     cnt += 1
#         if cnt == k:
#             ans += 1
# print(ans)

# D
# n = int(input())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# ans = 0
# t = n - 1
# for i in range(n):
#     lim = 2
#     if i == 0:
#         lim = 1
#     for j in range(lim):
#         if t > 0:
#             ans += a[i]
#             t -= 1
# print(ans)

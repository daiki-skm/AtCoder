# A
# l1, r1, l2, r2 = map(int, input().split())
# l = max(l1, l2)
# r = min(r1, r2)
# print(max(0, r - l))

# B
# n = int(input())
# a = [list(input()) for _ in range(n)]
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i][j] == 'D' and a[j][i] == 'D':
#             continue
#         if a[i][j] == 'W' and a[j][i] == 'L':
#             continue
#         if a[i][j] == 'L' and a[j][i] == 'W':
#             continue
#         print('incorrect')
#         exit()
# print('correct')

# C
# from collections import defaultdict
#
# n = int(input())
# d = defaultdict(int)
# for _ in range(n):
#     s = input()
#     if s in d:
#         print("{}({})".format(s, d[s]))
#         d[s] += 1
#     else:
#         d[s] = 1
#         print(s)

# D
# n, m = map(int, input().split())
# x = list(map(int, input().split()))
# b = [0] * (n + 1)
# for _ in range(m):
#     c, y = map(int, input().split())
#     b[c] += y
#
# INF = 10 ** 18
# dp = [[-INF] * (n + 1) for _ in range(n + 1)]
# dp[0][0] = 0
# for i in range(1, n + 1):
#     for j in range(n + 1):
#         now = -INF
#         if j == 0:
#             for k in range(n + 1):
#                 now = max(now, dp[i - 1][k])
#         else:
#             now = dp[i - 1][j - 1] + x[i - 1] + b[j]
#         dp[i][j] = now
#
# ans = 0
# for j in range(n + 1):
#     ans = max(ans, dp[-1][j])
# print(ans)

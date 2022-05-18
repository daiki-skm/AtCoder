# A
# s = set(list(input()))
# if len(s) == 1:
#     print('Won')
# else:
#     print('Lost')

# B
# n, x = map(int, input().split())
# alc = 0.0
# for i in range(n):
#     v, p = map(int, input().split())
#     alc += v * p
#     if alc > x * 100:
#         print(i + 1)
#         exit()
# print(-1)

# C
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for l in range(n):
#     x = a[l]
#     for r in range(l, n):
#         x = min(x, a[r])
#         ans = max(ans, x * (r - l + 1))
# print(ans)

# D
# n = int(input())
# dp = [1] * 2
# for i in range(n):
#     s = input()
#     p = [0] * 2
#     t = p
#     p = dp
#     dp = t
#     for j in range(2):
#         for x in range(2):
#             nj = j
#             if s == 'AND':
#                 nj &= x
#             else:
#                 nj |= x
#             dp[nj] += p[j]
#             print(p, dp)
# print(dp[0], dp[1])

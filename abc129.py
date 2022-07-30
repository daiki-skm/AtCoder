# A
# p, q, r = map(int, input().split())
# print(min(p + q, q + r, r + p))

# B
# n = int(input())
# w = list(map(int, input().split()))
# t = [0] * (n + 1)
# for i in range(n):
#     t[i + 1] = t[i] + w[i]
# m = 10 ** 9 + 7
# for i in range(n):
#     m = min(m, abs((t[-1] - t[i]) - t[i]))
# print(m)

# C
# n, m = map(int, input().split())
# mod = 10 ** 9 + 7
# broken = [0] * (n + 1)
# for i in range(m):
#     broken[int(input())] = 1
# dp = [0] * (n + 2)
# dp[n] = 1
# for i in range(n - 1, -1, -1):
#     if broken[i]:
#         dp[i] = 0
#         continue
#     dp[i] = (dp[i + 1] + dp[i + 2]) % mod
# print(dp[0])

# D
# h, w = map(int, input().split())
# s = [list(input()) for _ in range(h)]
# cnt = [[0] * w for _ in range(h)]
# for i in range(h):
#     done = [0] * w
#     for j in range(w):
#         if s[i][j] == '#':
#             continue
#         if done[j]:
#             continue
#         l = 0
#         while j + l < w:
#             if s[i][j + l] == '#':
#                 break
#             l += 1
#         for k in range(l):
#             cnt[i][j + k] += l
#             done[j + k] = 1
# for j in range(w):
#     done = [0] * h
#     for i in range(h):
#         if s[i][j] == '#':
#             continue
#         if done[i]:
#             continue
#         l = 0
#         while i + l < h:
#             if s[i + l][j] == '#':
#                 break
#             l += 1
#         for k in range(l):
#             cnt[i + k][j] += l
#             done[i + k] = 1
# ans = 0
# for i in range(h):
#     for j in range(w):
#         ans = max(ans, cnt[i][j] - 1)
# print(ans)

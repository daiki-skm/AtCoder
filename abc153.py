# A
# h, a = map(int, input().split())
# print((h + a - 1) // a)

# B
# h, n = map(int, input().split())
# a = list(map(int, input().split()))
# if h <= sum(a):
#     print('Yes')
# else:
#     print('No')

# C
# n, k = map(int, input().split())
# h = list(map(int, input().split()))
# if n <= k:
#     print(0)
#     exit()
# h.sort()
# ans = 0
# for i in range(n - k):
#     ans += h[i]
# print(ans)

# D
# h = int(input())
# bin_h = bin(h)[2:]
# print(2 ** len(bin_h) - 1)

# E
# inf = float('inf')
# h, n = map(int, input().split())
# dp = [inf] * (h + 1)
# dp[0] = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(h):
#         nj = min(j + a, h)
#         dp[nj] = min(dp[nj], dp[j] + b)
# print(dp[h])

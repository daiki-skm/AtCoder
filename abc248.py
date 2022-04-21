# A
# S = input()
# for i in range(10):
#     if not str(i) in S:
#         print(i)
#         exit()

# B
# A, B, K = map(int, input().split())
# ans = 0
# while A < B:
#     A *= K
#     ans += 1
# print(ans)

# C
# N, M, K = map(int, input().split())
# mod = 998244353
# dp = [[0]*(K+1) for _ in range(N+1)]
# dp[0][0] = 1
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         now = 0
#         for k in range(1, M+1):
#             if j-k >= 0:
#                 now += dp[i-1][j-k]
#                 now %= mod
#         dp[i][j] = now
# ans = 0
# for i in range(K+1):
#     ans += dp[N][i]
#     ans %= mod
# print(ans)

# D
# from bisect import bisect_left
# N = int(input())
# A = list(map(int, input().split()))
# two_arr = [[] for _ in range(N+1)]
# for i in range(N):
#     two_arr[A[i]].append(i)
# Q = int(input())
# for _ in range(Q):
#     L, R, X = map(int, input().split())
#     ans = bisect_left(two_arr[X], R) - bisect_left(two_arr[X], L-1)
#     print(ans)

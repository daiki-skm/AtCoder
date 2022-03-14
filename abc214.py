# N = int(input())
# if 1 <= N and N <= 125:
#     print(4)
# elif 126 <= N and N <= 211:
#     print(6)
# else:
#     print(8)

# S, T = map(int, input().split())
# ans = 0
# for i in range(S+1):
#     for j in range(S+1):
#         for k in range(S+1):
#             if i + j + k > S or i*j*k > T:
#                 break
#             ans += 1
# print(ans)

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
dp = [-1 for _ in range(N)]
dp[0] = T[0]
for i in range(2*N):
    dp[(i+1)%N] = min(dp[i%N]+S[i%N], T[(i+1)%N])
for i in range(N):
    print(dp[i])
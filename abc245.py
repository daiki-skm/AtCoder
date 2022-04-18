# A
# A, B, C, D = map(int, input().split())
# if A > C:
#     print('Aoki')
# elif A < C:
#     print('Takahashi')
# else:
#     if B > D:
#         print('Aoki')
#     else:
#         print('Takahashi')

# B
# N = int(input())
# A = list(map(int, input().split()))
# for i in range(2001):
#     if i not in A:
#         print(i)
#         exit()

# C
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# dp = [[False]*N for _ in range(2)]
# dp[0][0] = True
# dp[1][0] = True
# for i in range(1, N):
#     if (dp[0][i-1] == True and abs(A[i-1]-A[i]) <= K) or (dp[1][i-1] == True and abs(B[i-1]-A[i]) <= K):
#         dp[0][i] = True
#     if (dp[0][i-1] == True and abs(A[i-1]-B[i]) <= K) or (dp[1][i-1] == True and abs(B[i-1]-B[i]) <= K):
#         dp[1][i] = True
# if dp[0][N-1] == True or dp[1][N-1] == True:
#     print('Yes')
# else:
#     print('No')

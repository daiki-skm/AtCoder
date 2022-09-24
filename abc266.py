# A
# s = input()
# print(s[len(s)//2])

# B
# n = int(input())
# print(n%998244353)

# C
# p = [list(map(int, input().split())) for _ in range(4)]
# for i in range(4):
#   a = p[i]
#   b = p[(i+1)%4]
#   c = p[(i+2)%4]
#   vb = [b[0] - a[0], b[1] - a[1]]
#   vc = [c[0] - a[0], c[1] - a[1]]
#   area = vb[0]*vc[1] - vc[0]*vb[1]
#   if area <= 0:
#     print('No')
#     exit()
# print('Yes')

# D
# n = int(input())
# m = 10**5+5
# x = [0]*m
# a = [0]*m
# for i in range(n):
#   T, X, A = map(int, input().split())
#   x[T] = X
#   a[T] = A
# inf = 10**18
# dp = [[-inf]*5 for _ in range(m)]
# dp[0][0] = 0
# for i in range(m-1):
#   ni = i+1
#   for j in range(5):
#     for nj in range(j-1, j+2):
#       if nj < 0 or nj >= 5:
#         continue
#       dp[ni][nj] = max(dp[ni][nj], dp[i][j])
#   dp[ni][x[ni]] += a[ni]
# ans = -inf
# for j in range(5):
#   ans = max(ans, dp[m-1][j])
# print(ans)
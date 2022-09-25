# A
# s = input()
# if s == 'Monday':
#     print(5)
# if s == 'Tuesday':
#     print(4)
# if s == 'Wednesday':
#     print(3)
# if s == 'Thursday':
#     print(2)
# if s == 'Friday':
#     print(1)

# B
# s = input()
# c = 'x'
# if s[6] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[3] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[1] == '1' or s[7] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[0] == '1' or s[4] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[2] == '1' or s[8] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[5] == '1':
#     c += 'o'
# else:
#     c += 'x'
# if s[9] == '1':
#     c += 'o'
# else:
#     c += 'x'
# xo = 0
# for i in range(len(c)-1):
#     if c[i] == 'x' and c[i+1] == 'o':
#         xo += 1
# if s[0] == '0' and xo > 1:
#     print('Yes')
# else:
#     print('No')

# C
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# s = 0
# t = 0
# for i in range(m):
#     s += a[i]*(i+1)
# for i in range(m):
#     t += a[i]
# ans = s
# for i in range(n-m):
#     ns = s-t+a[i+m]*m
#     nt = t-a[i]+a[i+m]
#     s = ns
#     t = nt
#     ans = max(ans, s)
# print(ans)

# D
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# inf = 10**18
# dp = [[-inf]*(m+1) for _ in range(n+1)]
# dp[0][0] = 0
# for i in range(n):
#     for j in range(m+1):
#         dp[i+1][j] = max(dp[i+1][j], dp[i][j])
#         if j:
#             dp[i+1][j] = max(dp[i+1][j], dp[i][j-1]+a[i]*j)
# print(dp[n][m])

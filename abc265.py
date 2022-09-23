# A
# x, y, n = map(int, input().split())
# y = min(y, 3*x)
# print((n//3)*y + (n%3)*x)

# B
# from collections import defaultdict

# n, m, t = map(int, input().split())
# a = list(map(int, input().split()))
# xy = defaultdict(int)
# for _ in range(m):
#   x, y = map(int, input().split())
#   xy[x] = y
# for i in range(n-1):
#   t -= a[i]
#   t += xy[i+1]
#   if t <= 0:
#     print('No')
#     exit()
# print('Yes')

# C
# h, w = map(int, input().split())
# g = [list(list(input())) for _ in range(h)]
# visited = [[0]*w for _ in range(h)]
# i = 0
# j = 0
# while True:
#   visited[i][j] = 1
#   d = g[i][j]
#   if d == 'U' and i == 0:
#     break
#   if d == 'D' and i == h-1:
#     break
#   if d == 'L' and j == 0:
#     break
#   if d == 'R' and j == w-1:
#     break
#   if d == 'U':
#     i -= 1
#   if d == 'D':
#     i += 1
#   if d == 'L':
#     j -= 1
#   if d == 'R':
#     j += 1
#   if visited[i][j]:
#     print(-1)
#     exit()
# print(i+1, j+1)

# D
# n, p, q, r = list(map(int, input().split()))
# b = [p, q, r]
# a = list(map(int, input().split()))
# s = [0]*(n+1)
# for i in range(n):
#   s[i+1] = s[i]+a[i]
# st = set()
# for i in range(n+1):
#   st.add(s[i])
# for i in range(n+1):
#   ns = s[i]
#   for j in range(3):
#     ns += b[j]
#     if not ns in st:
#       break
#     if j == 2:
#       print('Yes')
#       exit()
# print('No')

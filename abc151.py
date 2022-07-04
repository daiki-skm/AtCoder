# A
# c = input()
# print(chr(ord(c) + 1))

# B
# n, k, m = map(int, input().split())
# a = list(map(int, input().split()))
# t = m * n - sum(a)
# if t < 0:
#     print(0)
# elif 0 <= t <= k:
#     print(t)
# else:
#     print("-1")

# C
# from collections import defaultdict
#
# n, m = map(int, input().split())
# d = defaultdict(int)
# a = 0
# b = 0
# for _ in range(m):
#     p, s = input().split()
#     if s == 'AC' and d[p] >= 0:
#         a += 1
#         b += d[p]
#         d[p] = -1
#         continue
#     if s == 'WA' and d[p] >= 0:
#         d[p] += 1
#         continue
# print(a, b)

# D
# from collections import deque
#
#
# def update(i, j, x):
#     global dist, inf, q
#     if dist[i][j] != inf:
#         return
#     dist[i][j] = x
#     q.append((i, j))
#
#
# h, w = map(int, input().split())
# s = [list(input()) for _ in range(h)]
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# inf = float('inf')
# ans = 0
# # bfs
# for si in range(h):
#     for sj in range(w):
#         if s[si][sj] == '#':
#             continue
#         dist = [[inf] * w for _ in range(h)]
#         q = deque()
#         update(si, sj, 0)
#         while q:
#             i, j = q.popleft()
#             for k in range(4):
#                 ni = i + dx[k]
#                 nj = j + dy[k]
#                 if 0 <= ni < h and 0 <= nj < w:
#                     if s[ni][nj] == '#':
#                         continue
#                     update(ni, nj, dist[i][j] + 1)
#         for i in range(h):
#             for j in range(w):
#                 if s[i][j] == '#':
#                     continue
#                 ans = max(ans, dist[i][j])
# print(ans)

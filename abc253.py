# A
# a, b, c = map(int, input().split())
# num = [a, b, c]
# num.sort()
# if num[1] == b:
#     print('Yes')
# else:
#     print('No')

# B
# import queue
#
# h, w = map(int, input().split())
# o = []
# for i in range(h):
#     s = list(input())
#     if 'o' in s:
#         for j in range(len(s)):
#             if s[j] == 'o':
#                 o.append([i, j])
# sy, sx = o[0][0], o[0][1]
# gy, gx = o[1][0], o[1][1]
# Q = queue.Queue()
# Q.put((sy, sx))
# visited = [[-1] * w for _ in range(h)]
# visited[sy][sx] = 0
# judge_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# while not Q.empty():
#     y, x = Q.get()
#     for i in range(4):
#         ny = y + judge_list[i][0]
#         nx = x + judge_list[i][1]
#         if 0 <= ny < h and 0 <= nx < w:
#             if visited[ny][nx] == -1:
#                 visited[ny][nx] = visited[y][x] + 1
#                 Q.put((ny, nx))
# print(visited[gy][gx])

# h, w = map(int, input().split())
# ip = []
# jp = []
# for i in range(h):
#     s = list(input())
#     for j in range(len(s)):
#         if s[j] == 'o':
#             ip.append(i)
#             jp.append(j)
# ans = 0
# ans += abs(ip[0] - ip[1])
# ans += abs(jp[0] - jp[1])
# print(ans)

# C
# import heapq
# from collections import defaultdict
#
# mx = []
# mn = []
# cnt = defaultdict(int)
#
# q = int(input())
# for i in range(q):
#     qi = list(map(int, input().split()))
#     if qi[0] == 1:
#         x = qi[1]
#         cnt[x] += 1
#         heapq.heappush(mx, -x)
#         heapq.heappush(mn, x)
#
#     if qi[0] == 2:
#         x, c = qi[1:]
#         cnt[x] = max(0, cnt[x] - c)
#
#     if qi[0] == 3:
#         while cnt[-mx[0]] == 0:
#             heapq.heappop(mx)
#         while cnt[mn[0]] == 0:
#             heapq.heappop(mn)
#         print(-mx[0] - mn[0])

# D
# from math import gcd
#
#
# def f(n):
#     return n * (n + 1) // 2
#
#
# def f2(n, a):
#     return f(n // a) * a
#
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
#
# n, a, b = map(int, input().split())
# ans = f(n) - f2(n, a) - f2(n, b) + f2(n, lcm(a, b))
# print(ans)

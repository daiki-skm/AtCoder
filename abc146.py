# A
# s = input()
# l = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
# print(l.index(s) + 1)

# B
# n = int(input())
# s = input()
# l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
#      'X', 'Y', 'Z']
# ans = ''
# for i in range(len(s)):
#     ans += l[(l.index(s[i]) + n) % 26]
# print(ans)

# C
# a, b, x = map(int, input().split())
# l = 0
# r = 10 ** 9 + 1
# while r - l > 1:
#     c = (l + r) // 2
#     if a * c + b * len(str(c)) <= x:
#         l = c
#     else:
#         r = c
# print(l)

# D
# import sys
#
# sys.setrecursionlimit(10 ** 9)
#
# n = int(input())
# to = [[] for _ in range(n)]
# ans = [0] * (n - 1)
#
#
# def dfs(v, c=-1, p=-1):
#     global to, ans
#     k = 1
#     for i in range(len(to[v])):
#         u = to[v][i][0]
#         ei = to[v][i][1]
#         if u == p:
#             continue
#         if k == c:
#             k += 1
#         ans[ei] = k
#         k += 1
#         dfs(u, ans[ei], v)
#
#
# for i in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     to[a].append([b, i])
#     to[b].append([a, i])
# dfs(0)
# mx = 0
# for i in range(n):
#     mx = max(mx, len(to[i]))
# print(mx)
# for i in range(n - 1):
#     print(ans[i])

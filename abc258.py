# A
# k = int(input())
# print("{:02d}:{:02d}".format(21 + k // 60, k % 60))

# B
# n = int(input())
# a = [list(input()) for _ in range(n)]
# ans = 0
# di = [-1, -1, -1, 0, 0, 1, 1, 1]
# dj = [-1, 0, 1, -1, 1, -1, 0, 1]
# for si in range(n):
#     for sj in range(n):
#         for v in range(8):
#             i = si
#             j = sj
#             x = ''
#             for k in range(n):
#                 x += a[i][j]
#                 i += di[v]
#                 j += dj[v]
#                 i %= n
#                 j %= n
#             ans = max(ans, int(x))
# print(ans)

# C
# n, q = map(int, input().split())
# s = input()
# p = 0
# for _ in range(q):
#     t, x = map(int, input().split())
#     if t == 1:
#         p += x
#         p %= n
#     else:
#         print(s[x - p - 1])

# D
# n, x = map(int, input().split())
# a = [0] * n
# b = [0] * n
# for i in range(n):
#     a[i], b[i] = map(int, input().split())
# ans = 10 ** 19
# s = 0
# l = 10 ** 18
# for r in range(n):
#     s += a[r] + b[r]
#     l = min(l, b[r])
#     if x < r + 1:
#         continue
#     now = s + l * (x - r - 1)
#     ans = min(ans, now)
# print(ans)

# A
# n, a, b = map(int, input().split())
# print(min(n * a, b))

# B
# n, d = map(int, input().split())
# x = [list(map(int, input().split())) for _ in range(n)]
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         t = 0
#         for k in range(d):
#             t += (x[i][k] - x[j][k]) ** 2
#         if t ** 0.5 == int(t ** 0.5):
#             ans += 1
# print(ans)

# C
# l, r = map(int, input().split())

# if r - l >= 2019:
#     print(0)
# else:
#     ans = 10 ** 18
#     for i in range(l, r + 1):
#         for j in range(i + 1, r + 1):
#             ans = min(ans, i * j % 2019)
#     print(ans)

# r = min(r, l + 4038)
# ans = 2018
# for i in range(l, r + 1):
#     for j in range(i + 1, r + 1):
#         ans = min(ans, i * j % 2019)
# print(ans)

# D
# n = int(input())
# a = list(map(int, input().split()))
# x2 = 0
# for i in range(n):
#     if i % 2:
#         x2 -= a[i]
#     else:
#         x2 += a[i]
# ans = [0] * n
# ans[0] = x2 // 2
# for i in range(n - 1):
#     ans[i + 1] = a[i] - ans[i]
# for i in range(n):
#     ans[i] *= 2
# print(*ans)

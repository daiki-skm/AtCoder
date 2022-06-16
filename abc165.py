# A
# k = int(input())
# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     if i % k == 0:
#         print('OK')
#         exit()
# print('NG')

# B
# x = int(input())
# now = 100
# ans = 0
# while now < x:
#     now += now // 100
#     ans += 1
# print(ans)

# C
# def dfs(A):
#     global n, m, q, a, b, c, d, ans
#
#     if len(A) == n + 1:
#         # print(A)
#         now = 0
#         for i in range(q):
#             if A[b[i]] - A[a[i]] == c[i]:
#                 now += d[i]
#         ans = max(ans, now)
#         return
#
#     for i in range(A[-1], m + 1):
#         dfs(A + [i])
#
#
# n, m, q = map(int, input().split())
# a = [0] * q
# b = [0] * q
# c = [0] * q
# d = [0] * q
# for i in range(q):
#     a[i], b[i], c[i], d[i] = map(int, input().split())
# ans = 0
# dfs([1])
# print(ans)

# D
# a, b, n = map(int, input().split())
# x = n
# if n >= b - 1:
#     x = b - 1
# ans = a * x // b - a * (x // b)
# print(ans)

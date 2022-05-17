# A
# a, b, c = map(int, input().split())
# if c == 0:
#     if a > b:
#         print('Takahashi')
#     else:
#         print('Aoki')
# else:
#     if a < b:
#         print('Aoki')
#     else:
#         print('Takahashi')

# B
# n, s, d = map(int, input().split())
# for _ in range(n):
#     x, y = map(int, input().split())
#     if x < s and d < y:
#         print('Yes')
#         exit()
# print('No')

# C
# n, m = map(int, input().split())
# a = [0] * m
# b = [0] * m
# for i in range(m):
#     a[i], b[i] = map(int, input().split())
# k = int(input())
# c = [0] * k
# d = [0] * k
# for i in range(k):
#     c[i], d[i] = map(int, input().split())
# ans = 0
# for i in range(2 ** k):
#     ab = [0] * n
#     for j in range(k):
#         if i >> j & 1:
#             ab[d[j]-1] = 1
#         else:
#             ab[c[j]-1] = 1
#     t = 0
#     for j in range(m):
#         if ab[a[j]-1] == 1 and ab[b[j]-1] == 1:
#             t += 1
#     ans = max(ans, t)
# print(ans)

# D
# def check(n, l):
#     t = n / l - l + 1
#     if abs(t) % 2 == 1:
#         return False
#     return True
#
#
# n = int(input())
# n *= 2
# ans = 0
# for x in range(1, int(n ** 0.5) + 1):
#     if n % x != 0:
#         continue
#     y = n // x
#     if check(n, x):
#         ans += 1
#     if check(n, y):
#         ans += 1
# print(ans)

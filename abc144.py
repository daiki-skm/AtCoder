# A
# a, b = map(int, input().split())
# if 1 <= a <= 9 and 1 <= b <= 9:
#     print(a * b)
# else:
#     print(-1)

# B
# n = int(input())
# for i in range(1, 10):
#     for j in range(1, 10):
#         if i * j == n:
#             print('Yes')
#             exit()
# print('No')

# C
# n = int(input())
# ans = 10 ** 18
# for i in range(1, int(n ** 0.5) + 1):
#     if n % i != 0:
#         continue
#     j = n // i
#     ans = min(ans, i + j - 2)
# print(ans)

# D
# from math import atan2, pi
#
# a, b, x = map(int, input().split())
# s = x / a
# rad = 0
# if s >= a * b / 2:
#     h = (a * b - s) * 2 / a
#     rad = atan2(h, a)
# else:
#     w = s * 2 / b
#     rad = atan2(b, w)
# deg = rad * 180 / pi
# print(deg)

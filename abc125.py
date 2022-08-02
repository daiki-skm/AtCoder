# A
# a, b, t = map(int, input().split())
# print(t // a * b)

# B
# n = int(input())
# v = list(map(int, input().split()))
# c = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     ans += max(0, v[i] - c[i])
# print(ans)

# C
# from math import gcd
#
# n = int(input())
# a = list(map(int, input().split()))
# l = [0] * (n + 1)
# r = [0] * (n + 1)
# for i in range(n):
#     l[i + 1] = gcd(l[i], a[i])
# for i in range(n - 1, -1, -1):
#     r[i] = gcd(r[i + 1], a[i])
# ans = 0
# for i in range(n):
#     ans = max(gcd(l[i], r[i + 1]), ans)
# print(ans)

# D
# n = int(input())
# a = list(map(int, input().split()))
# ta = [0] * n
# t = 0
# for i in range(n):
#     if a[i] < 0:
#         t += 1
#         ta[i] = -a[i]
#     else:
#         ta[i] = a[i]
# if t % 2 == 0:
#     print(sum(ta))
# else:
#     ta.sort()
#     print(sum(ta) - 2 * ta[0])

# A
# n = int(input())
# odd = 0
# for i in range(1, n + 1):
#     if i % 2 == 1:
#         odd += 1
# print(odd / n)

# B
# n, k = map(int, input().split())
# h = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     if h[i] >= k:
#         ans += 1
# print(ans)

# C
# n = int(input())
# a = list(map(int, input().split()))
# ans = [0] * n
# for i in range(n):
#     ans[a[i] - 1] = i + 1
# print(*ans)

# D
# from math import gcd
#
#
# def factorize(n):
#     res = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i:
#             continue
#         res.append([i, 0])
#         while n % i == 0:
#             n //= i
#             res[-1][1] += 1
#     if n != 1:
#         res.append([n, 1])
#     return res
#
#
# a, b = map(int, input().split())
# g = gcd(a, b)
# f = factorize(g)
# print(len(f) + 1)

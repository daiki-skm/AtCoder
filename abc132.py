# A
# from collections import Counter
#
# s = input()
# c = Counter(s)
# for k, v in c.items():
#     if v != 2:
#         print('No')
#         exit()
# print('Yes')

# B
# n = int(input())
# p = list(map(int, input().split()))
# ans = 0
# for i in range(n - 2):
#     if p[i] <= p[i + 1] <= p[i + 2] or p[i] >= p[i + 1] >= p[i + 2]:
#         ans += 1
# print(ans)

# C
# n = int(input())
# d = list(map(int, input().split()))
# d.sort()
# t1 = d[n // 2 - 1]
# t2 = d[n // 2]
# print(t2 - t1)

# D
# n, k = map(int, input().split())
# mod = 10 ** 9 + 7
#
#
# def choose(n, a, mod):
#     x = 1
#     y = 1
#     for i in range(a):
#         x *= n - i
#         x %= mod
#         y *= i + 1
#         y %= mod
#     # fermat's little theorem
#     return x * pow(y, -1, mod) % mod
#
#
# for i in range(1, k + 1):
#     t1 = choose(n - k + 1, i, mod)
#     t2 = choose(k - 1, i - 1, mod)
#     print(t1 * t2 % mod)

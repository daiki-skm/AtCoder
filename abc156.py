# A
# n, r = map(int, input().split())
# ans = 0
# if n < 10:
#     ans = r + 100 * (10 - n)
# else:
#     ans = r
# print(ans)

# B
# n, k = map(int, input().split())
# ans = 0
# while n > 0:
#     n //= k
#     ans += 1
# print(ans)

# C
# n = int(input())
# x = list(map(int, input().split()))
# ans = 10 ** 9
# for i in range(1, 101):
#     t = 0
#     for xi in x:
#         t += (xi - i) ** 2
#     ans = min(ans, t)
# print(ans)

# D
# n, a, b = map(int, input().split())
# mod = 10 ** 9 + 7
#
#
# def choose(n, a, mod):
#     x = 1
#     y = 1
#     for i in range(min(n - a, a)):
#         x *= n - i
#         x %= mod
#         y *= i + 1
#         y %= mod
#     # fermat's little theorem
#     return x * pow(y, mod - 2, mod)
#
#
# ans = pow(2, n, mod)
# ans -= 1
# ans -= choose(n, a, mod)
# ans -= choose(n, b, mod)
# print(ans % mod)

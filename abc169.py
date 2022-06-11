# A
# a, b = map(int, input().split())
# print(a * b)

# B
# n = int(input())
# a = list(map(int, input().split()))
# if 0 in a:
#     print('0')
#     exit()
# ans = 1
# for i in range(n):
#     ans *= a[i]
#     if ans > 10 ** 18:
#         ans = -1
#         break
# print(ans)

# C
# a, b = input().split()
# a = int(a)
# b = int(b.replace('.', ''))
# print(a * b // 100)

# D
# from collections import Counter
#
# n = int(input())
# l = []
# for p in range(2, int(n ** 0.5) + 1):
#     while n % p == 0:
#         l.append(p)
#         n //= p
# if n != 1:
#     l.append(n)
# C = Counter(l)
# ans = 0
# for c in C:
#     x = C[c]
#     b = 1
#     while b <= x:
#         x -= b
#         b += 1
#         ans += 1
# print(ans)

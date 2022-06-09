# A
# a = input()
# if 'A' <= a <= 'Z':
#     print('A')
# else:
#     print('a')

# B
# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# p.sort()
# print(sum(p[:k]))

# C
# def f(n):
#     if n == 0:
#         return ''
#     n -= 1
#     return f(n // 26) + chr(n % 26 + ord('a'))
#
#
# n = int(input())
# print(f(n))

# D
# from collections import defaultdict
#
# n = int(input())
# a = list(map(int, input().split()))
# d = defaultdict(int)
# for i in a:
#     d[i] += 1
# ans = 0
# for k, v in d.items():
#     ans += k * v
# q = int(input())
# for _ in range(q):
#     b, c = map(int, input().split())
#     ans -= b * d[b]
#     ans -= c * d[c]
#     d[c] += d[b]
#     d[b] = 0
#     ans += c * d[c]
#     ans += b * d[b]
#     print(ans)

# E
# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     s ^= a[i]
# for i in range(n):
#     a[i] ^= s
# for i in range(n):
#     print(a[i], end=' ')

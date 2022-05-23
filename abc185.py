# A
# a1, a2, a3, a4 = map(int, input().split())
# print(min(a1, a2, a3, a4))

# B
# n, m, t = map(int, input().split())
# bat = n
# now = 0
# for i in range(m):
#     a, b = map(int, input().split())
#     bat -= (a - now)
#     if bat <= 0:
#         print('No')
#         exit()
#     bat = min(n, bat + b - a)
#     now = b
# if t - now < bat:
#     print('Yes')
# else:
#     print('No')

# C
# l = int(input())
# n = l - 1
# r = 11
# if n // 2 < r:
#     r = n - r
# numerator = 1
# denominator = 1
# for i in range(n, n - r, -1):
#     numerator *= i
# for i in range(1, r + 1):
#     denominator *= i
# print(numerator // denominator)

# D
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort()
# a.append(n + 1)
# cur = 1
# s = []
# for i in range(m + 1):
#     w = a[i] - cur
#     if w != 0:
#         s.append(w)
#     cur = a[i] + 1
# k = n
# for w in s:
#     k = min(k, w)
# ans = 0
# for w in s:
#     ans += (w + k - 1) // k
# print(ans)

# A
# s = input()
# ans = ''
# if s[1] == 'B':
#     ans = 'ARC'
# if s[1] == 'R':
#     ans = 'ABC'
# print(ans)

# B
# n, k = map(int, input().split())
# nl = [0] * n
# for i in range(k):
#     d = int(input())
#     a = list(map(int, input().split()))
#     for j in a:
#         nl[j - 1] += 1
# ans = 0
# for i in nl:
#     if i == 0:
#         ans += 1
# print(ans)

# C
# n, m = map(int, input().split())
# h = list(map(int, input().split()))
# dic = [set() for _ in range(n)]
# for i in range(m):
#     a, b = map(int, input().split())
#     dic[a - 1].add(h[b - 1])
#     dic[b - 1].add(h[a - 1])
# ans = 0
# for i in range(n):
#     if len(dic[i]) == 0 or h[i] > max(dic[i]):
#         ans += 1
# print(ans)

# D
# x = int(input())
# for a in range(1, 1000):
#     a5 = 1
#     for _ in range(5):
#         a5 *= a
#     for b in range(-1000, 1000, 1):
#         b5 = 1
#         for _ in range(5):
#             b5 *= b
#         if a5 - b5 == x:
#             print(a, b)
#             exit()

# E
# from collections import defaultdict
#
# n = int(input())
# a = list(map(int, input().split()))
# mp = defaultdict(int)
# ans = 0
# for i in range(n):
#     sa = i - a[i]
#     ans += mp[sa]
#     wa = i + a[i]
#     mp[wa] += 1
#     print(ans, mp)
# print(ans)

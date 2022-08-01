# A
# y = int(input())
# if y % 4 == 0:
#     print(y + 2)
# if y % 4 == 1:
#     print(y + 1)
# if y % 4 == 2:
#     print(y)
# if y % 4 == 3:
#     print(y + 3)

# B
# from collections import defaultdict
#
# n, m = map(int, input().split())
# g = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
# ans = 0
# for i in range(1, n + 1):
#     for j in range(i + 1, n + 1):
#         for k in range(j + 1, n + 1):
#             if i in g[j] and j in g[k] and k in g[i]:
#                 ans += 1
# print(ans)

# C
# from collections import defaultdict
#
# n = int(input())
# a = list(map(int, input().split()))
# d = defaultdict(int)
# ans = 0
# same = 0
# for i in range(n):
#     if a[i] == i + 1:
#         same += 1
#     else:
#         if d[a[i]] == i + 1:
#             ans += 1
#             continue
#         d[i + 1] = a[i]
# print(ans + (same * (same - 1) // 2))

# D
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
mod = 998244353
ans = n
mx = max(a)
isprime = [True] * (int(mx ** 0.5) + 1)
# エラトステネスの篩
for i in range(2, int(mx ** 0.5) + 1):
    if not isprime[i]:
        continue
    for j in range(i * 2, int(mx ** 0.5) + 1, i):
        isprime[j] = False
print(isprime)
isprime[0] = False
isprime[1] = False
prime = []
for i in range(len(isprime)):
    if isprime[i]:
        prime.append(i)
print(prime)

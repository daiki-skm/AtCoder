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
# n = int(input())
# a = list(map(int, input().split()))

# for i in range(n):
#   a[i] -= 1

# same = 0
# for (i, x) in enumerate(a):
#   if i == x:
#     same += 1

# ans = same * (same - 1) // 2
# for (i, j) in enumerate(a):
#   if i < j and a[j] == i:
#     ans += 1

# print(ans)

# A
# n, m = map(int, input().split())
# if n == m:
#     print('Yes')
# else:
#     print('No')

# B
# a, b = map(int, input().split())
# if a <= b:
#     print(''.join([str(a) for i in range(b)]))
# else:
#     print(''.join([str(b) for i in range(a)]))

# C
# n = int(input())
# p = list(map(int, input().split()))
# m = p[0]
# ans = 1
# for i in range(1, n):
#     if m >= p[i]:
#         ans += 1
#     m = min(m, p[i])
# print(ans)

# D
# from collections import defaultdict
#
# n = int(input())
# d = defaultdict(int)
# for x in range(1, n + 1):
#     x = str(x)
#     p = (x[0], x[-1])
#     d[p] += 1
# ans = 0
# for x in range(1, n + 1):
#     x = str(x)
#     p = (x[0], x[-1])
#     q = (x[-1], x[0])
#     ans += d[q]
# print(ans)

# A
# s = input()
# if s == 'Sunny':
#     print('Cloudy')
# if s == 'Cloudy':
#     print('Rainy')
# if s == 'Rainy':
#     print('Sunny')

# B
# s = input()
# for i in range(len(s)):
#     if (i + 1) % 2 == 0 and s[i] == 'R':
#         print('No')
#         exit()
#     if (i + 1) % 2 == 1 and s[i] == 'L':
#         print('No')
#         exit()
# print('Yes')

# C
# from collections import defaultdict
#
# n, k, q = map(int, input().split())
# d = defaultdict(int)
# for i in range(q):
#     ai = int(input())
#     d[ai] += 1
# for i in range(1, n + 1):
#     if (k + d[i]) - q > 0:
#         print('Yes')
#     else:
#         print('No')

# D
# from heapq import heappush, heappop, heapify
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# for i in range(n):
#     a[i] = a[i] * (-1)
# heapify(a)
# for i in range(m):
#     ai = heappop(a) * (-1)
#     ai //= 2
#     heappush(a, ai * (-1))
# print(sum(a) * (-1))

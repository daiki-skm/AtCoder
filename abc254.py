# A
# n = input()
# print(n[-2:])

# B
# n = int(input())
# arr = [[0] * n for _ in range(n)]
# arr[0][0] = 1
# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             arr[i][j] = 1
#         else:
#             arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 0:
#             break
#         print(arr[i][j], end=" ")
#     print()

# C
# from collections import defaultdict
#
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# d = defaultdict(list)
# for i in range(n):
#     d[i % k].append(a[i])
# for i in range(k):
#     d[i].sort()
# mi = n // k
# for i in range(mi):
#     for j in range(1, k):
#         if d[j - 1][i] > d[j][i]:
#             print('No')
#             exit()
# if n % k != 0:
#     for i in range(1, n % k):
#         if d[i - 1][-1] > d[i][-1]:
#             print('No')
#             exit()
# print('Yes')

# D
# from math import sqrt
#
# n = int(input())
# ans = 0
# # for i in range(1, int(sqrt(n)) + 1):
# #     if n % i == 0:
# #         print(i, n // i)
# # print(ans)
#
# for i in range(1, n + 1):
#     for j in range(1, int(sqrt(n)) + 1):
#         if i ** 2 % j == 0:
#             print(i, j)
#             ans += 1
#         # if i % j == 0:
#         #     if i*i//j == i*i:
#         #         print(i, j)
#         #         ans += 1
# print(ans)

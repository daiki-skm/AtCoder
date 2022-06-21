# A
# n = input()
# if '7' in n:
#     print('Yes')
# else:
#     print('No')

# B
# n = int(input())
# ans = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     ans += i
# print(ans)

# C
# from math import gcd
#
# k = int(input())
# ans = 0
# for i in range(1, k + 1):
#     for j in range(1, k + 1):
#         ij = gcd(i, j)
#         for l in range(1, k + 1):
#             ans += gcd(ij, l)
# print(ans)

# D
# n = int(input())
# s = input()
# d = {'R': [], 'G': [], 'B': []}
# for i in range(n):
#     d[s[i]].append(i)
# ans = 1
# for i in d:
#     ans *= len(d[i])
# for j in range(n):
#     for i in range(j):
#         k = j + j - i
#         if k < n:
#             if s[i] == s[k]:
#                 continue
#             if s[i] == s[j]:
#                 continue
#             if s[k] == s[j]:
#                 continue
#             ans -= 1
# print(ans)

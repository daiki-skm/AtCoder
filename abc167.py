# A
# s = input()
# t = input()
# if s == t[:-1]:
#     print('Yes')
# else:
#     print('No')

# B
# a, b, c, k = map(int, input().split())
# xa = min(a, k)
# k -= xa
# xb = min(b, k)
# k -= xb
# xc = k
# ans = xa - xc
# print(ans)

# C
# n, m, x = map(int, input().split())
# dim = [list(map(int, input().split())) for _ in range(n)]
# ans = 10 ** 18
# for i in range(2 ** n):
#     tmp_c = 0
#     tmp = [0] * (m + 1)
#     for j in range(n):
#         if (i >> j) & 1:
#             tmp_c += dim[j][0]
#             for k in range(1, m + 1):
#                 tmp[k] += dim[j][k]
#     flg = True
#     for k in range(1, m + 1):
#         if tmp[k] < x:
#             flg = False
#             break
#     if flg:
#         ans = min(ans, tmp_c)
# if ans == 10 ** 18:
#     print(-1)
# else:
#     print(ans)

# D
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# s = []
# order = [-1] * (n + 1)
# c = 1
# l = 0
# v = 1
# while order[v] == -1:
#     order[v] = len(s)
#     s.append(v)
#     v = a[v - 1]
# c = len(s) - order[v]
# l = order[v]
# if k < l:
#     print(s[k])
# else:
#     k -= l
#     k %= c
#     print(s[l + k])

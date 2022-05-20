# A
# def s(n):
#     n = list(n)
#     return sum(int(i) for i in n)
#
#
# a, b = input().split()
# if s(a) >= s(b):
#     print(s(a))
# else:
#     print(s(b))

# B
# n = int(input())
# x = [None] * n
# y = [None] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         t = (y[i] - y[j]) / (x[i] - x[j])
#         if -1 <= t <= 1:
#             ans += 1
# print(ans)

# C
# n = int(input())
# s = dict()
# for i in range(n):
#     si = input()
#     flag = False
#     if si.count('!') == 1:
#         flag = True
#         si = si.replace('!', '')
#     if si in s:
#         if flag:
#             s[si][1] += 1
#             if s[si][0] > 0:
#                 print(si)
#                 exit()
#         else:
#             s[si][0] += 1
#             if s[si][1] > 0:
#                 print(si)
#                 exit()
#     else:
#         if flag:
#             s[si] = [0, 1]
#         else:
#             s[si] = [1, 0]
# print('satisfiable')

# D
# n = int(input())
# aoki_to_taka = [None] * n
# aoki = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     aoki += a
#     aoki_to_taka[i] = 2 * a + b
# aoki_to_taka.sort(key=lambda x: x, reverse=True)
# ans = 0
# for i in range(n):
#     aoki -= aoki_to_taka[i]
#     ans += 1
#     if aoki < 0:
#         break
# print(ans)

# A
# a = list(map(int, input().split()))
# if sum(a) <= 21:
#     print('win')
# else:
#     print('bust')

# B
# s = input()
# ans = 0
# t1 = s[:len(s) // 2]
# t2 = s[len(s) // 2:]
# if len(s) % 2 == 1:
#     t2 = t2[1:]
# t2 = t2[::-1]
# for i in range(len(t1)):
#     if t1[i] != t2[i]:
#         ans += 1
# print(ans)

# C
# g = [[-1] * 15 for _ in range(15)]
# n = int(input())
# for i in range(n):
#     m = int(input())
#     for j in range(m):
#         a, x = map(int, input().split())
#         a -= 1
#         g[i][a] = x
# ans = 0
# for i in range(1 << n):
#     d = [0] * n
#     for j in range(n):
#         if i >> j & 1:
#             d[j] = 1
#     ok = True
#     for j in range(n):
#         if d[j] == 0:
#             continue
#         for k in range(n):
#             if g[j][k] == -1:
#                 continue
#             if g[j][k] != d[k]:
#                 ok = False
#     if ok:
#         t = str(bin(i)[2:])
#         t = t.count('1')
#         ans = max(ans, t)
# print(ans)

# A
# n = int(input())
# print(2 ** n)

# B
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# mass = [0] * 4
# while a:
#     mass[0] = 1
#     ai = a.pop(0)
#     for i in range(3, -1, -1):
#         if mass[i] == 1:
#             mass[i] = 0
#             if ai + i > 3:
#                 ans += 1
#             else:
#                 mass[ai + i] = 1
# print(ans)

# C
# h1, h2, h3, w1, w2, w3 = map(int, input().split())
# h = [h1, h2, h3]
# w = [w1, w2, w3]
# n = 3
# a = [[n] * 3 for _ in range(n)]
# m = 30
# m4 = m ** 4
# ans = 0
# for i in range(m4):
#     tmp = i
#     a[0][0] = (tmp % m) + 1
#     tmp //= m
#     a[0][1] = (tmp % m) + 1
#     tmp //= m
#     a[1][0] = (tmp % m) + 1
#     tmp //= m
#     a[1][1] = (tmp % m) + 1
#     tmp //= m
#     ok = True
#     for j in range(2):
#         a[j][2] = h[j] - a[j][0] - a[j][1]
#         if a[j][2] < 1:
#             ok = False
#     for j in range(3):
#         a[2][j] = w[j] - a[0][j] - a[1][j]
#         if a[2][j] < 1:
#             ok = False
#     if a[2][0] + a[2][1] + a[2][2] != h[2]:
#         ok = False
#     if ok:
#         ans += 1
# print(ans)

# D
# n = int(input())
# a = [[0, 0] for _ in range(n)]
# for i in range(n):
#     a[i][0], a[i][1] = map(int, input().split())
# a.sort(key=lambda x: x[0])
# ans = []
# for i in range(n):
#     if len(ans) == 0 or ans[-1][1] < a[i][0]:
#         ans.append(a[i])
#     else:
#         ans[-1][1] = max(ans[-1][1], a[i][1])
# for i in range(len(ans)):
#     print(ans[i][0], ans[i][1])

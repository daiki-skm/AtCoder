# A
# n = int(input())
# print((n + 2 - 1) // 2)

# B
# a = []
# for i in range(3):
#     a.append(list(map(int, input().split())))
# n = int(input())
# for i in range(n):
#     b = int(input())
#     for j in range(3):
#         for k in range(3):
#             if a[j][k] == b:
#                 a[j][k] = 0
# if a[0][0] == 0 and a[0][1] == 0 and a[0][2] == 0:
#     print('Yes')
#     exit()
# if a[1][0] == 0 and a[1][1] == 0 and a[1][2] == 0:
#     print('Yes')
#     exit()
# if a[2][0] == 0 and a[2][1] == 0 and a[2][2] == 0:
#     print('Yes')
#     exit()
# if a[0][0] == 0 and a[1][0] == 0 and a[2][0] == 0:
#     print('Yes')
#     exit()
# if a[0][1] == 0 and a[1][1] == 0 and a[2][1] == 0:
#     print('Yes')
#     exit()
# if a[0][2] == 0 and a[1][2] == 0 and a[2][2] == 0:
#     print('Yes')
#     exit()
# if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
#     print('Yes')
#     exit()
# if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
#     print('Yes')
#     exit()
# print('No')

# C
# n, m = map(int, input().split())
# p = []
# for i in range(m):
#     p.append(list(map(int, input().split())))
# for x in range(1000):
#     keta = 1
#     nx = x // 10
#     d = [x % 10]
#     while nx > 0:
#         keta += 1
#         d.append(nx % 10)
#         nx = nx // 10
#     if keta != n:
#         continue
#     ok = True
#     d = d[::-1]
#     for i in range(m):
#         if d[p[i][0] - 1] != p[i][1]:
#             ok = False
#             break
#     if ok:
#         print(x)
#         exit()
# print('-1')

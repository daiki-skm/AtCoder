# A
# x, y = map(int, input().split())
# if max(x, y) - min(x, y) >= 3:
#     print('No')
# else:
#     print('Yes')

# B
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     ans += a[i] * b[i]
# if ans == 0:
#     print('Yes')
# else:
#     print('No')

# C
# n = int(input())
# a = list(map(int, input().split()))
# border = int(2 ** n / 2)
# m1 = max(a[:border])
# m2 = max(a[border:])
# t = min(m1, m2)
# print(a.index(t) + 1)

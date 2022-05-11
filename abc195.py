# A
# m, h = map(int, input().split())
# if h%m == 0:
#     print('Yes')
# else:
#     print('No')

# B
# a, b, w = map(int, input().split())
# w *= 1000
# l = 10**9+7
# r = -10**9-7
# for n in range(1, w+1):
#     if a*n <= w and w <= b*n:
#         l = min(l, n)
#         r = max(r, n)
# if l == 10**9+7:
#     print('UNSATISFIABLE')
# else:
#     print(l, r)

# C
# n = int(input())
# x = 1000
# ans = 0
# while n >= x:
#     ans += n-x+1
#     x *= 1000
# print(ans)

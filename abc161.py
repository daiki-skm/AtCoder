# A
# x, y, z = map(int, input().split())
# print("{} {} {}".format(z, x, y))

# B
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# border = sum(a) / (4 * m)
# for i in range(m):
#     if a[i] < border:
#         print('No')
#         exit()
# print('Yes')

# C
# n, k = map(int, input().split())
# t = n % k
# print(min(t, abs(t - k)))

# D
# k = int(input())
# a = [i for i in range(1, 10)]
# while True:
#     if k <= len(a):
#         print(a[k - 1])
#         break
#     k -= len(a)
#     na = []
#     for x in a:
#         for i in range(-1, 2, 1):
#             d = x % 10 + i
#             if d < 0 or d > 9:
#                 continue
#             nx = x * 10 + d
#             na.append(nx)
#     a = na

# A
# a, b = map(int, input().split())
# print(2 * a + 100 - b)

# B
# n = int(input())
# a = list(map(int, input().split()))
# mx = max(a)
# ans = 0
# num = 0
# for i in range(2, mx + 1):
#     t = 0
#     for j in a:
#         if j % i == 0:
#             t += 1
#     if t > num:
#         num = t
#         ans = i
# print(ans)

# C
# n = list(input())
# ans = 0
# for i in range(2 ** len(n)):
#     b = bin(i)[2:]
#     if b == '0':
#         continue
#     t = ''
#     for j in range(len(n)):
#         if (i >> j) & 1:
#             t += n[j]
#     x = int(t)
#     if x % 3 == 0:
#         ans = max(ans, x)
# if ans == 0:
#     print(-1)
# else:
#     print(len(n) - len(str(ans)))

# D
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# s = 0
# b = 0
# max_b = 0
# for i in range(n):
#     b += a[i]
#     max_b = max(max_b, b)
#     ans = max(ans, max_b + s)
#     s += b
# print(ans)

# A
# s = input()
# ans = 0
# t = 0
# for c in s:
#     if c == 'R':
#         t += 1
#     else:
#         ans = max(ans, t)
#         t = 0
# print(max(ans, t))

# B
# n = int(input())
# l = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
#                 if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
#                     ans += 1
# print(ans)

# C
# x, k, d = map(int, input().split())
# x = abs(x)
# ans = 0
# if x // d >= k:
#     ans = x - d * k
# else:
#     e = x // d
#     k -= e
#     x -= e * d
#     if k % 2 == 1:
#         x = abs(x - d)
#     ans = x
# print(ans)

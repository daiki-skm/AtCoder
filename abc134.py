# A
# r = int(input())
# print(3 * r ** 2)

# B
# n, d = map(int, input().split())
# t = d * 2 + 1
# print((n + t - 1) // t)

# C
# n = int(input())
# a = [int(input()) for _ in range(n)]
# s = sorted(a, reverse=True)
# for i in range(n):
#     ans = s[0]
#     if s[0] == a[i]:
#         ans = s[1]
#     print(ans)

# D
# n = int(input())
# t = list(map(int, input().split()))
# a = [0] * (n + 1)
# for i in range(n):
#     a[i + 1] = t[i]
# b = [0] * (n + 1)
# for i in range(n, 0, -1):
#     sum = 0
#     for j in range(i + i, n + 1, i):
#         sum ^= b[j]
#     b[i] = sum ^ a[i]
# ans = []
# for i in range(1, n + 1):
#     if b[i]:
#         ans.append(i)
# print(len(ans))
# print(*ans)

# A
# n = int(input())
# print(n ** 3)

# B
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     ans += b[a[i] - 1]
#     if i != 0 and a[i] == a[i - 1] + 1:
#         ans += c[a[i - 1] - 1]
# print(ans)

# C
# n = int(input())
# b = list(map(int, input().split()))
# ans = b[0]
# for i in range(n - 2):
#     ans += min(b[i], b[i + 1])
# ans += b[-1]
# print(ans)

# D
# n, k = map(int, input().split())
# s = input()
# score = 0
# for i in range(n - 1):
#     if s[i] == s[i + 1]:
#         score += 1
# print(min(score + 2 * k, n - 1))

# A
# x = int(input())
# if x >= 30:
#     print('Yes')
# else:
#     print('No')

# B
# n, d = map(int, input().split())
# ans = 0
# for _ in range(n):
#     x, y = map(int, input().split())
#     if x * x + y * y <= d * d:
#         ans += 1
# print(ans)

# C
# k = int(input())
# x = 7 % k
# s = set()
# ans = 1
# while not x in s:
#     if x == 0:
#         print(ans)
#         exit()
#     s.add(x)
#     x = (x * 10 + 7) % k
#     ans += 1
# print(-1)

# D
# n = int(input())
# s = input()
# a = 0
# b = 0
# for i in range(n):
#     if s[i] == 'R':
#         a += 1
# ans = max(a, b)
# for i in range(n):
#     if s[i] == 'R':
#         a -= 1
#     else:
#         b += 1
#     now = max(a, b)
#     ans = min(ans, now)
# print(ans)

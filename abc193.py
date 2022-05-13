# A
# a, b = map(int, input().split())
# print(100-100*(b/a))

# B
# n = int(input())
# ans = 10**9+7
# for i in range(n):
#     a, p, x = map(int, input().split())
#     if x-a > 0:
#         ans = min(ans, p)
# if ans == 10**9+7:
#     print(-1)
# else:
#     print(ans)

# C
# from math import sqrt
# n = int(input())
# ans = set()
# for a in range(2, int(sqrt(n))+1):
#     x = a*a
#     while x <= n:
#         ans.add(x)
#         x *= a
# print(n-len(ans))

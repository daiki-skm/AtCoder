# A
# n, a, x, y = map(int, input().split())
# if n <= a:
#     print(n * x)
# else:
#     print(a * x + (n - a) * y)

# B
# N = int(input())
# S = input()
# t = S.index('1')
# if t%2 == 0:
#     print('Takahashi')
# else:
#     print('Aoki')

# C
# from collections import defaultdict
# n, k = map(int, input().split())
# c = list(map(int, input().split()))
# ans = 0
# dict = defaultdict(int)
# now = 0
# for i in range(n):
#     if dict[c[i]] == 0:
#         now += 1
#     dict[c[i]] += 1
#     if i >= k:
#         dict[c[i-k]] -= 1
#         if dict[c[i-k]] == 0:
#             now -= 1
#     ans = max(ans, now)
# print(ans)

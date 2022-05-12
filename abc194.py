# A
# a, b = map(int, input().split())
# if a+b >= 15 and b >= 8:
#     print(1)
# elif a+b >= 10 and b >= 3:
#     print(2)
# elif a+b >= 3:
#     print(3)
# else:
#     print(4)

# B
# n = int(input())
# a = [0]*n
# b = [0]*n
# ans = 10**9
# for i in range(n):
#     a[i], b[i] = map(int, input().split())
# for i in range(n):
#     for j in range(n):
#         now = 0
#         if i == j:
#             now = a[i]+b[j]
#         else:
#             now = max(a[i], b[j])
#         ans = min(now, ans)
# print(ans)

# C
# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))
# max_a = 200
# ans = 0
# d = defaultdict(int)
# for i in range(n):
#     for j in range(-1*max_a, max_a+1, 1):
#         c = d[max_a+j]
#         x = a[i]-j
#         ans += x*x*c
#     d[max_a+a[i]] += 1
# print(ans)

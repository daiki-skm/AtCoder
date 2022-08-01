# A
# a, b = map(int, input().split())
# if a >= 13:
#     print(b)
# elif a >= 6:
#     print(b // 2)
# else:
#     print(0)

# B
# r, d, x = map(int, input().split())
# for _ in range(10):
#     x = r * x - d
#     print(x)

# C
# n, m = map(int, input().split())
# l = 0
# r = 10 ** 9
# for _ in range(m):
#     li, ri = map(int, input().split())
#     l = max(l, li)
#     r = min(r, ri)
# if l <= r:
#     print(r - l + 1)
# else:
#     print(0)

# D
# from heapq import heappush, heappop, heapify  # priority queue (ascending order)
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# q = []
# for i in range(n):
#     heappush(q, (-a[i], 1))
# for _ in range(m):
#     b, c = map(int, input().split())
#     heappush(q, (-c, b))
# ans = 0
# for _ in range(n):
#     c, b = heappop(q)
#     ans += -c
#     if b > 1:
#         heappush(q, (c, b - 1))
# print(ans)

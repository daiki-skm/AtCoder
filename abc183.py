# A
# x = int(input())
# if x < 0:
#     print(0)
# else:
#     print(x)

# B
# sx, sy, gx, gy = map(int, input().split())
# print((gx - sx) * (sy / (sy + gy)) + sx)

# C
# from itertools import permutations
#
# n, k = map(int, input().split())
# a = []
# for i in range(n):
#     t = list(map(int, input().split()))
#     a.append(t)
# order = [i for i in range(1, n)]
# ans = 0
# for t in permutations(order, len(order)):
#     val = 0
#     t = list(t)
#     t.append(0)
#     t.insert(0, 0)
#     for j in range(1, n + 1):
#         val += a[t[j - 1]][t[j]]
#     if val == k:
#         ans += 1
# print(ans)

# D
# n, w = map(int, input().split())
# max_t = 200005
# d = [0] * max_t
# for i in range(n):
#     s, t, p = map(int, input().split())
#     d[s] += p
#     d[t] -= p
# for i in range(1, max_t):
#     d[i] += d[i - 1]
# for i in range(max_t):
#     if d[i] > w:
#         print('No')
#         exit()
# print('Yes')

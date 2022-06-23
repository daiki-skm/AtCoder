# A
# s = input()
# if s[2] == s[3] and s[4] == s[5]:
#     print('Yes')
# else:
#     print('No')

# B
# x = int(input())
# ans = 0
# ans += x // 500 * 1000
# x %= 500
# ans += x // 5 * 5
# print(ans)

# C
# k, n = map(int, input().split())
# a = list(map(int, input().split()))
# ans = a[-1] - a[0]
# for i in range(n - 1):
#     ans = min(ans, k - (a[i + 1] - a[i]))
# print(ans)

# D
# N, X, Y = map(int, input().split())
#
#
# def get_dist(a, b):
#     d1 = abs(a - b)
#     d2 = abs(a - X) + 1 + abs(b - Y)
#     d3 = abs(a - Y) + 1 + abs(b - X)
#     return min(d1, d2, d3)
#
#
# result = [0] * N
# for start in range(1, N):
#     for goal in range(start + 1, N + 1):
#         result[get_dist(start, goal)] += 1
# for r in result[1:]:
#     print(r)

# E
# x, y, a, b, c = map(int, input().split())
# p = list(map(int, input().split()))
# q = list(map(int, input().split()))
# r = list(map(int, input().split()))
# p.sort(reverse=True)
# q.sort(reverse=True)
# d = []
# for i in range(x):
#     d.append(p[i])
# for i in range(y):
#     d.append(q[i])
# for i in range(c):
#     d.append(r[i])
# d.sort(reverse=True)
# ans = 0
# for i in range(x + y):
#     ans += d[i]
# print(ans)

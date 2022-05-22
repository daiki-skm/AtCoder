# A
# n, w = map(int, input().split())
# print(n // w)

# B
# h, w = map(int, input().split())
# a = [None for _ in range(h)]
# m = 10 ** 9 + 7
# for i in range(h):
#     t = list(map(int, input().split()))
#     a[i] = t
#     m = min(m, min(t))
# ans = 0
# for i in range(h):
#     for j in range(w):
#         if a[i][j] == m:
#             continue
#         ans += a[i][j] - m
# print(ans)

# C
# n = int(input())
# s = set()
# for i in range(1, n + 1):
#     if '7' in str(i) or '7' in str(oct(i)[2:]):
#         s.add(i)
# print(n - len(s))

# D
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# ans = 0
# s = a[0]
# for i in range(1, n):
#     ans += a[i] * i - s
#     s += a[i]
# print(ans)

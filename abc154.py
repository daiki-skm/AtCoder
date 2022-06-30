# A
# s, t = input().split()
# a, b = map(int, input().split())
# u = input()
# if s == u:
#     a -= 1
# if t == u:
#     b -= 1
# print(a, b)

# B
# s = input()
# l = len(s)
# print("".join(['x'] * l))

# C
# from collections import Counter
#
# n = int(input())
# a = list(map(int, input().split()))
# l = len(a)
# c = Counter(a)
# if l != len(c):
#     print("NO")
# else:
#     print("YES")

# D
# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# t = [0] * (1000 + 1)
# for i in range(1, 1001):
#     t[i] = t[i - 1] + i
# x = [0] * n
# for i in range(n):
#     x[i] = t[p[i]] / p[i]
# ans = sum(x[:k])
# before = ans
# for i in range(k, n):
#     ans = max(ans, before - x[i - k] + x[i])
#     before = before - x[i - k] + x[i]
# print(ans)

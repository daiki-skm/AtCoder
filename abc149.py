# A
# s, t = input().split()
# print(t + s)

# B
# a, b, k = map(int, input().split())
# if a <= k:
#     k -= a
#     a = 0
# else:
#     a -= k
#     k = 0
# if b <= k:
#     k -= b
#     b = 0
# else:
#     b -= k
#     k = 0
# print(a, b)

# C
# x = int(input())
# while True:
#     ok = True
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             ok = False
#             break
#     if ok:
#         break
#     x += 1
# print(x)

# D
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# s = input()
# ctoi = [0] * 256
# ctoi[ord('r')] = 2
# ctoi[ord('s')] = 0
# ctoi[ord('p')] = 1
# ans = 0
# for i in range(k):
#     x = []
#     for j in range(i, n, k):
#         x.append(ctoi[ord(s[j])])
#     dp = [0] * 2
#     pre = -1
#     for nx in x:
#         p = [0] * 2
#         t = dp[:]
#         dp = p[:]
#         p = t[:]
#         dp[0] = max(p[0], p[1])
#         if pre == nx:
#             dp[1] = p[0] + a[nx]
#         else:
#             dp[1] = max(p[0], p[1]) + a[nx]
#         pre = nx
#     ans += max(dp[0], dp[1])
# print(ans)

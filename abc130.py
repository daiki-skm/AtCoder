# A
# x, a = map(int, input().split())
# print(0 if x < a else 10)

# B
# n, x = map(int, input().split())
# l = list(map(int, input().split()))
# ans = 1
# now = 0
# for i in range(n):
#     now += l[i]
#     if now > x:
#         break
#     ans += 1
# print(ans)

# C
# w, h, x, y = map(int, input().split())
# ans = w * h / 2
# num = 0
# if w == x * 2 and h == y * 2:
#     num = 1
# print(ans, num)

# D
# 尺取法
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# s = 0
# j = 0
# ans = 0
# for i in range(n):
#     while j < n and s + a[j] < k:
#         s += a[j]
#         j += 1
#     ans += j - i
#     s -= a[i]
#     print(ans, s)
# ans = n * (n + 1) // 2 - ans
# print(ans)

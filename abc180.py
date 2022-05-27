# A
# n, a, b = map(int, input().split())
# print(n - a + b)

# B
# n = int(input())
# x = list(map(int, input().split()))
# m = 0
# y = 0
# t = 0
# for i in range(n):
#     m += abs(x[i])
#     y += abs(x[i]) ** 2
#     t = max(t, abs(x[i]))
# print(m)
# print(y ** 0.5)
# print(t)

# C
# n = int(input())
# ans = set()
# for i in range(int(n ** 0.5)):
#     if n % (i + 1) == 0:
#         ans.add(i + 1)
#         ans.add(n // (i + 1))
# ans = sorted(ans)
# for i in ans:
#     print(i)

# D
# x, y, a, b = map(int, input().split())
# ans = 0
# while True:
#     if y // a < x:
#         break
#     if a * x >= y:
#         break
#     if a * x >= x + b:
#         break
#     x *= a
#     ans += 1
# ans += (y - 1 - x) // b
# print(ans)

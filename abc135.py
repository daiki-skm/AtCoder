# A
# a, b = map(int, input().split())
# t = a + b
# if t % 2 == 1:
#     print("IMPOSSIBLE")
# else:
#     print(t // 2)

# B
# n = int(input())
# p = list(map(int, input().split()))
# c = sorted(p)
# if p == c:
#     print("YES")
#     exit()
# for i in range(n):
#     for j in range(i + 1, n):
#         t = p[i]
#         p[i] = p[j]
#         p[j] = t
#         if p == c:
#             print("YES")
#             exit()
#         t = p[i]
#         p[i] = p[j]
#         p[j] = t
# print("NO")

# C
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     if a[i] > b[i]:
#         ans += b[i]
#         a[i] -= b[i]
#     else:
#         ans += a[i]
#         b[i] -= a[i]
#         a[i] = 0
#         if a[i + 1] > b[i]:
#             ans += b[i]
#             a[i + 1] -= b[i]
#         else:
#             ans += a[i + 1]
#             b[i] -= a[i + 1]
#             a[i + 1] = 0
# print(ans)

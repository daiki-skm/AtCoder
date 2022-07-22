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
# cnt = 0
# for i in range(n):
#     if p[i] != i + 1:
#         cnt += 1
# if cnt == 0 or cnt == 2:
#     print("YES")
# else:
#     print("NO")

# C
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     l = min(a[i], b[i])
#     a[i] -= l
#     b[i] -= l
#     ans += l
#
#     r = min(a[i + 1], b[i])
#     a[i + 1] -= r
#     b[i] -= r
#     ans += r
# print(ans)

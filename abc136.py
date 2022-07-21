# A
# a, b, c = map(int, input().split())
# ans = c - (a - b)
# if ans < 0:
#     print(0)
# else:
#     print(ans)

# B
# n = int(input())
# ans = 0
# for i in range(1, n + 1):
#     t = str(i)
#     if len(t) % 2 == 1:
#         ans += 1
# print(ans)

# C
# n = int(input())
# h = list(map(int, input().split()))
# t = h[0]
# for i in range(1, n):
#     if t - h[i] > 1:
#         print("No")
#         exit()
#     t = max(t, h[i])
# print("Yes")

# D
# s = list(input())
# n = len(s)
# ans = [0] * n
# for ri in range(2):
#     cnt = 0
#     for i in range(n):
#         if s[i] == 'R':
#             cnt += 1
#         else:
#             ans[i] += cnt // 2
#             ans[i - 1] += (cnt + 1) // 2
#             cnt = 0
#
#     ans.reverse()
#     s.reverse()
#     for i in range(n):
#         if s[i] == 'L':
#             s[i] = 'R'
#         else:
#             s[i] = 'L'
# print(*ans)

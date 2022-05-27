# A
# n = int(input())
# if n % 2 == 1:
#     print('Black')
# else:
#     print('White')

# B
# n = int(input())
# ans = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     ans += (a + b) * (b - a + 1) // 2
# print(ans)

# C
# n = int(input())
# x = [0] * n
# y = [0] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             a = x[j] - x[i]
#             b = y[j] - y[i]
#             c = x[k] - x[i]
#             d = y[k] - y[i]
#             if a * d - b * c == 0:
#                 print('Yes')
#                 exit()
# print('No')

# D
# s = list(input())
# if len(s) == 1 and s[0] == '8':
#     print('Yes')
#     exit()
# if len(s) == 2:
#     if int(''.join(s)) % 8 == 0:
#         print('Yes')
#         exit()
#     s[0], s[1] = s[1], s[0]
#     if int(''.join(s)) % 8 == 0:
#         print('Yes')
#         exit()
# cnt = [0] * 10
# for i in range(len(s)):
#     cnt[int(s[i])] += 1
# for i in range(0, 1000, 8):
#     x = i
#     nc = [0] * 10
#     for j in range(3):
#         nc[x % 10] += 1
#         x //= 10
#     ok = True
#     for j in range(10):
#         if nc[j] > cnt[j]:
#             ok = False
#             break
#     if ok:
#         print('Yes')
#         exit()
# print('No')

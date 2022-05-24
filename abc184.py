# A
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# print(a * d - b * c)

# B
# n, x = map(int, input().split())
# s = input()
# for i in range(n):
#     if s[i] == 'o':
#         x += 1
#     else:
#         if x > 0:
#             x -= 1
# print(x)

# C
# r1, c1 = map(int, input().split())
# r2, c2 = map(int, input().split())
# if r1 == r2 and c1 == c2:
#     print(0)
#     exit()
# if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
#     print(1)
#     exit()
# if (r1 + c1) % 2 == (r2 + c2) % 2:
#     print(2)
#     exit()
# if abs(r1 - r2) + abs(c1 - c2) <= 6:
#     print(2)
#     exit()
# if abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
#     print(2)
#     exit()
# print(3)

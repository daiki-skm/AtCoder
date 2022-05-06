# A
# a, b, c = map(int, input().split())
# if a**2 + b**2 < c**2:
#     print("Yes")
# else:
#     print("No")

# B
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(max(min(b)-max(a)+1, 0))

# C
# n = int(input())
# s = list(input())
# q = int(input())
# fl = 0
# n2 = n*2
# for i in range(q):
#     t, a, b = map(int, input().split())
#     if t == 1:
#         a -= 1
#         b -= 1
#         if fl:
#             a = (a+n)%n2
#             b = (b+n)%n2
#         c = s[a]
#         s[a] = s[b]
#         s[b] = c
#     else:
#         fl ^= 1
# if fl:
#     s = s[n:] + s[:n]
# print(''.join(s))

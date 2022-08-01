# A
# n, k = map(int, input().split())
# s = list(input())
# # s = s[:k - 1] + s[k - 1].lower() + s[k:]
# if s[k - 1] == 'A':
#     s[k - 1] = 'a'
# elif s[k - 1] == 'B':
#     s[k - 1] = 'b'
# else:
#     s[k - 1] = 'c'
# print(''.join(s))

# B
# s = input()
# if int(s) == 0:
#     print("NA")
#     exit()
# if int(s[:2]) == 0 and int(s[2:]) >= 13:
#     print("NA")
#     exit()
# if int(s[2:]) == 0 and int(s[:2]) >= 13:
#     print("NA")
#     exit()
# if int(s[:2]) >= 13 and int(s[2:]) >= 13:
#     print("NA")
#     exit()
# if 1 <= int(s[:2]) <= 12:
#     if 1 <= int(s[2:]) <= 12:
#         print("AMBIGUOUS")
#         exit()
#     else:
#         print("MMYY")
#         exit()
# if 1 <= int(s[2:]) <= 12:
#     if 1 <= int(s[:2]) <= 12:
#         print("AMBIGUOUS")
#         exit()
#     else:
#         print("YYMM")
#         exit()

# C
# from math import log2, ceil
#
# n, k = map(int, input().split())
# ans = 0
# for i in range(1, n + 1):
#     if i >= k:
#         ans += 1
#         continue
#     ans += 0.5 ** ceil(log2(k / i))
# print(ans / n)

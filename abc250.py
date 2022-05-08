# TODO
# A
# h, w = map(int, input().split())
# r, c = map(int, input().split())
# if h == 1 and w == 1:
#     print(0)
#     exit()
# if h == 1:
#     if c == 1 or c == w:
#         print(1)
#         exit()
#     else:
#         print(2)
#         exit()
# if w == 1:
#     if r == 1 or r == h:
#         print(1)
#         exit()
#     else:
#         print(2)
#         exit()
# if 1 < r < h and 1 < c < w:
#     print(4)
#     exit()
# if 1 < r < h:
#     if c == 1 or c == w:
#         print(3)
#         exit()
# if 1 < c < w:
#     if r == 1 or r == h:
#         print(3)
#         exit()
# if (r == 1 and c == 1) or (r == h and c == 1) or (r == 1 and c == w) or (r == h and c == w):
#     print(2)
#     exit()

# B
# n, a, b = map(int, input().split())
# ans = []
# fl = 0
# for i in range(n):
#     t = []
#     for j in range(n):
#         if (i+j)%2 == 0:
#             t.append([['.']*b for _ in range(a)])
#         else:
#             t.append([['#']*b for _ in range(a)])
#     ans.append(t)
# # print(ans)
# for three in ans:
#     for i in range(a):
#         for j in range(n):
#             print(''.join(three[j][i]), end='')
#         print()

# C
# n, q = map(int, input().split())
# dict = {i: i for i in range(1, n+1)}
# for i in range(q):
#     x = int(input())
#     if x == n:
#         last_key = max(dict)
#         dict[last_key] -= 1
#         t = sorted(dict.values())[-2]
#         res = [a for a, sub in dict.items() if sub == t]
#         dict[res[-1]] += 1
#     else:
#         dict[x] += 1
#         dict[x+1] -= 1
#     print(dict)
# sorted_dict = sorted(dict.items(), key=lambda x: x[1])
# print(*[i[0] for i in sorted_dict])

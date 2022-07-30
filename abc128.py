# A
# a, p = map(int, input().split())
# print((a * 3 + p) // 2)

# B
# n = int(input())
# sp = []
# for i in range(n):
#     s, p = map(str, input().split())
#     p = -int(p)
#     sp.append((s, p, i + 1))
# sp.sort()
# for i in range(n):
#     print(sp[i][2])

# C
# n, m = map(int, input().split())
# vec = [[] for _ in range(m)]
# for i in range(m):
#     t = list(map(int, input().split()))
#     for j in range(t[0]):
#         vec[i].append(t[j + 1] - 1)
# p = list(map(int, input().split()))
# ans = 0
# for i in range(1 << n):
#     ok = True
#     for j in range(m):
#         c = 0
#         for id in vec[j]:
#             if (i >> id) & 1:
#                 c += 1
#         if c % 2 != p[j]:
#             ok = False
#     if ok:
#         ans += 1
# print(ans)

# A
# l, r = map(int, input().split())
# s = 'atcoder'
# print(s[l-1:r])

# B
# r, c = map(int, input().split())
# if max(abs(r-8), abs(c-8))%2 == 1:
#   print('black')
# else:
#   print('white')

# C
# h1, w1 = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(h1)]
# h2, w2 = map(int, input().split())
# b = [list(map(int, input().split())) for _ in range(h2)]
# for hs in range(2**h1):
#   for ws in range(2**w1):
#     rs = []
#     cs = []
#     for i in range(h1):
#       if hs>>i&1:
#         rs.append(i)
#     for j in range(w1):
#       if ws>>j&1:
#         cs.append(j)
#     if len(rs) != h2:
#       continue
#     if len(cs) != w2:
#       continue
#     c = [[0]*w2 for _ in range(h2)]
#     for i in range(h2):
#       for j in range(w2):
#         c[i][j] = a[rs[i]][cs[j]]
#     if b == c:
#       print('Yes')
#       exit()
# print('No')

# D
# from collections import defaultdict
# s = input()
# t = 'atcoder'
# n = len(t)
# mp = defaultdict(int)
# for i in range(n):
#   mp[t[i]] = i
# a = [0]*n
# for i in range(n):
#   a[i] = mp[s[i]]
# ans = 0
# for i in range(n):
#   for j in range(i):
#     if a[j] > a[i]:
#       ans += 1
# print(ans)

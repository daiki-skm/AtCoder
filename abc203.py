# A
# a, b, c = map(int, input().split())
# if a == b:
#     print(c)
# elif a == c:
#     print(b)
# elif b == c:
#     print(a)
# else:
#     print(0)

# B
# N, K = map(int, input().split())
# ans = 0
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         t = str(i) + '0' + str(j)
#         t = int(t)
#         ans += t
# print(ans)

# C
# N, K = map(int, input().split())
# ab = []
# for i in range(N):
#     a, b = map(int, input().split())
#     ab.append((a, b))
# ab.sort()
# for i in range(N):
#     if K >= ab[i][0]:
#         K += ab[i][1]
# print(K)

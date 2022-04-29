# A
# A, B, C = map(int, input().split())
# t1 = A + B
# t2 = A + C
# t3 = B + C
# print(max(t1, t2, t3))

# B
# A, B, C, D = map(int, input().split())
# ans = -1
# diff = C*D-B
# if 0 < diff:
#     ans = (A+diff-1)//diff
# print(ans)

# C
# N = int(input())
# l = [0]*N
# r = [0]*N
# for i in range(N):
#     t, l[i], r[i] = map(int, input().split())
#     l[i] *= 2
#     r[i] *= 2
#     if t >= 3:
#         l[i] += 1
#     if t%2 == 0:
#         r[i] -= 1
# ans = 0
# for i in range(N):
#     for j in range(i):
#         if r[i] < l[j]:
#             continue
#         if r[j] < l[i]:
#             continue
#         ans += 1
# print(ans)

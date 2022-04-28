# A
# A, B = map(int, input().split())
# if A <= B and B <= A*6:
#     print('Yes')
# else:
#     print('No')

# B
# P = int(input())
# fact = []
# ans = 1
# for i in range(1, 11):
#     ans *= i
#     fact.append(ans)
# fact.reverse()
# num = 0
# for i in fact:
#     if i > P:
#         continue
#     t = P//i
#     num += t
#     P -= t*i
#     if P == 0:
#         break
# print(num)

# C
# N, K = map(int, input().split())
# a = list(map(int, input().split()))
# all = K//N
# ans = [all]*N
# K %= N
# p = [0]*N
# for i in range(N):
#     p[i] = [a[i], i]
# p.sort()
# for i in range(K):
#     ans[p[i][1]] += 1
# for i in ans:
#     print(i)

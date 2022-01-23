# s = list(input())
# x, y = map(int, input().split())
# s[x-1], s[y-1] = s[y-1], s[x-1]
# print(''.join(s))

# from collections import Counter
# N = int(input())
# A = list(map(int, input().split()))
# t = Counter(A)
# # print(t)
# print(t.most_common()[N-1][0])

# N, M = map(int, input().split())
# S = list(map(str, input().split()))
# T = list(map(str, input().split()))
# # print(S, T)
# j = 0
# for i in range(N):
#   if S[i] == T[j]:
#     print('Yes')
#     j += 1
#   else:
#     print('No')

import sys
sys.setrecursionlimit(10**6)
N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]
ans = 0
def func(T, L, P):
    if P:
        for i in range(2*N-1):
            if L[i]:
                for j in range(i+1, 2*N):
                    if L[j]:
                        S = T ^ A[i][j-i-1]
                        M = [elem for elem in L]
                        M[i] = False
                        M[j] = False
                        func(S, M, P-1)
                break
    else:
        global ans
        ans = max(ans, T)
func(0, [True]*(2*N), N)
print(ans)
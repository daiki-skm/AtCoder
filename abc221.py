# A, B = map(int, input().split())
# print(32**(A-B))

# S = list(input())
# T = list(input())
# if S == T:
#     print('Yes')
#     exit()
# else:
#     for i in range(len(S)-1):
#         S[i], S[i+1] = S[i+1], S[i]
#         if S == T:
#             print('Yes')
#             exit()
#         S[i], S[i+1] = S[i+1], S[i]
#     print('No')

# import itertools
# import math
# N = list(input())
# p = itertools.permutations(N)
# ans = 0
# for i in range(math.ceil(len(N)/2), len(N)):
#     for pi in p:
#         A = int(''.join(pi[:i]))
#         B = int(''.join(pi[i:]))
#         if A*B > ans:
#             ans = A*B
# print(ans)

N = sorted(input(), reverse=True)
A = N[0::2]
B = N[1::2]
# print(N, A, B)
for i in range(min(len(A),len(B))):
	if A[i] != B[i]:
		A[i], B[i] = B[i], A[i]
		break
print(int("".join(A))*int("".join(B)))
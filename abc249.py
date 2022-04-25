# A
# a, b, c, d, e, f, x = map(int, input().split())
# p = x//(a+c)
# r = x%(a+c)
# s = p*a
# if r <= a:
#     s += r
# else:
#     s += a
# T = s*b
# p = x//(d+f)
# r = x%(d+f)
# s = p*d
# if r <= d:
#     s += r
# else:
#     s += d
# A = s*e
# if T < A:
#     print('Aoki')
# elif T > A:
#     print('Takahashi')
# else:
#     print('Draw')

# B
# S = input()
# S_t = set(list(S))
# if len(S) != len(S_t):
#     print('No')
# elif S.islower() or S.isupper():
#     print('No')
# else:
#     print('Yes')

# C
# N, K = map(int, input().split())
# S = []
# for _ in range(N):
#     S.append(input())
# ans = 0
# for i in range(2**N):
#     dict = {}
#     for j in range(N):
#         if i>>j&1:
#             for c in S[j]:
#                 if c in dict:
#                     dict[c] += 1
#                 else:
#                     dict[c] = 1
#     now = 0
#     for k, v in dict.items():
#         if v == K:
#             now += 1
#     ans = max(ans, now)
# print(ans)

# X = int(input())
# if X < 40:
#     print(40-X)
# elif X < 70:
#     print(70-X)
# elif X < 90:
#     print(90-X)
# else:
#     print('expert')

# S = [input() for _ in range(3)]
# T = input()
# ans = ''
# for i in T:
#     ans += S[int(i)-1]
# print(ans)

# X = input()
# N = int(input())
# A = [input() for _ in range(N)]
# def str_sort(A, B):
#     min_len = min(len(A), len(B))
#     for i in range(min_len):
#         if A[i] != B[i]:
#             A_index = X.index(A[i])
#             B_index = X.index(B[i])
#             if A_index < B_index:
#                 return A
#             else:
#                 return B
#     if len(A) < len(B):
#         return A
#     else:
#         return B
# A.sort(lambda x, y: str_sort(x, y))
# print(A)

X = input()
N = int(input())
S = [input() for _ in range(N)]
ans = sorted(S, key = lambda word: [X.index(c) for c in word])
for word in ans:
    print(word)
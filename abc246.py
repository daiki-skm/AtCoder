# A
# x_dict = {}
# y_dict = {}
# for _ in range(3):
#     x, y = map(int, input().split())
#     if x in x_dict:
#         x_dict[x] += 1
#     if y in y_dict:
#         y_dict[y] += 1
#     if not x in x_dict:
#         x_dict[x] = 1
#     if not y in y_dict:
#         y_dict[y] = 1
# x = 0
# for k, v in x_dict.items():
#     if v == 1:
#         x = k
# y = 0
# for k, v in y_dict.items():
#     if v == 1:
#         y = k
# print(x, y)

# B
# A, B = map(int, input().split())
# d = (A**2 + B**2)**0.5
# print(A/d, B/d)

# C
# N, K, X = map(int, input().split())
# A = list(map(int, input().split()))
# B = A[:]
# m = 0
# for i in range(N):
#     m += A[i]//X
#     B[i] %= X
#     if m >= K:
#         print(sum(A) - X*K)
#         exit()
# B.sort(reverse=True)
# n = 0
# K -= m
# for i in range(N):
#     if i+1 >= K:
#         print(sum(B[i+1:]))
#         exit()
# print(0)

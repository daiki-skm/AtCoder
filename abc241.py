# arr = list(map(int, input().split()))
# index = 0
# # for i in range(len(arr)):
# #     if i == 0:
# #         index = i
# #         break
# for _ in range(3):
#     index = arr[index]
# print(index)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# dict_A = {}
# for Ai in A:
#     if Ai in dict_A:
#         dict_A[Ai] += 1
#     else:
#         dict_A[Ai] = 1
# ans = len(dict_A)
# for Bi in B:
#     if Bi in dict_A:
#         dict_A[Bi] -= 1
#         if dict_A[Bi] < 0:
#             del dict_A[Bi]
#     else:
#         print('No')
#         exit()
# if ans == len(dict_A):
#     print('Yes')
# else:
#     print('No')

# def calc(x, y, dx, dy):
#   count = 0
#   for i in range(6):
#     if not (0 <= min(x, y) and max(x, y) < N):
#       return False
#     if S[x][y] == '#':
#       count += 1
#     x += dx
#     y += dy
#   return count >= 4
# N = int(input())
# S = [input()for _ in range(N)]
# Dx = [1, 0, 1, 1]
# Dy = [0, 1, 1, -1]
# for x in range(N):
#   for y in range(N):
#     for dx, dy in zip(Dx, Dy):
#       if calc(x, y, dx, dy):
#         print("Yes")
#         exit()
# print("No")

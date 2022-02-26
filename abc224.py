# S = input()
# if S[-1] == 't':
#     print('ist')
# else:
#     print('er')

# H, W = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(H)]
# arr_H = []
# arr_W = []
# for i in range(H):
#     for j in range(i, H):
#         if i < j:
#             arr_H.append([i, j])
# for i in range(W):
#     for j in range(i, W):
#         if i < j:
#             arr_W.append([i, j])
# for i in arr_H:
#     for j in arr_W:
#         if not (arr[i[0]][j[0]] + arr[i[1]][j[1]] <= arr[i[1]][j[0]] + arr[i[0]][j[1]]):
#             print('No')
#             exit()
# print('Yes')

from itertools import combinations
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
count = 0
for xy1, xy2, xy3 in list(combinations(XY, 3)):
    area = 1/2*abs((xy2[0]-xy1[0])*(xy3[1]-xy1[1])-(xy3[0]-xy1[0])*(xy2[1]-xy1[1]))
    if area != 0:
        count += 1
print(count)

# N = input()
# # if len(N) == 4:
# #     print(N)
# # elif len(N) == 3:
# #     print('0' + N)
# # elif len(N) == 2:
# #     print('00' + N)
# # elif len(N) == 1:
# #     print('000' + N)
# print(N.zfill(4))

# N, P = map(int, input().split())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#     if a[i] < P:
#         ans += 1
# print(ans)

N, M = map(int, input().split())
A = [list(map(str, input())) for _ in range(2*N)]
win_dict = {}
for i in range(2*N):
    win_dict[i] = 0
A_tenchi = []
for i in range(M):
    tmp = []
    for j in range(2*N):
        tmp.append(A[j][i])
    A_tenchi.append(tmp)
for i in range(M):
    values_sorted = sorted(win_dict.items(), reverse=True, key=lambda x : x[1])
    for j in range(0, 2*N, 2):
        if A_tenchi[i][values_sorted[j][0]] == 'G' and A_tenchi[i][values_sorted[j+1][0]] == 'C':
            win_dict[values_sorted[j][0]] += 1
        elif A_tenchi[i][values_sorted[j][0]] == 'C' and A_tenchi[i][values_sorted[j+1][0]] == 'G':
            win_dict[values_sorted[j+1][0]] += 1
        elif A_tenchi[i][values_sorted[j][0]] == 'P' and A_tenchi[i][values_sorted[j+1][0]] == 'C':
            win_dict[values_sorted[j+1][0]] += 1
        elif A_tenchi[i][values_sorted[j][0]] == 'C' and A_tenchi[i][values_sorted[j+1][0]] == 'P':
            win_dict[values_sorted[j][0]] += 1
        elif A_tenchi[i][values_sorted[j][0]] == 'P' and A_tenchi[i][values_sorted[j+1][0]] == 'G':
            win_dict[values_sorted[j][0]] += 1
        elif A_tenchi[i][values_sorted[j][0]] == 'G' and A_tenchi[i][values_sorted[j+1][0]] == 'P':
            win_dict[values_sorted[j+1][0]] += 1
values_sorted = sorted(win_dict.items(), reverse=True, key=lambda x : x[1])
for i, _ in values_sorted:
    print(i+1)
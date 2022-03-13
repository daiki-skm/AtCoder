# V, A, B, C = map(int, input().split())
# cnt = 0
# ans = ''
# while V >= 0:
#     if cnt%3 == 0:
#         V -= A
#         ans = 'F'
#         cnt += 1
#     elif cnt%3 == 1:
#         V -= B
#         ans = 'M'
#         cnt += 1
#     elif cnt%3 == 2:
#         V -= C
#         ans = 'T'
#         cnt += 1
# print(ans)

# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A_dict = defaultdict(int)
# ans = 0
# for i in range(N):
#     if A[i] == B[i]:
#         ans += 1
#     else:
#         A_dict[A[i]] += 1
# print(ans)
# ans = 0
# for i in range(N):
#     if A_dict[B[i]] > 0:
#         ans += 1
# print(ans)

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
S = list(input())
dict = {}
for i in range(N):
    if XY[i][1] not in dict:
        dict[XY[i][1]] = [(XY[i][0], S[i])]
    else:
        dict[XY[i][1]].append((XY[i][0], S[i]))
for i in dict.values():
    i.sort()
    if len(i) > 1:
        first = ''
        for j in range(len(i)):
            if i[j][1] == 'R':
                first = 'R'
            elif first == 'R' and i[j][1] == 'L':
                print('Yes')
                exit()
print('No')
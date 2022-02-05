# N = int(input())
# t = 2**31
# if -t <= N and N < t:
#     print('Yes')
# else:
#     print('No')

# H, W = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(H)]
# for i in range(W):
#     for j in range(H):
#         print(A[j][i], end=' ')
#     print()

# S = input()
# back_cnt = 0
# for i in range(len(S)-1, -1, -1):
#     if S[i] == 'a':
#         back_cnt += 1
#     else:
#         break
# front_cnt = 0
# for i in range(len(S)):
#     if S[i] == 'a':
#         front_cnt += 1
#     else:
#         break
# if back_cnt < front_cnt:
#     print('No')
#     exit()
# S = 'a'*(back_cnt-front_cnt) + S
# for i in range(int(len(S)/2)):
#     if S[i] != S[len(S)-i-1]:
#         print("No")
#         exit()
# print("Yes")

L = []
R = []
N = int(input())
S = input()
for i, c in enumerate(S):
    if c == 'L':
        R.append(i)
    else:
        L.append(i)
print(*(L+[N]+R[::-1]))
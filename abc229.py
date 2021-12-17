# s1 = input()
# s2 = input()
# s = s1 + s2
# flag = 0
# for i, j in enumerate(s):
#   if j == '#':
#     if i == 0:
#       if s1[1] != '#' and s2[0] != '#':
#         flag = 1
#     elif i == 1:
#       if s1[0] != '#' and s2[1] != '#':
#         flag = 1
#     elif i == 2:
#       if s1[0] != '#' and s2[1] != '#':
#         flag = 1
#     else:
#       if s1[1] != '#' and s2[0] != '#':
#         flag = 1
#   if flag == 1:
#     break
# if flag == 1:
#   print('No')
# else:
#   print('Yes')

# A, B = map(str, input().split())
# rA = reversed(A)
# rB = reversed(B)
# flag = 0
# for i, j in zip(rA, rB):
#   if int(i)+int(j) >= 10:
#     print('Hard')
#     flag = 1
#     break
# if flag == 0:
#   print('Easy')

# N, W = map(int, input().split())
# from sys import stdin
# arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
# ans = 0
# for tmp in sorted(arr, reverse=True):
#   if W-tmp[1] >= 0:
#     ans += tmp[0]*tmp[1]
#     W -= tmp[1]
#   else:
#     ans += W*tmp[0]
#     W = 0
#   if W == 0:
#     break
# print(ans)

# S = input()
# K = int(input())
# ans = 0
# flag = 0
# tmp = 0
# tmp_K = K
# li = S.split('.')
# if len(li) == 1:
#   print(len(S))
#   exit()
# li = S.split('X')
# if len(li) == 1:
#   print(K)
#   exit()
# for num, i in enumerate(S):
#   if flag == 0 and i == 'X':
#     flag = 1
#     tmp += 1
#   elif flag == 1:
#     if i == 'X':
#       tmp += 1
#     else:
#       if tmp_K <= 0:
#         flag = 0
#         if ans < tmp:
#           ans = tmp
#         tmp = 0
#         tmp_K = K
#       else:
#         tmp_K -= 1
#         tmp += 1
#         if num+1 == len(S):
#           ans = tmp
# flag = 0
# tmp = 0
# tmp_K = K
# for num, i in enumerate(reversed(S)):
#   if flag == 0 and i == 'X':
#     flag = 1
#     tmp += 1
#   elif flag == 1:
#     if i == 'X':
#       tmp += 1
#     else:
#       if tmp_K <= 0:
#         flag = 0
#         if ans < tmp:
#           ans = tmp
#         tmp = 0
#         tmp_K = K
#       else:
#         tmp_K -= 1
#         tmp += 1
#         if num+1 == len(S):
#           ans = tmp
# print(ans)

S = list(input())
n = len(S)
k = int(input())
cnt = [0 for _ in range(n + 1)]
for i in range(n):
    if S[i] == '.':
        cnt[i + 1] += cnt[i] + 1
    else:
        cnt[i + 1] += cnt[i]
ans = 0
right = 0
for left in range(n):
    while right < n and cnt[right + 1] - cnt[left] <= k:
        right += 1
    ans = max(ans, right - left)
print(ans)
# S = input()
# arr = [0]*26
# for i in S:
#   arr[ord(i)-97] += 1
# for i, val in enumerate(arr):
#   if val == 0:
#     print(chr(i+97))
#     break
# else:
#   print('None')

# N, M = map(int, input().split())
# arr = [0]*N
# for i in range(M):
#   a, b = map(int, input().split())
#   arr[a-1] += 1
#   arr[b-1] += 1
# for i in arr:
#   print(i)

# from sys import stdin
# W, H, N = map(int, input().split())
# W_arr = [0]*W
# H_arr = [0]*H
# arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
# for arr_i in arr:
#   if arr_i[2] == 1:
#     for i in range(arr_i[0]):
#       W_arr[i] = 1
#   elif arr_i[2] == 2:
#     for i in range(arr_i[0], W):
#       W_arr[i] = 1
#   elif arr_i[2] == 3:
#     for i in range(arr_i[1]):
#       H_arr[i] = 1
#   else:
#     for i in range(arr_i[1], H):
#       H_arr[i] = 1
# print(W_arr.count(0)*H_arr.count(0))

# N = int(input())
# dict = {}
# for i in range(N):
#   tmp = input()
#   if not tmp in dict.keys():
#     dict[tmp] = [1,0]
#   else:
#     dict[tmp][0] += 1
# M = int(input())
# for i in range(M):
#   tmp = input()
#   if not tmp in dict.keys():
#     dict[tmp] = [0,1]
#   else:
#     dict[tmp][1] += 1
# max = 0
# for i in dict:
#   if max < dict[i][0]-dict[i][1]:
#     max = dict[i][0]-dict[i][1]
# if max < 0:
#   print(0)
# else:
#   print(max)

# n,k = map(int, input().split())
# A = list(map(int, input().split()))
# from collections import Counter
# B = Counter(A)
# # print(B)
# a =[]
# for i in B:
#   # print(i, B[i])
#   a.append(B[i])
# a = sorted(a)
# # print(a)
# ans = sum(a[0:(len(B)-k)])
# print(ans)

# C = []
# for i in range(3):
#   C.append(list(map(int,input().split())))
# d1 = C[0][1]- C[0][0]
# d2 = C[0][2]- C[0][1]
# d3 = C[1][0]- C[0][0]
# d4 = C[2][0]- C[1][0]
# if(d1 == C[1][1] - C[1][0]
# and d1 == C[2][1] - C[2][0]
# and d2 == C[1][2] - C[1][1]
# and d2 == C[2][2] - C[2][1]
# and d3 == C[1][1] - C[0][1]
# and d3 == C[1][2] - C[0][2]
# and d4 == C[2][1] - C[1][1]
# and d4 == C[2][2] - C[1][2]):
#   print("Yes")
# else: print("No")

# A,B,C,X,Y = map(int,input().split())
# lst = []
# lst.append(X*A+B*Y)
# lst.append(C*max(X,Y)*2)
# if min(X,Y)==X:
#     lst.append(C*X*2+(Y-X)*B)
# else:
#     lst.append(C*Y*2+(X-Y)*A)
# print(min(lst))

# from math import sqrt
# N = int(input())
# max = 1000000000000
# for i in range(1, int(sqrt(N+1))+1):
#     if N%i == 0:
#         A = len(str(i))
#         B = len(str(int(N/i)))
#         if A < B:
#             if max > B:
#                 max = B
#         else:
#             if max > A:
#                 max = A
# print(max)

# x = int(input())
# xyz = list(map(int, input().split()))
# cnt = 1
# jdg = False
# for i in range(x-1):
#   if not jdg:
#     if xyz[i] < xyz[i+1]:
#       inc_flg = True
#       jdg = True
#     elif xyz[i] > xyz[i+1]:
#       inc_flg = False
#       jdg = True
#     continue
#   if inc_flg:
#     if xyz[i] > xyz[i+1]:
#       cnt += 1
#       inc_flg = False
#       jdg = False
#   else:
#     if xyz[i] < xyz[i+1]:
#       cnt += 1
#       inc_flg = True
#       jdg = False
# print(cnt)

# n,c,k = map(int,input().split())
# t = [int(input()) for _ in range(n)]
# t.sort()
# m = t[0] + k
# pp = 0
# cnt = 1
# for i in range(n):
#   pp += 1
#   if t[i] > m or pp > c:
#     m = t[i] + k
#     pp = 1
#     cnt += 1
# print(cnt)

# n = int(input())
# a = list(map(int, input().split()))
# ans1 = 0
# ans2 = 0
# sum = 0
# # 奇数の時の和を正、偶数の時の和を負にしたとき
# for i in range(n):
#   sum += a[i]
#   if i % 2 == 0 and sum <= 0:
#     ans1 += abs(sum) + 1
#     sum = 1
#   elif i % 2 == 1 and sum >= 0:
#     ans1 += sum + 1
#     sum = -1
# sum = 0
# # 奇数の時の和を負、偶数の時の和を正にしたとき
# for i in range(n):
#   sum += a[i]
#   if i % 2 == 0 and sum >= 0:
#     ans2 += sum + 1
#     sum = -1
#   elif i % 2 == 1 and sum <= 0:
#     ans2 += abs(sum) + 1
#     sum = 1
# ans = min(ans1, ans2)
# print(ans)

# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# butket = [0] * (A[-1] + 3)
# for i in range(N):
#   a = A[i]
#   butket[a] += 1
#   butket[a + 1] += 1
#   butket[a + 2] += 1
# print(max(butket))

# ABC = list(map(int, input().split()))
# ABC.sort()
# a = ABC[2]-ABC[0]
# b = ABC[2]-ABC[1]
# diff = a + b
# quo, rem = divmod(diff, 2)
# if rem == 1:
#   quo += 2
# print(quo)

# N = int(input())
# arr = list(map(int, input().split()))
# odd = [x for x in arr if x%2 == 1]
# if len(odd)%2 == 0:
#   print('YES')
# else:
#   print('NO')

# N,A,B = map(int,input().split())
# print('Borys' if (B-A)%2 != 0 else 'Alice')

# N = int(input())
# dict = {}
# cnt = 0
# for _ in range(N):
#   Ai = int(input())
#   if not Ai in dict.keys():
#     dict[Ai] = 1
#   else:
#     dict[Ai] += 1
# for i in dict:
#   if dict[i]%2 == 1:
#     cnt += 1
# print(cnt)

# H, W = map(int, input().split())
# from sys import stdin
# arr = [list(map(str, stdin.readline().split())) for _ in range(H)]
# dx = [1,0,-1,0,1,1,-1,-1]
# dy = [0,1,0,-1,1,-1,1,-1]
# ans = [[0]*W for _ in range(H)]
# for i in range(H):
#   for j in range(W):
#     if arr[i][0][j] == "#":
#       ans[i][j] = "#"
#     elif arr[i][0][j] == '.':
#       cnt = 0
#       for k in range(8):
#         if 0 <= i+dx[k] <= H-1 and 0 <= j+dy[k] <= W-1:
#           if arr[i+dx[k]][0][j+dy[k]] == "#":
#             cnt += 1
#       ans[i][j] = str(cnt)
# [print("".join(a)) for a in ans]

# H, W = map(int, input().split())
# from sys import stdin
# arr = [list(map(str, stdin.readline().split())) for _ in range(H)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# ans = [[0]*W for _ in range(H)]
# demo = 0
# for i in range(H):
#   for j in range(W):
#     if arr[i][0][j] == "#":
#       flag = 0
#       for k in range(4):
#         if 0 <= i+dx[k] <= H-1 and 0 <= j+dy[k] <= W-1:
#           if arr[i+dx[k]][0][j+dy[k]] == "#":
#             flag = 1
#             break
#       if flag == 0:
#         demo = 1
#         break
#   if demo == 1:
#     break
# if demo == 0:
#   print('Yes')
# else:
#   print('No')

# a, b, c, d = map(int, input().split())
# print(max(0, min(b, d) - max(a, c)))

# N = int(input())
# ans = 1
# for i in range(1, N+1):
#   ans = ans * i % 1000000007
# print(ans)

# N, K = map(int, input().split())
# print(K*((K-1)**(N-1)))

# a, b, x = map(int, input().split())
# t = (b//x+1)
# print(t)
# if a > 0:
#   t -= ((a-1)//x+1)
# print(t)

# A, B, C = map(int, input().split())
# sum = A
# divided = [A]
# for _ in range(B - 1):
#     sum += A
#     divided.append(sum)
# divided = [a % B for a in divided]
# if C in divided:
#     print("YES")
# else:
#     print("NO")

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr_flag = [0]*N
# cnt = 0
# btn = 1
# flag = 0
# while True:
#     if arr_flag[btn-1] == 1:
#         break
#     arr_flag[btn-1] = 1
#     btn = arr[btn-1]
#     cnt += 1
#     if btn == 2:
#         flag = 1
#         break
# if flag == 1:
#     print(cnt)
# else:
#     print(-1)

# N = int(input())
# A1 = list(map(int, input().split()))
# A2 = list(map(int, input().split()))
# arr = []
# for i in range(N):
#     ans = sum(A1[:i+1])
#     for j in range(i, N):
#         ans += A2[j]
#     arr.append(ans)
# print(max(arr))

# N = int(input())
# S = input()
# west = [0] * (N + 1)
# east = [0] * (N + 1) 
# for i in range(N):
#   if S[i] == 'E':
#     east[i + 1] = east[i] + 1
#     west[i + 1] = west[i]
#   else:
#     east[i + 1] = east[i]
#     west[i + 1] = west[i] + 1
# ans = float('inf')
# for i in range(N):
#   if i == 0:
#     ans = min(ans,east[N] - east[1])
#   elif i == N - 1:
#     ans = min(ans,west[N - 1] - west[0])
#   else:
#     ans = min(ans,west[i] - west[0] + east[N] - east[i + 1])
# print(ans)

# str = list(input())
# num_list = [int(i) for i in str]
# if num_list[0] + num_list[1] + num_list[2] + num_list[3] == 7:
#   print('{}+{}+{}+{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] - num_list[1] + num_list[2] + num_list[3] == 7:
#   print('{}-{}+{}+{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] + num_list[1] - num_list[2] + num_list[3] == 7:
#   print('{}+{}-{}+{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] - num_list[1] - num_list[2] + num_list[3] == 7:
#   print('{}-{}-{}+{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] + num_list[1] + num_list[2] - num_list[3] == 7:
#   print('{}+{}+{}-{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] - num_list[1] + num_list[2] - num_list[3] == 7:
#   print('{}-{}+{}-{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] + num_list[1] - num_list[2] - num_list[3] == 7:
#   print('{}+{}-{}-{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))
# elif num_list[0] - num_list[1] - num_list[2] - num_list[3] == 7:
#   print('{}-{}-{}-{}=7'.format(num_list[0],num_list[1],num_list[2],num_list[3]))

# from sys import stdin
# N = int(input())
# x = [list(map(int, stdin.readline().split())) for _ in range(N)]
# max = 0.0
# for i in range(N):
#   for j in range(i+1, N):
#     t = (x[i][0]-x[j][0])**2 + (x[i][1]-x[j][1])**2
#     if max < t:
#       max = t
# print('{:.6f}'.format(max**0.5))

# K, S = map(int, input().split())
# cnt = 0
# for i in range(K+1):
#   for j in range(K+1):
#     if 0 <= S-i-j <= K:
#       cnt += 1
# print(cnt)

# N, Y = map(int, input().split())
# flag = 0
# for i in range(N+1):
#   for j in range(N-i+1):
#     if 10000*i + 5000*j + 1000*(N-i-j) == Y:
#       print('{} {} {}'.format(i,j,N-i-j))
#       flag = 1
#       break
#   if flag == 1:
#     break
# if flag == 0:
#   print('-1 -1 -1')

# N = int(input())
# arr = list(map(int, input().split()))
# cnt = 0
# from itertools import combinations
# for v in combinations(arr, 3):
#   if v[0] != v[1] and v[0] != v[2] and v[1] != v[2]:
#     t = sorted(list(v))
#     if t[2] < t[0]+t[1]:
#       cnt += 1
# print(cnt)

# from itertools import product
# s=input()
# ans=0
# for bit in product(range(2),repeat=len(s)-1):
#   tmp=0
#   cnt=0
#   for i in range(len(s)-1):
#     if bit[i]==0:
#       tmp=tmp*10+int(s[i])
#     else:
#       tmp=tmp*10+int(s[i])
#       cnt+=tmp
#       tmp=0
#   tmp=tmp*10+int(s[-1])
#   cnt+=tmp
#   ans+=cnt
# print(ans)

# from itertools import product
# s = input()
# ans = ''
# for bit in product(range(2),repeat=len(s)-1):
#   tmp = int(s[0])
#   ans = s[0]
#   for i in range(len(s)-1):
#     if bit[i] == 0:
#       tmp += int(s[i+1])
#       ans = ans + '+' + s[i+1]
#     else:
#       tmp -= int(s[i+1])
#       ans = ans + '-' + s[i+1]
#   if tmp == 7:
#     ans += '=7'
#     break
# print(ans)

# D, G =map(int,input().split())
# P = []
# C = []
# for _ in range(D):
#   p, c = map(int, input().split())
#   P.append(p)
#   C.append(c)
# ans = 1e9
# for bit in range(2**D):
#   total = 0
#   num = 0
#   for i in range(D):
#     if(bit>>i)&1:
#       total += 100*(i+1)*P[i]+C[i]
#       num += P[i]
#   if total >= G:
#     ans = min(ans,num)
#   else:
#     for j in reversed(range(D)):
#       if (bit>>j)&1:
#         continue
#       target = G - total
#       if target <= P[j]*(100*(j+1)):
#         num += -(-target//(100*(j+1)))
#         ans = min(ans,num)
#         break
# print(ans)

# from itertools import product
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# minn = 10000000000
# for bit in product(range(2),repeat=N):
#   t1 = 0
#   t2 = 0
#   for i in range(N):
#     if bit[i] == 0:
#       t1 += arr[i]
#     else:
#       t2 += arr[i]
#   m = max(t1, t2)
#   if minn > m:
#     minn = m
# print(minn)

# from sys import stdin
# from itertools import product
# N, M = map(int, input().split())
# if M == 0:
#   print(1)
# else:
#   xyzs = [tuple(map(int, stdin.readline().split())) for _ in range(M)]
#   maxx = 1
#   for bit in product(range(2),repeat=N):
#     if bit.count(1) < 2:
#       continue
#     flg = 0
#     tmp = [id+1 for id, flag in enumerate(bit) if flag == 1]
#     for i in range(len(tmp)-1):
#       for j in range(i+1, len(tmp)):
#         if not (tmp[i], tmp[j]) in xyzs:
#           flg = 1
#           break
#     if flg == 0:
#       maxx = max(maxx, bit.count(1))
#   print(maxx)

# def check(group):
#     for p in group:
#         for q in group:
#             if q == p:
#                 continue
#             if q not in d[p]:
#                 return -1
#     return len(group)
# N, M = map(int, input().split())
# d = {}
# for i in range(1, N + 1):
#     d[i] = set([])
# for i in range(M):
#     a, b = map(int, input().split())
#     d[a].add(b)
#     d[b].add(a)
# # print(d)
# max_n = 1
# for i in range(2 ** N):
#     group = []
#     for j in range(N):
#         if (i >> j) & 1:
#             # print(i, j)
#             group.append(j + 1)
#     max_n = max(max_n, check(group))
# print(max_n)

# import sys
# sys.setrecursionlimit(200000)
# H, W = map(int, input().split())
# arr = [input() for _ in range(H)]
# tmp = [[0] * W for _ in range(H)]
# def explore(i, j):
#   if i < 0 or i >= H:
#     return 0
#   if j < 0 or j >= W:
#     return 0
#   if arr[i][j] == '#':
#     return 0
#   if tmp[i][j] == 1:
#     return 0
#   if arr[i][j] == 'g':
#     return 1
#   tmp[i][j] = 1
#   return explore(i+1, j) or explore(i-1, j) or explore(i, j+1) or explore(i, j-1)
# for i in range(H):
#   for j in range(W):
#     if arr[i][j] == "s":
#       if explore(i, j):
#         print("Yes")
#       else:
#         print("No")
#       break

# import sys
# import copy
# sys.setrecursionlimit(1000000000)
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# arr = [list(input()) for _ in range(10)]
# def check(tmp):
#   for i in range(10):
#     for j in range(10):
#       if tmp[i][j] == "o":
#         return False
#   return True
# def explore(x, y, tmp):
#   tmp[x][y] = 'x'
#   for p in range(4):
#     nx = x + dx[p]
#     ny = y + dy[p]
#     if (0 <= nx < 10) and (0 <= ny < 10) and tmp[nx][ny] == 'o':
#       explore(nx, ny, tmp)
# for i in range(10):
#   for j in range(10):
#     tmp = copy.deepcopy(arr)
#     if tmp[i][j] == 'x':
#       explore(i, j, tmp)
#       if check(tmp):
#         print('YES')
#         exit()
# print('NO')

# n, m = map(int, input().split())
# edges = [[] for _ in range(n)]
# for _ in range(m):
#   u, v = map(int, input().split())
#   u -= 1
#   v -= 1
#   edges[u].append(v)
#   edges[v].append(u)
# def dfs(b_pos, pos):
#   used[pos] = True
#   for n_pos in edges[pos]:
#     if n_pos == b_pos:
#       continue
#     if used[n_pos]:
#       return False
#     if not dfs(pos, n_pos):
#       return False
#   return True
# used = [False for _ in range(n)]
# ans = 0
# for i in range(n):
#   if used[i]:
#     continue
#   if dfs(-1, i):
#     ans += 1
# print(ans)

# R, C = map(int, input().split())
# sy, sx = map(int, input().split())
# gy, gx = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dist = [[-1]*C for _ in range(R)]
# from collections import deque
# Q = deque()
# Q.append([sy-1, sx-1])
# dist[sy-1][sx-1] = 0
# while len(Q) > 0:
#   x, y = Q.popleft()
#   for p in range(4):
#     nx = x + dx[p]
#     ny = y + dy[p]
#     if (0 <= nx < R) and (0 <= ny < C) and arr[nx][ny] == '.' and dist[nx][ny] == -1:
#       dist[nx][ny] = dist[x][y] + 1
#       Q.append([nx, ny])
# print(dist[gy-1][gx-1])

# H, W = map(int, input().split())
# arr = [list(input()) for _ in range(H)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dist = [[-1]*W for _ in range(H)]
# white = 0
# for i in arr:
#   for j in i:
#     if j == '.':
#       white += 1
# from collections import deque
# Q = deque()
# Q.append([0, 0])
# dist[0][0] = 0
# while len(Q) > 0:
#   x, y = Q.popleft()
#   for p in range(4):
#     nx = x + dx[p]
#     ny = y + dy[p]
#     if (0 <= nx < H) and (0 <= ny < W) and arr[nx][ny] == '.' and dist[nx][ny] == -1:
#       dist[nx][ny] = dist[x][y] + 1
#       Q.append([nx, ny])
# if dist[H-1][W-1] == -1:
#   print(-1)
# else:
#   print(white-(dist[H-1][W-1]+1))

# H, W = map(int, input().split())
# arr = [list(input()) for _ in range(H)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dist = [[-1]*W for _ in range(H)]
# from collections import deque
# Q = deque()
# for i in range(H):
#   for j in range(W):
#     if arr[i][j] == '#':
#       Q.append([i, j])
#       dist[i][j] = 0
# cnt = 0
# while len(Q) > 0:
#   x, y = Q.popleft()
#   for p in range(4):
#     nx = x + dx[p]
#     ny = y + dy[p]
#     if (0 <= nx < H) and (0 <= ny < W) and arr[nx][ny] == '.' and dist[nx][ny] == -1:
#       dist[nx][ny] = dist[x][y] + 1
#       Q.append([nx, ny])
# mx = 0
# for i in dist:
#   for j in i:
#     if j > mx:
#       mx = j
# print(mx)

# H, W = map(int, input().split())
# arr = [list(input()) for _ in range(H)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# dist = [[-1]*W for _ in range(H)]
# from collections import deque
# Q = deque()
# for i in range(H):
#   for j in range(W):
#     if arr[i][j] == 's':
#       Q.append([i, j])
#       dist[i][j] = 0
#       break
#   if len(Q) > 0:
#     break
# cnt = 0
# while len(Q) > 0:
#   x, y = Q.popleft()
#   for p in range(4):
#     nx = x + dx[p]
#     ny = y + dy[p]
#     if (0 <= nx < H) and (0 <= ny < W) and arr[nx][ny] == '.' and dist[nx][ny] == -1:
#       dist[nx][ny] = dist[x][y]
#       Q.appendleft([nx, ny])
#     elif (0 <= nx < H) and (0 <= ny < W) and arr[nx][ny] == '#' and dist[nx][ny] == -1:
#       dist[nx][ny] = dist[x][y] + 1
#       Q.append([nx, ny])
#     elif (0 <= nx < H) and (0 <= ny < W) and arr[nx][ny] == "g" and dist[nx][ny] == -1:
#       if dist[x][y] <= 2:
#         print('YES')    
#         exit()
#       break
# print('NO')

# from itertools import permutations
# n, m = map(int,input().split())
# graph = [[0]*n for _ in range(n)]
# for i in range(m):
#   a, b = map(int,input().split())
#   a -= 1
#   b -= 1
#   graph[a][b] = 1
#   graph[b][a] = 1
# ans = 0
# for num in permutations(range(n)):
#   # print(num)
#   if num[0] == 0:
#     count = 0
#     for i in range(n-1):
#       if graph[num[i]][num[i+1]] == 1:
#         count += 1
#     if count == n-1:
#       ans += 1
# print(ans)

# N, M = map(int, input().split())
# from operator import itemgetter
# arr = sorted([list(map(int, input().split())) for _ in range(M)], key=itemgetter(1))
# removed = -1
# ans = 0
# for a, b in arr:
#   if a > removed:
#     removed = b-1
#     ans += 1
# print(ans)

# from bisect import bisect_left
# INF = 10**5 + 1
# N = int(input())
# L = [list(map(int, input().split())) for _ in range(N)]
# L.sort(key=lambda x: (x[0], -x[1]))
# # print(L)
# dp = [INF] * N
# ans = 0
# for h, w in L:
#   idx = bisect_left(dp, w)
#   dp[idx] = w
#   # print(dp, idx)
#   ans = max(ans, idx+1)
# print(ans)

# S = input()
# T = input()
# n = len(S)
# g = set()
# for i in range(n - len(T) + 1):
#     for j in range(len(T)):
#         if S[i+j] == "?":
#             continue
#         if S[i+j] != T[j]:
#             break
#     else:
#         tmp = S[:i] + T + S[i+len(T):]
#         tmp = tmp.replace("?","a")
#         g.add(tmp)
# if len(g) == 0:
#     print("UNRESTORABLE")
# else:
#     # print(g)
#     g = sorted(g)
#     print(g[0])

A = input()
if len(A) > 1:
    print('a')
elif A == 'a':
    print(-1)
else:
    print('a')
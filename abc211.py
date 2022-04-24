# A
# A, B = map(int, input().split())
# print((A-B)/3 + B)

# B
# dict = {}
# for _ in range(4):
#   S = input()
#   if S in dict:
#     dict[S] += 1
#   else:
#     dict[S] = 1
# if len(dict) == 4:
#   print('Yes')
# else:
#   print('No')

# C
# S = input()
# T = 'chokudai'
# mod = 10**9+7
# dp = [[0]*(len(T)+1) for _ in range(len(S)+1)]
# for i in range(len(S)+1):
#   dp[i][0] = 1
# for i in range(len(S)):
#   for j in range(len(T)):
#     if S[i] != T[j]:
#       dp[i+1][j+1] = dp[i][j+1]
#     else:
#       dp[i+1][j+1] = (dp[i][j] + dp[i][j+1])%mod
# print(dp[-1][-1])

# D
N, M = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
	A, B = map(int, input().split())
	A -= 1
	B -= 1
	G[A].append(B)
	G[B].append(A)
que = [0]
dist = [None]*N
cnt = [0]*N
dist[0] = 0
cnt[0] = 1
for v in que:
	for vv in G[v]:
		if dist[vv] is None:
			dist[vv] = dist[v]+1
			que.append(vv)
			cnt[vv] = cnt[v]
		elif dist[vv] == dist[v]+1:
			cnt[vv] += cnt[v]
			cnt[vv] %= 10**9+7
print(cnt[N-1])

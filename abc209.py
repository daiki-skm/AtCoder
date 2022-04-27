# A
# A, B = map(int, input().split())
# if A > B:
#     print(0)
# else:
#     print(B-A+1)

# B
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# minus = len(A)//2
# if sum(A)-minus <= X:
#     print('Yes')
# else:
#     print('No')

# C
# n = int(input())
# c = list(map(int, input().split()))
# mod = 10**9+7
# c.sort()
# ans = 1
# for i in range(n):
#     ans *= max(c[i]-i, 0)
#     ans %= mod
# print(ans)

# D
import queue
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
que = queue.Queue()
color = [-1]*N
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1-color[t]
            que.put(i)
for i in range(Q):
    a, b = map(int, input().split())
    if color[a-1] == color[b-1]:
        print("Town")
    else:
        print("Road")

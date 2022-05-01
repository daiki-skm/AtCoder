# A
# x, y = map(int, input().split())
# ans = (6-x-y)%3
# print(ans)

# B
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#   if A[i] > 10:
#     ans += A[i]-10
# print(ans)

# C
n, m = map(int, input().split())
to = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  to[a-1].append(b-1)
ans = 0
for sv in range(n):
  visited = [False]*n
  visited[sv] = True
  q = [sv]
  ans += 1
  while len(q) > 0:
    v = q.pop()
    for nv in to[v]:
      if visited[nv]:
        continue
      visited[nv] = True
      q.append(nv)
      ans += 1
print(ans)

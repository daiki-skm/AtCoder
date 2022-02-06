# x = input()
# t1 = int(x)
# t2 = int(x[1:] + x[0])
# t3 = int(x[2:] + x[:2])
# print(t1+t2+t3)

# N = int(input())
# H = list(map(int, input().split()))
# mx = 0
# for Hi in H:
#     if Hi > mx:
#         mx = Hi
#     else:
#         break
# print(mx)

# from collections import defaultdict
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# m = defaultdict(list)
# # print(m)
# for i in range(N):
#   m[A[i]].append(i + 1)
# # print(m)
# for _ in range(Q):
#   x, k = map(int, input().split())
#   if k <= len(m[x]):
#     print(m[x][k - 1])
#   else:
#     print(-1)

from collections import deque
a, N = map(int, input().split())
M = 1
while M <= N:
  M *= 10
d = [-1] * M
Q = deque()
d[1] = 0
Q.append(1)
# print(M, d, Q)
while len(Q):
  c = Q.popleft()
  dc = d[c]
  op1 = a * c
  if op1 < M and d[op1] == -1:
    d[op1] = dc + 1
    Q.append(op1)
  if c >= 10 and c % 10 != 0:
    s = str(c)
    op2 = int(s[-1] + s[:-1])
    if op2 < M and d[op2] == -1:
      d[op2] = dc + 1
      Q.append(op2)
print(d[N])

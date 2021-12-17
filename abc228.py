# S, T, X = map(int, input().split())
# if S < T:
#   if S <= X and X < T:
#     print('Yes')
#   else:
#     print('No')
# else:
#   if S <= X or X < T:
#     print('Yes')
#   else:
#     print('No')

# N, X = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
# dict = {}
# for i in range(N):
#   dict[i+1] = [arr[i], 0]
# while True:
#   if dict[X][1] == 1:
#     break
#   dict[X][1] = 1
#   X = dict[X][0]
#   cnt += 1
# print(cnt)

# N, K = map(int, input().split())
# arr = []
# from sys import stdin
# for i in range(N):
#   x, y, z = map(int, stdin.readline().split())
#   arr.append(x+y+z)
# tmp = sorted(arr, reverse=True)
# for num in arr:
#   if num+300 >= tmp[K-1]:
#     print('Yes')
#   else:
#     print('No')

N = 2**20
A = [-1]*N
Q = int(input())
from sys import stdin
for i in range(Q):
  t, x = map(int, stdin.readline().split())
  if t == 1:
    h = x
    while A[h%N] != -1:
      h += 1
    A[h%N] = x
  else:
    print(A[x%N])
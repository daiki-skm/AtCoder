# N = int(input())
# if N >= 42:
#   N += 1
#   N = str(N).zfill(3)
#   print('AGC{}'.format(N))
# else:
#   N = str(N).zfill(3)
#   print('AGC{}'.format(N))

# s = input()
# t = 'oxxoxxoxxoxxoxx'
# if s in t:
#   print('Yes')
# else:
#   print('No')

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
tt = ['.' * (S-R+1) for _ in range(Q-P+1)]
for k in range(max(P-A, R-B), min(Q-A, S-B)+1):
  x = A+k-P
  y = B+k-R
  tmp = list(tt[x])
  tmp[y:y+1] = '#'
  tt[x] = "".join(tmp)
for k in range(max(P-A, B-S), min(Q-A, B-R)+1):
  x = A+k-P
  y = B-k-R
  tmp = list(tt[x])
  tmp[y:y+1] = '#'
  tt[x] = "".join(tmp)
for t in tt:
  print(t)
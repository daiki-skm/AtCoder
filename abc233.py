# import math
# x, y = map(int, input().split())
# if y - x < 0:
#   print(0)
# else:
#   t = y - x
#   print(math.ceil(t/10))

# L, R = map(int, input().split())
# S = input()
# tmp = S[L-1:R]
# str = S[:L-1] + tmp[::-1] + S[R:]
# print(str)

# N, X = map(int, input().split())
# arr = [list(map(int, input().split()))[1:] for _ in range(N)]
# import itertools
# import math
# cnt = 0
# for i in list(itertools.product(*arr)):
#   mu = math.prod(i)
#   if mu == X:
#     cnt += 1
# print(cnt)

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0
# csum = []
# t = 0
# for a in arr:
#   t = t + a
#   if t == K:
#     cnt += 1
#   csum.append(t)
# import itertools
# for tmp in itertools.combinations(csum, 2):
#   if abs(tmp[0]-tmp[1]) == K:
#     cnt += 1
# print(cnt)

from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
cumsum = [0]
for a in A:
  cumsum.append(cumsum[-1] + a)
cnt = Counter(cumsum)
# print(cnt)
ans = 0
for val in cumsum:
  cnt[val] -= 1
  ans += cnt[k + val]
  # print(cnt[k + val], val)
print(ans)
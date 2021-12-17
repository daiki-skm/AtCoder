N, L, R = map(int, input().split())
cnt = 0
# xyzs = [x for x in range(L, R+1) if x^N < N]
# print(len(xyzs))
for x in range(L, R+1):
  # print(x, bin(x), bin(N), x^N, bin(x^N))
  if len(bin(N)) < len(bin(x)):
    break
  if x^N < N:
    cnt += 1
print(cnt)
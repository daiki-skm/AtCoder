target = input()
zero = '0'*len(target)
# xor = '0b' + '1'*len(target)
# target = '0b' + target
# print(target.index('1'))
ans = 0
while True:
  ans += 1
  t = target.index('1')
  tmp = '0b' + target[t:]
  xor = '0b' + '1'*len(target[t:])
  demo = bin(int(tmp, 2) ^ int(xor, 2))[2:]
  target = target[:t] + demo
  if target == zero:
    break
print(ans)

# for i in range(len(target)-1, -1, -1):
#   # print(i)
#   if target[i] == '1':
#     t = target[i:]

# lo = int(input())
# hi = int(input())
# k = int(input())
# mx = 0
# for i in range(lo, hi+1):
#   for j in range(i+1, hi+1):
#     print(i, j)
#     if i^j <= k:
#       mx = max(mx, i^j)
# print(mx)

# s = input()
# x = input()
# num = x.index('*')
# print(num)
# print(x[:num])
# print(s.index(x))
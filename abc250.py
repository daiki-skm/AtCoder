# A
# h, w = map(int, input().split())
# r, c = map(int, input().split())
# ans = 0
# if r != 1:
#   ans += 1
# if c != 1:
#   ans += 1
# if r != h:
#   ans += 1
# if c != w:
#   ans += 1
# print(ans)

# B
# n, a, b = map(int, input().split())
# s = [['.']*n*b for _ in range(n*a)]
# for i in range(n*a):
#   for j in range(n*b):
#     r = i//a
#     c = j//b
#     if (r+c)%2 == 1:
#       s[i][j] = '#'
# for i in range(n*a):
#   print(''.join(s[i]))

# C
# n, q = map(int, input().split())
# ball = [0]*n
# pos = [0]*n
# for i in range(n):
#   ball[i] = i
#   pos[ball[i]] = i
# for _ in range(q):
#   x = int(input())
#   x -= 1
#   i = pos[x]
#   j = i+1
#   if j == n:
#     j = i-1
#   y = ball[j]
#   ball[i], ball[j] = ball[j], ball[i]
#   pos[x], pos[y] = pos[y], pos[x]
# for i in range(n):
#   print(ball[i]+1, end=' ')
# print()

# D
# M = 10**6
# isP = [True]*(M+1)
# primes = []
# isP[0] = False
# isP[1] = False
# for i in range(2, M+1):
#   if not isP[i]:
#     continue
#   primes.append(i)
#   for j in range(i*2, M+1, i):
#     isP[j] = False
# s = [0]*(M+1)
# for p in primes:
#   s[p] = 1
# for i in range(M):
#   s[i+1] += s[i]
# n = int(input())
# ans = 0
# for q in primes:
#   r = min(int(n/q/q/q), q-1)
#   ans += s[r]
# print(ans)

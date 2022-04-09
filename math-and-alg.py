# 001
# N = int(input())
# print(5+N)

# 002
# A1, A2, A3 = map(int, input().split())
# print(A1+A2+A3)

# 003
# N = int(input())
# A = list(map(int, input().split()))
# print(sum(A))

# 004
# A1, A2, A3 = map(int, input().split())
# print(A1*A2*A3)

# 005
# N = int(input())
# a = list(map(int, input().split()))
# print(sum(a)%100)

# 006
# N = int(input())
# print(2*N+3)

# 007
# N, X, Y = map(int, input().split())
# ans = 0
# for i in range(1, N+1):
#     if i%X == 0 or i%Y == 0:
#         ans += 1
# print(ans)

# 008
# N, S = map(int, input().split())
# ans = 0
# for i in range(1, N+1):
#   for j in range(1, N+1):
#     if i+j <= S:
#       ans += 1
# print(ans)

# 010
# N = int(input())
# ans = 1
# for i in range(N, 1, -1):
#   ans *= i
# print(ans)

# 011
# N = int(input())
# ans = []
# for i in range(2, N+1):
#   for j in range(2, i):
#     if i % j == 0:
#       break
#   else:
#     ans.append(i)
# print(*ans)

# 012
# from math import sqrt
# N = int(input())
# ans = 0
# for i in range(2, int(sqrt(N))+1):
#   if N % i == 0:
#     print('No')
#     exit()
# else:
#   print('Yes')

# 013
# from math import sqrt
# N = int(input())
# ans = []
# for i in range(1, int(sqrt(N))+1):
#   if N % i == 0:
#     ans.append(i)
#     ans.append(int(N/i))
# for i in ans:
#   print(i)

# 014
# from math import sqrt
# N = int(input())
# ret = []
# for i in range(2, int(sqrt(N))+1):
#   while N % i == 0:
#     ret.append(i)
#     N //= i
# if N != 1:
#   ret.append(N) 
# print(*ret)

# 015
# A, B = map(int, input().split())
# while (A >= 1 and B >= 1):
#   if A > B:
#     A %= B
#   else:
#     B %= A
# if A == 0:
#   print(B)
# else:
#   print(A)

# 016
# N = int(input())
# A = list(map(int, input().split()))
# def gcd(a, b):
#   while (a >= 1 and b >= 1):
#     if a > b:
#       a %= b
#     else:
#       b %= a
#   if a == 0:
#     return b
#   else:
#     return a
# for i in range(1, N):
#   A[i] = gcd(A[i-1], A[i])
# print(A[-1])

# 017
# N = int(input())
# A = list(map(int, input().split()))
# def gcd(a, b):
#   while (a >= 1 and b >= 1):
#     if a > b:
#       a %= b
#     else:
#       b %= a
#   if a == 0:
#     return b
#   else:
#     return a
# def lcm(a, b):
#   return a * b // gcd(a, b)
# for i in range(1, N):
#   A[i] = lcm(A[i-1], A[i])
# print(A[-1])

# 018
# N = int(input())
# A = list(map(int, input().split()))
# dict = {100: 0, 200: 0, 300: 0, 400: 0}
# for i in range(N):
#   dict[A[i]] += 1
# print(dict[100]*dict[400] + dict[200]*dict[300])

# 019
# N = int(input())
# A = list(map(int, input().split()))
# dict = {1: 0, 2: 0, 3: 0}
# for i in range(N):
#   dict[A[i]] += 1
# print(dict[1]*(dict[1]-1)//2 + dict[2]*(dict[2]-1)//2 + dict[3]*(dict[3]-1)//2)

# 020
# N = int(input())
# A = list(map(int, input().split()))
# ans = 0
# for i in range(N):
#   for j in range(i+1, N):
#     for k in range(j+1, N):
#       for l in range(k+1, N):
#         for m in range(l+1, N):
#           if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
#             ans += 1
# print(ans)

# 021
# n, r = map(int, input().split())
# if n//2 < r:
#   r = n-r
# numerator = 1
# denominator = 1
# for i in range(n, n-r, -1):
#   numerator *= i
# for i in range(1, r+1):
#   denominator *= i
# print(numerator//denominator)

# 022
# N = int(input())
# A = list(map(int, input().split()))
# dict = {}
# for i in range(N):
#   if A[i] in dict:
#     dict[A[i]] += 1
#   else:
#     dict[A[i]] = 1
# ans = 0
# for i in dict:
#   j = 100000 - i
#   if i == j:
#     ans += dict[i]*(dict[i]-1)//2
#   elif j in dict:
#     ans += dict[i] * dict[j]
#     dict[j] = 0
#     dict[i] = 0
# print(ans)

# 023
# N = int(input())
# B = list(map(int, input().split()))
# R = list(map(int, input().split()))
# print(sum(B)/N+sum(R)/N)

# 024
# N = int(input())
# ans = 0
# for i in range(N):
#   P, Q = map(int, input().split())
#   ans += Q/P
# print(ans)

# 025
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# print(sum(A)/3+2*sum(B)/3)

# 026
# N = int(input())
# ans = 0
# for i in range(1, N+1):
# 	ans += N/i
# print(ans)

# 027
# def MergeSort(A):
#   if len(A) == 1:
#     return A
#   m = len(A) // 2
#   A_Dash = MergeSort(A[0:m])
#   B_Dash = MergeSort(A[m:len(A)])
#   c1 = 0
#   c2 = 0
#   C = []
#   while (c1 < len(A_Dash) or c2 < len(B_Dash)):
#     if c1 == len(A_Dash):
#       C.append(B_Dash[c2])
#       c2 += 1
#     elif c2 == len(B_Dash):
#       C.append(A_Dash[c1])
#       c1 += 1
#     else:
#       if A_Dash[c1] < B_Dash[c2]:
#         C.append(A_Dash[c1])
#         c1 += 1
#       else:
#         C.append(B_Dash[c2])
#         c2 += 1
#   return C
# N = int(input())
# A = list(map(int, input().split()))
# Answer = MergeSort(A)
# print(*Answer)

# 028
# N = int(input())
# h = list(map(int, input().split()))
# dp = [0] * N
# dp[1] = abs(h[0]-h[1])
# for i in range(2, N):
#   dp[i] = min(dp[i-2] + abs(h[i]-h[i-2]), dp[i-1] + abs(h[i]-h[i-1]))
# print(dp[-1])

# 029
# N = int(input())
# dp = [0] * (N+1)
# for i in range(N+1):
#   if i <= 1:
#     dp[i] = 1
#   else:
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[-1])

# 030
# N, W = map(int, input().split())
# w = []
# v = []
# for _ in range(N):
#   wi, vi = map(int, input().split())
#   w.append(wi)
#   v.append(vi)
# dp = [[-1] * (W+1) for _ in range(N+1)]
# dp[0][0] = 0
# for i in range(N):
#   for j in range(W+1):
#     if j < w[i]:
#       dp[i+1][j] = dp[i][j]
#     else:
#       dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
# print(max(dp[-1]))

# 009
# N, S = map(int, input().split())
# A = list(map(int, input().split()))
# dp = [[-1] * (S+1) for _ in range(N+1)]
# dp[0][0] = True
# for i in range(1, S+1):
#   dp[0][i] = False
# for i in range(N):
#   for j in range(S+1):
#     if j < A[i]:
#       dp[i+1][j] = dp[i][j]
#     else:
#       if dp[i][j] == True or dp[i][j-A[i]] == True:
#         dp[i+1][j] = True
#       else:
#         dp[i+1][j] = False
# if dp[N][S] == True:
# 	print("Yes")
# else:
# 	print("No")

# 031
# N = int(input())
# A = list(map(int, input().split()))
# dp1 = [0] * (N+1)
# dp2 = [0] * (N+1)
# for i in range(1, N+1):
#   dp1[i] = dp2[i-1] + A[i-1]
#   dp2[i] = max(dp1[i-1], dp2[i-1])
# print(max(dp1[-1], dp2[-1]))

# 032
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# l = 0
# r = N
# while l < r:
#   m = (l+r)//2
#   if A[m] == X:
#     print('Yes')
#     exit()
#   if A[m] < X:
#     l = m+1
#   if A[m] > X:
#     r = m
# print('No')

# 033
# from math import sqrt
# def vector(B, A):
#   return (A[0]-B[0], A[1]-B[1])
# def inner(A, B):
#   return A[0]*B[0] + A[1]*B[1]
# def cross(A, B):
#   return abs(A[0]*B[1] - B[0]*A[1])
# def distance(A):
#   return sqrt(A[0]**2 + A[1]**2)
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# if inner(vector(b, a), vector(b, c)) < 0:
#   print(distance(vector(b, a)))
# elif inner(vector(c, a), vector(c, b)) < 0:
#   print(distance(vector(c, a)))
# else:
#   print(cross(vector(b, a), vector(b, c))/distance(vector(b, c)))

# 034
# N = int(input())
# x = []
# y = []
# for _ in range(N):
#   a, b = map(int, input().split())
#   x.append(a)
#   y.append(b)
# ans = 10**10
# for i in range(N):
#   for j in range(i+1, N):
#     ans = min(ans, ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5)
# print(ans)

# 035
# x1, y1, r1 = map(int, input().split())
# x2, y2, r2 = map(int, input().split())
# d = ((x1-x2)**2 + (y1-y2)**2)**0.5
# if d > r1+r2:
#   print(5)
# elif d == r1+r2:
#   print(4)
# elif d == abs(r1-r2):
#   print(2)
# elif d < abs(r1-r2):
#   print(1)
# else:
#   print(3)

# 036
# from math import pi, cos, sin
# A, B, H, M = map(int, input().split())
# Ax = A*cos((30*H + 0.5*M)*pi/180)
# Ay = A*sin((30*H + 0.5*M)*pi/180)
# Bx = B*cos(M*6*pi/180)
# By = B*sin(M*6*pi/180)
# print(((Ax-Bx)**2+(Ay-By)**2)**0.5)

# 037
# def cross(ax, ay, bx, by):
# 	return ax * by - ay * bx
# X1, Y1 = map(int, input().split())
# X2, Y2 = map(int, input().split())
# X3, Y3 = map(int, input().split())
# X4, Y4 = map(int, input().split())
# ans1 = cross(X2-X1, Y2-Y1, X3-X1, Y3-Y1)
# ans2 = cross(X2-X1, Y2-Y1, X4-X1, Y4-Y1)
# ans3 = cross(X4-X3, Y4-Y3, X1-X3, Y1-Y3)
# ans4 = cross(X4-X3, Y4-Y3, X2-X3, Y2-Y3)
# if ans1 == 0 and ans2 == 0 and ans3 == 0 and ans4 == 0:
# 	A = (X1, Y1)
# 	B = (X2, Y2)
# 	C = (X3, Y3)
# 	D = (X4, Y4)
# 	if A > B:
# 		tmp = B
# 		B = A
# 		A = tmp
# 	if C > D:
# 		tmp = D
# 		D = C
# 		C = tmp
# 	if max(A, C) <= min(B, D):
# 		print("Yes")
# 	else:
# 		print("No")
# else:
# 	IsAB = False
# 	IsCD = False
# 	if ans1 >= 0 and ans2 <= 0:
# 		IsAB = True
# 	if ans1 <= 0 and ans2 >= 0:
# 		IsAB = True
# 	if ans3 >= 0 and ans4 <= 0:
# 		IsCD = True
# 	if ans3 <= 0 and ans4 >= 0:
# 		IsCD = True
# 	if IsAB == True and IsCD == True:
# 		print("Yes")
# 	else:
# 		print("No")

# 038
# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# t = []
# for i in range(N):
#   if i == 0:
#     t.append(A[i])
#   else:
#     t.append(t[i-1] + A[i])
# ans = []
# for _ in range(Q):
#   l, r = map(int, input().split())
#   if l == 1:
#     ans.append(t[r-1])
#   else:
#     ans.append(t[r-1] - t[l-2])
# for i in ans:
#   print(i)

# 039
# N, Q = map(int, input().split())
# B = [0]*N
# for _ in range(Q):
#   l, r, x = map(int, input().split())
#   B[l-1] += x
#   if r < N:
#     B[r] += -x
# ans = ''
# for i in range(N-1):
#   if B[i+1] > 0:
#     ans += '<'
#   elif B[i+1] == 0:
#     ans += '='
#   else:
#     ans += '>'
# print(ans)

# 040
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = [0]*M
# for i in range(M):
# 	B[i] = int(input())
# S = [0]*N
# for i in range(1, N):
# 	S[i] = S[i - 1] + A[i - 1]
# ans = 0
# for i in range(M-1):
#   if B[i] < B[i+1]:
#     ans += S[B[i+1]-1] - S[B[i]-1]
#   else:
#     ans += S[B[i]-1] - S[B[i+1]-1]
# print(ans)


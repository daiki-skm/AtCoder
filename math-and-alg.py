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

# re: 009
# N, S = map(int, input().split())
# A = list(map(int, input().split()))
# # 配列の初期化
# dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
# dp[0][0] = True
# for i in range(1, S + 1):
# 	dp[0][i] = False
# # 動的計画法
# for i in range(1, N + 1):
# 	for j in range(0, S + 1):
# 		if j < A[i - 1]:
# 			# j < A[i-1] のとき、カード i を選べない
# 			dp[i][j] = dp[i - 1][j]
# 		else:
# 			# j >= A[i-1] のとき、選ぶ / 選ばない 両方の選択肢がある
# 			if (dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True):
# 				dp[i][j] = True
# 			else:
# 				dp[i][j] = False
# # 答えを出力
# if dp[N][S] == True:
# 	print("Yes")
# else:
# 	print("No")

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

# re: 014
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

# re: 017
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

# re: 022
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

# re: 026
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


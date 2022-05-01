# A
# A, B = map(int, input().split())
# print(A/100*B)

# B
# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# for i in range(N):
#     if A[i] != i+1:
#         print('No')
#         exit()
# print('Yes')

# C
# A, B, C = map(int, input().split())
# if C%2 == 0:
#     A = abs(A)
#     B = abs(B)
# if A < B:
#     print('<')
# if A == B:
#     print('=')
# if A > B:
#     print('>')

# D
# from bisect import bisect_left
# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# c = [0]*n
# for i in range(n):
#     c[i] = a[i]-i-1
# for i in range(q):
#     k = int(input())
#     r = bisect_left(c, k)
#     ans = 0
#     if r == 0:
#         ans = k
#     else:
#         ans = a[r-1] + k - c[r-1]
#     print(ans)

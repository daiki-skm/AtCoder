# A, B = map(int, input().split())
# print(A^B)

# N = int(input())
# A = list(map(int, input().split()))
# dic = {}
# for i in range(N):
#     dic[A[i]] = i+1
# sort = sorted(dic.items())
# print(sort[N-2][1])

# H, W, N = map(int, input().split())
# A = []
# B = []
# for i in range(N):
#     a, b = map(int, input().split())
#     A.append(a)
#     B.append(b)
# Adict = {x:i+1 for i,x in enumerate(sorted(list(set(A))))}
# Bdict = {y:i+1 for i,y in enumerate(sorted(list(set(B))))}
# for i in range(N):
#   print(Adict[A[i]], Bdict[B[i]])


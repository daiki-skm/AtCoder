# import math
# H = int(input())
# print(math.sqrt(H*(12800000+H)))

# X = int(input())
# print(X//10)

# def dist_sq(a, b, c, d):
#   return (a - c) ** 2 + (b - d) ** 2
# def solve(x1, y1, x2, y2):
#   for x in range(x1 - 2, x1 + 3):
#     for y in range(y1 - 2, y1 + 3):
#       if dist_sq(x, y, x1, y1) == dist_sq(x, y, x2, y2) == 5:
#         return "Yes"
#   return "No"
# x1, y1, x2, y2 = map(int, input().split())
# print(solve(x1, y1, x2, y2))

prime=[True]*201
prime[0]=False
prime[1]=False
for p in range(15):
  if prime[p]:
    for i in range(p*p,201,p):
      prime[i]=False
A,B,C,D=map(int,input().split())
for x in range(A,B+1):
  if all(not prime[x+y] for y in range(C,D+1)):
    print("Takahashi")
    exit()
print("Aoki")

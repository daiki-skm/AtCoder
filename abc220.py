# A, B, C = map(int, input().split())
# for i in range(A, B+1):
#     if i % C == 0:
#         print(i)
#         exit()
# print("-1")

# K = int(input())
# A, B = map(str, input().split())
# A = A[::-1]
# B = B[::-1]
# A_ten = 0
# B_ten = 0
# for i in range(len(A)-1, -1, -1):
#     A_ten += int(str(A)[i]) * (K ** i)
# for i in range(len(B)-1, -1, -1):
#     B_ten += int(str(B)[i]) * (K ** i)
# print(A_ten*B_ten)

# print(int(A, K)*int(B, K))

# N = int(input())
# A = list(map(int, input().split()))
# X = int(input())
# sum = sum(A)
# quotient = X//sum
# surplus = X%sum
# ans = len(A)*quotient
# tmp = 0
# for i in range(len(A)):
#     tmp += A[i]
#     ans += 1
#     if tmp > surplus:
#         break
# print(ans)

mod = 998244353
N = int(input())
A = list(map(int, input().split()))
dp = [[0]*10 for _ in range(N)]
le = A[0]
dp[0][le] = 1
for i in range(N-1):
    for j in range(10):
        dp[i+1][(j+A[i+1])%10] += dp[i][j]
        dp[i+1][(j+A[i+1])%10] %= mod
        dp[i+1][(j*A[i+1])%10] += dp[i][j]
        dp[i+1][(j*A[i+1])%10] %= mod
        print(dp)
for ans in dp[-1]:
    print(ans)

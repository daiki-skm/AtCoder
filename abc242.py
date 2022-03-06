# A, B, C, X = map(int, input().split())
# if X <= A:
#     print(1)
# elif X <= B:
#     print(C/(B-A))
# else:
#     print(0)

# S = list(input())
# S.sort()
# print(''.join(S))

# N = int(input())
# mod = 998244353
# A, B = 10**(N-1), 10**N
# ans = 0
# for i in range(A, B):
#     if str(i).count('0') != 0:
#         continue
#     for j in range(N-1):
#         if abs(int(str(i)[j]) - int(str(i)[j+1])) > 1:
#             break
#     else:
#         ans += 1
# print(ans % mod)

N = int(input())
MOD = 998244353
memo = [1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N-1):
    temp_memo = memo[:]
    for j in range(1, 10):
        if j == 1:
            memo[0] = (temp_memo[0] + temp_memo[1]) % MOD
        elif j == 9:
            memo[8] = (temp_memo[7] + temp_memo[8]) % MOD
        else:
            memo[j-1] = (temp_memo[j-2] + temp_memo[j-1] + temp_memo[j]) % MOD
ans = sum(memo) % MOD
print(ans)
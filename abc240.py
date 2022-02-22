# a, b = map(int, input().split())
# if abs(a - b) == 1 or abs(a - b) == 9:
#     print("Yes")
# else:
#     print("No")

# N = int(input())
# arr = list(map(int, input().split()))
# print(len(set(arr)))

## DPで解く
# N, X = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(2**N):
#     ans = 0
#     for j in range(N):
#         ans += arr[j][0] if (i >> j) & 1 else arr[j][1]
#         if ans > X:
#             break
#     if ans == X:
#         print("Yes")
#         exit()
# print("No")

# N, X = map(int, input().split())
# MAX_N = 100
# MAX_X = 10000
# dp = [[False]*(MAX_X+1) for _ in range(MAX_N+1)]
# dp[0][0] = True
# for i in range(N):
#     a, b = map(int, input().split())
#     for j in range(X):
#         if dp[i][j]: 
#             dp[i+1][j+a] = True 
#             dp[i+1][j+b] = True 
# print("Yes") if dp[N][X] else print("No")

# N = int(input())
# arr = list(map(int, input().split()))
# ans = [[arr[0], 1]]
# count = 1
# print(count)
# for i in range(1, N):
#     count += 1
#     if not ans:
#         ans.append([arr[i], 1])
#         print(count)
#         continue
#     if arr[i] == ans[-1][0]:
#         ans[-1][1] += 1
#         if ans[-1][0] == ans[-1][1]:
#             count -= ans[-1][0]
#             del ans[-1]
#     else:
#         ans.append([arr[i], 1])
#     print(count)

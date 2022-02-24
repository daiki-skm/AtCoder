# N, K, A = map(int, input().split())
# ans = (A + K - 1) % N
# if ans == 0:
#     ans = N
# print(ans)

# N = int(input())
# S = list(map(int, input().split()))
# MAX = 333
# count = 0
# for Si in S:
#     flg = 0
#     for i in range(1, MAX+1):
#         for j in range(1, MAX+1):
#             if Si == (4*i*j + 3*i + 3*j):
#                 flg = 1
#     if flg == 0:
#         count += 1
# print(count)

N = int(input())
ans = 0
for a in range(1, N+1):
    if a**3 > N:
        break
    for b in range(a, N+1):
        if a*b*b > N:
            break
        ans += N//a//b-b+1
        # print(a, b, ans)
print(ans)

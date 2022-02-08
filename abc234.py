# def f(t):
#     return t**2 + 2*t + 3
# t = int(input())
# print(f(f(f(t)+t) + f(f(t))))

# import itertools, math
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# mx = 0
# comb_arr = list(itertools.combinations(arr, 2))
# for i in comb_arr:
#     mx = max(mx, math.sqrt(abs(i[0][0] - i[1][0])**2 + abs(i[0][1] - i[1][1])**2))
# print(mx)

# K = bin(int(input()))[2:]
# print(K.replace('1', '2'))

import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
que = P[0:K]
print(min(que))
heapq.heapify(que)
# print(que)
for i in range(K,N):
    minima = heapq.heappop(que)
    # print('1: ', minima)
    minima = max(minima,P[i])
    # print('2: ', minima)
    heapq.heappush(que,minima)
    # print('3: ', que)
    ans = heapq.heappop(que)
    # print('4: ', ans)
    print(ans)
    heapq.heappush(que,ans)
    # print('5: ', que)

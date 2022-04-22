# A
# A, B = map(int, input().split())
# if 0 < A and B == 0:
#     print('Gold')
# elif A == 0 and 0 < B:
#     print('Silver')
# else:
#     print('Alloy')

# B
# S = list(input())
# if len(set(S)) == 1:
#     print('Weak')
#     exit()
# cnt = 0
# for i in range(len(S)-1):
#     if int(S[i])+1 == int(S[i+1]):
#         cnt += 1
#     if int(S[i]) == 9 and int(S[i+1]) == 0:
#         cnt += 1
# # print(cnt)
# if cnt == len(S)-1:
#     print('Weak')
# else:
#     print('Strong')

# C
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A.sort()
# B.sort()
# ai = 0
# bi = 0
# ans = 10**9
# while ai < N and bi < M:
#     ans = min(ans, abs(A[ai]-B[bi]))
#     if A[ai] < B[bi]:
#         ai += 1
#     else:
#         bi += 1
# print(ans)

# D
# import heapq
# Q = int(input())
# q = list()
# plus = 0
# for _ in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         heapq.heappush(q, query[1]-plus)
#     if query[0] == 2:
#         plus += query[1]
#     if query[0] == 3:
#         val = heapq.heappop(q)
#         print(val+plus)

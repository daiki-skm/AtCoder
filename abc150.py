# A
# k, x = map(int, input().split())
# if k * 500 >= x:
#     print('Yes')
# else:
#     print('No')

# B
# n = int(input())
# s = input()
# ans = 0
# for i in range(n - 2):
#     if s[i:i + 3] == 'ABC':
#         ans += 1
# print(ans)

# C
# from itertools import permutations
#
# n = int(input())
# p = list(map(int, input().split()))
# q = list(map(int, input().split()))
# pl = list(permutations([i for i in range(1, n + 1)], n))
# np = 0
# nq = 0
# for i in range(len(pl)):
#     if p == list(pl[i]):
#         np = i
#     if q == list(pl[i]):
#         nq = i
# print(abs(np - nq))

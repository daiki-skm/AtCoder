# A
# n = int(input())
# if n%100 == 0:
#     print(n//100)
# else:
#     print(n//100+1)

# B
# N, K = map(int, input().split())
# for _ in range(K):
#     if N%200 == 0:
#         N /= 200
#         N = int(N)
#     else:
#         n = str(N)
#         n += '200'
#         N = int(n)
# print(N)

# C
# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))
# mod_a = defaultdict(int)
# for i in a:
#     mod_a[i%200] += 1
# ans = 0
# for i in mod_a.values():
#     ans += i*(i-1)//2
# print(ans)

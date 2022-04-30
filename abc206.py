# A
# N = int(input())
# t = int(N*1.08)
# if t > 206:
#     print(':(')
# elif t == 206:
#     print('so-so')
# else:
#     print('Yay!')

# B
# N = int(input())
# ans = 0
# i = 0
# while ans < N:
#     i += 1
#     ans += i
# print(i)

# C
# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))
# dict = defaultdict(int)
# ans = 0
# for i in range(N):
#     ans += i-dict[A[i]]
#     dict[A[i]] += 1
# print(ans)

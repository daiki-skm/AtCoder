# A
# a = list(map(int, input().split()))
# t = set(a)
# print(len(t))

# B
# s = input()
# t = input()
# if t[:len(s)] == s:
#     print('Yes')
# else:
#     print('No')

# C
# n = int(input())
# p = list(map(int, input().split()))
# cnt = [0]*n
# for i in range(n):
#     j = (p[i]-i-1)%n
#     for k in range(3):
#         cnt[(j+k)%n] += 1
# ans = 0
# for i in range(n):
#     ans = max(ans, cnt[i])
# print(ans)

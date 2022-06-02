# A
# n, x, t = map(int, input().split())
# ans = 0
# if n % x == 0:
#     ans = n // x
# else:
#     ans = n // x + 1
# print(ans * t)

# B
# n = input()
# ans = 0
# for c in n:
#     ans += int(c)
# if ans % 9 == 0:
#     print('Yes')
# else:
#     print('No')

# C
# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# mx = 0
# for i in range(1, n):
#     mx = max(mx, a[i - 1])
#     if a[i] < mx:
#         ans += mx - a[i]
# print(ans)

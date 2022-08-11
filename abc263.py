# A
# a = list(map(int, input().split()))
# a.sort()
# if (a[0] == a[2] and a[3] == a[4]) or (a[0] == a[1] and a[2] == a[4]):
#     print("Yes")
# else:
#     print("No")

# B
# n = int(input())
# p = [0, 0] + list(map(int, input().split()))
# crr = n
# cnt = 0
# while crr != 1:
#     cnt += 1
#     crr = p[crr]
# print(cnt)

# C
# from itertools import combinations
#
# n, m = map(int, input().split())
# for i in combinations(range(1, m + 1), n):
#     print(*i)

# D
# n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# crr = 0
# ans = r * n
# for i in range(n):
#     crr = min(crr + a[i], l * (i + 1))
#     ans = min(ans, crr + r * (n - i - 1))
# print(ans)

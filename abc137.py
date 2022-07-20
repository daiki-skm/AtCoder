# A
# a, b = map(int, input().split())
# print(max(a + b, a - b, a * b))

# B
# k, x = map(int, input().split())
# for i in range(x - k + 1, x + k, 1):
#     print(i, end=' ')

# C
# from collections import defaultdict
#
# n = int(input())
# d = defaultdict(int)
# for _ in range(n):
#     s = list(input())
#     s.sort()
#     s = ''.join(s)
#     d[s] += 1
# ans = 0
# for v in d.values():
#     ans += v * (v - 1) // 2
# print(ans)

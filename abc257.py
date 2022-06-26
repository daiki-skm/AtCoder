# A
# n, x = map(int, input().split())
# i = (x - 1) // n
# print(chr(ord('A') + i))

# B
# n, k, q = map(int, input().split())
# a = list(map(int, input().split()))
# l = list(map(int, input().split()))
# for i in range(q):
#     li = l[i] - 1
#     if a[li] == n:
#         continue
#     if li < k - 1 and a[li + 1] == a[li] + 1:
#         continue
#     a[li] += 1
# print(*a)

# C
# from collections import defaultdict
#
# n = int(input())
# s = input()
# w = list(map(int, input().split()))
# mp = defaultdict(list)
# for i in range(n):
#     mp[w[i]].append(i)
# mp = sorted(mp.items(), key=lambda x: x[0])
# mp_sorted = {}
# for i in range(len(mp)):
#     mp_sorted[mp[i][0]] = mp[i][1]
# now = 0
# for i in range(n):
#     if s[i] == '1':
#         now += 1
# ans = now
# for p in mp_sorted.values():
#     for i in p:
#         if s[i] == '1':
#             now -= 1
#         else:
#             now += 1
#     ans = max(ans, now)
# print(ans)

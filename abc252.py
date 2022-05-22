# A
# n = int(input())
# print(chr(n))

# B
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# dict = {i + 1: a[i] for i in range(n)}
# max_keys = [key for key, value in dict.items() if value == max(dict.values())]
# for key in max_keys:
#     if key in b:
#         print('Yes')
#         exit()
# print('No')

# C
# from collections import defaultdict
#
# n = int(input())
# d = {i: defaultdict(int) for i in range(10)}
# for i in range(n):
#     s = list(input())
#     for j in range(10):
#         d[int(s[j])][j] += 1
# ans = 10 ** 9
# for i in range(10):
#     max_keys = [key for key, value in d[i].items() if value == max(d[i].values())]
#     if len(max_keys) == 1:
#         t = d[i][max_keys[0]]
#         ans = min(ans, (t - 1) * 10 + max_keys[0])
#         continue
#     max_keys.sort(reverse=True)
#     t = d[i][max_keys[0]]
#     ans = min(ans, (t - 1) * 10 + max_keys[0])
# print(ans)

# D
from collections import defaultdict
from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
s = set(a)
d = defaultdict(int)
for i in a:
    d[i] += 1
ans = 0
t = list(d.keys())
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        for k in range(j + 1, len(t)):
            ans += d[t[i]] * d[t[j]] * d[t[k]]
# for i in combinations(s, 3):
#     ans += d[i[0]] * d[i[1]] * d[i[2]]
print(ans)

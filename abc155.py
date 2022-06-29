# A
# from collections import Counter
#
# a = list(map(int, input().split()))
# a = Counter(a)
# if len(a) == 2:
#     print('Yes')
# else:
#     print('No')

# B
# n = int(input())
# a = list(map(int, input().split()))
# for ai in a:
#     if ai % 2 == 0 and ai % 3 != 0 and ai % 5 != 0:
#         print('DENIED')
#         exit()
# print('APPROVED')

# C
# from collections import Counter
#
# n = int(input())
# s = Counter()
# for i in range(n):
#     s[input()] += 1
# mx = max(s.values())
# t = []
# for k, v in s.items():
#     if v == mx:
#         t.append(k)
# t.sort()
# for tt in t:
#     print(tt)

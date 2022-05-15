# A
# s = input()
# if len(s) == 1:
#     print(s+s+s+s+s+s)
# elif len(s) == 2:
#     print(s+s+s)
# else:
#     print(s+s)

# B
# from itertools import combinations
# n, w = map(int, input().split())
# a = list(map(int, input().split()))
# ans = set()
# for i in combinations(a, 1):
#     if sum(i) <= w:
#         ans.add(sum(i))
# for i in combinations(a, 2):
#     if sum(i) <= w:
#         ans.add(sum(i))
# for i in combinations(a, 3):
#     if sum(i) <= w:
#         ans.add(sum(i))
# print(len(ans))

# C
# n = int(input())
# arr = set()
# max_val = 0
# max_id = 0
# for i in range(n):
#     s, t = input().split()
#     if not s in arr:
#         arr.add(s)
#         if int(t) > max_val:
#             max_val = int(t)
#             max_id = i
# print(max_id+1)

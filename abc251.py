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

# D
w = int(input())
ans = []
dict = {i:0 for i in range(1, w+1)}
# print(dict)
for i in range(int(w/2)):
    for j in range(int(w/2)):
        for k in range(int(w/2)):
            if i+j+k in dict.keys():
                dict[i+j+k] = [i, j, k]
                # ans.append([i, j, k])
print(dict)
# print(ans)

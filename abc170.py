# A
# x = list(map(int, input().split()))
# print(x.index(0) + 1)

# B
# x, y = map(int, input().split())
# for c in range(x + 1):
#     t = x - c
#     foot = c * 2 + t * 4
#     if foot == y:
#         print('Yes')
#         exit()
# print('No')

# C
# x, n = map(int, input().split())
# p = list(map(int, input().split()))
# not_p = [i for i in range(102) if i not in p]
# not_p.sort(reverse=True)
# ans = x
# ans_i = 0
# for i in not_p:
#     if abs(x - i) <= ans:
#         ans = abs(x - i)
#         ans_i = i
# print(ans_i)

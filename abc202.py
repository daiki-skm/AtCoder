# A
# a, b, c = map(int, input().split())
# print(21-(a+b+c))

# B
# s = list(input())
# s.reverse()
# for i in range(len(s)):
#     if s[i] == '6':
#         s[i] = '9'
#     elif s[i] == '9':
#         s[i] = '6'
# print(''.join(s))

# C
# from collections import defaultdict
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# a_dict = defaultdict(int)
# for i in a:
#     a_dict[i] += 1
# ans = 0
# for j in range(n):
#     if b[c[j]-1] in a_dict:
#         ans += a_dict[b[c[j]-1]]
# print(ans)

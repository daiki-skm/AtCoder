# A
# x = int(input())
# if x%100 == 0:
#     print(100)
# else:
#     print(100-x%100)

# B
# s = input()
# flag = False
# for c in s:
#     if flag == False and c.islower():
#         flag = True
#         continue
#     if flag == True and c.isupper():
#         flag = False
#         continue
#     print('No')
#     exit()
# print('Yes')

# C
# n, k = map(int, input().split())
# def g1(x):
#     t = list(str(x))
#     t.sort(reverse=True)
#     return int(''.join(t))
# def g2(x):
#     t = list(str(x))
#     t.sort()
#     return int(''.join(t))
# def f(x):
#     return g1(x) - g2(x)
# a = n
# for i in range(1, k+1):
#     a = f(a)
# print(a)

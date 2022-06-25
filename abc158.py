# A
# s = input()
# if s[0] == s[1] and s[1] == s[2]:
#     print('No')
# else:
#     print('Yes')

# B
# n, a, b = map(int, input().split())
# t1 = n // (a + b)
# t2 = n % (a + b)
# ans = t1 * a + min(t2, a)
# print(ans)

# C
# a, b = map(int, input().split())
# for i in range(10001):
#     if int(i * 0.08) == a and int(i * 0.1) == b:
#         print(i)
#         break
# else:
#     print('-1')

# D
# from collections import deque
#
# s = input()
# q = int(input())
# reverse = False
# Q = deque(s)
# for i in range(q):
#     qi = list(map(str, input().split()))
#     if qi[0] == '1':
#         reverse = not reverse
#     if qi[0] == '2':
#         f = qi[1]
#         if reverse:
#             f = str(3 - int(f))
#         if f == '1':
#             Q.appendleft(qi[2])
#         else:
#             Q.append(qi[2])
# if reverse:
#     Q.reverse()
# print(''.join(Q))

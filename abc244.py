# A
# N = int(input())
# S = input()
# print(S[-1])

# B
# N = int(input())
# T = input()
# x, y = 0, 0
# direction = 0
# for i in range(N):
#     t = T[i]
#     if t == 'S':
#         if direction%4 == 0:
#             x += 1
#         elif direction%4 == 1:
#             y -= 1
#         elif direction%4 == 2:
#             x -= 1
#         else:
#             y += 1
#     else:
#         direction += 1
#         direction %= 4
# print(x, y)

# C
# N = int(input())
# said = [False]*(2*N+1)
# while True:
#     taka = said.index(False)
#     print(taka+1)
#     said[taka] = True
#     aoki = int(input())
#     if aoki == 0:
#         break
#     said[aoki-1] = True

# D
# S = input()
# T = input()
# s = ''
# t = ''
# for i in range(0, 5, 2):
#     if S[i] == 'R':
#         s += '0'
#     if S[i] == 'G':
#         s += '1'
#     if S[i] == 'B':
#         s += '2'
#     if T[i] == 'R':
#         t += '0'
#     if T[i] == 'G':
#         t += '1'
#     if T[i] == 'B':
#         t += '2'
# def color(m):
#     if m == '012' or m == '201' or m == '120':
#         return 0
#     else:
#         return 1
# if color(s) == color(t):
#     print('Yes')
# else:
#     print('No')
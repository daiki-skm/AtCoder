# A
# S = input()
# print('0'+S[0:3])

# B
# N = int(input())
# s, t = [], []
# for _ in range(N):
#   u, v = input().split()
#   s.append(u)
#   t.append(v)
# for i in range(N):
#   can_give_a_nickname = False
#   for S in [s[i], t[i]]:
#     s_ok = True
#     for j in range(N):
#       if i != j:
#         if S == s[j] or S == t[j]:
#           s_ok = False
#     if s_ok == True:
#       can_give_a_nickname = True
#   if can_give_a_nickname == False:
#     print("No")
#     exit()
# print("Yes")

# C
# N = int(input())
# if N == 1:
#     print(1)
#     exit()
# def S(n):
#     if n == 2:
#         return [1,2,1]
#     return S(n-1) + [n] + S(n-1)
# print(*S(N))

# D
# Q_num = int(input())
# Q = []
# for _ in range(Q_num):
#     q = list(map(int, input().split()))
#     if q[0] == 1:
#         Q.append(q[1:])
#     if q[0] == 2:
#         final = q[1]
#         ans = 0
#         while final > 0:
#             if final < Q[0][1]:
#                 ans += Q[0][0]*final
#                 Q[0][1] -= final
#                 break
#             elif final == Q[0][1]:
#                 ans += Q[0][0]*final
#                 Q.pop(0)
#                 break
#             else:
#                 ans += Q[0][0]*Q[0][1]
#                 final -= Q[0][1]
#                 Q.pop(0)
#         print(ans)

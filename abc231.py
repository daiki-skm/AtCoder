# x = int(input())
# print(x/100)

# N = int(input())
# mydict = {}
# for i in range(N):
#   Si = input()
#   if not Si in mydict.keys():
#     mydict[Si] = 1
#   else:
#     mydict[Si] += 1
# max_k = max(mydict, key=mydict.get)
# print(max_k)

# N, Q = map(int, input().split())
# AN = sorted(list(map(int, input().split())))
# ss = [int(input()) for _ in range(Q)]
# from bisect import bisect_left
# for x in ss:
#   t = bisect_left(AN, x)
#   print(len(AN)-t)
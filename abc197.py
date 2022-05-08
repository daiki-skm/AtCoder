# A
# s = input()
# print(s[1:]+s[0])

# B
# h, w, x, y = map(int, input().split())
# x -= 1
# y -= 1
# mass = []
# for _ in range(h):
#     s = input()
#     mass.append(s)
# di = [-1, 0, 1, 0]
# dj = [0, -1, 0, 1]
# ans = 1
# for i in range(4):
#     ni = x
#     nj = y
#     while True:
#         ni += di[i]
#         nj += dj[i]
#         if ni < 0 or ni >= h or nj < 0 or nj >= w:
#             break
#         if mass[ni][nj] == '#':
#             break
#         ans += 1
# print(ans)

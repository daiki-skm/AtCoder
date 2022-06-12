# A
# n = input()
# hon = ['2', '4', '5', '7', '9']
# pon = ['0', '1', '6', '8']
# bon = ['3']
# if n[-1] in hon:
#     print('hon')
# elif n[-1] in pon:
#     print('pon')
# elif n[-1] in bon:
#     print('bon')

# B
# k = int(input())
# s = input()
# if len(s) <= k:
#     print(s)
# else:
#     print(s[:k] + '...')

# C
# from math import pi, sin, cos
#
# a, b, h, m = map(int, input().split())
# th = (h * 60 + m) / 720 * 2 * pi
# tm = m / 60 * 2 * pi
# xh = a * cos(th)
# yh = a * sin(th)
# xm = b * cos(tm)
# ym = b * sin(tm)
# dx = xh - xm
# dy = yh - ym
# ans = (dx ** 2 + dy ** 2) ** 0.5
# print(ans)

# A
# s = input()
# if s[-1] != 's':
#     print(s + 's')
# else:
#     print(s + 'es')

# B
# n = int(input())
# ans = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     if a == b:
#         ans += 1
#     else:
#         ans = 0
#     if ans == 3:
#         print('Yes')
#         exit()
# print('No')

# C
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += (n - 1) // i
print(ans)

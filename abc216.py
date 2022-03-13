# X, Y = map(int, input().split('.'))
# if 0 <= Y and Y <= 2:
#     print('{}-'.format(X))
# elif 3 <= Y and Y <= 6:
#     print('{}'.format(X))
# elif 7 <= Y and Y <= 9:
#     print('{}+'.format(X))

# N = int(input())
# arr = [input() for _ in range(N)]
# dict = {}
# for i in range(N):
#     if arr[i] in dict:
#         dict[arr[i]] += 1
#     else:
#         dict[arr[i]] = 1
# for i in dict.values():
#     if i > 1:
#         print('Yes')
#         exit()
# print('No')

N = int(input())
ans = []
while True:
    if N % 2 == 0:
        N //= 2
        ans.insert(0, 'B')
    else:
        N -= 1
        ans.insert(0, 'A')
    if N == 0:
        break
print(''.join(ans))
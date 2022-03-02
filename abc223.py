# X = int(input())
# if X != 0 and X%100 == 0:
#     print('Yes')
# else:
#     print('No')

# S = input()
# arr = []
# for i in range(len(S)):
#     arr.append(S[i:]+S[:i])
# arr.sort()
# print(arr[0])
# print(arr[-1])

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
sum_time = 0
for i in range(N):
    sum_time += AB[i][0]/AB[i][1]
sum_time /= 2
ans = 0
for i in range(N):
    if AB[i][0]/AB[i][1] <= sum_time:
        ans += AB[i][0]
        sum_time -= AB[i][0]/AB[i][1]
    else:
        ans += AB[i][1]*sum_time
        break
print(ans)

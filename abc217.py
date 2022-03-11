# S, T = input().split()
# arr = [S, T]
# arr.sort()
# if arr[0] == S:
#     print('Yes')
# else:
#     print('No')

# S1 = input()
# S2 = input()
# S3 = input()
# input = [S1, S2, S3]
# arr = ['ABC', 'ARC', 'AGC', 'AHC']
# for i in input:
#     arr.remove(i)
# print(arr[0])

N = int(input())
p = list(map(int, input().split()))
ans = [0]*N
for i in range(1, N+1):
    ans[p[i-1]-1] = i
print(*ans)
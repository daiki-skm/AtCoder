# x = str(input())
# if int(x[-3]) >= 5:
#     print(int(float(x))+1)
# else:
#     print(int(float(x)))


N = int(input())
ans = []
for i in range(N):
    L = list(input().split())
    print(L)
    ans.append(str(L[1:]))
print(ans)
print(set(ans))
print(len(set(ans)))
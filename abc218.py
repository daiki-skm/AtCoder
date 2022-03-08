# N = int(input())
# S = input()
# if S[N-1] == 'o':
#     print('Yes')
# else:
#     print('No')

# P = list(map(int, input().split()))
# ans = [chr(i+96) for i in P]
# print(''.join(ans))

N = int(input())
data = set()
for i in range(N):
    t = tuple(map(int, input().split()))
    data.add(t)
ans = 0
for p in data:
    for q in data:
        if ((p[0], q[1]) in data) and ((q[0], p[1]) in data) and p[0] != q[0] and p[1] != q[1]:
            ans += 1
            # print(p,q)
print(ans//4)
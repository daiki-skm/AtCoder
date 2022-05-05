# A
# a = list(map(int, input().split()))
# a.sort()
# if (a[2] - a[1]) == (a[1] - a[0]):
#     print("Yes")
# else:
#     print("No")

# B
# from collections import defaultdict
# N = int(input())
# st = defaultdict(int)
# for i in range(N):
#     s, t = map(str, input().split())
#     st[s] = int(t)
# st = sorted(st.items(), key=lambda kv: kv[1], reverse=True)
# print(st[1][0])

# C
from collections import defaultdict
s = input()
ans = 0
for i in range(10000):
    a = defaultdict(int)
    x = i
    for _ in range(4):
        d = x%10
        a[d] = 1
        x = x//10
    ok = True
    for k in range(10):
        if s[k] == 'o' and a[k] != 1:
            ok = False
            break
        if s[k] == 'x' and a[k] != 0:
            ok = False
            break
    if ok:
        ans += 1
print(ans)

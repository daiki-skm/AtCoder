# S = list(input())
# if S[0] == S[1] and S[1] == S[2] and S[0] == S[2]:
#     print(1)
# elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
#     print(6)
# else:
#     print(3)

# N = int(input())
# ab = [list(map(int, input().split())) for _ in range(N-1)]
# dict = {}
# for a, b in ab:
#     if a in dict:
#         dict[a].append(b)
#     else:
#         dict[a] = [b]
#     if b in dict:
#         dict[b].append(a)
#     else:
#         dict[b] = [a]
# # print(dict)
# max_kv_list = [len(kv[1]) for kv in dict.items()]
# if max(max_kv_list) == N-1:
#     print('Yes')
# else:
#     print('No')

# N = int(input())
# counter = [0]*(N+1)
# for i in range(N-1):
#   a,b = map(int,input().split())
#   counter[a] += 1
#   counter[b] += 1
# if N-1 in counter:
#   print("Yes")
# else:
#   print("No")

# N, M = map(int, input().split())
# B = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N-1):
#     if B[i+1][0] != B[i][0]+7:
#         print("No")
#         exit()
# for i in range(M-1):
#     if B[0][i]%7 == 0:
#         print("No")
#         exit()
# for i in range(N):
#     for j in range(M-1):
#         if B[i][j+1] - B[i][j] != 1:
#             print('No')
#             exit()
# print('Yes')

N, Q = map(int,input().split())
q = [list(map(int,input().split())) for _ in range(Q)]
linked=[[-1]*2 for _ in range(N)]
def query1(x0,y0):
    x,y=(x0-1),(y0-1)
    linked[x][1]=y
    linked[y][0]=x
def query2(x0,y0):
    x,y=(x0-1),(y0-1)
    linked[x][1]=-1
    linked[y][0]=-1
def query3(x0):
    x=x0-1
    here=x
    while linked[here][0]!=-1:
        here=linked[here][0]
        # print('-----1-----', here)
    output=[1,here+1]
    while linked[here][1]!=-1:
        output[0]+=1
        here=linked[here][1]
        # print('-----2-----', here)
        output.append(here+1)
    output0=" ".join(map(str,output))
    print(output0)
def query(q0):
    if q0[0]==1:
        query1(q0[1],q0[2])
    if q0[0]==2:
        query2(q0[1],q0[2])
    if q0[0]==3:
        query3(q0[1])
for i in range(Q):
    query(q[i])

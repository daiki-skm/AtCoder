# S = input()
# print(int(S[0])*int(S[2]))

S = input()
T = input()
diff = (26 - (ord(S[0]) - ord(T[0]))) % 26
for i in range(len(S)):
    if chr((ord(S[i]) - ord("a") + diff)%26 + ord("a")) == T[i]:
        continue
    else:
        print("No")
        exit()
print("Yes")

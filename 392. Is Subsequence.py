s,t = "b","abc"
j=0

if len(s)==0:
    print(True)

for i in range(len(s)):
    if s[j]==t[i]:
        j+=1

print(j==len(s))

s,t = "b","abc"
j=0

if len(s)==0:
    print(True)

for i in range(len(s)):
    if s[j]==t[i]:
        j+=1
    if j==len(s):
        print(True)
        break

print(False)


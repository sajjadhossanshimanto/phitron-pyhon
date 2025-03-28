# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S
s = input()

ans = []
l_count = 0
r_count = 0
l = 0
for r in range(len(s)):
    char = s[r]
    if char=="L":
        l_count+=1
    elif char=="R":
        r_count+=1
    
    if l_count==r_count:
        ans.append(s[l:r+1])
        l = r+1

print(len(ans))
for i in ans:
    print(i)
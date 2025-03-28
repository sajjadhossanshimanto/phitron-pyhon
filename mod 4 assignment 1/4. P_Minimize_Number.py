# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

n = int(input())
nums = list(map(int, input().split()))

op = 0
while all(i&1==0 for i in nums):
    for i in range(n):
        nums[i] = nums[i]//2
    op += 1

print(op)
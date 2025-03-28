# https://atcoder.jp/contests/arc087/tasks/arc087_a
from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

op = 0
freq = Counter(nums)
for k, v in freq.items():
    if v>k:
        op+=v-k
    elif v<k:
        op+=v

print(op)
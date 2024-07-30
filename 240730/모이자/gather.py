import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

max_sum = INT_MAX

for i in range(n):
    sum_diff = 0

    for j in range(n):
        sum_diff += abs(j-i) * arr[j]

    max_sum = min(max_sum,sum_diff)

print(max_sum)
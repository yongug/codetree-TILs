n, s = list(map(int, input().split() ))

num = list(map(int,input().split()))

ans = 100001

for i in range(0,n):
    sum_val = 0
    for j in range(i,n):
        sum_val += num[j]

        if sum_val >= s:
            break
        
        ans = min(ans,j-i+2)

print(ans)
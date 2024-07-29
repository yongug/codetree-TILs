n, s = list(map(int, input().split() ))
#print(n,s)
num = list(map(int,input().split()))
num.insert(0,0)
#print(num)
ans = 1000000

for i in range(1,n+1):
    sum_val = 0
    for j in range(i,n+1):
        sum_val += num[j]

        if sum_val >= s or (j-i+1) > ans:
            break
        
    if sum_val >=s:
        ans = min(ans,j-i+1)

if ans == 100001:
    print(-1)
else:
    print(ans)
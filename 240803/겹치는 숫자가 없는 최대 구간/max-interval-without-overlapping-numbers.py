n = int(input())
arr = list(map(int,input().split()))

count_array = [0] *100010


ans = 0
j = 0

for i in range(0,n):
    while j<n and count_array[arr[j]] <1:
        count_array[arr[j]] +=1
        j +=1

    ans = max(ans,j-i)

    count_array[arr[i]] -=1


print(ans)
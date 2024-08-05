n = int(input())

arr = list(map(int,input().split()))

sorted = False
while(sorted == False):
    sorted = True
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            sorted= False
    
for i in range(len(arr)):
    print(arr[i],end=' ')
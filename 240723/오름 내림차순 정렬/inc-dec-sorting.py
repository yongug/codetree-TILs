def solution(n,arr):
    arr.sort()
    for i in range(len(arr)):
        print(arr[i], end="")
        print(' ',end="")
    print('')

    arr.sort(reverse=True)
    for i in range(len(arr)):
        print(arr[i], end="")
        print(' ',end="")
    print('')

n = int(input())
arr = list(map(int,input().split()))

solution(n,arr)
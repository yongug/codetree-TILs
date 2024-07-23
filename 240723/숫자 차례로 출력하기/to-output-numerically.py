def printNumAsc(n):
    if n ==0:
        return
    
    printNumAsc(n-1)
    print(n, end="")
    print(' ',end="")

def printNumDesc(n):
    if n ==0:
        return
    
    print(n,end="")
    print(' ',end="")
    printNumDesc(n-1)


N = int(input())

printNumAsc(N)
print()
printNumDesc(N)
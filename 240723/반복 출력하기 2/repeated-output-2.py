def printRecursive(n):
    if n==0:
        return

    printRecursive(n-1)
    print("HelloWorld")

N = int(input())
printRecursive(N)
def printMin(a,b,c):
    min = a
    if(min>b):
        min = b
    if(min>c):
        min = c
    
    print(min)

a,b,c = map(int,input().split())

printMin(a,b,c)
def print_NN_squares(n):
    i = 1
    for _ in range(n):
        for _ in range(n):
            if i==10:
                i = 1
            print(i,end="")
            print(' ',end="")
            i +=1
            
        print()

N = int(input())
print_NN_squares(N)
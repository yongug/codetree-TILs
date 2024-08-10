n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))


def get_num_of_coin(row,col):
    num_of_coin = 0

    for i in range(row,row+3):
        for j in range(col,col+3):
            num_of_coin += arr[i][j]
    
    return num_of_coin


max_coin = 0

for row in range(n):
    for col in range(n):

        if col + 2 >= n:
            continue
        if row + 2 >= n:
            continue
        
        num_of_coin = get_num_of_coin(row,col)


        max_coin = max(max_coin,num_of_coin)

print(max_coin)
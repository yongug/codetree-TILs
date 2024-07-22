def print_n_m_Lines(n,m):
    for _ in range(n):
        print("1"*m)

row_num, col_num = tuple(map(int,input().split()))
print_n_m_Lines(row_num,col_num)
def is_magic_number(n):
    flag = 0
    
    while(n%10 >0):
        k = n%10
        
        if k == 3 or k == 6 or k == 9:
            flag = 1
        n = n//10
        
    return flag

def is_three_mul(n):
    return n%3 ==0


a,b = list(map(int,input().split()))

cnt = 0

for i in range(a,b+1):
    if is_magic_number(i) or is_three_mul(i):
        cnt +=1

print(cnt)
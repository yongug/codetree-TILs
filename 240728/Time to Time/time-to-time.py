a,b,c,d = list(map(int,input().split()))
elapsed_time = 0

elapsed_time = (c*60+d) - (a*60+b)

# while True:
#     if a == c and b == d:
#         break
    
#     elapsed_time += 1
#     b += 1

#     if b == 60:
#         a += 1
#         b = 0

print(elapsed_time)
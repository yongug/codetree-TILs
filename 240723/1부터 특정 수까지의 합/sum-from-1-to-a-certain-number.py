def solution(n):
    result = 0
    for i in range(1,n+1):
        result +=i
    
    result /= 10
    return int(result)

N = int(input())
print(solution(N))
import sys
sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n+1) ]
visited = [False] * (n+1)
parent= [0] * (n+1)


for _ in range(n-1):
    x, y = tuple(map(int,input().split()))
    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)

def traversal(x):
    # 노드 x에 연결된 간선을 살펴본다.
    for y in edges[x]:

        if not visited[y]:
            visited[y] = True
            parent[y] = x

            traversal(y)


#1번부터 트리 순회 진행
visited[1] = True
traversal(1)

for i in range(2,n+1):
    print(parent[i])
'''
입력
지도의 크기 N (정사각형)
N줄에는 N개의 자료

출력
총단지수
각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩
'''

from collections import deque

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))

answer=[]

dx=[-1,1,0,0] 
dy=[0,0,-1,1]

def bfs(graph,x,y):
        
    
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    cnt=1
    while queue:

        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                cnt+=1

    return cnt

    
answer=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            answer.append(bfs(graph,i,j))
            
            
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])

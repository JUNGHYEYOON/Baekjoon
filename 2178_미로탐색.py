from collections import deque

n,m=map(int,input().split())
graph=[]


for _ in range(n):
    graph.append(list(map(int, input())))

    
def bfs(x,y):
    #이동할 네가지 방향 정의(상,하,좌,우)
    
    #deque생성
    queue=deque()
    queue.append((x,y)) #현재위치를 추가
    
    while queue:
        x,y=queue.popleft()
        print('x,y',x,y)
        #현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4): 
            nx=x+dx[i]
            ny=y+dy[i]
            
            #위치가 벗어남
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            #벽인 경우는 무시
            if graph[nx][ny]==0:
                continue
            
            #벽이 아니므로 이동
            #해당 노드를 처음 방문하는 경우일 때 최단 거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny]=graph[x][y]+1
                #print('nx,ny',nx,ny)
                queue.append((nx,ny))   
                #print('graph[nx][ny]',graph[nx][ny])
                
 
    #print(graph[n-1][m-1])
    return graph[n-1][m-1]



    
dx=[-1,1,0,0] 
dy=[0,0,-1,1]
    
print(bfs(0,0))

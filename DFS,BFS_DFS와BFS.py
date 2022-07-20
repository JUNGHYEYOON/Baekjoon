'''
N: 정점의 개수
M: 간선의 개수
V: 탐색을 시작할 정점의 번호

출력
DFS 출력 결과
BFS 출력 결과
'''
import sys
from collections import deque


n,m,v=map(int,input().split())
visited=[False]*(n+1)
#m이 아닌 n+1인 이유는 각 정점에 간선으로 연결된 정점 넣기 위해
#n(정점)이 1부터 시작하기 때문
graph=[[] for _ in range(n+1)]



for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    

for i in range(len(graph)):
    graph[i].sort()
#print(graph)


def DFS(start):
    print(start,end=' ') #end='': 한줄에 여러개 출력
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
            visited[i]=True
            
            
def BFS(start):
    queue=deque([start])
    visited[start]=True
    
    while queue:
        now=queue.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
DFS(v)
visited=[False]*(n+1)
print()
BFS(v)

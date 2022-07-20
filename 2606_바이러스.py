'''
입력
컴퓨터 수
컴퓨터 쌍의 수

출력
웜 바이러스에 걸리게 되는 컴퓨터의 수
'''

num=int(input())
pair=int(input())


visited=[False]*(num+1)
graph=[[] for _ in range(num+1)]

for i in range(pair):
    p1,p2=map(int,input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
    

for i in range(len(graph)):
    graph[i].sort()
#print(graph)

answer=[]
def DFS(start):
    #print(start)
    answer.append(start)
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
    ans=len(answer)-1        
    return ans      
print(DFS(1))

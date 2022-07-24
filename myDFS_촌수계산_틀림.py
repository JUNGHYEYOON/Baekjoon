'''
입력
전체 사람의 수 n
촌수를 계산해야 하는 서로 다른 두 사람의 번호
부모 자식들간의 관계의 개수 m
부모 자식간의 관계를 나타내는 두 번호 x,y->x는 y의 부모 번호


출력
요구한 두 사람의 촌수를 나타내는 정수 
'''

n=int(input())
f1,f2=map(int,input().split())
m=int(input())

visited=[False]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    #graph[y].append(x)

print(graph)

answer=[]


global cnt
cnt=1

def DFS(graph,f1,f2):
    global cnt
    answer.append(f1)
    
    visited[f1]=True
    
    for i in range(len(graph)):
        if f1 in graph[i]:
            if f2 == i:
                print('f2==i')
                cnt=cnt
            elif f2 in graph[i]:
                print('f2 in graph[i]',f2,graph[i])
                print('cnt+1',cnt+1)
                cnt=cnt+1
            else:
                print('f1,graph[i]',f1,graph[i])
                cnt+=1
                print('cnt',cnt)
                DFS(graph,i,f2)
    print(f1,f2)
    ''' 
    -1처리하지 못함.
    if visited[f1] == True:
        if f2 not in graph[f1]:
            return -1          
                
    return cnt             
    '''            

print(DFS(graph,f1,f2))


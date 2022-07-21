from collections import deque

N,K=map(int,input().split())
MAX=10**5
answer=[0]*(MAX+1)

def BFS(x):
    queue=deque()
    queue.append(x)
    
    while queue:
        x=queue.popleft()
        
        if x == K:
            return answer[x]
            
        for i in (x-1,x+1,x*2):
            #주어진 범위 내에 존재
            '''
            not answer[i] 이부분이 어려웠는데,
            answer[i]=0 이고 이건 무조건 FALSE니까
            if문을 무조건 만족
            
            만약 x-1 -> x+1 수행하면 x그대로니까 그냥 실행 안해도 되는것.
            (이미 수행) -> 아마 이부분은 DFS에서 구현을 못해서 런타임 오류나는듯.
            '''
            if 0<=i<=MAX and not answer[i]:
               answer[i]=answer[x]+1
               queue.append(i)

print(BFS(N))

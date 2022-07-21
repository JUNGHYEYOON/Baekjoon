'''
입력
수빈 위치:N 동생 위치: K

출력
동생을 찾는 가장 빠른 시간
'''


'''
중요한 거 배웠는데 빠른 시간이라고 적혀있으면 BFS로 풀어야함.
내가 만든 코드 큰 수 넣으면 전혀 돌지 않음.
100 0 # 100
15964 89498 # 4781
100 1 # 99
100000 100000 # 0
0 100000 # 22
100000 0 # 100000
3482 45592 # 637
'''

N,K=map(int,input().split())

ans=[]

if K>=N:
    ans.append(K-N)
else:
    ans.append(N-K)


def DFS(x,answer):

    
    #print('x',x,answer,min(ans))
    
    if answer > min(ans):
        return 
    
    if x==K and answer<min(ans):
        ans.append(answer)
        
    else:
        return DFS(x+1,answer+1),DFS(x-1,answer+1),DFS(2*x,answer+1)
   
DFS(N,0)
print(min(ans))




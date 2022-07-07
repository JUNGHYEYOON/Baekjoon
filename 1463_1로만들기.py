'''
N
-> 3으로 나누어 떨어지면 3으로 나눔, 몫
-> 2로 나누어 떨어지면 2로 나눔, 몫
-> 1을 뺌

=> 1이 되게

출력: 횟수의 최소
'''

'''
1 -> 0
2 -> 1빼기 1
3 -> 3나누기 1
4 -> 2나누기 + dp(2) 2
5 -> 1빼기 N(4) 3
6 -> 2나누기+N(3) 2
7 -> 1+N(6) 3
8 

10-> /2하거나 -1중 작은거 1+N(9)
'''

N=int(input())
dp= [0] * 1000001


for i in range(2,N+1):
    if (i%3==0) and (i%2==0):
        dp[i]=1+min(dp[int(i/3)],dp[int(i/2)],dp[i-1])
    elif i % 3 == 0:
        dp[i]=1+min(dp[int(i/3)],dp[i-1])
    elif i % 2 ==0:
        dp[i]=1+min(dp[int(i/2)],dp[i-1])
    else:
        dp[i]=1+dp[i-1]
    
print(dp[N])   
#solution(3)

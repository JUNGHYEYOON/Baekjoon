'''
피보나치 수
N: N번째 피보나치 수 구하기
T: 테스트 케이스 개수
출력: 0이랑 1 몇번 출력되는지 찾아내기
'''


'''
피보나치 수 구하기 => ex) fibo(6)=fibo(5)+fibo(4)
fibo(0) => 1 0
fibo(1) => 0 1
fibo(2) => fibo(1) fibo(0) => 1 1
fibo(3) => fibo(2) fibo(1) => 1 2
fibo(4) => fibo(3) fibo(2) => 2 3
fibo(5) => fibo(4) fibo(3) => 3 5
fibo(6) => fibo(5) fibo(4) => 5 8
'''


T=int(input())
answer=[]
for i in range(T):
    N=int(input())
    dp=[[0,0]] * 41
    dp[0] = [1,0]
    dp[1] = [0,1]
    
    for j in range(2,N+1):
        dp[j]=[(dp[j-1][0]+dp[j-2][0]),(dp[j-1][1]+dp[j-2][1])]
        
        #print('dp[j]',dp[j])
    answer.append(dp[N])
for i in range(len(answer)):
    print(answer[i][0],answer[i][1])
    
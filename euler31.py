## Q31
## 영국 동전으로 2파운드 만드는 가지 수
## 기본적인 개념은 만들 수 있는 가장 큰 동전을 하나씩 줄여가면서 재귀함수를 쓰는 것이다.
## 예를 들어 10파운드를 만든다고 하면
## 10파운드 동전 하나, 다음은 5파운드 동전 둘, 다음 5파운드 동전 하나 2파운드 동전 둘 1파운드 하나
## 이런 식으로 하나씩 큰 동전을 줄여가면서 다시 잔돈에 대해 동전을 쌓는 방식이다.

coin = [1,2,5,10,20,50,100,200]

## 만들 수 있는 가장 큰 동전 구하는 함수
def coin_pocket(target):
    if target >= coin[-1]:          ## 200파운드가 넘어가면
        index = len(coin)-1
        return index                ## 바로 200파운드 index 리턴
    index = 0
    while True:
        if coin[index] >= target:   ## target한 돈이 coin을 넘어가면
            break
        index += 1
    return index                    ## 최대 동전의 index 반환

cnt = 0

def coin_maker(r,n):                            ## r은 잔돈, n은 coin의 index
    global cnt                                  ## cnt할 수
    if n == 0:                                  ## 1파운드까지 가면
        cnt += 1                                ## cnt += 1
    else:
        for i in range(r//coin[n], -1, -1):     ## 잔돈에 가장 큰 코인의 개수에 대해
            remainder = r - (coin[n] * i)       ## 코인 뺀 잔돈
            if remainder == 0:                  ## 0이면 cnt += 1
                cnt += 1
            else:                               ## 0이 아니면 재귀함수
                coin_maker(remainder, n-1)

idx = coin_pocket(200)
coin_maker(200,idx)
print(cnt)              ## 73682

## thread에서 찾은 최적화된 방법
## 1파운드씩 늘어갈수록 각각의 target에 대한 동전의 요구가 달라진다.
## 1파운드는 언제나 필요할 것이고, 2파운드는 잔돈으로 2파운드가 남았을 때, 5파운드는 5파운드가 잔돈으로 남았을 때 필요할 것이다.
## 이를 index에서 step으로 표현하여 가지 수를 표현할 수 있다.

coin = [2,5,10,20,50,100,200]
def coins(cash):
    N = cash + 1
    K = [1] * N                                 ## target 금액에 대해 target+1만큼의 1을 생성한다. 이는 1파운드에 대한 요구이다.
    for i in coin:
        K = [sum(K[j::-i]) for j in range(N)]   ## 동전의 크기에 대해 하나씩 늘려준다.
    return K[-1]                                ## 마지막 200파운드로 늘려간 동전 가지 수를 반환
print(coins(200))       ## 73682

## 아직 많이 공부가 필요하다.
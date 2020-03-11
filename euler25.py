## Q25
## fibonacci 수열에서 처음으로 길이가 1000이 넘는 수가 나타나는 index
## 그냥 함수를 돌리면 당연하게도 과부하걸려서 안돌아간다.
## 그래서 이전에 def 공부하면서 익혔던 memoize를 활용할 것이다.

start = time.time()


def memoize(f):                 ## memoize할 함수를 만듦. 인자는 function을 받을 예정
    memo = defaultdict()        ## dictionary를 만들어준다.

    def helper(x):              ## helper라는 함수 안에는
        if x not in memo:       ## 만약 memo dictionary에 그 값이 없으면
            memo[x] = f(x)      ## 기억해줌

        return memo[x]          ## memo dictionary를 return

    return helper               ## helper 함수를 return


def fibo(n):                    ## 익히 알고있는 fibonacci 수열 함수를 만든다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


fibo = memoize(fibo)            ## 이 fibonacci 수열 함수를 memoize함수에 넣어 지정해준다.

length = 0
n = 0
while length < 1000:            ## 1000이 넘어가면 그만
    n += 1
    length = len(str(fibo(n)))

end = time.time() - start
print(n, end)                   ## 4782 0.03153085708618164초

## 또는 그냥 굳이 함수를 만들지 않고 dictionary에 바로 넣어서 만들어줘도 된다.

start = time.time()
fibo2 = defaultdict()           ## fibo2라는 dictionary를 만든다. 이 dictionary에는 피보나치 수열이 들어갈 것이다.
fibo2[1] = 1
fibo2[2] = 1

n = 2
while len(str(fibo2[n])) < 1000:            ## 길이가 1000이 넘어가면 그만
    n += 1
    fibo2[n] = fibo2[n-1] + fibo2[n-2]      ## 이 전의 수와 이 전전의 수를 합하여 만들어준다.
end = time.time() - start
print(n, end)                   ## 4782 0.029958009719848633초 속도는 거의 동일
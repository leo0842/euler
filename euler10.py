## Q10
## find summation of all the primes below 2m
## 10 - 1
def sum_of_prime(n):
    prime = [2]                         ## 소수를 넣을 배열을 만든다.
    for is_prime in range(3, n + 1):    ## 3부터 n까지 소수를 확인할 예정
        prime_check = True              ## 먼저 prime_check 변수에 True를 넣어준다.
        for j in prime:                 ## 소수인지 확인할 수를 해당 수 이하의 소수들로 하나씩 나눠본다.
            if is_prime % j == 0:       ## 나눠지면
                prime_check = False     ## prime_check 변수에 False를 넣음
                break                   ## 나눠지면 break
        if prime_check:                 ## prime_check가 어떤 소수로도 나눠지지 않았으면
            prime.append(is_prime)      ## 소수 배열에 넣는다
    return sum(prime), len(prime)

## 200만 넣으니까 컴퓨터가 소리질러서 20만을 넣어봤다. 그리고 시간도 재보았다.
import time
start = time.time()
a = sum_of_prime(200000)
end = time.time()-start
print(end)
a                                       ## 9.044475078582764초가 나온다. 다른 방법을 강구해야한당.

## 10 - 2
## 하루가 지났다. 도저히 떠오르지 않아서 찾아보았다.
start = time.time()
def is_prime(num):
    prime = True
    for i in range(2,int(num**0.5)+1):  ## 새로 알게 되었다. 해당 수를 루트 씌운 수에서 1을 더한 수 까지 나눠지는 수가 없으면 그 수는 소수이다.
                                        ## 위의 방법으로 반복문을 돌리는 범위를 대폭 줄일 수 있었다.
        if num % i == 0:
            prime = False
            break
    return prime
sum_prime = 0
for i in range(2,2000000):
    if is_prime(i):
        sum_prime += i
print("sum: ",sum_prime)

elapsed = (time.time() - start)         ## 200만을 돌렸을 때 11.4629487991333초가 나왔다.
print("This code took: " + str(elapsed) + " seconds")

## 그런데 굳이 루트 씌운 수 이하의 모든 수를 나눌 필요가 없다. 불만이었다. 그래서 내가 처음 만들었던 함수를 결합하였다.
## 10 - 3
def sum_of_prime1(n):
    prime = [2]
    prime_sqrt = [2]                    ## 루트 씌운 수만 돌릴 배열을 따로 만든다.
    for is_prime in range(3, n + 1):
        prime_check = True
        for j in prime_sqrt:            ## 모든 소수가 아닌 prime_sqrt만큼만 돌릴 것이다.
            if is_prime % j == 0:
                prime_check = False
                break                   ## 개념은 위와 같다.
        if prime_check:
            prime.append(is_prime)
            if prime_sqrt[-1] <= int(is_prime**0.5)+1:                      ## 해당 수에 루트 씌우고 1을 더한 수가 prime_sqrt보다 크면
                prime_sqrt.append(prime[prime.index(prime_sqrt[-1])+1])     ## prime 배열에서 찾아와 그 다음 소수를 sqrt배열에 붙인다.
    return sum(prime), len(prime)

start = time.time()
primt(sum_of_prime1(2000000))
end = time.time() - start
print(end)                              ## 1.8267602920532227초가 나왔다.

## 10 - 4
## 에라토스테네스의 체를 이용한 방법이다.

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

## 내가 시도해보았던 에라토스테네스의 체는 너무 오래 걸려서 포기했었다. 그런데 새로운 방법이다. 이해는 하지 못했당,,ㅎ
start = time.time()
print(sum(rwh_primes1(2000000)))
end = time.time() - start
print(end) ## 0.11496090888977051초. 소수는 에라토스테네스.
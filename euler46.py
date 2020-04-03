## Q46
## 골드바흐는 모든 홀수인 합성수는 소수 + (2 * 제곱수)로 표현할 수 있다고 주장했지만 잘못되었음이 증명되었다.
## 골드바흐의 추측으로 나타낼 수 없는 가장 작은 홀수 합성수는?
## 기본 개념은 소수와 홀수 리스트를 limit까지 만들어내고 for문을 돌려 홀수 리스트에서 만들어낸 합성수를 없앤다.
## 남은 홀수 리스트가 없다면 리미트를 늘려서 계속 확인한다.
## 리미트를 추측하기 어려워 애를 좀 먹었다..

import time

start = time.time()

def primes(n):                                      ## n까지 소수 리스트를 만들어내는 함수
    num = 3
    prime_list = []
    while num < n:
        TF = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                TF = False
                break
        if TF:
            prime_list.append(num)
        num += 1

    return prime_list


def odd(n):                                         ## n까지 홀수 리스트를 만들어내는 함수 수가 많아서 set()으로 모았다.
    odd_set = set()
    num = 1
    while num < n:
        num += 2
        odd_set.add(num)

    return odd_set


def goldbach_conj(limit):                           ## limit까지 할 예정
    conjecture_remaining = odd(limit)               ## limit내의 모든 홀수를 대상으로, 없앨 합성수 리스트를 만들어낸다.

    for i in primes(limit):                         ## limit내의 소수가 차례대로 들어간다.

        if i in conjecture_remaining:               ## 리스트에 이 소수가 있으면
            conjecture_remaining.remove(i)          ## 일단 먼저 지워준다.

        for j in range(1, int(limit ** 0.5) + 1):   ## limit까지 만들었기 때문에 제곱수가 들어갈 거니까 root limit까지 확인

            conjecture = i + 2 * (j ** 2)           ## 공식대로 넣고

            if conjecture in conjecture_remaining:  ## 리스트에 만들어낸 합성수가 있으면
                conjecture_remaining.remove(conjecture) ## remove

    return conjecture_remaining                     ## 모든 과정을 거치면 limit내에 만들지 못한 홀수 합성수를 return


n = 1
while True:
    limit = 10 ** n                                 ## 10부터 제곱승으로 limit를 생산
    if goldbach_conj(limit):                        ## 미처 만들어내지 못한 홀수 합성수가 있다면
        print(min(goldbach_conj(limit)))            ## print
        break
    else:
        n += 1

end = time.time() - start

print(end, "seconds")

## 5777
## 0.1429896354675293 seconds
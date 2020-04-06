## Q49
## 1487, 4817, 8147은 3330씩 늘어나는 등차수열.
## 두 가지 특징: 1. 세 수 모두 소수 2. 서로 자리를 바꿔 만들 수 있는 순열
## 네 자리 소수중 위와 같은 특징을 가진 수열이 하나 더 존재
## 처음에는 4자리 permutation을 만들고 하나씩 자리를 바꿔가면서 소수인지 찾고 3개 이상 모이면 공차를 확인하여 둘 이상 같으면 print하게 하였다.
## 예시로 나타난 수열밖에 나오지 않았다.
## 계속 생각해봐도 떠오르지 않아서 구글링을 하였다.
## 보니 중복을 허용하는 순열이었다.
## 그래서 네 자리 소수를 먼저 찾고 각각 수를 4자리 permutation하고 소수인지 확인 후 3개 이상 모이면 조합으로 3개를 뽑아 공차를 확인하는 방식이다.
## 참조: https://bety.tistory.com/72

from itertools import permutations as P, combinations as C

def primes(n):                                                              ## n자리 소수 생성하는 함수
    prime_list = []
    for i in range(10 ** (n - 1), 10 ** n):
        TF = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                TF = False
                break
        if TF:
            prime_list.append(i)

    return prime_list


prime_list = primes(4)                                                      ## 네 자리 소수 생성

while prime_list:                                                           ## 방식이 독특. 하나씩 대상으로 하면서 지워감

    p = prime_list[0]                                                       ## 리스트의 첫 번째 소수

    # Find permutation
    p_permu = map(lambda x: int(''.join(x)), P(str(p), 4))                  ## 첫 번째 소수를 permutations함
    p_permu = list(set(filter(lambda x: x in prime_list, p_permu)))         ## 소수인지 확인
    p_permu.sort()

    if not p_permu or len(p_permu) <= 2:                                    ## 없거나 두개 이하면
        prime_list.pop(0)                                                   ## 그 소수 리스트에서 지워버리고 다음
        continue

    prime_list = list(filter(lambda x: x not in p_permu, prime_list))       ## 아니면 우선 세 개 이상인 소수를 리스트에서 지워줌

    # Check if the permutation fits the condition
    for numbers in list(C(p_permu, 3)):                                     ## 3개씩 뽑아서 공차 확인
        if numbers[2] - numbers[1] == numbers[1] - numbers[0]:              ## 공차가 같으면
            print(numbers)                                                  ## print

## (1487, 4817, 8147)
## (2969, 6299, 9629)

## while 돌리는 방식이 인상적.
## 조합과 순열 코딩도 매우 깔끔하다.. 배울 점이 많다.


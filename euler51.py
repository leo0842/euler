## Q51
## 56**3 은 *을 0~9로 한 번씩 대체했을 때 7개의 소수를 가진다. 56003, 56113, 56333, 56443, 56663, 56773, 56993
## 이와 같이 0~9까지 대체를 할 때 8개의 소수를 가지는 수의 첫 번째 소수는?
## 먼저 n자리 수를 만들고 고정할 수와 *의 수를 하나씩 늘려간다. 예를들어 5자리 수를 만들고 *의 개수가 2개, 고정할 수는 3개이다.
## 없으면 *의 수를 하나씩 늘리고 *의 수가 n개가 되면 자리 수를 하나 늘리고 *을 1개부터 다시 시작.
## 고정할 수는 중복을 허용하여 조합을 만들어낸다. 고정할 수와 *은 O, X로 표현하여 만들었다.

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


from itertools import permutations as P, combinations as C, product
import time

start = time.time()
digit = 2                                                               ## n자리 수
replaces = 1                                                            ## *의 수
while True:
    find = False
    OX = ["o"] * (digit - replaces) + ["x"] * replaces                  ## 개수만큼 OX를 만든다. 위의 예를 들면 O 3개 X 2개
    number_list = list(range(10))                                       ## 0~9 수 리스트
    generator = []                                                      ## OX 수열을 만들 리스트

    for i in set(P(OX)):                                                ## permutation으로 만들어내고 set으로 중복을 제거
        generator.append(list(i))                                       ## list로 만듦
    ## digit 5, replaces 2일 때 generator안에는 OOOXX, OOXOX, OOXXO 등등,,,

    duple_list = []                                                     ## 고정할 수에 들어갈 중복조합 수 리스트

    for i in set(product(number_list, repeat=(digit - replaces))):
        duple_list.append(list(i))
    ## digit 5, replaces 2일 때 duple_list에는 000, 001 , ..., 999 이렇게 들어감

    for duple in duple_list:                                            ## 000부터 시작, 만약 563이면

        for ox_list in generator:                                       ## 그리고 만약 OOXXO이면

            fixed_list = ox_list[:]                                     ## fixed_list는 OOXXO

            n = 0                                                       ## 순서대로 넣을 것

            for i in range(len(fixed_list)):
                if fixed_list[i] == "o":                                ## O이면
                    fixed_list[i] = duple[n]                            ## 563의 인덱스 0인 5
                    n += 1                                              ## n인덱스 + 1
            ## 예시의 결과는 56XX3이 나타남

            prime_list = []

            for i2 in range(10):                                        ## 0부터 9까지 넣을 것
                replacing_list = fixed_list[:]                          ## 56XX3이 replacing_list에 들어감

                for i3 in range(len(replacing_list)):
                    if replacing_list[i3] == "x":                       ## X자리에 0부터 9가 들어갈 것
                        replacing_list[i3] = i2

                completed_number = ""

                for i4 in replacing_list:
                    completed_number += str(i4)                         ## 56003을 붙여줌

                if is_prime(int(completed_number)) and len(str(int(completed_number))) == (digit):
                    ## 소수인지, 앞자리가 0인지 확인
                    prime_list.append(completed_number)                 ## 소수면 prime_list에 넣음

            if len(prime_list) == 8:                                    ## 56003, 56113, ..., 56993 개수가 8개면
                find = True                                             ## find를 True로 바꾸고
                print(prime_list)                                       ## print하고
                break                                                   ## break
    if find:                                                            ## 찾았으면 while문을 break
        break

    if digit == replaces + 1:                                           ## 못찾았을 때 *의 개수가 꽉 차면
        digit += 1                                                      ## n자리 수를 하나 늘리고
        replaces = 1                                                    ## *을 1부터 다시 시작
    else:                                                               ## *의 개수가 꽉 차지 않았으면
        replaces += 1                                                   ## * 개수 + 1

end = time.time() - start
print(end)

## ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']
## 74.91327738761902

## 어려운 문제를 풀긴 풀었는데 74초가 걸렸다...
## 영문 thread에 있는 코드를 봤다. 잘하는 사람들이 매우 많다.
## 이 코드는 1001부터 수를 하나씩 늘려가면서 그 수를 *을 1개부터 자리 수까지 넣어보고 아니면 수를 2씩 늘려갔다. 짝수면 어차피 8개가 안되기 때문에.
start = time.time()

import itertools


def is_prime(n):                                        ## 매우 빨리 소수인지 확인하는 코드
    # https://en.wikipedia.org/wiki/Primality_test
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def test_digits(n, combi):
    n_primes = 0
    primes = set()
    x0 = list(str(n))
    for digit in range(10):
        if digit == 0 and combi[0] == 0:
            continue
        x = x0
        chardigit = str(digit)
        for i in combi:
            x[i] = chardigit
        if is_prime(int(''.join(x))):
            n_primes += 1
            primes.add(int(''.join(x)))
        if n_primes + 9 - digit < 8:
            return False
        if n_primes == 8:
            print('=', min(primes))
            return True


def euler051():
    n = 1001
    while True:
        if is_prime(n):
            s = str(n)
            for n_index in range(1, len(s) - 1 + 1):
                for combi in itertools.combinations(range(len(s)), n_index):
                    if test_digits(n, combi):
                        return
        n += 2


euler051()
end = time.time() - start
print(end)

## = 121313
## 3.9107868671417236
## 배울 점이 참 많다.
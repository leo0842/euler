## Q60
## 네 개의 소수 3, 7, 109, 673는 어떤 수라도 두 개를 뽑아 두 개를 앞 뒤로 이어 붙여도 소수가 된다. ex) 3109, 1093
## 어떤 수라도 두 개를 뽑아 두 개를 앞 뒤로 이어 붙여도 소수가 되는 5개의 소수 리스트 중 그 합이 가장 작은 것
## 본 문제중에 가장 어려웠다,, 시간도 가장 오래 걸렸다.
## 여러 가지 방법을 시도해봤는데 효율적이지 못해 답을 찾지 못했다.
## 결국 구글링으로 알고리즘을 찾아보았다.
## 찾아본 알고리즘들도 대부분 brute force로 효율적이지는 않았다..
## 과정은 n 이하의 소수 리스트를 만들어내고 brute force 방식으로 하나씩 붙이면서 소수 5개를 찾아내는 것이다.

from itertools import combinations as C, permutations as P
import time


def is_prime(n):
    if n == 0: return False
    if n == 1: return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_lists(n):
    a = []
    for i in range(2, n + 1):
        TF = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                TF = False
                break
        if TF:
            a.append(i)
    return a


def concatenation(lists):                           ## 두 수를 앞뒤로 한번씩 붙여서 두 개의 수를 return
    b = []
    for i, j in list(C(lists, 2)):
        b.append(int(str(i) + str(j)))
        b.append(int(str(j) + str(i)))
    return b


start = time.time()


def euler60(n):
    a = prime_lists(n)                                              ## n이하의 소수 리스트
    for i1 in range(len(a) - 2):                                    ## 차례대로,,
        for i2 in range(i1 + 1, len(a) - 1):
            TF = True
            b = concatenation([a[i1], a[i2]])
            for i in b:
                if not is_prime(i):                                 ## 뽑은 두 수 중 하나라도 소수가 아니면
                    TF = False
                    break                                           ## break
            if TF:                                                  ## 두 수가 모두 소수이면 소수를 하나 더 추가해서 확인
                for i3 in range(i2 + 1, len(a)):
                    TF = True
                    c = concatenation([a[i1], a[i2], a[i3]])
                    for j in c:
                        if not is_prime(j):
                            TF = False
                            break
                    if TF:

                        for i4 in range(i3 + 1, len(a)):
                            TF = True
                            d = concatenation([a[i1], a[i2], a[i3], a[i4]])
                            for k in d:
                                if not is_prime(k):
                                    TF = False
                                    break
                            if TF:
                                for i5 in range(i4 + 1, len(a)):                            ## 다섯 개까지 확인 후
                                    TF = True
                                    e = concatenation([a[i1], a[i2], a[i3], a[i4], a[i5]])
                                    for l in e:
                                        if not is_prime(l):
                                            TF = False
                                            break
                                    if TF:                                                  ## 통과하면
                                        return [a[i1], a[i2], a[i3], a[i4], a[i5]], sum(    ## return
                                            [a[i1], a[i2], a[i3], a[i4], a[i5]])


print(euler60(10000))
end = time.time() - start
print(end)

## ([13, 5197, 5701, 6733, 8389], 26033)
## 52.79186010360718

## 뭔가 되게 아쉬운 문제이다. 효율성을 어떻게 극대화할지 지속적으로 생각해봐야겠다.
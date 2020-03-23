## Q37
## 3797처럼 왼쪽부터 하나씩 없애도, 오른쪽부터 하나씩 없애도 모두 소수인 수
## 2,3,5,7을 제외하고 11개가 있다.
## 소수인지 check하는 definition, 왼쪽부터 없애줄 definition, 오른쪽부터 없애줄 definition을 각각 만들어서 해결

def prime_check(num):                                   ## 소수인지 체크하는 함수
    TF = True
    if num == 0: return False
    if num == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return TF


def left_to_right(num):                                 ## 왼쪽부터 없앨 함수

    n = len(str(num))                                   ## n에 자리수를 넣음

    remains = num                                       ## remains라는 변수에 10의 자리 수를 나눈 나머지를 넣을 예정
                                                        ## 3797이면 1000을 나눈 나머지, 797이면 100을 나눈 나머지
    while n != 1:                                       ## n이 1이되면 끝

        remains = remains % (10 ** (n - 1))             ## 위와 같은 방식으로 제일 앞자리를 뗀 수를 넣음

        if prime_check(remains):                        ## 소수이면 패스

            pass

        else:

            return False                                ## 아니면 return False

        n -= 1                                          ## n을 1씩 줄여감

    return True                                         ## While을 통과하면 True


def right_to_left(num):                                 ## 오른쪽에서부터 없앨 예정

    remains = num // 10                                 ## 이거는 간단하게 10을 나눈 몫 3797이면 379만 남음

    while remains:                                      ## remaindl 0이 될 때 까지

        if prime_check(remains):

            pass

        else:

            return False

        remains = remains // 10

    return True


import time

start = time.time()

prime_set = set()                       ## list로 해도 되는데 그냥 set으로 했다.

digit = 11

while len(prime_set) < 11:              ## 11개밖에 없다고 한다.

    if prime_check(digit):              ## 소수인지 통과하면

        if left_to_right(digit):        ## 왼쪽부터 오른쪽

            if right_to_left(digit):    ## 통과하면 오른쪽부터 왼쪽

                prime_set.add(digit)    ## 통과하면 add

    digit += 1

end = time.time() - start

print(sum(prime_set), end, "seconds")   ## 748317 3.1743297576904297 seconds
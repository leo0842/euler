## Q58
## 37 36 35 34 33 32 31
## 38 17 16 15 14 13 30
## 39 18  5  4  3 12 29
## 40 19  6  1  2 11 28
## 41 20  7  8  9 10 27
## 42 21 22 23 24 25 26
## 43 44 45 46 47 48 49
## 위와 같은 방식으로 커지는 격자무의 대각선 수 중 소수의 비율이 10% 아래로 떨어질 때의 가로의 크기
## 대각선위의 수 4개는 가로의 크기에 맞춰 규칙적인 수열을 이룬다. 대충 세네줄 만들어본 후 규칙을 찾았다.
## 이 규칙에 맞춰 대각선위의 수를 array에 넣고 소수인지 확인
## 소수인지 확인할 수를 줄이기 위해 매번 크기를 키울 때 array를 다시 초기화하고 확인을 4개씩만 할 것

import time

def is_prime(n):                                        ## 소수 확인하는 함수
    if n == 0: return False
    if n == 1: return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


start = time.time()
find = False                                            ## while문을 돌릴 변수
diag_array = [1]                                        ## 처음은 예외라서 만들어줌
n = 1                                                   ## 가로의 크기
cnt = 0                                                 ## 소수의 개수
length = 1                                              ## 대각선 위의 수의 개수. 처음 1때문에 1부터 시작

while not find:                                         ## 찾을 때 까지

    if n == 1:                                          ## n이 1일 때에는 예외이기때문에 따로 만들어줌

        n += 2

        diag_array = [diag_array[-1] + (n - 1)]

        continue

    if diag_array[-1] == n ** 2:                        ## 가로의 크기의 제곱이 담기면, 즉 대각선 수 4개를 다 채우면

        length += 4                                     ## 대각선 수의 크기를 +4 하고

        for i in diag_array:                            ## array에 담긴 4개의 수 소수인지 확인

            if is_prime(i):                             ## 소수면 cnt += 1
                cnt += 1

        if cnt / length < 0.1:                          ## 비율 확인하고 10% 아래면
            find = True                                 ## while문 빠져나오기

        else:                                           ## 10%이상이면

            n += 2                                      ## 새로 대각선위의 수를 만들기 위해 가로의 크기를 2 늘려주고

            diag_array = [diag_array[-1] + (n - 1)]     ## array를 다시 제정
    else:                                               ## 가로의 크기의 제곱이 담기지 않았으면, 즉 대각선 위의 수 4개가 다 차지 않았으면

        diag_array.append(diag_array[-1] + (n - 1))     ## 계속 붙이기

end = time.time() - start

print(n, end)       ## 26241 7.634566068649292
## Q55
## 뒤집어서 본래의 수와 더한 뒤 대칭인지 확인하고 아니면 다시 뒤집어서 본래의 수와 더한 뒤 대칭인지 확인
## 1만 이하에서 위의 과정이 50번이 넘으면 결국 대칭되지 않는다고 가정 이 수를 라이크렐 수라고 한다
## 1만 이하 라이크렐 수의 개수는?

import time
def is_palindrome(n):                               ## 대칭인지 확인하는 definition
    string = str(n)
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def reverse_number(n):                              ## 뒤집는 함수
    return int(str(n)[::-1])


Lychrel = 0                                         ## 개수 셀 변수

start = time.time()
for i in range(10001):                              ## 10000까지
    cnt = 0                                         ## 반복 횟수를 셀 변수
    n = i
    while True:
        if is_palindrome(n + reverse_number(n)):    ## 뒤집고 더해서 대칭수면
            break                                   ## 그만
        else:                                       ## 대칭이 아니면
            cnt += 1                                ## 반복 횟수 + 1
            n = n + reverse_number(n)               ## n을 더한 수로 대체하여 다시 대칭인지 확인
        if cnt == 50:                               ## 반복 횟수가 50이 되면
            Lychrel += 1                            ## 라이크렐 수로 인정
            break

end = time.time() - start
print(Lychrel, end)         ## 249 0.1011362075805664
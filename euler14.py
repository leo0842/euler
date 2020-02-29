## Q14
## Longest Collatz Sequence
## 짝수면 나누기 2, 홀수면 곱하기 3 + 1 하는 수열. 결국에는 1로 수렴
## 1m 이하의 수 중 1로 수렴하기까지 과정이 가장 많은 수는?

import time

def Collatz_sequence(limit):                ## 상한을 매길 수를 인자로 받음

    max_cnt = 0                             ## 가장 과정을 많이 거치는 수를 넣을 변수

    for n in range(1, int(limit)):          ## 1부터 1m 까지 수 중
        cnt = 1                             ## 과정 1
        num = n
        while n != 1:                       ## n이 1이 되면 반복문을 벗어남

            if n % 2 == 0:                  ## 짝수면
                n = n // 2                  ## 나누기 2
            else:                           ## 홀수면
                n = 3 * n + 1               ## 곱하기 3 더하기 1
            cnt += 1                        ## 위의 if 과정을 한 번 거치면 과정 + 1
        if max_cnt < cnt:                   ## 위의 while 과정을 다 거친 후 해당 수의 과정이 이전 수 중 max과정보다 높으면
            max_cnt = cnt                   ## max 교체
            max_cnt_num = num               ## 그 때의 수

    return max_cnt, max_cnt_num


start = time.time()
print(Collatz_sequence(1e6))
end = time.time() - start
print(end)                                  ## (525, 837799) 17.88568878173828
                                            ## 837799일 때 525번의 과정을 거침. 17초가 나온다.. 이 방법은 잘못되었다.

## 아무리 고쳐도 걸리는 시간이 잘못되었다. 애초에 구상이 잘못되었나보다.
## 그래서 포럼을 찾아보았다.
## 해당 과정을 우선 함수로 넣어주고
## 과정을 거치는 중에 수가 이 전의 수가 되면 그 수가 거쳤던 과정을 입력하고 이후 과정을 생략함.
## memorable하게 알고리즘을 짰다.


def problem_14(max_start):
    next_element = lambda n: n // 2 if n % 2 == 0 else 3 * n + 1

    max_start = int(max_start)
    length = [0] * max_start  # create an array to store 'known' results
    for test_n in range(1, max_start):
        count = 1
        n = test_n
        while n != 1:
            if n < test_n:
                count += length[n] - 1  # use the previously stored result
                n = 1
            else:
                n = next_element(n)  # go to next element
            count += 1
        length[test_n] = count  # store result for this test_n

    return length.index(max(length))


start = time.time()
print(problem_14(1e6))
end = time.time() - start
print(end)                      ##837799      1.485874891281128초
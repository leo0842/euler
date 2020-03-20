## Q34
## 각 자리의 수를 각각 팩토리얼하여 더한 값이 원래의 수와 같은 수
## ex) 145 = 1! + 4! + 5!
## 먼저 계속 팩토리얼 계산하는 것을 방지하기 위해 dict에 0~9까지 팩토리얼 한 값을 넣는다.
## for문에 넣을 limit값을 정하고 for문을 돌린다. 각 자리 수의 팩토리얼 값은 10으로 나눈 나머지로 계산할 예정

from collections import defaultdict
import time

## 팩토리얼 dict를 만듦
start = time.time()
factorial_dict = defaultdict()                          ## dict를 만든다.
for num in range(10):                                   ## 0~9까지
    if num == 0:                                        ## 0이면 1
        factorial_dict[num] = 1
    mul = 1
    for i in range(1, num + 1):                         ## 팩토리얼 계산을 하여
        mul *= i
    factorial_dict[num] = mul                           ## dict에 넣어준다.

## limit을 정함

n = 1                                                   ## 자리 수를 나타낼 n
while True:
    if len(str(factorial_dict[9] * n)) < n:             ## 각 자리의 수가 9일 때 최대가 되는데 이를 다 더한 값이 자리 값을 넘어서면
        limit = factorial_dict[9] * (n - 1)             ## 그 전의 자리값에 자리값만큼 9! 한 값을 limit에 넣는다.
        break
    n += 1

ans_list = []
for i in range(3, limit):                               ## 문제에서 1과 2를 빼라고 했으니 3부터
    test_num = i                                        ## 10으로 나눌 것이기 때문에 본래의 수가 손상되지 않게 test_num 변수에 넣어준다.
    test_num_sum = 0                                    ## 각 자리수 팩토리얼 값을 더할 변수
    while test_num:                                     ## 몫이 0이 되면 중지
        test_num_sum += factorial_dict[test_num % 10]   ## 나머지 즉 맨 끝의 수부터 팩토리얼 값을 더한다.
        test_num = test_num // 10                       ## 끝의 수를 뗀다.
    if i == test_num_sum:                               ## 다 더한 값이 본래의 수와 같으면
        ans_list.append(i)                              ## append

end = time.time() - start
print(sum(ans_list), end, "seconds")        ## 40730 4.052933216094971 seconds
## Q23
## 초과수 두 개의 합으로 만들지 못하는 28123이하의 수 의 합

## 먼저 초과수 리스트를 만들어준다.

import time
start = time.time()
abundant_list = []
for i in range(2,28123):                            ## 28123이하의 수
    num = i
    divisors_sum = 0
    for check_num in range(2,int(num**0.5)+1):
        if num % check_num == 0:
            divisors_sum += check_num
            divisors_sum += num//check_num
        if num/check_num == check_num:
            divisors_sum -= check_num
    if divisors_sum > i:                            ## 진약수의 합이 해당 수를 넘어가면
        abundant_list.append(i)                     ## append

end = time.time() - start
print(len(abundant_list),end)       ## 6965개 있고 0.6102778911590576초가 걸림

## for문 두 개를 만들어서 합한 수가 28123에 있으면 그 수를 리스트에서 빼려고 하였다.

number = list(range(28124))
for i in range(len(abundant_list)):
    for j in range(i, len(abundant_list)):
        if abundant_list[i] + abundant_list[j] in number:
            number.remove(abundant_list[i] + abundant_list[j])      ## 대박 오래걸린다. 아무래도 이 방법이 아닌 것 같았다.

print(sum(number))      ## ??

## 계속 생각해봐도 다른 방법이 생각이 나지 않아 구글링을 하였다.
## 방식은 완전 같았다. 다른 것은 오직 하나 28123의 number list를 set으로 바꾼 것이었다.

start = time.time()
number = set(range(28124))              ## set으로 바꿈
for i in abundant_list:
    for j in abundant_list:
        if i + j in number:
            number.remove(i + j)        ## 합한 수가 있으면 remove

end = time.time() - start
print(sum(number), end)              ## 4179871   5.239766597747803초

## 왜인지는 모르겠다.. set이 정수 계산에서 빠른가보다..

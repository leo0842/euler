## Q43
## http://euler.synap.co.kr/prob_detail.php?id=43 처럼 각각의 소수에 자리수별로 나눠지는
## pandigital 숫자들의 합
## 기본 개념: 가장 잘 걸러낼 수 있는 17의 배수를 만들어서 pandigital인 세 자리수를 추려내어 이 숫자들에 순열을 앞에 붙임
## 그리고 나머지는 이 순열이 붙여진 숫자들에 대해 각 자리수에 맞는 소수들이 나눠지는지 확인

from itertools import permutations

def is_divisions(num, n):
    return num % n == 0

permute_list = []
n = 6
while True:                                                 ## 세 자리의 17의 배수만 추려냄
    multiples = 17 * n
    if len(str(multiples)) == 4:
        break
    if len(set(list(str(multiples)))) == 3:
        permute_list.append(str(multiples))
    n += 1

permute_list2 = []
number_list = "0,1,2,3,4,5,6,7,8,9"
number_list = number_list.split(",")

for i in permute_list:                                      ## 세 자리의 17의 배수들 중
    number_list_removed = number_list[:]
    for j in list(i):
        number_list_removed.remove(j)                       ## 세 자리의 17의 배수의 각 자리의 수를 제외시키고
    permute = permutations(number_list_removed)             ## 제외시킨 나머지 숫자들로 순열을 만들어서
    for k in permute:
        permute_except_17 = "".join(list(k)) + i            ## 기존의 세 자리의 17의 배수와 연결
        permute_list2.append(permute_except_17)

answer_list = []
prime_list = [2, 3, 5, 7, 11, 13]
for i in permute_list2:
    TF = True
    for index in range(len(prime_list)):                    ## index로 주어진 문제의 각 자리수를 구분
        if is_divisions(int(i[(index + 1):index + 4]), prime_list[index]):
            index += 1
        else:
            TF = False                                      ## 하나라도 나눠지지 않으면 False
            break
    if TF:
        answer_list.append(i)                               ## 모두 각각의 자리수에 나눠 떨어지면 append

print(sum(map(int, answer_list)))   ## 16695334890
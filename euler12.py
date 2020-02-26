## Q12
## 삼각수 중 처음으로 약수가 500개 이상인 수
## 흐름: 소인수분해를 하고 소수의 지수 + 1만큼씩 곱하면 약수의 개수를 알 수 있다. 중학교때인가 고등학교때 배운 거
# 1. triangular number를 만듦 -
# 2. 해당 수의 소수들의 집합 배열을 만듦(소인수분해) -
# 3. 소인수분해한 배열에서 소수의 개수를 세기 위해 unique한 소수 배열을 만듦 -
# 4. 소수의 개수를 세고 각각의 개수에서 +1을 한 후 곱을 한다.
# 5. 500이 넘어가면 중지

def tri_num(cnt):                                               ## triangular number 만드는 함수.
    tri_number = 0

    for i in range(1, cnt + 1):                                 ## cnt까지 다 더함
        tri_number += i

    return tri_number


def div_array(number):                                          ## 인자로 받은 수를 소인수분해할 함수
    divisors_array = []

    divisors = 2

    checked_divisors = number                                   ## 나눠질 수를 변수로 지정

    while checked_divisors != 1:                                ## 1까지 나눠지면 중지

        if checked_divisors % divisors == 0:                    ## 나눠지면:

            checked_divisors = checked_divisors // divisors     ## 나눠진 수를 다시 변수로 지정하고

            divisors_array.append(divisors)                     ## 나눈 수를 배열에 append

        else:

            divisors += 1                                       ## 안나눠지면 나눌 수 + 1

    return divisors_array


def div_array_unique(array):                                    ## 소수 배열에서 소수만 unique하게 가져오는 함수
    divisors_array_unique = []

    for j in array:

        if j not in divisors_array_unique:                      ## 없으면:
            divisors_array_unique.append(j)                     ## 배열에 append

    return divisors_array_unique


##################################################
def num_of_div(n):                                              ## 약수의 개수를 세는 함수, 즉 이 문제를 풀기 위해 돌릴 함수
    cnt = 1                                                     ## 1부터 시작

    num_of_divisors = 1                                         ## 약수의 개수를 확인할 변수를 지정

    while num_of_divisors < n:                                  ## 약수의 개수가 n개 이상이면 중지

        cnt += 1                                                ## 2부터 차례대로

        num_of_divisors = 1

        tri_number = tri_num(cnt)                               ## cnt를 삼각수

        divisors_array = div_array(tri_number)                  ## 소인수분해

        divisors_array_unique = div_array_unique(divisors_array)## 소수의 unique 배열

        for k in range(len(divisors_array_unique)):             ## 각각의 소수에 대해서
            num_of_divisors *= (divisors_array.count(divisors_array_unique[k]) + 1) ## 개수를 세고 +1 한 다음 곱해줌

    return num_of_divisors, tri_number                          ## 약수의 개수와 삼각수를 return

start = time.time()
print(num_of_div(500))
end = time.time() - start
print(end, "seconds")       ## 결과값은 (576, 76576500) 걸린 시간은 6.81062388420105 seconds

## 훨씬 간단한 코딩
## 약수의 대칭을 이용
## 훨씬 간단한거

start = time.time()
x = 500                                     ## 목표 약수의 개수
count = 1                                   ## 점점 늘려갈 변수
sum = 0                                     ## 삼각수를 만들기 위한 변수
z = 0                                       ## 해당 삼각수의 약수의 개수
while z < x:                                ## 목표 약수의 개수가 넘어가면 중지
    sum += count                            ## 삼각수를 만듦
    for i in range(1, int(sum**0.5)+1):     ## 해당 수의 제곱근까지 범위 즉 약수들을 배열했을 때 반환점까지
        if sum % i == 0:                    ## 나눠지면:
            z += 1                          ## 약수 개수 하나 늘림
    if z > x//2:                            ## 반환점까지의 약수가 목표 약수의 개수 나누기 2보다 크면
        print(sum)                          ## print하고
        break                               ## 중지
    count += 1                              ## 아니면 +1하고
    z = 0                                   ## 약수의 개수 변수를 다시 0으로 만듦
print("end")
end = time.time() - start
print(end)                  ## 76576500 end  결린 시간은 5.334469795227051
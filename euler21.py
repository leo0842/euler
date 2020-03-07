## Q21
## 10000이하 amicable number 의 합
## 먼저 진약수의 합을 dictionary에 넣고 amicable number들만 더할 예정

from collections import defaultdict

divisors_sum_dict = defaultdict()                       ## defaultdict 생성

for i in range(2, 10001):                               ## 2부터 10000까지 반복
    num = i                                             ## 해당 수를 num 변수에 넣음
    divisors_sum = 0                                    ## 더할 변수 지정
    for check_num in range(2, int(num ** 0.5) + 1):     ## 2부터 제곱근까지 약수를 확인
        if num % check_num == 0:                        ## 0으로 나눠 떨어지면 즉 약수이면
            divisors_sum += check_num                   ## 해당 약수를 더하고
            divisors_sum += num // check_num            ## 약수를 나눈 몫을 더함 ex) num = 100이고 check_num이 5이면
                                                        ## 5와 20을 더함.
        if num / check_num == check_num:                ## 위의 방식대로 하면 제곱수의 약수를 두 번 더하는 결과가 나타난다. 이를 빼기 위해
            divisors_sum -= check_num                   ## 제곱수이면 즉 약수와 약수로 나눈 몫이 같다면 한 번 빼준다. 두 번 더해졌으니까
    divisors_sum_dict[i] = divisors_sum + 1             ## 1도 약수이므로 마지막에 더해줌

amicable_sum = 0                                        ## amicable 수이면 더해줄 변수
for key in divisors_sum_dict:                           ## 위에서 생성했던 dictionary를 순서대로
    try:                                                ## try를 쓴 이유는 error가 나타날 것이기 때문에
        if (key == divisors_sum_dict[divisors_sum_dict[key]]) and key != divisors_sum_dict[key]: ## 완전수 제외
                                                        ## if 문을 돌리면 error가 나타나는 경우가 있다. 소수는 진약수의 합이 1인데
                                                        ## dictionary에서는 1에 대한 key값을 만들지 않았기 때문에 key 에러가 나타남
            amicable_sum += key                         ## amicable 이면 key 값을 더함
    except:                                             ## key 값이 1이면 패스
        pass
print(int(amicable_sum))         ## 31626
## Q26
## 2부터 999까지 수 중 1로 나눈 수 중 길이가 가장 긴 것은? (반복되는 수는 순환마디로 표현)
## /를 사용하면 한계가 있다. 17자리까지밖에 나타나지 않는다.
## 그래서 기본적인 나눗셈 개념을 이용하여 푼다.
## 나머지를 해당 수로 나누고 몫은 소수점으로, 나머지는 *10을 하여 다시 나눈다.
## 위의 과정을 거치면서 순환한다 싶으면 그만두고 순환소수로 표현하여 길이를 도출
## 나누는 수가 두 자리수이면 *100을 하여 순환하는지 확인
## 마찬가지로 나누는 수가 세 자리수이면 *1000을 하여 순환하는지 표현
## ex) 49로 나눌 때 만약 나머지가 2이면 몫이 0, 나머지가 3이어도 몫이 0이지만 순환하는 것으로 표현하면 안된다.

start = time.time()
length_dict = defaultdict()                                     ## 각 수 별로 length값을 넣을 dictionary를 만듦
for i in range(2, 1000):                                        ## 2부터 999까지
    remainder_list = []                                         ## 소수점을 적을 list
    remainder = 1                                               ## 단위수 1
    quotient = 0                                                ## 몫은 처음에 0
    while remainder_list.count(quotient) == 0:                  ## 같은 것을 찾을 때 까지 즉 순환할 때 까지
        remainder_list.append(quotient)                         ## 몫을 append해줌
        if remainder == 0:                                      ## 나누어 떨어지면 while문을 break
            break
        else:                                                   ## 아니면
            if i // 100 and i != 100:                           ## 세 자리수이면서 100이 아니면
                quotient = (remainder * 1000) // i              ## 나머지*1000을 하여 나눈 몫을 quotient에
                remainder = (remainder * 1000) % i              ## 그리고 나눈 나머지를 다시 remainder에 넣음
            elif i // 10 and i != 10:                           ## 두 자리수일 때
                quotient = (remainder * 100) // i               ## *100
                remainder = (remainder * 100) % i
            else:
                quotient = (remainder * 10) // i                ## 한 자리수
                remainder = (remainder * 10) % i
    length_dict[i] = len(remainder_list)                        ## while문이 끝나면 length를 dictionary에 넣어준다.

end = time.time() - start
print(max(zip(length_dict.values(), length_dict.keys())), end)  ## (983, 983) 0.20467615127563477초

## divmod 함수를 이용하는 방법도 있는데 개념이 같기때문에 따로 짜지는 않았다.
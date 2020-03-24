## Q38
## 어떤 수에 정수 1,2,3,... 을 곱하고 붙여서 pandigital이 되는 수
## for문의 범위를 구하는 부분에서 가장 머리를 많이 썼다.

pan_mul = []

for i in range(1, 10000):                           ## 1 곱하고 붙이고 2 곱하고 붙이고 할 때, 곱해질 수가 다섯자리를 넘어가면
                                                    ## pandigital 범위를 넘어가게 된다. 따라서 곱해질 수는 네 자리가 최대
    integer = 1                                     ## 곱할 정수. 1부터 쭉쭉

    multiples = str(i * integer)                    ## 붙이기 쉽게 곱한 수를 str로 바꿔준다.

    while len(multiples) < 9:                       ## 붙인 수의 자리 수가 9를 넘어가면 스탑

        integer += 1                                ## 정수를 + 1로 만들어준다.

        multiples = multiples + str(i * integer)    ## 곱해서 다시 붙여줌. 이 과정을 반복

    if "".join(sorted(multiples)) == "123456789":   ## 붙인 수가 sort해서 "123456789"이면

        pan_mul.append([multiples, i])              ## append

print(max(pan_mul))     ## ['932718654', 9327]

## 꽤나 쉬웠다.

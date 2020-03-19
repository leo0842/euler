## Q33
## 49/98은 분자와 분모의 9를 지워도 값은 같다. 이렇게 이상하게 약분되는 분수를 찾고 그 분수들의 곱의 분모를 구하라
## 분자와 분모는 두 자리수, 30/50처럼 10의 배수는 X
## 분자와 분모에 수를 넣고 분자 두 개의 수 중 분모에 있으면 이를 하나씩 없애줄 예정.

fraction_list = []                                          ## 위의 방식을 만족하는 분수 list를 만듦
for num in range(11, 100):                                  ## 분자에 넣을 for문
    str_num = str(num)                                      ## 수를 하나 없앨 것이기 때문에 str로 바꿔줌
    for deno in range(num + 1, 100):                        ## 분수의 제한은 진분수이기 때문에 분자보다 1 큰 수부터 분모를 for문
        str_deno = str(deno)
        for i in str_num:                                   ## 분자의 수를 하나씩 쪼개서
            if i not in str_deno:                           ## 쪼갠 수가 분모에 없으면
                pass                                        ## pass
            elif "0" in str_num:                            ## 분자와 분모에 0이 있으면
                pass
            elif "0" in str_deno:
                pass                                        ## pass
            else:
                cancelled_num = str_num.replace(i, "")      ## 그 수를 분자와 분모에서 없애준다.
                cancelled_deno = str_deno.replace(i, "")
                if len(cancelled_num) == 0:                 ## 만약 11과 같이 같은 수를 replace하면 둘 다 없어지기 때문에
                    cancelled_num = i                       ## 하나를 다시 생성해줌
                if len(cancelled_deno) == 0:                ## 상동
                    cancelled_deno = i
                if int(cancelled_num) / int(cancelled_deno) == num / deno:  ## 맞아 떨어지면
                    fraction_list.append([num, deno])       ## append

## 이제 append한 분수의 곱의 분모를 구할 예정

mul_num = 1
mul_deno = 1
for a, b in fraction_list:
    mul_num *= a                ## 분자와 분모들을 다 따로 곱해줌
    mul_deno *= b

for dev in range(2, int(mul_num ** 0.5) + 1):       ## 약분이 되면 약분해준다.
    while mul_num % dev == 0:
        mul_num = mul_num // dev
        mul_deno = mul_deno // dev

print(mul_deno)     ## 100

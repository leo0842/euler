## Q52
## 2배, 3배, ..., 6배 해도 같은 수로 이루어진 수
## 51번 문제가 꽤 어려웠는지 이번 문제는 다소 쉽게 나왔다.

def same_number(digit):                                                 ## 몇 배까지 맞는지 선택
    n = 1
    while True:
        find = True
        for i in range(2, digit+1):                                     ## 2배부터 인자 digit배 까지
            if "".join(sorted(str(n * i))) != "".join(sorted(str(n))):  ## 2배부터 시작해서 하나라도 틀리면
                find = False                                            ## find는 false로 하고
                break                                                   ## for문 break

        if find:                                                        ## for문에서 break당하지 않고 다 맞으면
            break                                                       ## while문 break
        else:                                                           ## 아니면
            n += 1                                                      ## n += 1

        if len(str(n)) != len(str(n * digit)):                          ## 조금이라도 알고리즘을 줄이기 위해 digit배가 길이가 달라지면
            n = 10 ** (len(str(n)))                                     ## 다음 자리수로 넘어감
    return n

same_number(6)  ## 142857
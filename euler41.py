## Q41
## n자리 pandigital 중 가장 큰 소수
## 처음에는 n자리의 소수를 생산하고 그 소수가 pandigital인지 확인하였다.
## 그러니까 너무 오래 걸렸다.
## 그래서 순열로 10 P n 의 순열을 만들어 이 중 소수인 것을 추려내었다.

def n_digit(n):


    prime_pandigital = []                               ## 소수이면서 pandigital인 수의 list

    n_pandigital = ""                                   ## pandigital인지 확인해 줄 string

    permute_list = []                                   ## pandigital 수 list

    number_list = list(map(str,list(range(1,n+1))))     ## permutations에 넣어서 순열을 만들 list

    permute = permutations(number_list)                 ## 순열, 즉 pandigital 수 생산

    for i in permute:
        permute_list.append("".join(list(i)))           ## 구조를 적절하게 바꿔줌

    for j in range(1,n+1):
        n_pandigital = n_pandigital + str(j)            ## n자리의 pandigital 만듦

    for i in permute_list:                              ## 확인할 차례

        if prime_check(int("".join(i))):                ## 생산한 순열 수 중 소수이면
            prime_pandigital.append(i)                  ## append

    return prime_pandigital                             ## list 리턴

start = time.time()
print(max(n_digit(7)))                                  ## 8자리와 9자리는 없음
end = time.time() - start
print(end)

##7652413
##0.2462148666381836초
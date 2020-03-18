## Q32
## Pandigital Products
## 39 × 186 = 7254와 같이 9개의 수가 모두 다른 수
## 9P5 조합의 리스트를 만든 후 2/3으로 쪼개 곱하여 Pandigital이 맞는지 확인할 예정이다.

from itertools import permutations

number_list = list(map(str, list(range(1, 10))))    ## 1부터 9까지 str로 만들어 list 생성
permute_list = []                                   ## 9P5의 조합을 넣을 list 생성
permute = permutations(number_list, 5)              ## permutations 메소드를 활용하여 permute변수에 담는다.
for i in permute:
    permute_list.append("".join(list(i)))           ## permute_list에 list형태로 append

set_results = set()                                 ## Pandigital Product인 수를 담을 set.
                                                    ## 다른 조합을 곱하여 같은 수가 나올 수 있기 때문에 set으로 만든다.
for mul in permute_list:                            ## 하나씩 넣어준다.

    prod = int(mul[:2]) * int(mul[2:])              ## 2/3으로 쪼개서 prod변수에 담는다.
    TF = True                                       ## Pandigital인지 판별할 TF변수
    for char in mul:
        if len(str(prod)) != 4:                     ## 아래의 모든 if는 Pandigital에 대해 판별할 if이다.
            TF = False
            break
        if len(set(list(str(prod)))) != 4:
            TF = False
            break
        if "0" in str(prod):
            TF = False
            break
        if char in str(prod):
            TF = False
            break
    if TF:                                          ## 위 4개의 엄격한 if문을 통과하면
        set_results.add(prod)                       ## set_results에 추가

## 그런데 안타깝게도 틀렸다.
## 문제가 무엇인지 골똘히 생각해보니 한 자리수 * 네 자리수 = 네 자리수이기때문에 Pandigital Product를 만족할 수 있다.
## 그래서 1/4로 쪼개서 다시 돌렸다.
for mul in permute_list:
    prod = int(mul[:1]) * int(mul[1:])
    TF = True
    for char in mul:
        if len(str(prod)) != 4:
            TF = False
            break
        if len(set(list(str(prod)))) != 4:
            TF = False
            break
        if "0" in str(prod):
            TF = False
            break
        if char in str(prod):
            TF = False
            break
    if TF:
        set_results.add(prod)

print(sum(set_results))             ## 45228

## 아무래도 코드가 되게 지저분하여 thread를 찾아보았다.
## 매우 간단한 코드를 찾았다.
## 마치 고등학교 수학시간 경우의 수 문제를 풀 때 나타났던 문제점과 동일하였다.
## 나는 이것빼고 저것빼고 해서 풀려고 했는데 이 코드는 맞는 것만 딱 찾았다. 여집합처럼 푼 것이다.

set_results2 = set()
for x in range(2, 100):             ## 2부터 99까지
    for y in range(123, 4790):      ## 123부터 4789까지
        if "".join(sorted(str(x) + str(y) + str(x * y))) == "123456789": ## sorted해서 123456789이면

            set_results2.add(x * y) ## add

print(sum(set_results2))

## 넘나 멋있다..
## Q40
## 0.123456789101112131415161718192021...
## 양의 정수를 소수점 뒤에 계속 붙여 나가는 수를 Champernowne's constant 라고 한다. 무리수이다.
## 1,10,100,...,1000000 번째 수를 곱한 값은?

integer = 1

Champernowne = str(integer)

while len(Champernowne) <= 1e6:                         ## 길이기 백만이 될 때까지 붙인다.

    integer += 1                                        ## 차례대로 붙일 수를 올린다.

    Champernowne = Champernowne + str(integer)          ## 붙임

sum_of_digit = 1                                        ## 곱한 값을 표시할 수

for i in range(7):                                      ## 0부터 6까지 10의 제곱승으로 더함

    sum_of_digit *= int(Champernowne[(10 ** i) - 1])

print(sum_of_digit)     ## 210

## 포럼을 찾아봐도 번뜩이는 알고리즘은 없는 것 같다.
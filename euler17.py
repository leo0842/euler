## Q17
## letter length of digit
## 구현하기 위한 최소한의 단어만 넣는다.

from collections import defaultdict

letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty",
           "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
letter_digit = defaultdict()

for i in range(len(digit)):
    letter_digit[digit[i]] = letters[i]                     ## dictionary에 넣어준다.


def tens(n):                                                ## 두 자리 수와 세 자리 수를 따로 방법을 만든다.

    if n in letter_digit:

        return len(letter_digit[n])                         ## dict에 있으면 바로 return
    else:

        return (len(letter_digit[n % 10]) + len(letter_digit[(n // 10) * 10]))  ## 없으면 10의 자리와 1의 자리를 나눠서 글자를 만듦


def hundreds(n):                                            ## 세 자리 수 단어로 바꾸기

    if n % 100 == 0:                                        ## 100, 200 이런 애들은 and가 안 붙기 때문에 따로 처리

        return len(letter_digit[n // 100] + "hundred")

    hund = len(letter_digit[n // 100] + "hundredand")       ## 나머지 수 들은 100의 자리 수를 따로 떼서 hundredand를 붙이고

    ten = tens(n % 100)                                     ## 10의 자리 부터는 위에서 만들었던 방법을 사용

    return (hund + ten)


letter_sum = 0

for i in range(1, 1001):
    if i // 1000:                                           ## 1000은 그냥 따로 만들었다.
        letter_sum += len("onethousand")
    elif i // 100:                                          ## 세 자리 수는
        letter_sum += hundreds(i)                           ## hundreds
    else:                                                   ## 두 자리 수는
        letter_sum += tens(i)                               ## tens

print(letter_sum)         ## 21124

## 찾아보니 이에 관련된 메소드가 있다.

import inflect
e = inflect.engine()
len(e.number_to_words(342).replace("-","").replace(" ",""))
## 이 방법은 "three hundred and forty-two" 정식 명칭으로 반환하기때문에 "-"와 공백을 제거해줘야 해당 문제를 풀 수 있다.
f = 0
for i in range(1, 1001):
    f += len(e.number_to_words(i).replace("-", "").replace(" ", ""))

print(f)                  ## 21124
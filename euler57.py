## Q57
## 제곱근 2를 연분수로 1000번을 확장할 때 각 과정에서 분자의 길이가 분모의 길이보다 긴 횟수
## 즉 3/2, 7/5, ... 로 확장하다가 8번째 확장에서 1393/985로 분자의 길이가 분모의 길이보다 처음 길어진다.
## 규칙성을 찾아보기 위해 공책에 끄적이다가 아래와 같은 규칙을 찾았다. 굳이 계산을 하지 않고도 풀 수 있는 문제였다.
## 그래서 while문에 규칙을 넣고 쉽게 풀었다.

num = 3
deno = 2
cnt = 1
ans = 0
while cnt <= 1000:
    num += deno
    temp_deno = deno
    deno = num
    num = temp_deno
    num += deno
    if len(str(num)) != len(str(deno)):
        ans += 1
    cnt += 1
print(ans)      ## 153

## 사실 처음에 연분수의 규칙을 연산을 이용하여 풀려고 하였는데 분모와 분자를 나타내기 힘들었다.
## 그래서 Fraction 함수를 이용하여 풀어보려고 했는데 이상한 숫자가 나왔다. 그래서 위와 같이 푼 것이다.
## 근데 thread를 찾아보니 훨씬 예쁘게 푼 코드가 있었다.

from fractions import Fraction
x = 1
c = 0
for i in range(1000):
    x = 1 + Fraction(1, x+1)
    if len(str(x.numerator))>len(str(x.denominator)):
        c += 1
print(c)        ## 153


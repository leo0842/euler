## Q20
## 100! 의 모든 자리수의 합
## 새로운 방식으로 풀고 싶었는데 딱히 떠오르는 거는 없었다.
## 문제가 쉽고 코딩도 간단하여 여러가지 방법으로 해보았다.

## 1. range의 step과 pop 메소드 이용
n = 1
for i in range(100,0,-1):   ## -1씩 스텝 100부터 1까지
    n *= i                  ## 곱해준다

n2 = list(str(n))           ## 위의 n을 리스트로 한다.
s = 0
while n2:                   ## n2의 리스트가 []이 될 때 까지
    s += int(n2.pop())      ## pop한 것을 더한다.
print(s)        ## 648

## 2. 재귀함수 + 나머지로 풀기
def factorial(n):               ## factorial은 n을 인자로 받는다
    if n == 0:                  ## 0까지 오면
        return 1                ## return 1
    return n * factorial(n-1)   ## 아니면 n에다가 n-1 팩토리얼을 곱해준다.

a = factorial(100)              ## factorial(100)을 a 인자에 넣고
s2 = 0                          ## 더해줄 변수 s2 생성
while a:                        ## a 가 0이 될 때 까지
    s2 += a % 10                ## 10으로 나눈 나머지 즉 1의 자리 수 더하고
    a = a//10                   ## 10으로 나눈 몫을 a에 넣는다.
print(s2)       ## 648

## 3. 재귀함수를 한 문장으로 표현. 오일러 사이트 thread에서 찾음
facto = lambda x: 1 if x == 1 else x * facto(x-1)       ## 익혀야겠다.
print(sum([int(i) for i in list(str(facto(100)))]))     ## 리스트로 바꾼 뒤 다 더해버림

## 4. map 함수를 이용
print(sum(map(int, str(factorial(100)))))               ## map 함수도 여러 방면에서 유용해보인다. 익혀야겠다.
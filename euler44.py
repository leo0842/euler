## Q44
## 오각수 공식은 Pn = n (3n − 1)/2, 오각수들 중 빼고, 더해도 오각수인 두 수 중 뺀 값이 가장 작은 값.
## 처음에는 set으로 오각수를 넣고 하나씩 빼고 더하면서 확인하였다.
## range를 구하기도 힘들었고 시간도 오래 걸렸다.

penta = set()
for i in range(1, 10000):
    penta.add(i * (3 * i - 1) // 2)

answer = set()
for i in penta:
    for j in penta:
        if abs(j + i) in penta:
            if abs(j - i) in penta:
                answer.add(abs(j - i))

print(answer)   ## {5482660}

## 그래서 thread를 보면서 더 나은 개념과 알고리즘을 찾아보았다.
## 오각수인지 확인하기 위해 n을 기준으로 정리하여 이 수가 정수가 나오면 오각수인 것을 응용한 것이다.

start = time.time()

def pen_num(n):                                                     ## 오각수 생산하는 함수
    return (n / 2) * (3 * n - 1)

def is_pen_num(n):                                                  ## 오각수인지 확인하는 함수
    return ((1 + (1 + 24 * n) ** (1 / 2)) / 6).is_integer()         ## 즉, n에 1또는 5를 넣으면 integer일 것이고 아니면 False


i = 1
check = True
penta = set()
while check:
    curr = pen_num(i)                                               ## 먼저 1부터 오각수를 생산
    penta.add(curr)                                                 ## penta에 add
    for j in penta:                                                 ## penta에 있는 수를 차례대로
        back = j
        if is_pen_num(curr - back) and is_pen_num(curr + back):     ## 뺀 값과 더한 값이 모두 오각수이면
            print(curr - back)                                      ## print하고
            check = False                                           ## 더 이상 그만
    i += 1                          ## 아니면 다음 오각수 생산하기 위해 i += 1

print(time.time() - start)
## 5482660.0
## 1.080759048461914

## 오늘도 한 수 배우고 갑니다..
## Q9
## a + b + c = 1000을 만족하는 직각삼각형 세 변의 곱
def pytha_products(n):                      ## 함수 생성, 합을 인자로 받음
    pytha = False                           ## 피타고라스 정리가 성립되는지 알아 보기 위한 변수
    for a in range(1, n):                   ## a 에 1부터 n 까지 넣을 예정
        for b in range(a, n):               ## b 에 a부터 n 까지 넣을 예정 a 이하는 이미 a에서 넣을 것이기에 필요없음
            c = n - a - b                   ## c 는 나머지
            if c <= b:                      ## b 가 c 보다 커지면 break. 이 함수 안에서는 c를 빗변으로 간주하기 때문에
                break
            if c ** 2 == a ** 2 + b ** 2:   ## 피타고라스 정리 확인
                pytha = True                ## 성립하면 pytha 변수가 True로 바뀜
                break                       ## 성립하면 break
        if pytha:                           ## pytha가 True면 모든 반복 그만 둬. 왜냐하면 합이 n인 a,b,c는 하나일 것이기 때문에
            break
    if a < b and b < c:                     ## 최종적으로 a<b<c인지 확인
        return a, b, c, a * b * c           ## 맞으면 return
    else:
        return "they are not integer"       ## else는 없겠지만 만약을 위해ㅎㅎ


pytha_products(1000)
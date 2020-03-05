## Q19
## 20C 매 월 1일이 일요일인 달의 수, 1900년 1월 1일은 월요일
## 일반적으로 알고있는 datetime 메소드로 하기보다는 실제 알고리즘을 만들고자 하였다.
## datetime은 구글링하면 활용법이 쉽게 나오기 때문이다.
## 단서인 1900년 1월 1일을 가지고 시작하였다.
## 본 사이트에는 윤년을 계산하는 방법도 나타나있다.
## 윤년을 계산하는 방법: 4의 배수 해는 윤년, 100의 배수면 윤년 X, 400의 배수면 윤년
## ex) 1896 윤년, 1900 윤년 X, 2000 윤년

month_dic = defaultdict()                       ## 해당 해의 달 날짜를 넣을 dictionary
days = ["월", "화", "수", "목", "금", "토", "일"]   ## 월화수목금토일 리스트
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
thirty = ["Apr", "Jun", "Sep", "Nov"]           ## 30일인 달

for mon in months:
    if mon in thirty:                           ## 30일 리스트에 있으면
        month_dic[mon] = 30                     ## 30일
    else:                                       ## 없으면
        month_dic[mon] = 31                     ## 31일. 2월이 없는 이유는 매년 바뀌기 때문에 for구문 안에서 2월 날짜를 만들 예정

first = "월"                                     ## 1900년 1월 1일부터 시작함. 이 날은 월요일
cnt = 0                                         ## 1일이 일요일이면 += 1 해줄 카운트 변수
for year in range(1900, 2001):                  ## 1900년부터 2000년, 1900년은 아래에서 거를 예정

    if year % 4 != 0:                           ## 윤년 계산할 if문
        month_dic["Feb"] = 28
    elif year % 100 == 0 and year % 400 != 0:
        month_dic["Feb"] = 28
    else:
        month_dic["Feb"] = 29

    for i in month_dic:                         ## 매 달 i에 넣는다

        if first == "일" and year >= 1901:       ## 첫째 날이 일요일이고 year가 1901년 이상부터
            cnt += 1                            ## cnt += 1

        last_days = month_dic[i] % 7            ## 해당 월 나누기 7 해서 마지막 날 계산할 예정

        first = days[(days.index(first) + last_days) % 7] ## 새로운 첫 날은 위에서 만들었던 days 인덱스로 계산할 것

print(cnt)          ## 171

## 쉽게 datetime으로 계산하는 방법
import datetime
cnt = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            cnt += 1
print(cnt)          ## 171
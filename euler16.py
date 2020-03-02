## Q16
## 2**1000의 각 자리의 수를 더한 값
## 혹시 다른 방법이 있나 생각을 많이 해보았다.
## 끝자리가 2, 4, 8, 6으로 진행되는 것 이외에는 전혀 떠오르지 않았다..
## 그래서 가장 직관적인 방법으로 해답을 구하고 thread를 들여다보았다.

n = 2 ** 1000
aa = 0
for i in range(len(str(n))):
    aa += int(str(n)[i])
print(aa)

## 역시 다른 개념으로 푼 사람은 없었다.
## 이용하는 method가 이쁜 것 몇 개를 가져와 보았다.
## 1. pop을 이용한 방식이다.

a=str(2**1000)
b=list(a)
c=0
while b:
    c+=int(b.pop(0))
print(c)

## 2. 10으로 나누어 나머지들을 계속 더하는 방식이다.

def sumofpower(n):
    Number = 2**n
    Sum = 0
    while Number:
        Reminder = Number % 10
        Sum = Sum + Reminder
        Number = Number //10
    return Sum

#Output
n= 1000
print(sumofpower(n))


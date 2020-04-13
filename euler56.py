## Q56
## a, b < 100일 때 a ** b 수 중 각 자리의 합이 가장 큰 것은?
## 쉬어가는 문제인가보당
## 각 자리의 수를 구하는 것은 수를 활용하고 싶어 string으로 바꾸지 않고 10으로 나눈 몫을 활용하였다.
## while 문은 0이 될 때 까지로

max_sum = 0

for a in range(100):
    for b in range(100):
        number = a ** b
        digit_sum = 0
        while number:
            digit_sum += (number % 10)
            number = number // 10
        if max_sum < digit_sum:
            max_sum = digit_sum
            max_ab = [a, b]

print(max_sum, max_ab) ## 972 [99, 95]
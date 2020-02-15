## Q6
## 1부터 100까지 더하고 제곱한 수와 제곱하고 더한 수와의 차이

def difference(num):
    plus_square = ((1 + num) * (num // 2) + (num % 2) * (num // 2 + 1)) ** 2

    for i in range(1, num + 1):
        plus_square -= i ** 2

    return plus_square

print(difference(100))

##using well known fomula
def difference2(limit):
    limit = 100
    sum2 = limit * (limit + 1) // 2
    sum_sq = (2 * limit + 1) * (limit + 1) * limit // 6
    return sum2 ** 2 - sum_sq

print(difference2(100))
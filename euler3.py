## Q3
## 소인수분해하기
def max_prime_factor(num):
    n = 2
    b = []
    while num != 1:
        for i in range(n, int(num) + 1):
            if num % i == 0:
                break
        num = num / i
        n = i
        b.append(n)

    return b, max(b)


max_prime_factor(600851475143)


## from forum, 반복문 한번만 씀,,,
def big_prime(n):
    p = 2
    while n != 1:
        if n % p == 0:
            n = n / p
        else:
            p = p + 1
    return p


print(big_prime(600851475143))
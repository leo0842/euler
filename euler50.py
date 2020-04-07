## Q50
## 백만 이하의 소수 중 연속된 소수의 합이 가장 긴 소수의 값은?

def prime_generator(n):
    sieve = [False] * 2 + [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False
    return [x for x in range(len(sieve)) if sieve[x]]


def next_prime(n):
    if n == 0 or n == 1:
        return 2
    a = n + 1
    while True:
        TF = True
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                TF = False
                a += 1
                break
        if TF:
            return a


a = prime_generator(int(1e6))
b = [7]
d = []
while a:
    c = a[0]
    if sum(b) == c:
        b.append(next_prime(b[-1]))
        d.append([c, len(b) - 1])
        a.pop(0)
    elif sum(b) < c:
        b.append(next_prime(b[-1]))
    else:
        a.pop(0)

max(d)
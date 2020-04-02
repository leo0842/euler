## Q45
## 삼각수	Tn = n (n + 1) / 2, 오각수 Pn = n (3n − 1) / 2, 육각수 Hn = n (2n − 1)
## 삼각수도 되고 오각수도 되고 육각수도 되는 수 40755 보다 큰 수

Tris = lambda n: n*(n+1)/2
def is_penta(num):
    return ((1 + (1 + 24*num)**0.5)/6).is_integer()

def is_hexa(num):
    return ((1 + (1 + 8 * num)**0.5)/4).is_integer()

n = 1
while True:
    num = Tris(n)
    if is_penta(num) and is_hexa(num) and num > 40755:
        print(int(num), n)
        break
    n += 1
## 1533776805 55385

## 44번 문제를 응용하였다. 또한 오각수를 일일이 찾아봐야 했던 44번에 비해 훨씬 단순하였다.
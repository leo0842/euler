## Q64
## √23 = [4;(1,3,1,8)]로 연분수를 포현하며 반복 주기는 4로 짝수이다.
## N <= 10000 의 제곱근을 연분수로 나타낼 때 반복 주기가 홀수인 경우

from math import sqrt
import time

start = time.time()


def shape_maker(i, d):
    global N

    n = (d * ((sqrt(N) + i))) / (N - i ** 2)

    integer = (int(n) * (N - i ** 2) / d) - i

    deno = (N - i ** 2) / d

    return integer, deno


N = 1
cnt = 0
while N <= 10000:
    left_list = []
    if (N ** 0.5).is_integer():
        N += 1
        continue

    i = int(sqrt(N))
    d = 1
    shape = [i, d]
    shape_list = []
    while True:
        if shape in shape_list:
            break
        else:
            shape_list.append(shape)
            i, d = shape_maker(i, d)
            shape = [i, d]
    if len(shape_list) % 2 == 1:
        cnt += 1
    N += 1

end = time.time() - start
print(cnt, end)
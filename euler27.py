## Q27
## n**2 + n*a + b, -999<=a, b <=999 를 만족하는 정수 a, b에 대하여
## 위의 식 n에 0부터 정수를 넣을 때 연속적인 소수가 나오게 하는 a, b 중 연속적인 소수를 가장 많이 만드는 a, b
## 위의 식으로 나온 수가 소수인지 판단하는 def를 만들고 for문을 돌림

import time
from collections import defaultdict

start = time.time()
coord = defaultdict()

def prime_check(num):                           ## prime_check라는 함수, 인자로 들어온 수가 소수인지 판단
    if num < 0:                                 ## 너무 많이 만들어서 설명 생략
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for a in range(-1000, 1000):                    ## a 범위
    for b in range(-1000, 1000):                ## b 범위
        n = 0                                   ## n은 0부터
        test = n**2 + n*a + b                   ## test에 식에서 나오는 수를 넣어줌
        while prime_check(test):                ## 참이면
            n += 1                              ## 계속 +1
            test = n**2 + n*a + b               ## +1한 후 식에 넣음
        coord["%d, %d" % (a, b)] = n            ## while을 벗어나게 되어 나오는 n을 dictionary에 넣어줌

end = time.time() - start
print(max(zip(coord.values(), coord.keys())), end)      ## (71, '-61, 971') 6.801011085510254초

## 조금 오래 걸리긴 하는데 thread를 찾아봐도 비슷하게 알고리즘을 짜고 비슷한 속도를 보였다.
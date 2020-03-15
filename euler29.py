## Q29
## 2 <= a, b <= 100를 만족하는 a, b에 대하여 중복을 제외한 a ** b의 개수
## 의도를 파악하기위해 다른 방식으로 풀어보려했지만 실패하였다. 그래서 그냥 가장 직관적인 방법으로 풀었다.
## 너무 쉽게 풀어서 괜히 def를 넣어보았다.

start = time.time()

def power_set(a_max, b_max):
    powers = set()
    for a in range(2, a_max + 1):
        for b in range(2, b_max + 1):
            powers.add(a ** b)
    return powers

end = time.time() - start

print(len(power_set(100, 100)), end) ## 9183 0.0001468658447265625초

## forum을 찾아보아도 다들 비슷하다. 한 줄로 코딩한 것을 가져와보았다.
print(len(set(a**b for a in range(2, 101) for b in range(2, 101))))
## 한줄이긴한데 그게 그거다.
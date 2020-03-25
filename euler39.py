## Q39
## 각 변의 길이가 자연수 {a, b, c}인 직각삼각형의 둘레를 p라고 할 때, 1000이하의 p 중 가장 많이 직각삼각형을 생산해내는 p
## 처음에는 p에 사로잡혀 p를 기준으로 a, b, c를 만들어 계산하였다.
## 그러니까 너무 오래 걸려서 이 방법 외에 더 효율적인 방법을 forum에서 찾아보았다.
## p에 집중하기 보다는 삼각형을 만들어낼 수 있는 자연수 a, b, c를 만들고 이 변을 직각삼각형과 p <= 1000인지 확인하는 것이 훨씬 빨랐다.

start = time.time()

def is_right(a, b, c):
    return (a ** 2 + b ** 2) == c ** 2              ## 직각삼각형인지 check하는 definition

def is_int(c):
    return int(c) == c                              ## c가 자연수인지 check

number_of_triangle = defaultdict()                  ## 위의 조건을 만족하면 둘레를 담을 dict

for a in range(1, 334):                             ## 변 길이의 조건 1
    for b in range(a, 500):                         ## 변 길이의 조건 2
        c = (a ** 2 + b ** 2) ** 0.5                ## c를 만듦

        if is_int(c) and (a + b + c) <= 1000:       ## c가 자연수인지, p가 1000이하인지 확인
            if is_right(a, b, c):                   ## 직각삼각형인지 확인
                p = a + b + c                       ## 조건을 만족하면 둘레를 p에 담고
                if p in number_of_triangle:         ## dict에 있으면
                    number_of_triangle[p] += 1      ## += 1
                else:                               ## 없으면
                    number_of_triangle[p] = 1       ## 새로 key를 만들어줌

end = time.time() - start
print(max(zip(number_of_triangle.values(), number_of_triangle.keys())), end, "seconds")

## (8, 840.0) 0.12273216247558594 seconds


## Q15
## lattice paths
## n X k 의 격자무늬 사각형에서 (0, 0)에서 (n, k)으로 가는 방법의 수
## 매우 유명한 것이기 때문에 알려진 공식도 있다. (n + k)!/(n! * k!)
## 별로 이 공식으로 풀어넘기고 싶진 않았다. 그래서 공책을 폈다.
## 공책 두 페이지를 소비한 후 한가지 규칙을 알아냈다.
## (a, b)까지 가는 방법의 수는 (a - 1, b)까지 가는 방법의 수와 (a, b-1)까지 가는 방법의 수를 더한 것이었다.
## (a - 1, b)와 (a, b-1)까지 가는 각각의 방법의 수 또한 같은 방식으로 구한다.
## x축과 y축위의 좌표까지 가는 방법은 오직 한 가지 방법이다.
## 왼쪽 위에서 오른쪽 아래로 대각선을 긋고 이 선을 대칭축으로 하는 모든 대칭 좌표들의 방법의 수는 같다.
## 그래서 아래쪽 삼각형만을 기준으로 방법의 수를 구하고 마지막은 곱하기 2를 하는 방식으로 한다.

from collections import defaultdict
import time


def lattice_paths(n):                       ## 정사각형의 좌표를 기준으로 하여 한 축의 크기를 받은 n 인자이다.

    grid = defaultdict()                    ## dic으로 할 예정

    grid["0, 0"] = 0                        ## (0, 0)은 0

    for row in range(1, n + 1):             ## 행부터 계산

        idx = "%d, %d" % (row, 0)           ## 좌표가 key로 들어가기 때문에 string으로 바꿔서 넣어준다.

        grid[idx] = 1                       ## 행축의 좌표로 가는 방법은 모두 1

        for col in range(1, row + 1):       ## 열 반복문

            idx = "%d, %d" % (row, col)     ## 마찬가지로 string

            if col == row:                  ## 행과 열이 같은 좌표는

                grid[idx] = grid["%d, %d" % (row, col - 1)] * 2 ## 왼쪽과 위쪽의 좌표가 같기 때문에 그냥 곱하기 2한다.

            else:                           ## 아니면

                grid[idx] = grid["%d, %d" % (row - 1, col)] + grid["%d, %d" % (row, col - 1)] ## 왼쪽과 위쪽의 방법의 수를 더함

    return grid


start = time.time()
grid = lattice_paths(20)                    ## 20 * 20 의 사각형
end = time.time() - start
print(grid["20, 20"], round(end, 5), "seconds") ## 137846528820가지, 0.00032 seconds

## 얼마전에 공부했던 재귀함수가 생각났다.
## 그래서 활용해보고 싶었다.

def lattice_paths2(n, m):                   ## (n, m)까지 가는 방법의 수를 구할 것

    grid = defaultdict()                    ## 마찬가지로 dic을 사용

    idx = "%d, %d" % (n, m)                 ## 좌표를 idx변수에 지정

    if n == 0 and m == 0:                   ## (0, 0)이면

        grid[idx] = 0                       ## 0

        return grid[idx]                    ## return

    elif n == 0 or m == 0:                  ## 행축이거나 열축에 있는 좌표면

        grid[idx] = 1                       ## 1

        return grid[idx]                    ## return

    else:                                   ## 나머지 좌표들은

        grid[idx] = lattice_paths2(n - 1, m) + lattice_paths2(n, m - 1) ## 위에서 찾았던 규칙 적용. 규칙을 적용할 때는 재귀함수로

    return grid[idx]                        ## return

## 재귀함수의 고질적인 문제점이 나타난다. (10, 10)부터 시간이 걸리기 시작하더니
## (15, 15)부터는 너무 오래 걸려서 포기
## 그래서 재귀함수 공부할 때 배웠던 메모잉을 활용

def memoize(f):                             ## 이전에 나왔던 좌표를 기억하는 함수
    memo = {}

    def helper(x, y):

        idx = "%d, %d" % (x, y)

        if idx not in memo:                 ## 없으면 dic에 추가.

            memo[idx] = f(x, y)

        return memo[idx]

    return helper


def lattice_paths3(n, m):                   ## 다시 재귀함수 시작

    grid = defaultdict()

    idx = "%d, %d" % (n, m)

    if n == 0 and m == 0:
        grid[idx] = 0

        return grid[idx]

    if n == 0 or m == 0:
        grid[idx] = 1

        return grid[idx]

    grid[idx] = lattice_paths3(n - 1, m) + lattice_paths3(n, m - 1)

    return grid[idx]


lattice_paths3 = memoize(lattice_paths3)

start = time.time()
print(lattice_paths3(20, 20))
end = time.time() - start
print(round(end, 5), "seconds")         ## 137846528820, 0.00129 seconds

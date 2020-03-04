## Q18
## 인접한 아래의 두 숫자중 하나를 더하여 끝까지 더했을 때 max값
## 처음 생각했던 방법은 문제의 note에서도 나타나듯 층이 늘어날수록 2의 제곱씩 과정이 늘어난다.
## max만 선택하기에는 모든 수를 더했을 때 max임을 보장할 수 없다.
## ex)
## 1
## 99 1
## 99 1 1
## 99 1 1 10000
## 위의 예시에서 처음 max를 선택하면 99를 선택하고 밑으로도 쭉 99를 선택한다. 하지만 이러한 max 과정을 선택하면 10000을 놓치게 된다.
## 수 시간을 생각해도 답이 나오지않아 구글링을 하였다.
## 아래에서부터 올라오면 확정적이기 때문에 max값을 알 수 있다. 또한 과정이 sum(range(1,층의 수-1)) 만큼 나와 부담도 적다.

a = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
b = a.split("\n")
for i in range(len(b)):
    b[i] = b[i].split(" ")
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])
cnt = 0
for i in range(len(b)-2,-1,-1):

    for j in range(len(b[i])):

        if b[i+1][j] > b[i+1][j+1]:
            b[i][j] += b[i+1][j]
        else:
            b[i][j] += b[i+1][j+1]
        cnt += 1
print(b[0][0])
print()
print(cnt)

## https://mingrammer.com/project-euler-maximum-path-sum/
## 깔끔한 코딩

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

triangle_leaves = []
for line in triangle.strip().splitlines():
    triangle_leaves.append([int(i) for i in line.split()])

n = len(triangle_leaves)
for i, leaves in enumerate(triangle_leaves[-2::-1]):
    for j, leaf in enumerate(leaves):
        left = triangle_leaves[n-i-1][j]
        right = triangle_leaves[n-i-1][j+1]
        triangle_leaves[n-i-2][j] += max(left, right)

print(triangle_leaves[0][0])


## 처음 생각했던 구조
## 매우 오래 걸린다. 모든 방법의 수와 과정을 리스트에 넣기 때문에.

max_c = []
a = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
b = a.split("\n")
for i in range(len(b)):
    b[i] = b[i].split(" ")
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])

def recurs(x, y, pn):
    if x == len(b):
        return 0
    pn += int(b[x][y])
    max_c.append(pn)
    recurs(x + 1, y, pn)
    recurs(x + 1, y + 1, pn)


recurs(0, 0, 0)

max(max_c)
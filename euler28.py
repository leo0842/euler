## Q28
## 21 22 23 24 25
## 20  7  8  9 10
## 19  6  1  2 11
## 18  5  4  3 12
## 17 16 15 14 13
## 위의 규칙대로 배열을 만들어갈 때 행과 열이 1001일 때 모든 대각선 위 수들의 합
## 첫 번째는 규칙을 찾아서 식을 만들어 풀이
## 한 번 가장자리가 만들어질 때 수는 더할 수는 4개
## 가장자리가 늘어갈 때 마다 더할 수들의 차이도 규칙적으로 늘어남.

n = 1
diag_sum = 0
diag_array = [1]
while n <= 1001:

    if diag_array[-1] == n ** 2:                        ## 모서리가 열의 수의 제곱이면

        diag_sum += sum(diag_array)                     ## 모은 대각선 위의 수를 다 더함

        n += 2                                          ## 그리고 n에 2를 더해줌

        diag_array = [diag_array[-1] + (n - 1)]         ## 그리고 마지막 대각선 위의 수에 n-1을 넣어준다.

    else:

        diag_array.append(diag_array[-1] + (n - 1))     ## 아니면 계속 diag_array에 n-1만큼 더한 수를 더한다.

print(diag_sum)         ## 669171001

## 뭔가 규칙적으로 늘어나는 순열이다. 2차원이라서 설명하기 좀 힘들다..
## 두 번째 방법은 모든 좌표의 수를 dictionary에 넣고 대각선 위의 수를 다 더하는 방법이다.
## 1일때 1,1로 시작한다.

start = time.time()
row = 1                                         ## 처음 행 좌표 지정
col = 1                                         ## 처음 열 좌표 지정
grid = defaultdict()
idx = "%d, %d" % (row, col)                     ## idx에 좌표를 character로 넣어줌
cnt = 1                                         ## cnt는 좌표에 들어갈 수. 1씩 늘어간다.
grid[idx] = cnt                                 ## 아까 만든 dictionary에 cnt가 value로 들어감
max_num = 1                                     ## 규칙을 만들 max_num
min_num = 1                                     ## 상동
diag = 1                                        ## 모서리들의 value값을 더해줄 diag 변수 생성
while len(grid) < 1001 ** 2:                    ## 행과 열이 1001일 때 1001**2 까지 수가 생성된다.
    cnt += 1                                    ## 시작을 알리는 cnt += 1
    if col == max_num and row == min_num:       ## 좌표가 우측 맨 위에 있을 경우
        max_num += 1                            ## 행과 열의 제한을 1만큼 늘린다.
        min_num -= 1
        cnt -= 1                                ## 행과 열의 제한을 늘리는 if문이기 때문에 cnt는 다시 원래대로 돌려준다.

    elif col == max_num and row < max_num:      ## 맨 우측에 있을 시
        row += 1                                ## row를 1만큼 더한다.
        idx = "%d, %d" % (row, col)             ## 그리고 그 좌표를 idx 변수에 넣고
        grid[idx] = cnt                         ## dic에 넣는다.

    elif col > min_num and row == max_num:      ## 맨 아래에 있을 시
        col -= 1                                ## col을 1만큼 뺀다.
        idx = "%d, %d" % (row, col)
        grid[idx] = cnt

    elif col == min_num and row > min_num:      ## 맨 왼쪽에 있을 시
        row -= 1                                ## row를 1만큼 뺀다.
        idx = "%d, %d" % (row, col)
        grid[idx] = cnt

    else:                                       ## 그 외의 경우에는
        col += 1                                ## col을 1만큼 더한다. 즉 우측으로 간다.
        idx = "%d, %d" % (row, col)
        grid[idx] = cnt

    if (row == max_num and col == max_num) or (row == max_num and col == min_num) or (
            row == min_num and col == min_num) or (row == min_num and col == max_num):
                                                ## 모서리에 있을 경우
        diag += grid[idx]                       ## diag변수에 해당 value를 더함

end = time.time() - start
print(diag, end)            ## 669171001 1.569281816482544초

## numpy를 이용하여 풀이해보고 싶었지만 아직 numpy에 대한 지식이 모잘랐다. 공부해서 다시 풀어봐야겠다.
## Q30
## 각 자리의 수를 5제곱하여 다 더했을 때 자기 자신이 나오는 수
## 각 자리의 수를 5제곱하여 다 더했을 때 자리 수를 넘어가지 않는 max수를 구하고 max수까지 for문을 돌린다.

start = time.time()
n = 1                                   ## 처음 자리수 1
while True:
    max_num = (9 ** 5) * n              ## max_num 변수에 자리 수 5제곱이 최대가 되는 수를 넣는다. 즉 9의 5제곱을 자리 수 개수만큼 더한다.

    if n > len(str(max_num)):           ## 자리 수가 max_num을 넘어가면, 예를 들어 n이 7자리 수인데 9**5 * 7이 6자리 이면 스탑

        max_num = (9 ** 5) * (n - 1)    ## 그 이전의 max수를 max_num 변수에 넣는다.

        break

    n += 1

fifth_powers = []                       ## 리스트 변수 생성

for i in range(2, max_num + 1):         ## 위에서 만들었던 max_num까지를 for문 돌림

    power_sum = 0                       ## 각 자리수 5제곱을 더해줄 변수

    for j in str(i):

        power_sum += int(j) ** 5

    if i == power_sum:                  ## 다 더한 값이 본래의 수와 같으면

        fifth_powers.append(i)          ## append

end = time.time() - start
print(sum(fifth_powers), end)           ## 443839 1.2651901245117188
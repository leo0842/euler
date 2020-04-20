## Q62
## 345^3 = 41063625, 이 수를 순열로 만들면 그 중 56623104 = 384^3, 66430125 = 405^3이 또한 세제곱 수
## 이처럼 자리수로 만든 순열중 세제곱수가 5개인 수 중 가장 작은 수
## 과정: 순열을 sorted해서 딕셔너리에 넣어주고 5개가 쌓이면 stop
## 그리고 그 순열의 최소 수를 찾는다.

from collections import defaultdict
import time

start = time.time()
cubic_dict = defaultdict()
n = 1
while True:
    cubic_num = str(n ** 3)                         ## 세제곱수를 str로 만들어준다.

    sorted_cubic = "".join(sorted(cubic_num))       ## sorted한다.

    if sorted_cubic in cubic_dict:                  ## 딕셔너리 key에 이미 존재하면
        cubic_dict[sorted_cubic] += 1               ## += 1

    else:                                           ## 처음이면
        cubic_dict[sorted_cubic] = 1                ## 1

    if cubic_dict[sorted_cubic] == 5:               ## 5개가 쌓이면
        break                                       ## break
    else:
        n += 1                                      ## n을 하나씩 올림

print(sorted_cubic)         ## 012334556789

n2 = 1
while True:
    cubic_num = str(n2 ** 3)                        ## 순열의 최소 수를 찾는 과정

    finding_num = "".join(sorted(cubic_num))

    if finding_num == sorted_cubic:                 ## 맞으면
        print(n2 ** 3, n2)                          ## print하고 스탑
        break
    else:                                           ## 아니면 계속 += 1
        n2 += 1

end = time.time() - start
print(end)
## 127035954683 5027
## 0.02962803840637207

## 막 깔끔하지는 않다,,

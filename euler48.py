## Q48
## 1**1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000의 마지막 10자리 수
## 딱히 설명할 것이 없다..

all_sum = 0
for num in range(1,1001):
    if len(str(num ** num)) > 10:
        all_sum += int(str(num ** num)[-10:])
    else:
        all_sum += num ** num
int(str(all_sum)[-10:])     ## 9110846700

## thread도 별반 다를 게 없다..
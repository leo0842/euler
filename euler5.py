## Q5
## 1부터 20까지 모든 수에서 나누어 떨어지는 수 중 최소값
prime_array = [1]
prime_multiple = 1
for i in range(2,21):
    remains = i
    for j in prime_array:
        if remains % j == 0:
            remains = remains/j
    if remains != 1:
        prime_array.append(int(remains))
    prime_multiple *= remains

print(int(prime_multiple))
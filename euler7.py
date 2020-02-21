## Q7
## 10001번째 소수 찾기

prime_list = [2] ##소수 쌓을 리스트 생성
num_checked = 2 ## 소수인지 확인할
while len(prime_list) < 10001:  ## 10001번째
    is_prime = True             ## 소수인지 판별하기 위한 변
    num_checked += 1            ## 차례대로
    for i in prime_list:        ## 소수 리스트를 i에 넣음
        if num_checked % i == 0: ## 소수로 나눠지는지 확인
            is_prime = False   ## 소수로 나눠지면 소수가 아님
            break
    if is_prime:                ## is_prime이 어떤 소수로도 나눠지지 않음
        prime_list.append(num_checked) ## 소수 리스트에 추가

max(prime_list)

## Q35
## 백만 이하 circular prime의 개수
## circular prime은 197과 같이 971, 719처럼 왼쪽으로 회전시키면서 소수를 만족시키는 수
## 앞자리를 pop시켜 맨 뒤에 붙히고 그 수가 소수인지 체크

start = time.time()


def prime_check(n):                                     ## 소수인지 체크할 definition
    TF = True
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            TF = False
            break
    return TF


prime_list = []
for i in range(2, int(1e6)):                            ## 아래 circular 확인할 for문의 range를 줄이기 위해 먼저 소수 리스트를 만듦
    if prime_check(i):
        prime_list.append(str(i))                       ## list로 만들기 위해 str형태로 list에 넣는다.

circular_prime = []
for j in prime_list:
    rotate_list = list(j)                               ## pop과 append를 위해 list로 만든다.
    TF_check = True                                     ## 확인할 변수
    while True:
        rotate_list.append(rotate_list.pop(0))          ## 0번 index를 떼서 맨 뒤에 append
        if rotate_list == list(str(j)):                 ## 한 번 회전해서 처음 수와 같아지면
            break                                       ## 그만
        if prime_check(int("".join(rotate_list))):
            pass
        else:                                           ## 회전시킨 수가 소수가 아니면
            TF_check = False                            ## False로 만들고
            break                                       ## 그만
    if TF_check:                                        ## While문을 돌리고나서도 True이면
        circular_prime.append(j)                        ## append

end = time.time() - start
print(len(circular_prime), end, "seconds")      ## 55 5.203920125961304 seconds
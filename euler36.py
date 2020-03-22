## Q36
## 585와 같이 십진법에서도, 이진법(1001001001)에서도 palindrome(좌우가 같은)인 수를 백만 이하에서 찾아서
## 다 더하기
## 처음에는 내장함수인 bin()을 이용하여 간단하게 풀었다.

start = time.time()
a = []
for i in range(1,int(1e6)+1):
    if (str(i) == str(i)[::-1]) and (bin(i)[2:] == str(bin(i)[2:])[::-1]):
        ## str로 바꿔 ::를 이용, bin()을 이용하면 str로 나타나고 앞에 2진법을 나타내는 시그널이 붙어 이를 제외하여 확인
        a.append(i)
end = time.time() - start
print(sum(a), end)          ## 872187 0.6619088649749756초

## 너무 쉬워서 bin()을 def를 이용하여 새로 한번 만들어보았다.
## 만드는 개념은 먼저 이진법으로 나타낼 자리수를 구하고 그 자리수에 맞게 1 또는 0을 붙일 것이다.

start = time.time()

def to_binary(num):
    n = 0
    while True:
        if num < (2 ** n):          ## n에 자리수를 배정 ex) num이 10이면 네 자리
            n -= 1
            break
        n += 1
    bin_num = []                    ## 1 또는 0을 append할 리스트
    for i in range(n, -1, -1):      ## 최대 자리 수에서 0까지
        if num - (2 ** i) >= 0:     ## 2에 자리 수를 제곱하여 뺀 값이 0 이상이면
            bin_num.append("1")     ## 1을 붙이고
            num -= (2 ** i)         ## 그 크기만큼 빼준다.
        else:
            bin_num.append("0")     ## 아니면 0을 붙인다.

    return "".join(bin_num)


palind_list = []
for i in range(1, int(1e6) + 1):
    binary_number = to_binary(i)
    if (str(i) == str(i)[::-1]) and (binary_number == binary_number[::-1]):
        palind_list.append(i)

end = time.time() - start
print(sum(palind_list), end)        ## 872187 18.718788146972656초

## 꽤 오래 걸린다.
## 근데 심심해서 이진법 뿐만 아니라 다른 진법에서도 적용할 수 있는 definition을 만들고싶었다.
## 기본적인 개념은 위와 같다.
## 다만 0 과 1을 붙이는 while문에서 조금 더 복잡하고 견고하게 만들 필요가 있게 되었다.

start = time.time()

def to_base(num, base):
    n = 0
    while True:
        if num < (base ** n):
            n -= 1
            break
        n += 1
    base_number = []
    for i in range(n, -1, -1):
        cnt = 1                                 ## cnt 라는 항목을 추가하였다.
        while num - ((base ** i) * cnt) >= 0:   ## 자리 수를 제곱한 수에서 얼마만큼 뺄 수 있는지 cnt한다.
            cnt += 1
        cnt -= 1
        base_number.append(str(cnt))            ## 이 cnt를 append한다. 1과 0처럼.
        num = num - ((base ** i) * cnt)         ## 그리고 이 수를 빼준다.

    return "".join(base_number)


palind_list2 = []
for i in range(1, int(1e6) + 1):
    c = to_base(i, 2)                                   ## 진법도 나타나야 하기 때문에 인자가 2개가 되었다.
    if (str(i) == str(i)[::-1]) and (c == c[::-1]):
        palind_list2.append(i)
end = time.time() - start
print(sum(palind_list2), end)   ## 872187 29.88209104537964초

## 복잡해져서 그런지 디게 오래 걸린다.


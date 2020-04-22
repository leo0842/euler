## Q63
## a ** n이 n자리 수인 경우의 개수
## 꽤나 쉬운 문제였다.
n = 1
a = 1
cnt = 0
while True:
    if len(str(a ** n)) == n:
        cnt += 1
        a += 1
    elif len(str(a ** n)) < n:
        a += 1
    else:
        if (len(str(9 ** n))) != n:
            break
        else:
            n += 1
            a = 1

print(cnt) ## 49
## Q2
## 피보나치 수열 4m 미만 짝수 합
def fibo(n):
    a1 = 1
    a2 = 2
    f_array = []
    for i in range(n):
        if i == 0:
            an = a1
        elif i == 1:
            an = a2
        else:
            an = f_array[i-1] + f_array[i-2]
        f_array.append(an)
    return f_array
##
n = 1
fib_q = fibo(1)
while fib_q[n-1] <= 4000000:
    fib_q = fibo(n+1)
    n += 1
##
even_fib = 0
for i in range(len(fib_q)):
    if fib_q[i] % 2 == 0:
        even_fib += fib_q[i]
even_fib
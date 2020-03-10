## Q24
## 0부터 9까지 사용하여 만들 수 있는 수 중 1m 번째 수
## 0도 맨 앞에 들어갈 수 있는 문제이기 때문에 만들 수 있는 수는 10!이다.
## 지금까지의 문제 중 가장 시간을 오래 썼던 문제이다. 근데도 제대로 된 알고리즘을 짜지는 못하였다.
## 재귀함수를 이용하여 문제를 풀려고 했지만 제약이 있었다.
## return을 할 때 for문을 사용하여 return을 해야하는데 이를 해결하지 못하였다.
## 결국 해결하지 못했는데 오기가 생겨서 일단 for 문을 10개 만들어서 풀고 답을 맞춘 뒤 구글링을 하고싶었다.
## 아래 for문은 5개의 수에 관한 알고리즘이고 실제 코드는 for 문이 5개 더 있다. 보기 흉측하여 생략하였다.

c = []
a6 = ["0","1",'2','3','4']
    for i3 in range(len(a3)):
        aa3 = a3[i3]
        bb3 = a3[:]
        del bb3[i3]
        a2 = bb3
        for i2 in range(len(a2)):
            aa2 = a2[i2]
            bb2 = a2[:]
            del bb2[i2]
            a1 = bb2
            for i1 in range(len(a1)):
                aa1 = a1[i1]
                bb1 = a1[:]
                del bb1[i1]
                d = bb1
                    for i in range(len(a)):
                        aa = a[i]
                        bb = a[:]
                        del bb[i]
                        bb.append(aa)
                        bb.append(a1[i1])
                        bb.append(a2[i2])
                        bb.append(a3[i3])
                        c.append(bb)

for i in range(len(c)):
    c[i] = "".join(c[i])
abc = list(map(int,c))
abc.sort()
print(abc[int(1e6)-1])  ## 2783915460

## 답을 맞춘 후 thread도 찾아보고 구글링도 해보았는데 이쁜 코드를 꽤나 찾기 힘들었다.
## itertools 모듈의 permutations 이라는 메소드를 이용하거나 순서대로 백만번째의 수를 찾고 끝을 내거나 하는 알고리즘이 많았다.
## 마침내 재귀함수를 이용한 아주 멋있고 이쁜 코드를 찾았다.
## 비록 코드를 완전히 이해하지는 못하였지만 어느 정도 구동 방식을 알아차렸다.
array=[0,1,2,3,4,5,6,7,8,9]
results=[]
def generate(k, A):
    if k==1:
        results.append(str(A))
    else:
        generate(k-1,A)             ## 내가 가장 잘못 생각한 부분이 이 부분이다. array를 계속 줄여나가려고 하니 return을 만들기 힘들었다.
                                    ## 이 코드는 array를 가만히 두고 array 내의 순서를 계속 바꿔 수를 생산해냈다.
        for i in range(k-1):        ## k 가 1이면 바로 생산해내고 k가 2이면 앞의 두 개의 순서를 바꿔 생산, k가 3이면 앞의 세 개의 순서를 바꿈
                                    ## 쭉쭉 이어나가 10개의 순서를 모두 바꿀 수 있는 알고리즘이다.
            if k%2==0:              ## k가 짝수면 아래와 같이 바꾼다.
                b=A[i]
                A[i]=A[k-1]
                A[k-1]=b
            else:                   ## k가 홀수면 맨 처음과 맨 끝의 수를 바꾼다.
                b=A[0]
                A[0]=A[k-1]
                A[k-1]=b
            generate(k-1,A)         ## 위의 for 구문으로 모든 index의 순서를 바꿔 생산해내는 코드를  수 있다.

generate(10,array)
results.sort()
print(results[999999])          ## [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]

## 오늘도 재야의 고수들 앞에서 한없이 작아진 하루였다.
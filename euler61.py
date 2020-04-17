## Q61
## 8128, 2882, 8281 세 숫자에는 세 가지 성질
## 1. 각 숫자의 뒤 두 자리와 다음 숫자의 앞 두 자리가 같다. 순환적으로(8281 -> 8128도 순환)
## 2. 각 숫자 모두 서로 다른 다각수
## 3. 이처럼 순환하는 네 자리의 세 수는 위의 수들이 유일
## 위와 같이 순환하면서 모두 서로 다른 다각수인 6개의 유일한 순서쌍의 합
## 삼각수	P3,n = n(n+1)/2, 사각수 P4,n = n2, 오각수 P5,n = n(3n−1)/2 등등,, 팔각수까지 공식 나옴
## 먼저 polygon인지 아닌지 확인할 함수를 만든다. 그런데 하나의 수가 여러 다각수일 수 있기때문에 list로 반환.
## 답을 만들 list에는 두 가지의 리스트를 붙인다. 하나는 순환할 숫자 순서쌍, 다른 하나는 각 수의 n각수의 n
## 그래서 계속 마지막의 순서쌍의 수의 끝 두 자리에 00~99를 붙여 네 자리 수를 만들고 다각수인지 확인, 이 수의 n각수의 n을 앞선 순서쌍의 n 리스트에서 확인
## 깔끔하게 나오기는 해서 뿌듯하긴 하지만 더 알고리즘을 줄일 수 있는지 계속 생각해봐야겠다.

def is_Polygon(n):                                          ## list 또는 False로 반환
    polygon = []
    if ((-1 + ((1 + 8 * n) ** 0.5)) / 2).is_integer():
        polygon.append(3)

    if (n ** 0.5).is_integer():
        polygon.append(4)

    if ((1 + ((1 + 24 * n) ** 0.5)) / 6).is_integer():
        polygon.append(5)

    if ((1 + ((1 + 8 * n) ** 0.5)) / 4).is_integer():
        polygon.append(6)

    if ((3 + ((9 + 40 * n) ** 0.5)) / 10).is_integer():
        polygon.append(7)

    if ((2 + ((4 + 12 * n) ** 0.5)) / 6).is_integer():
        polygon.append(8)

    if polygon:
        return polygon
    else:
        return False

import time

start = time.time()

polygon_number = []                                                             ## 우선 네 자리의 다각수를 뽑음
ans_list = []                                                                   ## 나중에 쓸 답 순서쌍 list
for i in range(1000, 10000):
    if is_Polygon(i):
        polygon_number.append(i)

for num in polygon_number:                                                      ## 시작
    first_num = str(num)                                                        ## 처음 수를 str로 넣음

    polygon_chain = [[[first_num], [is_Polygon(int(first_num))[0]]]]            ## 예를 들면 [[[8128],[3]]] 으로 들어감
    cnt = 1                                                                     ## 6번 반복할 cnt 이미 하나가 들어가있어서 1부터
    while cnt < 6:
        cnt += 1
        temp_chain = []                                                         ## 임시 list를 만들어줌
        for j in range(len(polygon_chain)):                                     ## 위의 예라면 j에 0

            for i in range(100):                                                ## 00~99까지
                num_list = polygon_chain[j][0][:]                               ## [8128]이 들어감
                poly_list = polygon_chain[j][1][:]                              ## [3]이 들어감
                if i < 10:                                                      ## 인위적으로 네 자리를 만들기 때문에 나눠줌
                    temp_num = polygon_chain[j][0][-1][-2:] + "0" + str(i)      ## 마지막 수의 끝 두 자리 28 + 0i
                else:
                    temp_num = polygon_chain[j][0][-1][-2:] + str(i)            ## 또는 28 + i
                if is_Polygon(int(temp_num)) and int(temp_num) > 1000:          ## temp_num이 다각수이고 네 자리 수면
                    temp_poly = is_Polygon(int(temp_num))                       ## 이 수의 다각수 리스트를 만들어줌
                    for poly in temp_poly:                                      ## 여러 다각수일 수 있기때문에
                        if poly not in poly_list:                               ## 앞선 리스트에서 이 다각수가 없다면
                            num_list.append(temp_num)                           ## num_list에 append [8128, 2882] 등등
                                                                                ## 여러개 나오긴 한다.
                            poly_list.append(poly)                              ## poly_list에도 append [3, 5] 등 나타남
                            temp_chain.append([num_list, poly_list])            ## 이 만든 리스트를 temp_chain에 붙여줌
                            ## ex) [[[8128,2850], [3,6]],[[8128,2882],[3,5]]] 등등 나타난다.

        polygon_chain = temp_chain[:]                       ## 모두 polygon_chain에 전달
        if not polygon_chain:                               ## 6까지 가는 중에 한 번이라도 끊기면 스탑
            break
    for num_check in polygon_chain:                         ## 마지막 확인 작업 6번째 순서쌍과 1번째 순서쌍의 순환 여부 확인
        if num_check[0][0][:2] == num_check[0][-1][-2:]:
            print(num_check)
            ans_list.append(num_check[0])

for ans_num_list in ans_list:
    sum_of_num = 0
    for n in ans_num_list:
        sum_of_num += int(n)
    print(sum_of_num)

end = time.time() - start
print(end)

## [['2882', '8256', '5625', '2512', '1281', '8128'], [5, 3, 4, 7, 8, 6]]
## [['8256', '5625', '2512', '1281', '8128', '2882'], [3, 4, 7, 8, 6, 5]]
## 28684
## 28684
## 2.1621789932250977

## 유일하다고해서 봤는데 두 개가 나왔다. 확인해보니 다른 수끼리 순서만 바뀌고 같은 순서쌍이었다.
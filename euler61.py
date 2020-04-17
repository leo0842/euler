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

def is_Polygon(n):
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

polygon_number = []
ans_list = []
for i in range(1000, 10000):
    if is_Polygon(i):
        polygon_number.append(i)
for num in polygon_number:
    first_num = str(num)

    polygon_chain = [[[first_num], [is_Polygon(int(first_num))[0]]]]
    cnt = 1
    while cnt < 6:
        cnt += 1
        temp_chain = []
        for j in range(len(polygon_chain)):

            for i in range(100):
                num_list = polygon_chain[j][0][:]
                poly_list = polygon_chain[j][1][:]
                if i < 10:
                    temp_num = polygon_chain[j][0][-1][-2:] + "0" + str(i)
                else:
                    temp_num = polygon_chain[j][0][-1][-2:] + str(i)
                if is_Polygon(int(temp_num)) and int(temp_num) > 1000:
                    temp_poly = is_Polygon(int(temp_num))
                    for poly in temp_poly:
                        if poly not in poly_list:
                            num_list.append(temp_num)
                            poly_list.append(poly)
                            temp_chain.append([num_list, poly_list])

        polygon_chain = temp_chain[:]
        if not polygon_chain:
            break
    for num_check in polygon_chain:
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
## Q11
## The greatest product in the same direction

raw_grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48""" ##raw_grid

raw_grid = raw_grid.replace("\n", " ")                  ## "\n" 부터 제거
raw_grid_array = raw_grid.split(" ")                    ## " "로 쪼개서 array로 만든다.
grid_array = []
for i in raw_grid_array:                                ## 한 자리 수는 자리수를 맞추기 위해 앞에 0이 붙어있다. 파이썬은 이를 파악하지
    if i[0] == '0':                                     ## 못하기 때문에 이를 처리해준다.
        grid_array.append(i[1])
    else:
        grid_array.append(i)


def to_int(array):                                      ## str인 숫자들을 int로 바꿔주는 함수를 만든다.
    for i in range(len(array)):
        array[i] = int(array[i])
    return array


array = to_int(grid_array)                              ## 함수에 적용


def grid_product(array, rows=20, prod_num=4):           ## grid_product라는 함수를 만든다. array, rows, prod_num을 인자로 받게끔
    n = rows

    num = prod_num

    product_list = []

    for i in range(len(array)):                         ## 반복문의 시작 첨부터 끝까지 할 예정

        if (i + (num - 1)) % n not in range(num - 1):   ## 횡방향 곱을 할 예정. 곱할 수 중 마지막 수의 인덱스가 범위를 넘어가면 False

            right_digit = 1                             ## 곱해줄 수 변수지정

            for j in range(i, i + num):                 ## 해당 인덱스부터 곱할 갯수까지 범위로 지정
                right_digit *= array[j]                 ## 다다닥 곱함

            product_list.append(right_digit)            ## product_list에 붙임

        if (i + n * (num - 1)) < n * n:                 ## 종방향 곱을 할 예정. 가장 아래 있는 수의 인덱스가 범위를 넘어가면 False

            down_digit = 1                              ## 변수 지정

            for j in range(i, i + n * num, n):          ## n만큼, 즉 아래 줄의 수만큼 step을 두는 range

                down_digit *= array[j]                  ## 다다닥

            product_list.append(down_digit)

        if ((i + (num - 1)) % n not in range(num - 1)) and ((i + n * (num - 1)) < n * n):   ## 오른쪽 아래로 곱할 예정

            rdiag_digit = 1

            for j in range(i, i + n * num, n + 1):      ## 줄 + 1만큼의 step

                rdiag_digit *= array[j]

            product_list.append(rdiag_digit)

        if (i % n not in range(num - 1)) and ((i + n * (num - 1)) < n * n):     ## 위와 비슷 왼쪽 아래로 곱할 예정

            ldiag_digit = 1

            for j in range(i, i + n * (num - 1), n - 1):    ## 줄 - 1만큼의 step

                ldiag_digit *= array[j]

            product_list.append(ldiag_digit)

    return (product_list)


array = to_int(grid_array)                              ## to_int 함수 적용
for i in range(3, 6):                                   ## 3부터 5개로 곱해봄 위의 문제는 4개 곱하는 거
    print(max(grid_product(array, prod_num=i)))
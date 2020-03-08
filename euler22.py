## Q22
## 이름에 점수 부여하고 모든 점수 더하기

f = open("names.txt", "r")                      ## 파일 다운받아서 "r"로 오픈
names_raw = f.read()                            ## 읽어온다.
names_raw = names_raw.replace('"', '')          ## 텍스트파일의 내용은 이름들. 근데 이름들이 ""로 묶여있어서 "를 다 제거해줌
names_list = names_raw.split(",")               ## 콤마로 구분되어있어서 콤마로 split
sorted_names = sorted(names_list)               ## 순서대로 점수를 부여할 것이기 때문에 sorted

##
alphabet = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z" ## 쌍따옴표쓰기 귀찮아서 이렇게 만들고 split할 예정
alphabet = alphabet.split(",")                  ## 스플릿

alphabet_point = defaultdict()                  ## alphabet의 순서에 따른 점수를 부여할 것이기에 dictionary 생성

for i in alphabet:
    alphabet_point[i] = alphabet.index(i) + 1   ## index가 0부터 시작하기때문에 +1

##
point_list = []                                 ## 점수를 붙일 리스트 생성

for name in sorted_names:                       ## sorted_names 안의 순서대로 name

    points = 0                                  ## 점수 더할 변수

    for char in name:                           ## name 스트링의 순서대로 char
        points += alphabet_point[char]          ## dictionary 에서 찾아서 그 점수를 더함

    points *= (sorted_names.index(name) + 1)    ## 해당 이름의 순서 index도 더하라고 해서 더함

    point_list.append(points)                   ## 점수를 point_list에 붙여줌

print(sum(point_list))          ##871198282
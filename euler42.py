## Q42
## 주어진 단어들을 알파벳별로 점수를 내서 합한 값이 삼각수인 단어들의 개수

from collections import defaultdict

## 파일 불러오기
file = open("words.txt", "r")
words = file.read()
words = words.replace('"', "")
words = words.split(",")

## 알파벳 별 점수 dictionary에 넣기
alphabet = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
alphabet = alphabet.split(",")
alphabet_point = defaultdict()
for i in alphabet:
    alphabet_point[i] = alphabet.index(i) + 1

## 삼각수의 범위를 지정하기 위해 가장 길이가 긴 수를 찾는다.
max_len = 0

for i in words:
    if len(i) > max_len:
        max_len = len(i)

## 삼각수 범위 지정
triple = []
n = 0
triple_num = 0

while triple_num < max_len * alphabet_point["Z"]: ## 길이 * Z의 포인트까지를 범위로 지정
    n += 1
    triple_num = (1 / 2) * (n) * (n + 1)
    triple.append(int(triple_num))

triple_words = []

for word in words:
    word_point = 0
    for alphabet in word:
        word_point += alphabet_point[alphabet]      ## 알파벳별로 점수를 더함
    if word_point in triple:                        ## 삼각수리스트에 더한 점수가 있으면
        triple_words.append(word)                   ## append

print(len(triple_words))    ## 162

## 오늘은 별로 설명할 것이 없당.
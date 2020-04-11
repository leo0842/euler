## Q54
## 포커 결과 내기.
## 매우 오래 걸렸다.. 깔끔해보이지도 않는당,,, ㅠㅡㅠ
## 지속적으로 업데이트

from collections import defaultdict, Counter

file = open("poker.txt", "r")
poker = file.read()
poker = poker.split("\n")
value_index = defaultdict()
a = "2,3,4,5,6,7,8,9,T,J,Q,K,A"
a = a.split(",")
n = 1
for i in a:
    value_index[i] = n
    n += 1

rank_index = defaultdict()
ranks = "RF,SF,FK,FH,Fl,St,TK,TP,OP,HC"
ranks = ranks.split(",")
n = len(ranks)
for i in ranks:
    rank_index[i] = n
    n -= 1

suit_index = defaultdict()
suits = "C,D,H,S"
suits = suits.split(",")
n = 0
for i in suits:
    suit_index[i] = n
    n += 1


def rank_generator(value, suit):
    global value_raw
    if value == list(range(9, 14)) and 5 in suit:
        return "RF"
    if (len(set(value)) == 5) and (value[-1] - value[0] == 4) and (5 in suit):
        return "SF"
    if (value == [1, 2, 3, 4, 13]) and (5 in suit):
        return "SF"
    value_count = list(Counter(value).values())
    if 4 in value_count:
        return "FK"
    if (3 in value_count) and (2 in value_count):
        return "FH"
    if 5 in suit:
        return "Fl"
    if (len(set(value)) == 5) and (value[-1] - value[0] == 4):
        return "St"
    if value == [1, 2, 3, 4, 13]:
        return "St"
    if 3 in value_count:
        for i, j in Counter(value).items():
            if j == 3:
                value_number = i
        for key, values in value_index.items():
            if value_number == values:
                value_raw = key
        return "TK" + value_raw

    if (2 in value_count) and len(value_count) == 3:
        value_number = 0
        for i, j in Counter(value).items():
            if j == 2:
                if value_number < i:
                    value_number = i

        for key, values in value_index.items():
            if value_number == values:
                value_raw = key

        return "TP" + value_raw

    if (2 in value_count):
        value_number = 0
        for i, j in Counter(value).items():
            if j == 2:
                value_number = i

        for key, values in value_index.items():
            if value_number == values:
                value_raw = key
        return "OP" + value_raw
    value_number = 0
    for i, j in Counter(value).items():
        if value_number < i:
            value_number = i
    for key, values in value_index.items():
        if value_number == values:
            value_raw = key
    return "HC" + value_raw

sungsan = []
jubeom = []
for i in poker:
    sungsan.append(i.split(" ")[:5])
    jubeom.append(i.split(" ")[5:])

cnt = 0
cnt2 = 0
for i in range(1000):
    sungsan_value = []
    sungsan_suit = []
    for j in sungsan[i]:
        sungsan_value.append(j[0])
        sungsan_suit.append(j[1])

    for k in range(len(sungsan_value)):
        sungsan_value[k] = value_index[sungsan_value[k]]

    sungsan_value_result = sorted(sungsan_value)

    sungsan_suit_count = Counter(sungsan_suit)
    sungsan_suit_result = list(sungsan_suit_count.values())

    sungsan_rank = rank_generator(sungsan_value_result, sungsan_suit_result)

    jubeom_value = []
    jubeom_suit = []
    for j in jubeom[i]:
        jubeom_value.append(j[0])
        jubeom_suit.append(j[1])

    for k in range(len(jubeom_value)):
        jubeom_value[k] = value_index[jubeom_value[k]]

    jubeom_value_result = sorted(jubeom_value)

    jubeom_suit_count = Counter(jubeom_suit)
    jubeom_suit_result = list(jubeom_suit_count.values())

    jubeom_rank = rank_generator(jubeom_value_result, jubeom_suit_result)
    if rank_index[sungsan_rank[:2]] > rank_index[jubeom_rank[:2]]:
        cnt += 1

    elif rank_index[sungsan_rank[:2]] == rank_index[jubeom_rank[:2]]:
        if value_index[sungsan_rank[2]] > value_index[jubeom_rank[2]]:
            cnt += 1
        elif value_index[sungsan_rank[2]] == value_index[jubeom_rank[2]]:
            su = []
            ju = []
            for i, j in zip(sungsan_value_result, jubeom_value_result):
                if i != value_index[sungsan_rank[2]]:
                    su.append(i)
                if j != value_index[jubeom_rank[2]]:
                    ju.append(j)
            if max(su) > max(ju):
                cnt += 1
            else:
                cnt2 += 1

        else:
            cnt2 += 1
    else:
        cnt2 += 1

print(cnt, cnt2)        ## 376 624
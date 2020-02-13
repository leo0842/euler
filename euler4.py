## Q4
## 세자리 수 곱으로 만들 수 있는 최대 대칭수
pali_array = []
for i in range(999,9,-1):
    for j in range(i,9,-1):
        TF_array = []
        multi = i * j
        multi_str = str(multi)
        len_multi = len(multi_str)
        if len_multi != 6:
            break
        else:
            for k in range(int(len_multi/2)):
                if multi_str[k] == multi_str[len_multi-k-1]:
                    TF_array.append(True)
                else:
                    TF_array.append(False)
            if all(TF_array):
                pali_array.append(multi)
print(max(pali_array))

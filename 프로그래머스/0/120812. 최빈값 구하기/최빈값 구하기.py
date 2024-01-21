def solution(array):
    dic = {i:array.count(i) for i in set(array)}
    freq = list(dic.values())
    max_freq = max(freq)

    if freq.count(max_freq)>=2:
        return -1
    else:
        for k, v in dic.items(): 
            if v == max_freq:
                return k
    

def solution(array):
    dic = {i:array.count(i) for i in set(array)}
    freq = list(dic.values())
    max_freq = max(freq)
    print(dic)
    print(freq)
    print(max_freq)
    answer = 0
    if freq.count(max_freq)>=2:
        return -1
    else:
        for k, v in dic.items(): 
            if v == max_freq:
                return k
    
#     return -1 if freq.count(max_freq) >= 2 else dic
    
#     [key for key, value in mydict.items() if value == val]
    
    # return -1 if freq_dict.count(max_freq)>=2 else freq_dic[]
    
    # if freq.count(max(freq)) >= 2:
    #     answer = -1
    # else:
    #     answer = max(freq)
    # print(answer)
#     for i in set(array):
#         if max < array.count(i):
#             max = array.count(i)
        
#     return max
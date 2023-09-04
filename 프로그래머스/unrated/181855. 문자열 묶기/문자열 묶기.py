def solution(strArr):
    len_dic = {}
    for i in strArr:
        if len_dic.get(len(i)) == None:
            len_dic[len(i)] = 1
        else:
            len_dic[len(i)]+=1
    return max(len_dic.values())

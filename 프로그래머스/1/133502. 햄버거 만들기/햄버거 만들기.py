def solution(ingredient):
    answer = 0
    i = 0
    while i <= len(ingredient) - 4:
        if ingredient[i:i+4] == [1,2,3,1]:   # 빵-야채-고기-빵 (1-2-3-1)
            del ingredient[i:i+4]
            answer += 1
            i  = max(0, i-3)
        else:
            i +=1 
            
    # for i,v in enumerate(ingredient):
    #     if (v == start) and (ingredient[i:i+4]==[1, 2, 3, 1]): 
    #         del ingredient[i:i+4]
    #         answer += 1
    
    return answer
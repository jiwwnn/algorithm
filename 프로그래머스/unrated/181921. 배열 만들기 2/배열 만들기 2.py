def solution(l, r):
    answer = []
    num = '05'
    for i in range(l, r+1):
        count = 0
        for j in str(i):
            if j not in num: 
                continue
            count +=1
        if count == len(str(i)):
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
    return answer

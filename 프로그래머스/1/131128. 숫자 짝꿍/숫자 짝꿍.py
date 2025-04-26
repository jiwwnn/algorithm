def solution(X, Y):
    answer = ''
    
    X_set = set(X)
    Y_set = set(Y)
    
    for i in X_set:
        if i in Y_set:
            count = min(X.count(i), Y.count(i))
            answer += i * count
        
    answer = ''.join(sorted(answer, reverse=True))
    
    if not answer:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer
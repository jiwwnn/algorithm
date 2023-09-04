def solution(s):
    answer = 0
    s = s.split(' ')
    for i, v in enumerate(s):
        if v == 'Z':
            answer -= int(s[i-1])
        else:            
            answer += int(v)
    return answer
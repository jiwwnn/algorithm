def solution(n):
    answer = ''
    for i in range(n):
        if i == 0:
            answer += '수'
        elif i > 0 and answer[i-1] == '박':
            answer += '수'
        elif i > 0 and answer[i-1] == '수':
            answer += '박'
    return answer
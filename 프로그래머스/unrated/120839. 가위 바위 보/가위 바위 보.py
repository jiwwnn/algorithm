def solution(rsp):
    win_case = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    
    for i in rsp:
        answer += win_case[i]
    return answer
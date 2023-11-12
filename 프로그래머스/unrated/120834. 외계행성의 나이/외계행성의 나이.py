def solution(age):
    num = '0123456789'
    alphabet = 'abcdefghij'
    dic = dict(zip(num, alphabet))
    
    answer = ''
    for i in str(age):
        answer += dic[i]    
    return answer
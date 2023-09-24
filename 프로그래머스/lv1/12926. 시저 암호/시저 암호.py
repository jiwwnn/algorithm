def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        if 65 <= ord(i) <= 90 and ord(i) + n > 90:
            i = 65 + ((ord(i)+n)-90-1)
        elif 97 <= ord(i) <= 122 and ord(i) + n > 122:    
            i = 97 + ((ord(i)+n)-122-1)
        else:        
            i = ord(i) + n
        answer += chr(i)
    print(answer)
    return answer
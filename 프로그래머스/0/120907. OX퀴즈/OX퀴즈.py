def solution(quiz):
    answer = []
    result = 0
    for i in quiz:
        x = str(i).split()
        
        if x[1] == '+':
            result = int(x[0]) + int(x[2])
        else:
            result = int(x[0]) - int(x[2])
        
        if result == int(x[-1]):
            answer.append('O')
        else:
            answer.append('X')
        

    return answer
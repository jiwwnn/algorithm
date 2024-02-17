def solution(emergency):
    answer = []
    emergency1 = sorted(emergency.copy(), reverse=True)
    for i in emergency:
        answer.append(emergency1.index(i)+1)
    return answer
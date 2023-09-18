def solution(n):
    answer = 0
    for i in range(n%2, n+1, 2):
        if n%2 == 0:
            answer += i**2
        else:
            answer += i
    return answer
def solution(A, B):
    # A는 오름차순, B는 내림차순 정렬
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer

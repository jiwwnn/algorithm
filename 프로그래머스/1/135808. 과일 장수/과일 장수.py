def solution(k, m, score):
    score.sort(reverse=True) # 점수 높은 순서로 정렬
    
    price = 0
    for i in range(0, len(score) - m + 1, m): # 시작 인덱스 한계선 설정
        box = score[i:i + m] 
        price += min(box) * m # 최소 이익 점수를 기준으로 계산
    return price
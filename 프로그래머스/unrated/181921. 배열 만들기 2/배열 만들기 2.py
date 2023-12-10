def solution(l, r):
    answer = []
    num = '05'
    for i in range(l, r+1):       # 5~555까지 for문 돌기
        count = 0                 # 0 or 5 포함여부 카운트할 변수 생성
        for j in str(i):          # 정수를 문자로 변환
            if j not in num:      # '05'에 해당 문자 포함여부 확인
                continue
            count +=1             # 있을 시 카운트 +1
        if count == len(str(i)):  # 카운트한 개수 == 정수 자리수(즉, 전체 자리수가 다 0 or 5)
            answer.append(i)      # 해당 정수 answer 리스트에 추가
    
    if len(answer) == 0:          # answer 리스트에 담긴 정수 없을 경우 
        answer.append(-1)         # -1 반환
    return answer

def solution(topping):
    answer = 0

    right = {}
    left = {}
    
    for t in topping:
        right[t] = right.get(t, 0) + 1 # dict에서 특정 key 값에 해당하는 value 가져옴

    for t in topping:
        left[t] = left.get(t, 0) + 1

        right[t] -= 1
        if right[t] == 0:
            del right[t]

        # 토핑 종류 개수 비교
        if len(left) == len(right):
            answer += 1

    return answer

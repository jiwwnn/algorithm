from collections import Counter

# def solution(want, number, discount):
#     answer = 0
    
#     for i in range(len(discount)):
#         x = Counter(discount[i:i+10])
#         if x[want[i]] != number[i]:
#             break
#         answer+= 1
#     return answer

def solution(want, number, discount):
    target = dict(zip(want, number))  
    # print(target)
    answer = 0
    for i in range(len(discount) - 9):  # 윈도우 시작점의 유효 범위
        if Counter(discount[i:i+10]) == target:
            # print(Counter, target)
            answer += 1
    return answer

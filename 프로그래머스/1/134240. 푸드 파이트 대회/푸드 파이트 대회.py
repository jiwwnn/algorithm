# def solution(food):
#     answer = []
#     for i, v in enumerate(food[1:]):
#         if v >= 2:
#             count = v // 2
#             answer.extend([i+1]*count)
            

#     water_idx = len(answer) // 2
#     answer.insert(water_idx, 0)     
#     answer = str(answer)
#     return answer



# def solution(food):
#     answer = []
#     for i, v in enumerate(food[1:]):
#         if v >= 2:
#             if v % 2 != 0:
#             v -= 1
#             for num in range(v):
#                 answer[0].insert(i+1) # 빈 리스트이므로 인덱스 접근 X
#                 answer[-1].insert(i+1)

#     water_idx = len(answer) // 2
#     answer.insert(water_idx, 0)     
#     answer = str(answer)
#     return answer


def solution(food):
    left = []
    for i, v in enumerate(food[1:]):
        if v >= 2:
            count = v // 2
            left.extend([i+1]*count)
        
    answer = left + [0] + left[::-1] 
    return ''.join(map(str, answer))
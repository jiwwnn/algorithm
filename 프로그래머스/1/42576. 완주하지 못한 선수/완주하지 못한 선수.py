def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


# from collections import Counter

# def solution(participant, completion):
#     p_counter = Counter(participant) # 리스트에서 해당 요소가 몇 번 나왔는지 딕셔너리로 저장
#                                      # {'leo': 1, 'kiki': 1, 'eden': 1}
#     c_counter = Counter(completion)
#                                      # {'eden': 1, 'kiki': 1}
        
#     answer = p_counter - c_counter   # {'leo': 1}
#     return list(answer.keys())[0]

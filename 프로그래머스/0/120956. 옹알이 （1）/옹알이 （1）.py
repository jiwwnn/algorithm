# def solution(babbling):
    # count = 0
    # say = ['aya', 'ye', 'woo', 'ma']
    # for i, word1 in enumerate(say):
    #     lst = say.pop(i)
    #     for word2 in lst:
    #         say.append(word1 + word2)
    # print(say) # 시간 초과 (실행시간 10초 초과)
    
#     for i, b in enumerate(babbling):
#         for s in say:
#             # 일치하는 단어 제거
#             if s == b:
#                 count +=1
#                 babbling.pop(i)
#             # 부분적으로 일치하는 부분 제거
#             if s in b:
#                 babbling[i] = b.replace(s, '')

#     for i, b in enumerate(babbling):
#         for i in say:
#             if s == b:
#                 count+=1
                
import re


def solution(babbling):
    answer = 0
    for char in babbling:
        if re.match(r"^(aya|ye|woo|ma)+$", char):
            answer += 1
    return answer
                



    
    
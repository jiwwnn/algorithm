# def solution(prices):
#     answer = []
#     for i,v in enumerate(prices):
#         count = 0
#         prior = v
#         for j in prices[i+1:]:
#             count += 1
#             if j < prior:  
#                 break
#         answer.append(count)
#     return answer # 시간초과


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 인덱스를 저장하는 스택

    for i, price in enumerate(prices):
        # 스택에 있는 값들과 비교해서, 떨어졌으면 꺼내면서 정답 확정
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 안 떨어진 가격들 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

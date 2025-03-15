# def solution(k, score):
#     post = []
#     honor = []
    
#     for i in score:
#         honor.append(i)
#         honor.sort() # 효율성 문제
        
#         if len(honor) > k:
#             honor.pop(0)
#         post.append(honor[0])
#     return post


# heapq 구조 활용
import heapq
def solution(k, score):
    post = []
    honor = []
    
    for i in score:
        heapq.heappush(honor, i)
        
        if len(honor) > k:
            heapq.heappop(honor)
        post.append(honor[0])
    return post

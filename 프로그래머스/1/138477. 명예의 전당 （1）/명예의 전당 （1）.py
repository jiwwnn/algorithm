def solution(k, score):
    post = []
    honor = []
    
    for i in score:
        honor.append(i)
        honor.sort()
        
        if len(honor) > k:
            honor.pop(0)
        post.append(honor[0])
    return post
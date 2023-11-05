def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    answer = []
    for i in photo:
        score = 0
        for j in i:
            try:
                score += score_dict[j]
            except:
                pass
        answer.append(score)
    return answer
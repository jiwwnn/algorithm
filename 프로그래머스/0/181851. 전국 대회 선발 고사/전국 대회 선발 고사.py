def solution(rank, attendance):
    lst = []
    for r,a in zip(rank, attendance):
        if a != 0:        
            lst.append(r)
    lst = sorted(lst)[:3]
    return 10000 * rank.index(lst[0]) + 100 * rank.index(lst[1]) + rank.index(lst[2])

    
def solution(d, budget):
    cost = 0
    count = 0
    d.sort()
    for i in d:
        cost += i
        if cost > budget:
            break
        count += 1
    return count
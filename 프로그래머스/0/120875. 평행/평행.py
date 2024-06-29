def solution(dots):
    def calc_slop(dot1, dot2):
        p1, p2 = dot1
        p3, p4 = dot2
        slop = (p4 - p2) / (p3 - p1)
        return slop
    
    i, j, k, l = dots
    check1 = calc_slop(i, j) == calc_slop(k, l)
    check2 = calc_slop(i, k) == calc_slop(j, l)
    check3 = calc_slop(j, k) == calc_slop(i, l)
        
    if 1 in [check1, check2, check3]:
        return 1
    else:
        return 0
    
#     slops = []
#     for i in range(len(dots)):
#         for j in range(i+1, len(dots)):
#             p1, p2 = dots[i]
#             p3, p4 = dots[j]
#             slop = (p4 - p2) / (p3 - p1)
#             slops.append(slop)
    
#     for i in range(len(slops)):
#         for j in range(i+1, len(slops)):
#             if slops[i] == slops[j]:
#                 return 1
#     return 0
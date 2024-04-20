def solution(a, d, included):
    add_a, add_d = 0, 0
    for i, v in enumerate(included):
        add_a += a*v # 첫째항
        add_d += d*i*v # 공차항
    return add_a + add_d

# (3 + 4*0) (3 + 4*1) (3 + 4*2) (3 + 4*3) 
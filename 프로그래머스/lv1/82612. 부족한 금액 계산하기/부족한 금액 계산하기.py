def solution(price, money, count):
    total = 0
    
    # 총액 += 금액*횟수
    for num in range(1, count+1):
        total += price*(num)
        
    if total > money:
        return total-money
    else:
        return 0

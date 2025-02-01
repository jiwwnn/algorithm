def count_triplets(number, index=0, count=0, total=0):
    if count == 3:  # 숫자 3개를 선택했을 때
        return 1 if total == 0 else 0  # 합이 0이면 1을 반환
    
    if index >= len(number):  # 배열 범위를 벗어나면 종료
        return 0

    # 현재 숫자를 선택하는 경우와 선택하지 않는 경우로 나누어 탐색
    return count_triplets(number, index + 1, count + 1, total + number[index]) + count_triplets(number, index + 1, count, total)

def solution(number):
    return count_triplets(number)
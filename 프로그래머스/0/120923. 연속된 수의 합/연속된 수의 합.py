def solution(num, total):
    # n을 계산하기 위해 공식 사용
    n = (total - (num * (num - 1)) // 2) // num
    # n부터 시작해서 num개의 연속된 수를 리스트로 생성하여 반환
    return [n + i for i in range(num)]
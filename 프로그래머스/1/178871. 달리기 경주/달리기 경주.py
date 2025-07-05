def solution(players, callings):
    # 선수 이름 -> 등수 매핑 (딕셔너리)
    situ_dict = {v: k for k, v in enumerate(players)}
    
    for call in callings:
        idx = situ_dict[call]            # 불린 선수의 현재 등수
        front = players[idx - 1]         # 앞에 있는 선수

        # 선수 순위 바꾸기
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        # 딕셔너리 위치도 바꿔줘야 함
        situ_dict[call] -= 1
        situ_dict[front] += 1

    return players

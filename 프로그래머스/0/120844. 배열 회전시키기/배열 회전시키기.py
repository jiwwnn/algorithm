def solution(numbers, direction):
    if direction == 'right':
        num = numbers.pop()
        numbers.insert(0, num)
    else:
        num = numbers.pop(0)
        # print(numbers)
        numbers.append(num)
    return numbers    
def number_sum(data: list) -> int:
    result: int = 0
    for i in data:
        result += i
    return result
print(number_sum([1, 2, 3, 4, 5]))
def sort_numbers(numbers: list, reverse: bool = False) -> list:
    result = sorted(numbers,reverse=False)
    return result




nums = [3, 7, 10, -5, -8, 15, 22, 0]

print(sort_numbers(nums))
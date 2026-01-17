def filter_positive(numbers: list) -> list:
    result = []
    for item in numbers:
        if item.get("value", 0) > 0:
            result.append(item)
    return result


print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))

print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))
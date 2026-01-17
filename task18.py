def square_values(numbers: list) -> list:
    new_list = []
    for item in numbers:
        new_list.append({"value": item["value"] ** 2})
    return new_list


nums = ([{'value': 2}, {'value': 3}, {'value': 4}])

print(square_values(numbers=nums))
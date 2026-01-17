def filter_long_names(students: list, min_length: int = 5) -> list:
    result = []
    for name in students :
        if len(name) >= min_length :
            result.append(name)
    return result
    
names = ["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]

total = filter_long_names(students = names,min_length=4)
print(total)
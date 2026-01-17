def find_min_max(numbers: list) -> dict:
    result = {
       'max': max(numbers) ,
       'imn': min(numbers)
    }
    


    return result 



nums = [3, 7, 10, -5, -8, 15, 22]

print(find_min_max(numbers=nums))
def calculate_stats(numbers: list) -> dict:
    result = 0
    average = 0
    for num in numbers :
            result += num
            average +=1
            if average > 0:
              avg = result / average
    return {"sum": result, "average": average}



nums = [3, 7, 10, -5, -8, 15, 22]
result = calculate_stats(numbers=nums)
print(result)
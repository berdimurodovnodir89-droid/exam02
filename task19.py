def find_longest_name(names: list) -> str:
    result = max(names,key = len)
                 

    return result


names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']

print(find_longest_name(names=names))
def count_words(text: str) -> dict:
    result = {}
    text_lower = text.lower()
    words = text_lower.split()
    for i in words :
        if i in result:
         result[i] += 1
        else :
         result[i] = 1

    return result



words = "salom salom dunyo"

print(count_words(text = words))
def find_shortest_name_student(students: list) -> str:
     shortest_student = min(students, key=lambda x: len(x['name']))
     return shortest_student




students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]

print(find_shortest_name_student(students=students))
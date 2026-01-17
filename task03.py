def calculate_tax(salary: int) -> dict:
    if salary <= 5_000_000:
        rate = "0%"
        tax = 0
    elif salary <= 10_000_000:
        rate = "12%"
        tax = salary * 12 // 100
    elif salary <= 20_000_000:
        rate = "18%"
        tax = salary * 18 // 100
    else:
        rate = "25%"
        tax = salary * 25 // 100

    net = salary - tax
    return  {
        "gross": salary,
        "tax": tax,
        "net": net,
        "rate": rate }


salary = int(input("Salary: "))
result = calculate_tax(salary)
print(result)
    
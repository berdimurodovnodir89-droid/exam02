def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2

def main():
    num1 = float(input("Birinchi sonni kiriting: "))
    num2 = float(input("Ikkinchi sonni kiriting: "))
    operator = input("Operatorni kiriting (+, -, *, /): ")
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)

    elif operator == '*':
        print(num1 * num2)

    elif operator == '/':
        if num2 == 0:
            print("Nolga bolish mumkin emas")
        else:
            print(num1 / num2)

    else:
        print("Noto'g'ri operator kiritildi")


main()


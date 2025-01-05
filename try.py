#task1
try:
    number = int(input("Введіть число: "))
    if number < 0:
        raise ValueError("Факторіал від'ємного числа не визначений.")
    factorial = 1
    for i in range(1, number+ 1):
        factorial *= i
    print(f"Факторіал числа {number}: {factorial}")
except ValueError as e:
    print(f"Помилка: {e}")

#task2
def calculate_factorial_safe(number):
    try:
        if number < 0:
            raise ValueError("Факторіал від'ємного числа не визначений.")
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial
    except ValueError as e:
        return f"Помилка: {e}"

number = int(input("Введіть число: "))
result = calculate_factorial_safe(number)
print(result)

#task3-4
numbers = []
print("Введіть числа для списку (завершіть введення словом 'стоп'):")
while True:
    user_input = input()
    if user_input.lower() == "стоп":
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Будь ласка, введіть коректне число.")

while True:
    print("\nМеню:")
    print("1. Відобразити список")
    print("2. Отримати максимальне значення у списку")
    print("3. Отримати мінімальне значення у списку")
    print("4. Відобразити значення за індексом")
    print("5. Видалити елемент за індексом")
    print("6. Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print(f"Список: {numbers}")
    elif choice == "2":
        if numbers:
            print(f"Максимальне значення: {max(numbers)}")
        else:
            print("Список порожній.")
    elif choice == "3":
        if numbers:
            print(f"Мінімальне значення: {min(numbers)}")
        else:
            print("Список порожній.")
    elif choice == "4":
        try:
            index = int(input("Введіть індекс: "))
            print(f"Значення за індексом {index}: {numbers[index]}")
        except (ValueError, IndexError):
            print("Помилка: некоректний індекс.")
    elif choice == "5":
        try:
            index = int(input("Введіть індекс: "))
            removed = numbers.pop(index)
            print(f"Елемент {removed} видалено.")
        except (ValueError, IndexError):
            print("Помилка: некоректний індекс.")
    elif choice == "6":
        break
    else:
        print("Некоректний вибір.")

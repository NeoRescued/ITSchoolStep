import time

#task1
def odd_numbers_in_range(start, end):

    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

for odd in odd_numbers_in_range(1, 10):
    print(odd)

#task2
def values_out_of_range(lst, range_start, range_end):
    for value in lst:
        if not (range_start <= value <= range_end):
            yield value
my_list = [1, 5, 10, 15, 20, 25]
for value in values_out_of_range(my_list, 10, 20):
    print(value)

#task3
def horizontal_line(symbol):
    print(symbol * 20)


def vertical_line(symbol):
    for _ in range(10):
        print(symbol)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

user_symbol = input("Введіть символ для лінії: ")
line_type = input("Введіть тип лінії (горизонтальна або вертикальна): ").strip().lower()

if line_type == "горизонтальна":
    show_line(user_symbol, horizontal_line)
elif line_type == "вертикальна":
    show_line(user_symbol, vertical_line)
else:
    print("Невідомий тип лінії. Виберіть 'горизонтальна' або 'вертикальна'.")

#task4
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Початок вимірювання часу
        result = func(*args, **kwargs)
        end_time = time.time()  # Кінець вимірювання часу
        elapsed_time = end_time - start_time
        print(f"Час виконання: {elapsed_time:.6f} секунд")
        return result
    return wrapper

@timer_decorator
def get_even_numbers():
    return [number for number in range(0, 100001) if number % 2 == 0]
even_numbers = get_even_numbers()
print(even_numbers)

#task5
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() 
        elapsed_time = end_time - start_time
        print(f"Час виконання: {elapsed_time:.6f} секунд")
        return result
    return wrapper

@timer_decorator
def get_even_numbers_in_range(start, end):
    return [number for number in range(start, end + 1) if number % 2 == 0]

start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))

even_numbers = get_even_numbers_in_range(start_range, end_range)
print(even_numbers)
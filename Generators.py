import time

#task1
def even_numbers(start, end):

    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

for num in even_numbers(1, 10):
    print(num)

#task2
def values_in_range(lst, start, end):
    for item in lst:
        if start <= item <= end:
            yield item

my_list = [1, 5, 8, 12, 20, 25]
for val in values_in_range(my_list, 10, 20):
    print(val)

#task3

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

def check_value(value_to_check, function_to_call):
    return function_to_call(value_to_check)

number = 7

print(check_value(number, is_even))

print(check_value(number, is_odd))

#task4
def get_current_time():
    return time.strftime("%H:%M")

def add_stars(func):
    def wrapper():
        result = func()
        decorated_result = f"{'*' * 27}\n{result}\n{'*' * 27}"
        return decorated_result
    return wrapper

decorated_get_current_time = add_stars(get_current_time)

print(decorated_get_current_time())

#task5
def get_current_time():
    return time.strftime("%H:%M")

def add_stars(func):
    def wrapper():
        result = func()
        decorated_result = f"{'*' * 27}\n{result}\n{'*' * 27}"
        return decorated_result
    return wrapper

def add_dashes(func):
    def wrapper():
        result = func()
        decorated_result = f"{'-' * 27}\n{result}\n{'-' * 27}"
        return decorated_result
    return wrapper

decorated_with_stars = add_stars(get_current_time)
fully_decorated = add_dashes(decorated_with_stars)

print(fully_decorated())

#task6
def add_stars(func):
    def wrapper():
        result = func()
        decorated_result = f"{'*' * 27}\n{result}\n{'*' * 27}"
        return decorated_result
    return wrapper

def add_dashes(func):
    def wrapper():
        result = func()
        decorated_result = f"{'-' * 27}\n{result}\n{'-' * 27}"
        return decorated_result
    return wrapper

@add_dashes
@add_stars
def get_current_time():
    return time.strftime("%H:%M")

print(get_current_time())
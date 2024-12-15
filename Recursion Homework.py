import random

#task1
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(2, 3))

#task2
def sum_range(a, b):
    if a > b:
        return 0
    return a + sum_range(a + 1, b)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Sum of numbers from {a} to {b}: {sum_range(a, b)}")

#task3
def print_stars(n):
    if n <= 0:
        return ""
    return "*" + print_stars(n - 1)
n = int(input("Enter the number of stars: "))
print(print_stars(n))

#task4
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Хід гравця {current_player}")

        row = int(input("Введіть рядок (0, 1, 2): "))
        col = int(input("Введіть стовпець (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Переміг гравець {winner}!")
                break

            if is_draw(board):
                print_board(board)
                print("Нічия!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Некоректний хід. Спробуйте ще раз.")

tic_tac_toe()

#task5
def find_min_sum_index(numbers, index=0, min_sum=float('inf'), min_index=0):
    if index > len(numbers) - 10:
        return min_index
    current_sum = sum(numbers[index:index + 10])
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = index
    return find_min_sum_index(numbers, index + 1, min_sum, min_index)

numbers = [random.randint(0, 100) for _ in range(100)]
min_index = find_min_sum_index(numbers)
print(f"List: {numbers}")
print(f"Starting index of the sequence with the smallest sum: {min_index}")
print(f"Sequence: {numbers[min_index:min_index + 10]}")



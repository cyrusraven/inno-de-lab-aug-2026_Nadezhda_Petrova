# Task 5: The “Guess the Number” Game
import random

print('Я загадал число от 1 до 20. У тебя 5 попыток!')
random_num = random.randint(1, 20)  # Generate number

attempts = 5  # Max attempts
count = 1  # Initialize attempt counter

while attempts > 0:
    num = int(input(f'Попытка {count}. Введите число: '))  # Get user input a number

    if num == random_num:  # Check if the correct number
        print('Ты угадал! Отличная работа.')
        break  # Exit loop
    elif num > random_num:
        print(f'Слишком много! Осталось попыток: {attempts - 1}')
    else:
        print(f'Слишком мало! Осталось попыток: {attempts - 1}')

    attempts -= 1  # Decrease remaining attempts
    count += 1  # Increase attempt counter

    if attempts > 0:  # If game continues
        print()  # Print empty line for spacing

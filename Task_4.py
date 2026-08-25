# Task 4: Checking a number for evenness
num = input('Введите целое число: ')

if int(num) % 2 == 0:  # A condition that checks for the evenness of a number
    print(f'Число {num} - четное.')
else:  # If it is odd, then:
    print(f'Число {num} - нечетное.')

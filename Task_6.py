# Task 6: Calculator
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
operator = input('Введите оператор (+, -, *, /): ')

if operator == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif operator == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif operator == '/':
    if num2 == 0:  # Check the division by zero
        print('Ошибка: на ноль делить нельзя!')
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
else:
    print('Ошибка: неверный оператор!')  # Catching any other symbols

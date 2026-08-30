MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0):
    """
    This function calculates the total cost of a batch of discs and
    checks whether the limit has been exceeded.

    Args:
        quantity (int): The number of disks in the batch.
        rental_rate (float): The price of renting one disk.
        discount (float, optional): Discount rate (from 0 to 1). Default value is 0.0.
    Returns:
        tuple[float, bool]:
            final_sum (float): The final cost of the batch, rounded to 2 decimal places.
            is_limit (bool): True if final_sum exceeds MAX_RENTAL_BATCH_LIMIT, otherwise False.
    """
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    if final_sum > MAX_RENTAL_BATCH_LIMIT:
        is_limit = True
    else:
        is_limit = False
    result = (final_sum, is_limit)
    return result


if __name__ == "__main__":
    # Данные партий: (название, количество, цена, скидка)
    batches = [
        ("Academy Dinosaur", 30, 2.99, 0.0),
        ("Affair Prejudice", 40, 4.99, 0.1),
        ("Agent Truman", 10, 1.99, 0.0),
        ("African Egg", 50, 3.50, 0.2),
    ]

    print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

    # Positional arguments example
    sum1, exceed1 = calculate_rental_batch(30, 2.99)  # позиционные
    print(f"Партия 1 (Academy Dinosaur): Сумма {sum1:.2f}$. Превышение лимита: {exceed1}")

    # Keyword arguments example (explicitly named)
    sum2, exceed2 = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)  # именованные
    print(f"Партия 2 (Affair Prejudice): Сумма {sum2:.2f}$. Превышение лимита: {exceed2}")

    sum3, exceed3 = calculate_rental_batch(10, 1.99)
    print(f"Партия 3 (Agent Truman): Сумма {sum3:.2f}$. Превышение лимита: {exceed3}")

    sum4, exceed4 = calculate_rental_batch(50, 3.50, 0.2)  # скидка передана позиционно
    print(f"Партия 4 (African Egg): Сумма {sum4:.2f}$. Превышение лимита: {exceed4}")

from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine (film_name: str, days_overdue: Any, fine_rate: Any):
    """
        Safely calculates the overdue fine and return index for a film.

        The function attempts to convert `days_overdue` and `fine_rate` to floats.
        If conversion fails, division by zero occurs, or type errors arise,
        appropriate error messages are printed and None is returned.

        Handled errors:
            - ValueError: when conversion to float fails (e.g., non‑numeric string).
            - TypeError: when the input is of an unsupported type (e.g., list).
            - ZeroDivisionError: when `days_overdue` is zero.

        Args:
            film_name (str): Name of the film (used in error messages).
            days_overdue (Any): Raw input representing the number of overdue days.
            fine_rate (Any): Raw input representing the daily fine rate.

        Returns:
            Optional[Tuple[float, float]]:
                A tuple (total_fine, return_index) if successful,
                otherwise None.
    """
    try:
        numeric_days = float(days_overdue)
        numeric_rate = float(fine_rate)

        total_fine = numeric_days * numeric_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        return total_fine, return_index
    except ValueError as exc:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_name}': {exc}")
        return None

    except TypeError as exc:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_name}': {exc}")
        return None

    except ZeroDivisionError as exc:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_name}': {exc}")
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")

if __name__ == "__main__":
    # Test data: (film_name, days_overdue, fine_rate)
    test_cases = [
        ("Matrix", 5, 1.5),
        ("Inception", "пять", 2.0),
        ("Avatar", 0, 2.5),
        ("Interstellar", [3], 3.0),
    ]

    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

    for name, days, rate in test_cases:
        result = calculate_overdue_fine(name, days, rate)

        # If the calculation succeeded, print the formatted result
        if result is not None:
            fine, index = result
            print(f"Фильм: '{name}' | Итоговый штраф: {fine}$ | Индекс: {index}")

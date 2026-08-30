import time
from typing import Callable, Any, List, Dict, Union

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]):
    """
        Decorator that measures and logs the execution time of the wrapped function.

        The log message is printed in the format:
            <PERFORMANCE_LOG_PREFIX> Function '<func_name>' executed in <time> sec.

        Args:
            func (Callable[..., Any]): The function to be wrapped.

        Returns:
            Callable[..., Any]: The wrapped function that logs performance data.
    """

    def wrapper(*args: Any, **kwargs: Any):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        formatted_time = f'{elapsed_time:.{TIME_DECIMALS}f}'

        print(f"{PERFORMANCE_LOG_PREFIX} Function '{func.__name__}' executed in {formatted_time} sec.")

        return result

    return wrapper


@performance_logger
def get_sorted_report(data_sales: List[Dict[str, Union[str, float]]]):
    """
        Sorts a list of category-sales dictionaries in descending order of total_sales.

        Args:
            data (List[Dict[str, [str, float]]]): List of dictionaries, each containing
                'category' (str) and 'total_sales' (float).

        Returns:
            List[Dict[str, Union[str, float]]]: The sorted list (descending by total_sales).
            :param data_sales:
    """
    sorted_data = sorted(data_sales, key=lambda item: item["total_sales"], reverse=True)
    return sorted_data


if __name__ == "__main__":
    # Test datasets as specified
    test_sets = [
        # Set 1 (Standard)
        [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55}
        ],
        # Set 2 (Equal revenue)
        [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00}
        ],
        # Set 3 (Single element)
        [
            {"category": "Drama", "total_sales": 500.00}
        ]
    ]

    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

    for idx, dataset in enumerate(test_sets, start=1):
        print(f"--- ТЕСТ {idx} ---")
        # Call the decorated function; performance log will be printed automatically
        sorted_result = get_sorted_report(dataset)

        # Print the top categories
        print("Топ категорий по выручке:")
        for rank, item in enumerate(sorted_result, start=1):
            print(f"{rank}. {item['category']}: {item['total_sales']}")
        # Add a blank line between tests for readability (not strictly required)
        if idx != len(test_sets):
            print()

"""
Date Started: July 1, 2026

Python fundamentals and interview practice.
Focus: writing clean functions, clear variable names, and testing manually.
"""

def find_max(numbers):
    """
    Return the largest number in a non-empty list.

    Args:
        numbers: A list of integers or floats.

    Returns:
        The largest number in the list.
    """
    if not numbers:
        raise ValueError("numbers list cannot be empty")

    max_number = numbers[0]

    for current_number in numbers:
        if current_number > max_number:
            max_number = current_number

    return max_number


def find_min(numbers):
    """
    Return the smallest number in a non-empty list.

    Args:
        numbers: A list of integers or floats.

    Returns:
        The smallest number in the list.
    """
    if not numbers:
        raise ValueError("numbers list cannot be empty")

    min_number = numbers[0]

    for current_number in numbers:
        if current_number < min_number:
            min_number = current_number

    return min_number


def count_element(numbers, target):
    """
    Count how many times the target appears in the list.

    Args:
        numbers: A list of numbers.
        target: The number we want to count.

    Returns:
        The number of times target appears in numbers.
    """
    count = 0

    for current_number in numbers:
        if current_number == target:
            count += 1

    return count


def main():
    numbers = [4, 1, 5, 0, 1, -3]

    print(f"Maximum number: {find_max(numbers)}")
    print(f"Minimum number: {find_min(numbers)}")

    values = [1, 2, 2, 3, 2, 4]
    target = 2

    print(f"{target} appears {count_element(values, target)} times.")


if __name__ == "__main__":
    main()
"""
Problem 2: Find Min in a List of Numbers

Description:
Write a function called find_min that takes a list of numbers
as input and returns the smallest number in the list.

Example:
Input: numbers = [4, 1, 5, 0, 1, -3]
Output: -3

Logic:
1. Assume the first number is the minimum.
2. Go through each number in the list.
3. If the current number is smaller than min_number,
   update min_number to current_number.
4. After checking all numbers, return min_number.
"""


def find_min(numbers):
    """
    Return the smallest number in a non-empty list.
    """
    if not numbers:
        raise ValueError("numbers list cannot be empty")

    min_number = numbers[0]

    for current_number in numbers:
        if current_number < min_number:
            min_number = current_number

    return min_number


def main():
    numbers = [4, 1, 5, 0, 1, -3]
    print(f"Minimum number: {find_min(numbers)}")


if __name__ == "__main__":
    main()
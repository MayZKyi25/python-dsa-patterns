"""
Problem 1: Find Max in a List of Numbers

Description:
Write a function called find_max that takes a list of numbers
as input and returns the largest number in the list.

Example:
Input: numbers = [4, 1, 5, 0, 1, -3]
Output: 5

Logic:
1. Assume the first number is the maximum.
2. Go through each number in the list.
3. If the current number is bigger than max_number,
   update max_number to current_number.
4. After checking all numbers, return max_number.
"""


def find_max(numbers):
    """
    Return the largest number in a non-empty list.
    """
    if not numbers:
        raise ValueError("numbers list cannot be empty")

    max_number = numbers[0]

    for current_number in numbers:
        if current_number > max_number:
            max_number = current_number

    return max_number


def main():
    numbers = [4, 1, 5, 0, 1, -3]
    print(f"Maximum number: {find_max(numbers)}")


if __name__ == "__main__":
    main()
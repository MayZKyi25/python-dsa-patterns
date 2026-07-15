"""
Problem 3: Count Occurrences of an Element in a List

Description:
Write a function called count_element that takes a list and a target element
as input, and returns how many times the target appears in the list.

Example:
Input: items = [1, 2, 2, 3, 2, 4], target = 2
Output: 3

Logic:
1. Start count at 0.
2. Go through each item in the list.
3. If the current item is equal to the target,
   increase count by 1.
4. Return count.
"""


def count_element(items, target):
    """
    Return how many times target appears in items.
    """
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def main():
    values = [1, 2, 2, 3, 2, 4]
    target = 2

    print(f"{target} appears {count_element(values, target)} times.")


if __name__ == "__main__":
    main()
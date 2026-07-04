"""
Python fundamentals and interview practice solutions.

This file includes practice problems completed as part of Python review,
coding interview preparation, and LeetCode-style problem solving.

Practice questions:
https://colab.research.google.com/drive/1J_p-AT02T7JyYz0L50J1rPfgfTB6DpQc#scrollTo=EGN9Of_UdKPz
"""


# Problem 1: Find Max and Min
# Description:
# Write functions called find_max and find_min that take a list of numbers
# as input and return the largest/smallest number in the list.
#
# Example:
# Input: numbers = [4, 1, 5, 0, 1, -3]
# Output: 5  for find_max
# Output: -3 for find_min
#
# Logic for find_max:
# 1. Assume the first number is the max.
# 2. Go through each number in the list.
# 3. If the current number is bigger than max_number:
#       update max_number to current number.
# 4. After checking all numbers, return max_number.


def find_max(numbers):
    max_number = numbers[0]

    for current_number in numbers:
        if current_number > max_number:
            max_number = current_number

    return max_number


def find_min(numbers):
    min_number = numbers[0]

    for current_number in numbers:
        if current_number < min_number:
            min_number = current_number

    return min_number


# Problem 2: Count Occurrences of an Element
# Description:
# Write a function called count_element that takes a list and a target element
# as input, and returns how many times the target appears in the list.
#
# Example:
# Input: numbers = [1, 2, 2, 3, 2, 4], target = 2
# Output: 3
#
# Logic:
# 1. Start count at 0.
# 2. Go through each number in the list.
# 3. If the current number is equal to the target:
#       increase count by 1.
# 4. Return count.


def count_element(numbers, target):
    count = 0

    for current_number in numbers:
        if current_number == target:
            count += 1

    return count




# Problem 3: Same Word Count
# Write a function called count_words that takes a string as input and returns a dictionary where each key is a word and each value is how many times that 
# word appears in the string.

# Example:

# Input:  "the cat sat on the mat the cat"
# Output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}:

# Logic:
# split sentence into words
# make empty dictionary
# for each word:
#     if word already in dictionary:
#         add 1 to count
#     else:
#         put word in dictionary with count 1


def count_words(sentence):
    list_of_words = sentence.split()
    word_count = {}

    for each_word in list_of_words:
        if each_word in word_count:
            word_count[each_word] += 1
        else:
            word_count[each_word] = 1

    return word_count



def main():
    numbers = [4, 1, 5, 0, 1, -3]
    print(f"Maximum number in the list is: {find_max(numbers)}")
    print(f"Minimum number in the list is: {find_min(numbers)}")

    values = [1, 2, 2, 3, 2, 4]
    target = 2
    print(f"Count occurrence of element {target} is {count_element(values, target)} times.")

    sentence = "the cat sat on the mat the cat"
    print(f"Word count in given sentence is {count_words(sentence)}")



if __name__ == "__main__":
    main()


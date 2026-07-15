# Slicing and Indexing
list_A = [4, 1, 5, 0, -3]

list_A[0:3]   # [4, 1, 5]  start at index 0, stop before index 3
list_A[1:4]   # [1, 5, 0]
list_A[2:]    # [5, 0, -3] start at index 2 to the end
list_A[:3]    # [4, 1, 5]  start from beginning, stop before index 3


# Negative Indexing
list_A[-1]     # -3  (last element)
list_A[-2]     # 0   (second to last)
list_A[-3:]    # [5, 0, -3] (last 3 elements)
list_A[:-2]    # [4, 1, 5]  (everything except last 2)


# Step/Skip in Slicing
list_A[::2]    # [4, 5, -3]  every 2nd element
list_A[::-1]   # [-3, 0, 5, 1, 4]  REVERSE a list — O(n) time, O(n) space


# Two Pointers
left, right = 0, len(list_A) - 1
while left < right:
    # do something with list_A[left] and list_A[right]
    left += 1
    right -= 1


# Enumerate
for i, val in enumerate(list_A):
    print(i, val)   # 0 4, 1 1, 2 5 ...


# zip
list_A = [1, 2, 3]
list_B = [4, 5, 6]
for x, y in zip(list_A, list_B):
    print(x + y)    # 5, 7, 9


# Dictionary as a frequency counter
from collections import defaultdict, Counter

freq = Counter(list_A)        # {4:1, 1:1, 5:1, 0:1, -3:1}
freq = Counter("aabbbc")      # {'b': 3, 'a': 2, 'c': 1}
freq['a']                     # 2
freq['z']                     # 0 (no KeyError!)

freq = defaultdict(int)
for val in list_A:
    freq[val] += 1


# Sets - O(1) lookup 
seen = set()
seen.add(5)
5 in seen          # True  ← O(1), not O(n) like a list!
seen.discard(5)    # remove without error


# Swap without temp variable
list_A[0], list_A[1] = list_A[1], list_A[0]   # swap two elements in place
a, b = b, a                                   # swap two variables

''' 
Example Exercises - 

Slicing

Reverse a string
Return the last 3 elements of a list
Return every other element of a list


Negative Indexing

Return the second to last element without using len()
Remove the last 2 elements of a list without pop()


Step in Slicing

Check if a string is a palindrome using slicing
Rotate a list to the right by k steps


Two Pointers

Given a sorted list, find two numbers that add up to a target
Move all zeros to the end of a list without creating a new list
Reverse a list in place without slicing


Enumerate

Find the index of the first element greater than 3 in a list
Return a list of (index, value) pairs where value is even


zip

Given two lists, return a new list where each element is the sum of the pair
Check if two strings are anagrams by comparing character pairs


Dictionary / Counter / defaultdict

Count the frequency of each character in a string
Find the most common element in a list
Given a list, return the first element that appears more than once
Check if two strings are anagrams using a Counter


Sets

Remove duplicates from a list while preserving order
Find the intersection of two lists (elements in both)
Given a list, find the first element you've already seen (duplicate detector)


Swap

Reverse a list in place using swaps only (no slicing)
Given a list, swap every pair of adjacent elements


Big O / Mindset

Given a list, find if any two numbers add up to a target — do it in O(n)
Given two lists, find common elements — do it in O(n) not O(n²)
Count how many times each word appears in a sentence
'''


"""
Problem 4: Count Same Words 

Description:
Write a function called count_words that takes a string as input
and returns a dictionary where each key is a word and each value
is how many times that word appears in the string.

Example:
Input:  "the cat sat on the mat the cat"
Output: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}

Logic:
1. Split the sentence into words.
2. Create an empty dictionary.
3. Go through each word.
4. If the word is already in the dictionary, add 1 to its count.
5. If the word is not in the dictionary, add it with count 1.
6. Return the dictionary.
"""


def count_words(sentence):
    word_list = sentence.split()
    word_counts = {}

    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def main():
    sentence = "the cat sat on the mat the cat"
    print(count_words(sentence))


if __name__ == "__main__":
    main()



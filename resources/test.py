# Tests for selected solutions


"""
Problem 4: Count Words

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


'''Variable	Meaning
sentence_text	the full sentence/string input
word_list	the sentence split into a list of words
counts_by_word	dictionary that stores word → count
current_word	the word we are checking right now'''


# Practice Date: July 5, 2026

def count_words(sentence_text):
    # Split the sentence into a list of words
    word_list = sentence_text.split()

    # Create an empty dictionary to store each word and its count
    counts_by_word = {}

    # Go through each word in the word list
    for current_word in word_list:

        # If the word is already in the dictionary,
        # increase its count by 1
        if current_word in counts_by_word:
            counts_by_word[current_word] += 1

        # If the word is not in the dictionary yet,
        # add it and start its count at 1
        else:
            counts_by_word[current_word] = 1

    # Return the final dictionary
    return counts_by_word



def main():
    sentence_text = "the cat sat on the mat the cat"
    print(f"{count_words(sentence_text)}")



if __name__ == "__main__":
    main()






    














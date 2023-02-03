# Print the following letters of the list, without duplicates, using list comprehension
word_list = ["cat", "dog", "rabbit"]
letter_list = [letter for i, letter in enumerate("".join(word_list)) if i == "".join(word_list).index(letter)]
print(letter_list)
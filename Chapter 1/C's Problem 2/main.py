# Guess a 7-digit phone password that is created with a word in mind.

# First letter is i
# Second digit is 8

digits_to_letters = {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}

letters_to_digits = {
    "a": 2, "b": 2, "c": 2,
    "d": 3, "e": 3, "f": 3,
    "g": 4, "h": 4, "i": 4,
    "j": 5, "k": 5, "l": 5,
    "m": 6, "n": 6, "o": 6,
    "p": 7, "q": 7, "r": 7, "s": 7,
    "t": 8, "u": 8, "v": 8,
    "w": 9, "x": 9, "y": 9, "z": 9
}

words = set()
with open("Chapter 1/C's Problem 2/words.txt", "r") as file:
    words = set([word.lower().strip() for word in file.readlines()])
words = set(filter(lambda word : len(word) <= 7, words))

words_by_length = [{}]
for i in range(1, 8):
    words_by_length.append(set(filter(lambda word : len(word) == i, words)))

all_permutations_of_lengths = []
def add_to_all(list_thing):
    global all_permutations_of_lengths
    for i in range(1, 8 - sum(list_thing)):
        add_to_all(list_thing + [i])
    if sum(list_thing) == 7:
        all_permutations_of_lengths.append(list_thing)
add_to_all([])

possible_solutions = set()
for j, perm in enumerate(all_permutations_of_lengths):
    solutions = set([""])
    for i, length in enumerate(perm):
        if i == 0:
            words = set(filter(lambda word : word.startswith("i"), words_by_length[length]))
        else:
            words = words_by_length[length]
        new_solutions = set()
        for solution in solutions:
            for word in words:
                new_solutions |= {solution + word}
        solutions = new_solutions
    possible_solutions |= set(filter(lambda solution : solution[1] in digits_to_letters[8], solutions))

with open("Chapter 1/C's Problem 2/output.txt", "w") as file:
    file.write("\n".join(["".join([str(letters_to_digits[letter]) for letter in word]) for word in possible_solutions]))
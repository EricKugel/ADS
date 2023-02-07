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
    solutions = set()
    for i, length in enumerate(perm):
        if i == 0:
            words = set(filter(lambda word : word.startswith("i"), words_by_length[length]))
        else:
            words = words_by_length[length]
        new_solutions = set()
        for solution in solutions:
            for word in words:
                new_solutions |= {solution + word}
            # [new_solutions |= {solution + word} for word in words]
        solutions = new_solutions
    possible_solutions |= set(filter(lambda solution : solution[1] in digits_to_letters[8], solutions))
    print(j)

with open("output.txt", "w") as file:
    file.write("\n".join(list(possible_solutions)))
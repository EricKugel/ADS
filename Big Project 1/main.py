# Interpreter for a language
from functions import functions

data = []
with open("input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

VALID_NUMBERS = "1234567890."
VALID_OPS = "^*/+-%"
ORDER_OF_OPS = ["^", "*/%", "+-"]


line = data[0]
print(evaluate(parse(line)))

def parse(chunk):
    pass

def get_chunk_at(i, text):
    j = i + 1
    counter = 1
    while counter != 0 and j < len(text):
        if text[j] == "(":
            counter += 1
        elif text[j] == ")":
            counter -= 1
        j += 1
    return text[i:j]

def clean(text):
    new_text = ""
    i = 0
    while i < len(text):
        character = text[i]
        if character in VALID_NUMBERS or character in VALID_OPS or character in "()":
            new_text += character
        elif is_function(i, text):
            func = get_function(i, text)
            new_text += func
            i += len(func) - 1
        i += 1
    return new_text

def is_function(i, text):
    any([text[i:].startswith(func) for func in functions.keys()])

def get_function(i, text):
    return max([func for func in functions.keys() if text[i:].startsWith(func)], key = lambda func : len(func))

def parse(text):
    text = clean(text)
    parsed = []
    is_op = False
    i = 0
    while i < len(text):
        character = text[i]
        if character == "(":
            chunk = get_chunk_at(i, text)
            i += len(block)
            parsed.append(parse(chunk[1:-1]))
            is_op = True
        else:
            if not is_op:
                if is_function(i, text):
                    # reduce function to a constant
                    func_input = get_chunk_at(text.index("(", i + 1), text)
                    func_input = evaluate(parse(func_input[1:-1]))
                    func = get_function(i, text)
                    parsed.append(functions[func](func_input))
                    i += len(func_input) + len(func)
                else:
                    token = ""
                    while (character in VALID_NUMBERS or (character == "-" and len(token) == 0)) and i < len(text):
                        token += character
                        try:
                            character = text[i]
                        except Exception:
                            character = ""
                    parsed += float(token)
                is_op = True
            else:
                parsed.append(character)
                i += 1
                is_op = False
    return parsed


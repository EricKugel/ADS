# Interpreter for a language
from functions import functions, operators

VALID_NUMBERS = "1234567890."
VALID_OPS = "^*/+-%"
ORDER_OF_OPS = ["^", "*/%", "+-"]

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
        elif is_variable(i, text):
            var = get_variable(i, text)
            new_text += var
            i += len(var) - 1
        i += 1
    return new_text

def is_function(i, text):
    return any([text[i:].startswith(func) for func in functions.keys()])

def is_variable(i, text):
    return any([text[i:].startswith(var) for var in variables.keys()])
    
def get_function(i, text):
    return max([func for func in functions.keys() if text[i:].startswith(func)], key = lambda func : len(func))

def get_variable(i, text):
    return max([var for var in variables.keys() if text[i:].startswith(var)], key = lambda var : len(var))

def parse(text):
    text = clean(text)
    parsed = []
    is_op = False
    i = 0
    while i < len(text):
        character = text[i]
        if character == "(":
            chunk = get_chunk_at(i, text)
            i += len(chunk)
            parsed.append(parse(chunk[1:-1]))
            is_op = True
        else:
            if not is_op:
                if is_function(i, text):
                    # reduce function to a constant
                    func = get_function(i, text)
                    func_input = get_chunk_at(text.index("(", i + 1), text)
                    i += len(func_input) + len(func)
                    func_input = evaluate(parse(func_input[1:-1]))
                    parsed.append(functions[func](func_input))
                elif is_variable(i, text):
                    var = get_variable(i, text)
                    i += len(var)
                    parsed.append(variables[var])
                else:
                    token = ""
                    while (character in VALID_NUMBERS or (character == "-" and len(token) == 0)) and i < len(text):
                        token += character
                        i += 1
                        try:
                            character = text[i]
                        except Exception:
                            character = ""
                    parsed.append(float(token))
                is_op = True
            else:
                parsed.append(character)
                i += 1
                is_op = False
    return parsed

def evaluate(parsed):
    for item in parsed:
        if isinstance(item, list):
            item = evaluate(item)
    for current_op in ORDER_OF_OPS:
        i = 0
        while i < len(parsed) - 2:
            op = parsed[i + 1]
            if op in current_op:
                result = operators(op)(parsed[i], parsed[i + 2])
                parsed[i + 1] = result
                parsed.pop(i + 2)
                parsed.pop(i)
                i -= 2
            i += 2
    return parsed[0]

variables = {}

data = []
with open("Big Project 1/input.esar", "r") as file:
    data = [line.strip() for line in file.readlines()]

for line in data:
    if "=" in line:
        assignment = line.split("=")
        variables[assignment[0].strip()] = evaluate(parse(assignment[1]))
    else:
        evaluate(parse(line))
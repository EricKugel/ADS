alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaBET = alphabet + alphabet.upper()
variables = alphaBET + "_"
operators = ["+", "-", "*", "/", "//", "+=", "-=", "*=", "^" "/=", "//=", "%=", "%", "&", "!", "|", "<", "<=", ">", ">=", "==", "!="]
precedence = {"^": 10,"~": 9.5,"!": 9.5,"*": 9,"/": 9,"//": 9,"%": 9,"+": 8,"-": 8,"<": 7,"<=": 7,">": 7,">=": 7,"==": 7,"!=": 7,"&": 6,"|": 5,"+=": 4,"-=": 4,"*=": 4,"/=": 4,"//=": 4,"%=": 4}
numbers = "0.123456789"

import time

def is_operator(data, i):
    return any([i + len(op) < len(data) and data[i:i+len(op)] == op for op in operators])

def find_operator(data, i):
    return max([op for op in operators if i + len(op) < len(data) and data[i:i+len(op)] == op], key = lambda op : len(op))

def tokenize(data):
    tokens = []
    i = 0
    token = ""
    while i < len(data):
        char = data[i]
        if char in "(),:;":
            if len(token) > 0:
                tokens.append(token)
            token = ""
            tokens.append(char)
            i += 1
        elif char in "[\{":
            if len(token) > 0:
                tokens.append(token)
            token = ""
            open = char
            close = {"[": "]", "{": "}"}[open]
            block = "" + char
            counter = 1
            i += 1
            while i < len(data) and counter > 0:
                char = data[i]
                block += str(char)
                if char == close:
                    counter -= 1
                elif char == open:
                    counter += 1
                i += 1 
            tokens.append([open] + tokenize(block[1:-1]) + [close])
        elif char in " \t\n":
            if len(token) > 0:
                tokens.append(token)
            token = ""
            i += 1
        elif char == '"':
            if len(token) > 0:
                tokens.append(token)
            token = ""
            token += char
            i += 1
            while i < len(data) and not(data[i] == '"' and data[i - 1] != "\\"):
                token += data[i]
                i += 1
            token += char
            i += 1
            tokens.append(token)
            token = ""
        elif is_operator(data, i):
            if len(token) > 0:
                tokens.append(token)
            op = find_operator(data, i)
            if op == "-" and not (tokens[-1] == ")" or all([letter in variables for letter in tokens[-1]]) or all([letter in numbers for letter in tokens[-1]])):
                token = "~"
            else:
                token = op
            i += len(op)
        elif char in variables:
            if len(token) > 0:
                tokens.append(token)
            token = ""
            while i < len(data) and data[i] in variables:
                token += data[i]
                i += 1
        elif char in numbers:
            if len(token) > 0:
                tokens.append(token)
            token = ""
            while i < len(data) and data[i] in numbers:
                token += data[i]
                i += 1
        else:
            i += 1
    return tokens

def postfix(tokens):
    output = []
    stack = []
    while tokens:
        token = tokens.pop(0)
        if all([letter in numbers for letter in token]):
            output.append(token)
        elif token == "{":
            

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaBET = alphabet + alphabet.upper()
variables = alphaBET + "_"
operators = ["+", "-", "*", "/", "//", "+=", "-=", "*=", "/=", "//=", "%=", "%", "&", "!", "|", "<", "<=", ">", ">=", "==", "!="]
numbers = "0.123456789"

def is_operator(data, i):
    

def find_operator(data, i):
    return max([op for op in operators if i + len(op) < len(data) and data[i:i+len(op)] == op], key = lambda op : len(op))

def tokenize(data):
    tokens = []
    i = 0
    token = ""
    while i < len(data):
        char = data[i]
        if char in "([\{\}]),:;":
            if len(token) > 0:
                tokens.append(token)
            token = ""
            tokens.append(char)
        if char == " ":
            if len(token) > 0:
                tokens.append(token)
            token = ""
        if char == '"':
            token += char
            i += 1
            while not (data[i] == '"' and data[i - 1] != "\\"):
                token += data[i]
            token += char
            tokens.append(token)
            token = ""
        
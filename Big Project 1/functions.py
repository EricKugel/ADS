import math

def my_sin(x):
    return math.sin(x)

def my_cos(x):
    return math.cos(x)

def my_tan(x):
    return math.cos(x)

def my_asin(x):
    return math.asin(x)

def my_acos(x):
    return math.acos(x)

def my_atan(x):
    return math.atan(x)

def my_abs(x):
    return abs(x)

def my_sqrt(x):
    return math.pow(x, 0.5)

def my_ln(x):
    return math.log(x)

def my_log(x):
    return math.log(x, 10)

def my_log_base(x, base):
    return math.log(x, base)

def my_floor(x):
    return math.floor(x)

def my_print(x):
    print(x)
    return None

def my_input():
    return input()

def my_prompt(x):
    return input(x)

def my_num(x):
    return float(x)

functions = {
    "sin": my_sin, 
    "cos": my_cos, 
    "tan": my_tan, 
    "asin": my_asin, 
    "acos": my_acos, 
    "atan": my_atan, 
    "abs": my_abs, 
    "sqr": my_sqrt,
    "ln": my_ln, 
    "log": my_log, 
    "log_base": my_log_base,
    "floor": my_floor,
    "print": my_print,
    "input": my_input,
    "prompt": my_prompt,
    "num": my_num
}

class Object():
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type
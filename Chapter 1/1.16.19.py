# Most of the 1.16 exercises would be a waste of time.
# I'll do exercise 19, making a sudoku solver.

input = (
    (0,9,0,8,6,5,2,0,0),
    (0,0,5,0,1,2,0,6,8),
    (0,0,0,0,0,0,0,4,0),
    (0,0,0,0,0,8,0,5,6),
    (0,0,8,0,0,0,4,0,0),
    (4,5,0,9,0,0,0,0,0),
    (0,8,0,0,0,0,0,0,0),
    (2,4,0,1,7,0,5,0,0),
    (0,0,7,2,8,3,0,9,0)
)

output = [list(row) for row in input]

coord = (0, 0)
next_coord = lambda coord : (coord[0], coord[1] + 1) if coord[1] + 1 != 9 else (coord[0] + 1, 0)
last_coord = lambda coord : (coord[0], coord[1] - 1) if coord[1] - 1 != -1 else (coord[0] - 1, 0)

def get_blocks():
    global output
    blocks = []
    for row in range(3):
        for col in range(3):
            block = []
            [[block.append(output[row + r][col + c]) for r in range(3)] for c in range(3)]
            blocks.append(block)
    return blocks

def all_chill():
    global output
    for row in output:
        if not all([row.count(i) <= 1 for i in range(1, 10)]):
            return False
    for col in list(zip(*output)):
        if not all([col.count(i) <= 1 for i in range(1, 10)]):
            return False
    for block in get_blocks():
        if not all([block.count(i) <= 1 for i in range(1, 10)]):
            return False
    return True

while True:
    if input[coord[0]][coord[1]] == 0 and not all_chill():
        if output[coord[0]][coord[1]] == 9:
            output[coord[0]][coord[1]] = 0
            coord = last_coord(coord)
        output[coord[0]][coord[1]] += 1
    elif input[coord[0]][coord[1]] == 0:
        output[coord[0]][coord[1]] += 1
    if all_chill():
        coord = next_coord(coord)
        if coord[0] == 9:
            break

[print(line) for line in output]
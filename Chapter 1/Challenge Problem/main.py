data = []
with open("Chapter 1/Challenge Problem/input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

horizontals = data
verticals = ["".join([data[row][col] for row in range(len(data))]) for col in range(len(data[0]))]

diagonals = []
column = 1 - len(horizontals[0])
while column < len(horizontals[0]):
    diagonal = []
    row = 0
    col = column
    while row < len(horizontals):
        if 0 <= col < len(horizontals[0]):
            diagonal.append(horizontals[row][col])
        else:
            diagonal.append(" ")
        row += 1
        col += 1
    diagonals.append("".join(diagonal))
    column += 1

rotated_diagonals = ["".join([diagonals[row][col] for row in range(len(diagonals))]) for col in range(len(diagonals[0]))]

diagonals = [diagonal.strip() for diagonal in diagonals]
rotated_diagonals = [diagonal.strip() for diagonal in rotated_diagonals]
data = []
with open("Chapter 1/C's Problem/input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

largest_group = []
for row in range(len(data)):
  for col in range(len(data[0])):
    if (row, col) in largest_group:
      continue
    queue = [(row, col)]
    group = [(row, col)]
    while queue:
      cell = queue.pop()
      for r in range(-1, 2):
        for c in range(-1, 2):
          if not (
            (cell[0] + r, cell[1] + c) in group) and 0 < cell[0] + r < len(
              data) and 0 < cell[1] + c < len(data[0]) and data[cell[0] + r][
                cell[1] + c] == data[row][col] and not (c == 0 and r == 0):
            queue.append((cell[0] + r, cell[1] + c))
            group.append((cell[0] + r, cell[1] + c))
    if len(group) > len(largest_group):
      largest_group = group

output_file = open("output.txt", "w")
output = ""
for r, row in enumerate(data):
  for c, letter in enumerate(row):
    if (r, c) in largest_group:
      output += "#"
    else:
      output += letter
  output += "\n"

output_file.write(output)
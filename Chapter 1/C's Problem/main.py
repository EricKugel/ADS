# Read input
data = []
with open("Chapter 1/C's Problem/input.txt", "r") as file:
    data = [line.strip() for line in file.readlines()]

largest_group = []

# Iterates over each cell (inefficient) and does a breadth-first search on each.
for row in range(len(data)):
  for col in range(len(data[0])):
    # Make sure the cell isn't already in the largest group
    if (row, col) in largest_group:
      continue
    
    queue = [(row, col)]
    group = [(row, col)]
    while queue:
      cell = queue.pop()
      # Check each cell around the cell
      for r in range(-1, 2):
        for c in range(-1, 2):
          # If the cell is part of the group, add it and add it to the queue to be checked
          if not (
            (cell[0] + r, cell[1] + c) in group) and 0 < cell[0] + r < len(
              data) and 0 < cell[1] + c < len(data[0]) and data[cell[0] + r][
                cell[1] + c] == data[row][col] and not (c == 0 and r == 0):
            queue.append((cell[0] + r, cell[1] + c))
            group.append((cell[0] + r, cell[1] + c))
    
    if len(group) > len(largest_group):
      largest_group = group

# Mark the largest group with hashtags
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
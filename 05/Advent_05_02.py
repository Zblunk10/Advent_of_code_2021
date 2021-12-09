import pandas as pd
import numpy as np

with open("05/input.txt", "r") as f:
  file_content = f.read()

# splits instructions
file_content = file_content.split("\n")
file_content = [x.split(" -> ") for x in file_content]


instructions = []
for x in file_content:
  left = [int(x) for x in x[0].split(",")]
  right = [int(x) for x in x[1].split(",")]
  instructions.append([left[0], left[1], right[0], right[1]])
#print(instructions)


field = pd.DataFrame(np.zeros((1000,1000)))
# field.loc[3:3, 5:7] = 6
# print(field.loc[0,0])
# print(field)
n=0
for instruction in instructions:
  start_column = instruction[0]
  start_row = instruction[1]
  end_column=instruction[2]
  end_row = instruction[3]
  rows = [start_row, end_row]
  columns = [start_column, end_column]
  # only take into account horizontal/vertical
  if start_column == end_column or start_row == end_row:
    field.loc[min(rows):max(rows), min(columns):max(columns)] +=1

# diagonal
  else:
    diff = max(rows) - min(rows)
    if (start_column < end_column and start_row < end_row) or (start_column > end_column and start_row > end_row):
      for i in range(diff+1):
        field.loc[min(rows)+i,(min(columns)+i)] += 1
    elif (start_column > end_column and start_row < end_row) or (start_column < end_column and start_row > end_row):
      for i in range(diff+1):
        field.loc[(min(rows)+i,(max(columns)-i))] += 1
      




print((field))
x = field[field>1].count()
print(x.sum())



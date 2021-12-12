with open("11/input.txt", "r") as f:
  file_content = f.read().splitlines()

dumbos = []
for line in file_content:
  dumbos.append([int(x) for x in line])
  


#3 is test, 100 final
iterations = 100
explode_count= 0

def check_if_nine(line, column):
  if line<0 or line > 9 or column<0 or column > 9:
    pass
  else:
    check_value = (dumbos[line][column])
    if check_value ==9:
      # if nine, add one
      dumbos[line][column] +=1
      explode(line, column)
    else:
      dumbos[line][column] += 1

def explode(line, column):
  global explode_count 
  explode_count += 1
  # up
  check_if_nine(line-1, column)
  # down
  check_if_nine(line+1, column)
  # left
  check_if_nine(line, column-1)
  # right
  check_if_nine(line, column+1)
  # diagonal up right
  check_if_nine(line-1, column+1)
  # diagonal up left
  check_if_nine(line-1, column-1)
  # diagonal down right
  check_if_nine(line+1, column+1)
  # diagonal down left
  check_if_nine(line+1, column-1)




while iterations > 0:
  iterations -= 1
  for line in range(len(dumbos)):
    for column in range(len(dumbos[0])):
      check_if_nine(line, column)

   # reset   
  for line in range(len(dumbos)):
    for column in range(len(dumbos[0])):
      
      if dumbos[line][column] > 9:
        dumbos[line][column] = 0

print("explode_count: ", explode_count)

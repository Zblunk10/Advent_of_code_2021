with open("13/input.txt", "r") as f:
  file_content = f.read().split("\n\n")


# Coordinates processing
coordinates = file_content[0].split("\n")
coordinates  = [x.split(",") for x in coordinates]

def get_field_size(coordinates):
  x_list = []
  y_list = []
  for item in coordinates:
    x= int(item[0])
    y = int(item[1])
    x_list.append(x)
    y_list.append(y)
  return(max(x_list),max(y_list)) 


def get_coordinates(coordinates):
  new_coordinates = []
  x_list = []
  y_list = []
  for item in coordinates:
    x = int(item[0])
    y = int(item[1])
    x_list.append(x)
    y_list.append(y)
    new_coordinates.append((x, y))
  return new_coordinates


coordinates = get_coordinates(coordinates)


# Folds
folds = file_content[1]
new_folds = []
for i in folds.split("\n"):
  num = i.split("=")[1]
  if i.find("x")>0:
    i.split("=")
    new_folds.append(("x", num))
  else:
    i.split("=")
    new_folds.append(("y", num))

folds = new_folds

# complete
line_count = 894
columns_count = 1310

#test
# line_count = 14
# columns_count = 10


for fold in folds:
  field_size = get_field_size(coordinates)
  #print("field_size", field_size)
  print(fold)
  fold_type = fold[0]
  fold_line = int(fold[1])
  new_coordinates = []
  if fold_type == "y":
    for line in range(fold_line):
      for column in range(field_size[0]+1):
        index = (column, line)
        #print(index)
        folded_index = (column, (field_size[1]-line))
        #print("folded_index", folded_index)
        if (index in coordinates) or folded_index in coordinates:
          new_coordinates.append(index)
          #print(index, "added")
  elif fold_type == "x":
    for line in range(field_size[1]+1):
      for column in range(fold_line):
        index = (column, line)
        #print("index",index)
        folded_index = (field_size[0]-column, line)
        #print("folded_index", folded_index)
        if (index in coordinates) or (folded_index in coordinates):
          new_coordinates.append(index)
          #print(index, "added")
  print("len", len(new_coordinates))
  #print((new_coordinates))
  coordinates = new_coordinates

#print(len(coordinates))
final_coordinates= coordinates


print(final_coordinates)


# print
field_size = get_field_size(final_coordinates)
for line in range(field_size[1]+1):
  line_text =[]
  
  for column in range(field_size[0]+1):
    index = (column, line)
    if index in final_coordinates:
      line_text.append("█")
    else:
      line_text.append(".")
  line_text.append("\n")
  print(line_text)

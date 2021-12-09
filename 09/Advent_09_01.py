with open("09/input.txt", "r") as f:
  file_content = f.read().split("\n")

def split_to_nums(line):
  splitted =  list(line)
  to_integer = [int(x) for x in splitted]
  return to_integer
file_content = [split_to_nums(x) for x in file_content]

row_count = len(file_content)


def get_previous_line_num(row_index, item_index):
  previous_line = row_index -1
  if previous_line == -1:
    pass
  else:
    return file_content[previous_line][item_index]


def get_following_line_num(row_index, item_index):
  following_line = row_index + 1
  if following_line >= 100:
    pass
  else:
    return file_content[following_line][item_index]


def get_previous_num(row_index, item_index):
  previous_index = item_index -1 
  if previous_index ==-1:
    pass
  else:
    return file_content[row_index][previous_index]


def get_following_num(row_index, item_index):
  following_index = item_index + 1
  if following_index >=100:
    pass
  else:
    return file_content[row_index][following_index]


def check_if_all_nums_bigger(surrounding_numbers, item_value):
  for x in surrounding_numbers:
    if item_value>= x:
      return False
  return True


# for row_index in range(row_count):
surrounded_by_bigger_nums = []
for row_index in range(row_count):
#  print(file_content[row_index])
  for item_index in range(100):
    item_value = file_content[row_index][item_index]
    a = get_previous_line_num(row_index, item_index)
    b = get_following_line_num(row_index, item_index)
    c= get_previous_num(row_index, item_index)
    d = get_following_num(row_index, item_index)

    surrounding_numbers = [a,b,c,d]
#    print(item_value, surrounding_numbers)
    surrounding_numbers = [x for x in surrounding_numbers if x is not None]

    if check_if_all_nums_bigger(surrounding_numbers, item_value):
      surrounded_by_bigger_nums.append(item_value)

sum_of_surrounded = sum(surrounded_by_bigger_nums)
count_of_surrounded = len(surrounded_by_bigger_nums)
print(sum_of_surrounded+count_of_surrounded)

from collections import  defaultdict


# open file
with open("08/input.txt", "r") as f:
  file_content = f.read()
file_content = file_content.split("\n")

# basic parsing and string reordering
def split_to_parts(content):
  lines = []
  for line in content:
    line = line.split(" | ")
    line = [x.split(" ") for x in line]
    line = order_letters(line)
    lines.append(line)
  return lines

def order_letters(lines):
  x = []
  for part in lines:
    y = ["".join(sorted(x)) for x in part]
    x.append(y)
  return x

def get_lengths(patterns):
  results = defaultdict(list)
  for clue in patterns:
    length = len(clue)
    results[length].append(clue)
  return results



parts = split_to_parts(file_content)
output_numbers = []

for part in parts:
# solve patterns to create a map
  patterns = part[0]

# easy numbers solved by unique lengths
  clues_by_lengths = get_lengths(patterns)
  num_1 = clues_by_lengths[2][0]
  num_4 = clues_by_lengths[4][0]
  num_7 = clues_by_lengths[3][0]
  num_8 = clues_by_lengths[7][0]

# num 6 (only 6 segment number that do not contain whole number one)
  for item in clues_by_lengths[6]:
    if num_1[0] in item and num_1[1] in item:
      continue
    else:
      num_6 = item

# segment c (is part of 8, but not of 6 - needed for differentiating in 5-segment letters)
  for letter in num_8:
    if letter not in num_6:
      segment_c = letter

#5 segments (3 includes both segments from number 1, 2 includes c segment, 5 doesn't include c segment)
  for item in clues_by_lengths[5]:
    if (num_1[0] in item) and (num_1[1] in item):
      num_3 = item
    elif segment_c in item:
      num_2 = item
    else:
      num_5 = item

# segment e (segment e is only segment from number 2 that doesn't exist in numbers 3 and 1)
  for letter in num_2:
    if (letter not in num_3) and (letter not in num_1):
      segment_e = letter

# 6 segments (num 6 solved previously, 0 contains segment e, 9 doesnt contain segment e)
  for item in clues_by_lengths[6]:
    if item == num_6:
      num_6 = item
    elif segment_e in item:
      num_0 = item
    else:
      num_9 = item

# map creation - key is ordered string
  new_map = {num_1: 1, num_2:2, num_3:3, num_4:4, num_5:5, num_6:6, num_7:7, num_8:8, num_9:9, num_0:0}
  

# now we get to "output" part of the input file  
  output = part[1]
  number = []
  # transforms letter strings to numbers by map
  for digit in output:
    a= new_map[digit]
    number.append(a)
  
  output_numbers.append(number)

# joins numbers to create four-digit output values
nums = []
for item in output_numbers:
  x = [str(y) for y in item]
  x = "".join(x)
  nums.append(x)


nums = [int(x) for x in nums]
print(sum(nums))


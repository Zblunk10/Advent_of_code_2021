import numpy as np
import collections

with open("06/input.txt", "r") as f:
  file_content = f.read().split(",")

# input to integer
initial_state = [int(x) for x in file_content]


# set number of iterations 256 final
number_of_iterations = 256



def substract_one(counter_dict):
  new_counts ={}
  for key, val in counter_dict.items():
    new_counts[key-1] = val
  return new_counts

# resets fish in final stadium and adds the new fish
def reset_add_fish(counter_dict):
  new_counts = counter_dict
  for key, val in counter_dict.items():
    if key == -1:
      new_counts.pop(-1)
      new_counts[8] = new_counts.get(8,0) + val
      new_counts[6] = new_counts.get(6, 0) + val
      break
  return new_counts



counts_dict = collections.Counter(initial_state)
for i in range(number_of_iterations):
  counts_dict = substract_one(counts_dict)
  counts_dict = reset_add_fish(counts_dict)


print(sum(counts_dict.values()))



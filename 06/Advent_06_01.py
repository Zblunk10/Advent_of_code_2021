import numpy as np

with open("06/input.txt", "r") as f:
  file_content = f.read().split(",")

# input to integer
initial_state = [int(x) for x in file_content]
#print("initial_state", initial_state)

# set number of iterations
number_of_iterations = 80

# substracts one from the previous state
def remove_one_from_state(state):
  return np.subtract(state, 1).tolist()


# detects number of fish in final stage that needs to be reset and added
def check_for_final_stage(state):
  final_stage_count = state.count(-1)
  return final_stage_count

# reset fish that produced another fish to 6
def reset_fish(state):
  state = np.array(state)
  fish_reseted = np.where(state==-1, 6, state).tolist()
  return fish_reseted

# newly produced fish starts at 8
def add_new_fish(state, count_of_fish_to_add):
  new_fish = [8 for x in range(count_of_fish_to_add)]
  state.extend(new_fish)
  return state


state = initial_state
for i in range(number_of_iterations):
#  print(i, " : ", state)
  state = remove_one_from_state(state)
  final_stage_count = check_for_final_stage(state)
  state = reset_fish(state)
  state = add_new_fish(state, final_stage_count)
print(len(state))




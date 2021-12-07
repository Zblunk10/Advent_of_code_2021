with open("07/input.txt", "r") as f:
  file_content = f.read()

# splits start position string to list and converts each position to integer
start_positions = file_content.split(",")
start_positions = [int(x) for x in start_positions]

# get position of submarine farthest from zero
max_position = max(start_positions)

def fuel_sum(n):
  x = sum([i for i in range(1, n+1)])
  return x

meeting_points_distances = []
for possible_meeting_point in range(0, max_position):
  position_distances = 0
  for position in start_positions:
    distance = abs(position-possible_meeting_point)
    fuel = fuel_sum(distance)
    position_distances = position_distances + fuel

  meeting_points_distances.append(position_distances)


#Minimum of spent fuel
print(min(meeting_points_distances))



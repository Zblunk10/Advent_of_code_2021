with open("02/input.txt", "r") as f:
  file_content = f.read()
instructions = file_content.splitlines()

depth = 0
position = 0
for i in instructions:
  separ = i.split()
  direction = separ[0]
  step = int(separ[1])
  if direction == "down":
    depth += step
  elif direction == "up":
    depth -= step
  elif direction == "forward":
    position+=step

print(f"Depth: {depth}, Position: {position}, multiplied:{depth*position}")
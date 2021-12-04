with open("02/input.txt", "r") as f:
  file_content = f.read()
record = file_content.splitlines()

instructions = [(x.split()[0], x.split()[1]) for x in record]

motions = {}
for i in instructions:
  motions[i[0]] = motions.get(i[0],0)+int(i[1])
print(motions)
print((motions["down"] - motions["up"])*motions["forward"])


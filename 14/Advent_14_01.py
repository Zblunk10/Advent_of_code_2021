from collections import Counter
with open("14/input.txt", "r") as f:
  file_content = f.read().splitlines()

template = file_content[0]
pair_insertions = [x.split(" -> ") for x in file_content[2:]]
pairs = {}
for p in pair_insertions:
  pairs[p[0]] = p[1]

#final 10, test 2
iterations = 10

for i in range(iterations):
#  print(i)
  new_template=[template[0]]
  for a in range(len(template)-1):
    double = (template[a:(a+2)])
    new_template.append(pairs[double])
    new_template.append(template[a+1])
  template = "".join(new_template)

counts = (Counter(template))
max_value = (counts[max(counts, key=counts.get)])
min_value = (counts[min(counts, key=counts.get)])
print(max_value-min_value)

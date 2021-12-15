from collections import Counter
from itertools import islice



with open("14/input_test.txt", "r") as f:
  file_content = f.read().splitlines()

template = file_content[0]
pair_insertions = [x.split(" -> ") for x in file_content[2:]]
pairs = {}
for p in pair_insertions:
  pairs[p[0]] = p[1]

#final 10, test 2
iterations = 40


def window(seq, n=2):
  it = iter(seq)
  result = tuple(islice(it, n))
  if len(result) == n:
      yield result
  for elem in it:
      result = result[1:] + (elem,)
      yield result

for i in range(iterations):
  print(i)
  new_template = [template[0]]
  looping_window = window(template,2)
  for slice in looping_window:
    double = "".join(slice)
    new_template.append(pairs[double])
    new_template.append(slice[1])
  template = "".join(new_template)
#print(template)
counts = (Counter(template))

max_value= (counts[max(counts, key=counts.get)])
min_value = (counts[min(counts, key=counts.get)])
print(max_value-min_value)

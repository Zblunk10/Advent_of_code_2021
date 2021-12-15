from collections import Counter
from itertools import islice


with open("14/input.txt", "r") as f:
  file_content = f.read().splitlines()

template = file_content[0]
pair_insertions = [x.split(" -> ") for x in file_content[2:]]
pairs = {}
for p in pair_insertions:
  pairs[p[0]] = p[1]


def window(seq, n=2):
  it = iter(seq)
  result = tuple(islice(it, n))
  if len(result) == n:
      yield result
  for elem in it:
      result = result[1:] + (elem,)
      yield result




#Initial iteration
first_iter_template = []
looping_window = window(template,2)
for slice in looping_window:
  double = "".join(slice)
  to_insert = pairs[double]
  first_iter_template.append("".join([slice[0], to_insert]))
  first_iter_template.append("".join([to_insert, slice[1]]))

polymer_counts = Counter(first_iter_template)
#print(polymer_counts)

#test 10, final 40 (really 39, because first is separate)
iterations = 39

for i in range(iterations):
  new_counts = {}
  for key, val in polymer_counts.items():
    if len(pairs[key])>0:
      to_insert = pairs[key]
      multiplier = val
      new_key1 = "".join([key[0],to_insert])
      new_key2 = "".join([to_insert, key[1]])
      new_counts[new_key1] = new_counts.get(new_key1, 0) + val
      new_counts[new_key2] = new_counts.get(new_key2, 0) + val
    else:
      print("not in keys")
      new_counts[key] = new_counts.get(key, 0) + val
  polymer_counts = new_counts
#print(polymer_counts)


#final counts

#rozdělit na jednotlivé část a count - jenže pak duplicity
separate_count={}
for key, val in polymer_counts.items():
  separate_count[key[0]] = separate_count.get(key[0],0) + val
  separate_count[key[1]] = separate_count.get(key[1],0) + val

print(separate_count)
max_value= (separate_count[max(separate_count, key=separate_count.get)])
min_value = (separate_count[min(separate_count, key=separate_count.get)])
print("max_value", max_value)
print("min_value", min_value)
print((max_value-min_value)/2)

from collections import Counter
import collections

with open("08/input.txt", "r") as f:
  file_content = f.read()

file_content = file_content.split("\n")

output_lengths = []
for line in file_content:
  line = line.split(" | ")
  output = line[1]
  output_length = [len(x) for x in output.split(" ")]
  [output_lengths.append(x) for x in output_length]


length_counts = collections.Counter(output_lengths)
print(length_counts)
result = length_counts[2]+length_counts[3]+length_counts[4]+length_counts[7]
print(result)
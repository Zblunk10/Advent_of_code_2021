import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

with open("01/input.txt", "r") as f:
  file_content = f.read()

numbers = [int(x) for x in file_content.split()]

numbers = np.array(numbers)

result = np.sum(np.lib.stride_tricks.sliding_window_view(numbers, window_shape=3), axis=1)

n = 0
for i in range(1, len(result)):

  if result[i] > result[i-1]:
    n += 1


print(n)


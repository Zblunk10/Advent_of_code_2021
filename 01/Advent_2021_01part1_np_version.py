import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


with open("01/input.txt", "r") as f:
  file_content = f.read()

numbers = [x for x in file_content.split()]


numbers = [int(x) for x in file_content.split()]

numbers = np.array(numbers)

result = np.lib.stride_tricks.sliding_window_view( numbers, window_shape=2)


n = 0
for i in result:
  if i[0]< i[1]:
    n+=1
print(n)

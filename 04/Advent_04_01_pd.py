import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

with open("04/input2.txt", "r") as f:
  bingo_numbers = f.read()

file_content = pd.read_csv("04/input.txt", sep=r"\s+", header=None)

# BINGO numbers
bingo_numbers = bingo_numbers.split(",")
bingo_numbers = pd.Series(bingo_numbers)
bingo_numbers = pd.to_numeric(bingo_numbers).to_frame(name="numbers").reset_index()
# print(bingo_numbers)



results = []

def calculate(test, chunk):
  count_of_matched = len(test["index"])
  max_matched_index = max(test["index"])
  last_num = bingo_numbers.iloc[max_matched_index]
  last_num = last_num["numbers"]

  all_called_numbers = bingo_numbers.iloc[0:max_matched_index+1,1].tolist()
  chunk_numbers = pd.DataFrame.to_numpy(chunk).flatten()
  not_called_numbers = [x for x in chunk_numbers if x not in all_called_numbers]
  not_called_numbers = sum([x for x in chunk_numbers if x not in all_called_numbers])
  final_result = not_called_numbers*last_num


#  print(len(not_called_numbers))
  result = {"Table_number": chunk_number, "Table_Sum": sum_chunk, "Count_of_Matched_Numbers_in_r_c": count_of_matched,
            "Latest_matched_index": max_matched_index, "last_num": last_num, "not_called_numbers": not_called_numbers, "final_result": final_result}
  results.append(result)

#set up first chunk
x = 0
y = 5
n = 1
#500 final. 20 for tests
while x<500:
  chunk = file_content[x:y]
#  print(chunk)
  sum_chunk = chunk.values.sum()
  chunk_number = n
  
  for ind, row in chunk.iterrows():
    test = pd.merge(row, bingo_numbers, right_on="numbers", left_on=ind)
    calculate(test, chunk)

  for ind, column in chunk.iteritems():
    test = pd.merge(column, bingo_numbers, right_on="numbers", left_on=ind)
    calculate(test, chunk)


  #set up next chunk
  x +=5
  y +=5
  n +=1


resulting_DF = pd.DataFrame.from_dict(results)
print(resulting_DF.sort_values(by="Latest_matched_index").head())

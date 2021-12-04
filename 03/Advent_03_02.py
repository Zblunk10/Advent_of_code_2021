from collections import defaultdict
from collections import Counter


with open("03/input.txt", "r") as f:
  file_content = f.read()
diagnostic_report = file_content.splitlines()

records_count = len(diagnostic_report)


def get_position_values(records, position):
  position_values = [x[position] for x in records]
  return position_values

def get_common_value(list_of_values, default_num):
  value_count = Counter(list_of_values)

  if value_count["0"] == value_count["1"]:
    return default_num
  else:
    most_common = max(value_count, key=value_count.get)
    return most_common


def get_least_common_value(list_of_values, default_num):
  value_count = Counter(list_of_values)

  if value_count["0"] == value_count["1"]:
    return default_num
  else:
    most_common = min(value_count, key=value_count.get)
    return most_common


# most common
records = diagnostic_report
most_common_list = []
for pos in range(12):
  pos_values = get_position_values(records, pos)
  common_value = get_common_value(pos_values,default_num="1")
  most_common_list.append(common_value)
  records = [record for record in records if record[pos] == common_value]

oxygen_generator_rating = records[0]
oxygen_generator_rating = int(oxygen_generator_rating, 2)
print(oxygen_generator_rating)

# least common
records = diagnostic_report
most_common_list = []
for pos in range(12):
  pos_values = get_position_values(records, pos)
  common_value = get_least_common_value(pos_values, default_num="0")
  records = [record for record in records if record[pos] == common_value]


co2_scrubber_rating = records[0]
co2_scrubber_rating = int(co2_scrubber_rating, 2)
print(co2_scrubber_rating)

life_support = oxygen_generator_rating*co2_scrubber_rating
print("oxygen_generator_rating", oxygen_generator_rating)
print("co2_scrubber_rating", co2_scrubber_rating)
print("life_support", life_support)

# oxygen_generator_rating = find_one_responding_record(oxygen_generator_rating, records)
# print(oxygen_generator_rating)
# oxygen_generator_rating = int(oxygen_generator_rating,2)
# print(oxygen_generator_rating)

# co2_scrubber_rating = find_one_responding_record(co2_scrubber_rating, records)
# print(co2_scrubber_rating)
# co2_scrubber_rating = int(co2_scrubber_rating,2)
# print(co2_scrubber_rating)



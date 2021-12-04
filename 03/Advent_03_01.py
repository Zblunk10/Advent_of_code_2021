from collections import defaultdict
from collections import Counter


with open("03/input.txt", "r") as f:
  file_content = f.read()
diagnostic_report = file_content.splitlines()

records_count = len(diagnostic_report)


occurrence = defaultdict(list)
for item in diagnostic_report:
  for i in range(len(item)):
    number = item[i]
    occurrence[i].append(int(item[i]))

gamma_rate = []
epsilon_rate = []
for position in occurrence:
  ratio = Counter(occurrence[position])
  if ratio[0] > ratio[1]:
    gamma_rate.append("0")
    epsilon_rate.append("1")
  else:
    gamma_rate.append("1")
    epsilon_rate.append("0")
print("bin gamma_rate", "".join(gamma_rate))
print("bin epsilon_rate", "".join(epsilon_rate))

gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate),2)
print("gamma_rate", gamma_rate)
print("epsilon_rate" ,epsilon_rate)

power_consumption = gamma_rate*epsilon_rate
print("power_consumption", power_consumption)


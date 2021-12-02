with open("01/input.txt", "r") as f:
  file_content = f.read()

numbers = [x for x in file_content.split()]

n = 1
for i in range(1,(len(numbers))):
  
  if numbers[i] > numbers[i-1]:
    n+=1


print(n)

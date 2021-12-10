with open("10/input.txt", "r") as f:
  file_content = f.read().split()




openList = ["[", "{", "(", "<"]
closeList = ["]", "}", ")", ">"]

# original copied from stackoverflow
def balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


def balance2(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return i
    if len(stack) == 0:
        return "Balanced"

results = []
for x in file_content:
  results.append(balance2(x))

results = [x for x in results if x is not None]
print(len(results))
sums=[]
for item in results:
  if item == "]":
    sums.append(57)
  elif item == ")":
    sums.append(3)
  elif item == "}":
    sums.append(1197)
  elif item == ">":
    sums.append(25137)
print(sum(sums))

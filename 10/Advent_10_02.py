with open("10/input.txt", "r") as f:
  file_content = f.read().split()




openList = ["[", "{", "(", "<"]
closeList = ["]", "}", ")", ">"]


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
                return None
    if len(stack) == 0:
        return None
    else:
      return myStr


def missing_to_balance(myStr):
    stack = []
    for i in myStr:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if (len(stack) > 0) and (openList[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return None
    if len(stack) == 0:
        return None
    else:
      return stack


def add_and_multiply(val, score):
  counting = (val*5)+score

  return counting


points = {"(": 1, "[": 2, "{": 3, "<": 4}
start_value = 0


def points_calculation(parenthesis_list):
    scores = []
    for par in parenthesis_list:

      scores.append(points[par])
    val = start_value
#    print(scores)
    for score in scores:
      val = add_and_multiply(val, score)
#      print(val)
    return val

unfinished = []
for x in file_content:

  unfinished.append(balance(x))

unfinished = [x for x in unfinished if x is not None]

completition_strings = []
for x in unfinished:
  completition_strings.append(missing_to_balance(x))


#list parentheses needs to be reversed to create a missing part
completition_values = []
for x in completition_strings:
  x.reverse()
  completition_values.append(points_calculation(x))

print(len(completition_values))
completition_values.sort()
print(completition_values)
print(completition_values[24])

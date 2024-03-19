from art import logo


#Add
def add(n1, n2):
  total = n1 + n2
  print(f"{n1} + {n2} = {total}")
  return total


#Subtract
def subtract(n1, n2):
  total = n1 - n2
  print(f"{n1} - {n2} = {total}")
  return total


#Multiply
def multiply(n1, n2):
  total = n1 * n2
  print(f"{n1} * {n2} = {total}")
  return total


#Divide
def divide(n1, n2):
  if n2 > 0:
    total = n1 / n2
    print(f"{n1} / {n2} = {total}")
    return total
  else:
    print("Can't divide by 0")


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print(logo)

total = 0
calculation_start = True

n1 = int(input("What's the first Number?: "))
for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation: ")
n2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(n1, n2)

while calculation_start:
  want_to_continue = input(
      f"Type 'y' to continue with {first_answer}, or type 'n' to start a new calculation: "
  )

  if want_to_continue == "y":
    n1 = total
    operation_symbol = input("Pick an operation: ")
    n2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, n2)
    calculation_start = True
  elif want_to_continue == 'n':
    calculation_start = False

print("System closed!")

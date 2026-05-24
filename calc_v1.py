print("Welcome to my first calculator app. Choose between the following, ADD SUBTRACT MULTIPLY DIVIDE")
#THis is the entry 

operation = (input("Enter your mathematical operation: "))
#This will tell us which operation the user wants to do

is_multiply = operation.strip().lower() == "multiply"
is_add = operation.strip().lower() == "add"
is_subtract = operation.strip().lower() == "subtract"
is_divide = operation.strip().lower() == "divide"




if is_multiply:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number"))

else:
    pass

if is_add:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number"))

else:
    pass

if is_subtract:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number"))

else:
    pass


if is_divide:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number"))

else:
    pass




if is_multiply:
   answer = number_one * number_two


else:
    pass

if is_add:
    answer = number_one + number_two


else:
    pass

if is_subtract:
  answer = number_one - number_two


else:
    pass


if is_divide:
    answer = number_one / number_two


else:
    pass



print(int(answer)) if answer.is_integer() else print(answer)
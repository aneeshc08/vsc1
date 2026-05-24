print("Welcome to my first calculator app. Choose between the following, ADD SUBTRACT MULTIPLY DIVIDE")
#THis is the entry 

operation = (input("Enter your mathematical operation: ")).strip().lower()
#This will tell us which operation the user wants to do

is_multiply = operation in ["multiply" , "multiplication"]
is_add = operation in ["add" , "addition"]
is_subtract = operation in ["minus" , "sub" , "subtraction"]
is_divide = operation in ["divide" , "division"]




if is_multiply or is_add or is_subtract:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))



elif is_divide:
    number_one = float(input("Enter the first number: "))
    number_two = float(input("Enter the second number: "))
    while number_two == 0:
        number_two = float(input("Enter new number for denominator: "))


    

else:
    print("Invalid Operation. ")
    exit()
        




if is_multiply:
   answer = number_one * number_two

elif is_add:
    answer = number_one + number_two


elif is_subtract:
  answer = number_one - number_two



elif is_divide:
    answer = number_one / number_two



print(int(answer)) if answer.is_integer() else print(answer)
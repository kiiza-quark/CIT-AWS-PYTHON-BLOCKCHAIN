ADD = 1
MULTIPLY = 2
SUBTRACT = 3
DIVIDE = 4

val1= int(input("Enter 1st number: "))
val2 = int(input("Enter 2nd number: "))
operator = int(input("Enter the operator to use:"
                    "Addition, enter 1"
                    "Multiplication, enter 2"
                    "Subtraction, enter 3\nDivision, enter 4\n"
                    ))

if operator == ADD:
    print(f"{val1} + {val2} =  {val1 + val2}")

elif operator == MULTIPLY:
    print(f"{val1} * {val2} =  {val1 * val2}")

elif operator == SUBTRACT:
    print(f"{val1} - {val2} =  {val1 - val2}")

elif operator == DIVIDE:
    print(f"{val1} / {val2} =  {val1 / val2}")

else:
    print("Please enter a correct operator!")
choice = input("Enter 'cf' to convert from celcius to fahrenheit\nEnter 'fc' to convert from fahrenheit to celcius\nEnter:  ")

temp = input("Enter the temperature to convert: ")
if choice == 'cf':
    f = eval(temp)*(9/5) + 32
    print(f'{temp} Celcius = {f} Fahrenheit')
elif choice == 'fc':
    c = (5/9)*(eval(temp)) - 32
    print(f'{temp} Fahrenheit = {c} Celcius')
else:
    print("Enter the correct response")

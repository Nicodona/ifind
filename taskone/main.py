print("welcome please enter weight to convert to either kilos or pounds")
print("__________________________________________________________\n")

choice = int(input('enter 1 to input weight in kilogram \nenter 2 to input weight in pounds \n'))
print("__________________________________________________________\n")

try:
    if(choice == 1):
        print(" please enter weight in kilos and have a result in pounds")
        weight = float(input("\n"))
        result = round((weight/0.454),2)
        print(f'your new weight is {result}, thanks')

    elif (choice == 2):
        print(" please enter weight in pound and have a result in kilos")
        weight = float(input("\n"))
        result = round((weight*0.454),2)
        print('the new value of your weight is',format(result))

except ValueError:
    print("hey we have an error")

#In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then 
#calculates and outputs the result as a floating-point value formatted to one decimal place. 
#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:


eq = input("Expression: ").split(" ")

try:

    x = eq[0]
    y = eq[1]
    z = eq[2]

    while True:

        if y == "+":
            sum = int(x) + int(z)
        elif y == "-":
            sum = int(x) - int(z)
        elif y == "*":
            sum = int(x) * int(z)
        elif y == "/":
            sum = int(x) / int(z)
        else:
            print("Wrong format")
            break
            
        print(f"{sum:.1f}")
        break
except IndexError:
    print("Wrong Format")



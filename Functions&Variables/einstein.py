#Implement a program in py that prompts the user for mass as an integer (in kilo) and then outputs the equiv number of joules as an int. assume that the user will input an int. 


#E = Mc 2 

x = input("Enter int: ")
c = 300000000
m = int(x)

e = (m * (c * c))
print(e)


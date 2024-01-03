#Implement a program that prompts the user for the answer to the question of life. Outputting Yes if the user inputs 42 or case insensitive forty-two or forty two.
#Else output no

question = input("What is the answer to the great question of life, the universe and everything? ").lower()

if question in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")

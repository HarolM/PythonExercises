# implement a program that prompts the user for a greeting. if the greeting starts with "hello" output $0. 
#if the greeting starts with an "h" but not hello, output $20
#otherwise, output #100. Ignore any leading whitespace in the users greeting and treat the users greeting case-insensitive

greet = input("Greeting: ").lower()

for i in range(len(greet)):
    if "hello" in greet:
        print("$0")
        break
    
    elif "h" in greet[0]:
        print("$20")
        break

    else:
        print("$100")
        break
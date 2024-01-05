#Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 and any :( to 🙁
#Implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 

def convert(string):

    output = string.replace(":)", "🙂").replace(":(", "🙁")
    return output

def main():
    text = input("Enter text here: ")

    print(convert(text))

main()
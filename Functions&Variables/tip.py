#write a program that calculates tips. takes a user input and strips the $ and returns how much tip should be left.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    tip = d.strip("$")
    return int(tip)


def percent_to_float(p):
    percent = dollars_to_float(p)
    p = int(percent) / 100
    return p


main()
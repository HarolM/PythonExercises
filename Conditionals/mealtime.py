#Implement a program that prompts user for a time and outputs whether it is breakfast time, lunch time, or dinner time. If it is not time for a meal don't oputput anything
# Assume input will be in 24 hour format 
#7 - 8 is breakfast | 12 - 13 is lunch | 18 - 19 is dinner . any time between 7 - 8 is still breakfast and so on
import sys

def main():
    hour = input("What time is it? ").split(":")
    try:
        if int(hour[0]) < 24:
            if int(hour[1]) < 60:
                x = hour[0]
            else:
                print("Incorrect time format, XX:XX")
                sys.exit()

        print(convert(x))
    except (IndexError, UnboundLocalError):
        print("Incorrect time format, XX:XX")


def convert(time):
    if time == "7":
        mealtime = "Breakfast Time"
        return mealtime
    elif time == "12":
        mealtime = "Lunch Time"
        return mealtime
    elif time == "18":
        mealtime = "Dinner Time"
        return mealtime
    else:
        sys.exit(1)


if __name__=="__main__":
    main()
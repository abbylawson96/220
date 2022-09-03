"""
Name: <Abby Lawson>
<hw1>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)



def shooting_percentage():
     total_shots = eval(input("Enter the players total shots: "))
     shots_made = eval(input("Enter number of shots made by the player: "))
     shooting_percentage = (shots_made / total_shots) * 100.0
     print("Shooting percentage =", shooting_percentage, "%")

def coffee():
     coffee_lbs = eval(input("How many pounds of coffee would you like? "))
     total = coffee_lbs * (10.50 + 0.86) + 1.50
     print("Your total is: =", total)


def kilometers_to_miles():
     kilometers = eval(input("How many kilometers did you travel? "))
     #conversion factor
     conv_fac = 0.621371
     miles = kilometers * conv_fac
     print("That's", miles, "miles!")


if __name__ == '__main__':
    name = input("Enter your name: ")
    print("Hello", name, "!")

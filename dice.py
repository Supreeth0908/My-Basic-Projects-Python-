import random
print("Check your luck\nGet number 6 on the dice to win the lottery")
x = "Roll"
while x == "Roll":
    number = random.randint(1,6)
    if number == 1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
        print("Try again honey")
    if number == 2:
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")
        print("Try again honey")
    if number == 3:
        print("---------")
        print("|   O   |")
        print("|   O   |")
        print("|   O   |")
        print("---------")
        print("Try again honey")
    if number == 4:
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
        print("Try again honey")
    if number == 5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
        print("Try again honey")
    if number == 6:
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")
        print("\tYeah!\t\nCongarats! You won the lottery")
    x = input("Press Roll to roll the dice\nPress No to stop rolling: ")

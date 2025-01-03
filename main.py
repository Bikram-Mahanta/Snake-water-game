import random

computer = random.choice([1, -1, 0])

youStr = input("Enter your number: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"You Choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It is a draw")

else:
    if(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 1 and you == 0):
        print("You Win")

    if(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("You Lose")

    if(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 0 and you == 1):
        print("You Lose")


'''
1 for stone
-1 for paper
0 for scissor
'''

import random

# Choices: 1 for Stone, -1 for Paper, 0 for Scissor
youDict = {"s": 1, "p": -1, "c": 0}
reverseDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

# Get the computer's choice
computer = random.choice([1, -1, 0])

# Get the user's choice
youstr = input("Enter your choice (s for stone, p for paper, c for scissor): ").lower()
you = youDict[youstr]

# Display the choices
print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Determine the result
if computer == you:
    print("Draw")
elif (computer == 1 and you == 0) or (computer == -1 and you == 1) or (computer == 0 and you == -1):
    print("You Lose")
else:
    print("You Win")
 
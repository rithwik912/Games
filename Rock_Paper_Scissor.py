import random

choices = ["rock","paper","scissor"]

user = input("Enter rock , paper or scissor: ")

computer = random.choice(choices)

print("User Choice: ", user)
print("Computer Choice: ", computer)

if(user==computer):
    print("It is a tie!")
elif((user=="rock" and  computer=="scissor") or 
     (user=="paper" and  computer=="rock") or 
     (user=="scissor" and  computer=="paper")):
    print("You Win!")
else:
    print("Computer Win!")
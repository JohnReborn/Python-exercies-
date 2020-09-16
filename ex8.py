# Exercise 8
# Make a two player Rock, Paper, Scissors game
import random

print("Rock, Paper,Scissors")
loop = True
move = ["rock", "paper", "scissors"]

while loop:
    bot = random.choice(move)
    p1 = input("What do you choose\n")
    p1 = p1.lower()
    
    if p1 == bot:
        print("Tie")
        if input("Do you want to continue\n") == "yes":
            continue
        else:
            print("Game over")
            break
    elif (p1 == "rock" and bot == "scissors") or (p1 == "paper" and bot == "rock") or (p1 == "scissors" and bot == "paper"):
        print("Player 1 wins")
        if input("Do you want to continue\n") == "yes":
            continue
        else:
            print("Game over")
            break
        
    elif (p1 == "rock" and bot =="paper") or (p1 =="scissors" and bot == "rock") or (p1 =="paper" and bot =="scissors"):
        print("Player 2 Lost")
        if input("Do you want to continue\n") == "yes":
            continue
        else:
            print("Game over")
            break
    else:
        print("Try again, invalid entry")
    

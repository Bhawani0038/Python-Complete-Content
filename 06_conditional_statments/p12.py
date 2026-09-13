# Rock Paper Scissor Game
import random
user_choice = input("enter user choice (rock , paper or scissor)").strip().lower()
computer_choice = random.choice(["rock", "paper", "scissor"]) # com choice choosen randomly

if user_choice == computer_choice:
    print("tie")

elif user_choice == "rock" and computer_choice == "scissor":
    print("user won")

elif user_choice == "paper" and computer_choice == "rock":
    print("user won")

elif user_choice == "scissor" and computer_choice == "paper":
    print("user won")

else:
    print("com won")
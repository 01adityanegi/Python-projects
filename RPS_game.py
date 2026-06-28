import random

def get_choice():
    player_choice =input("Enter you choice (rock, paper, scissors): ")
    options= ["rock" , "paper" , "scissor"]
    computer_choice = random.choice(options)
    choices = {"Player" : player_choice , "computer" : computer_choice}
    return choices

def check_choice(player , computer):
    print(f"You chose : {player} , Computer chose : {computer}")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
            
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
            
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
choices= get_choice()
result= check_choice(choices["Player"],choices["computer"])
print(result)
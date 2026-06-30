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
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    messages = {
        ("rock", "scissors"): "Rock smashes scissors!",
        ("paper", "rock"): "Paper covers rock!",
        ("scissors", "paper"): "Scissors cut paper!"
    }

    if wins[player] == computer:
        return f"{messages[(player, computer)]} You win!"
    else:
        return f"{messages[(computer, player)]} You lose."
choices= get_choice()
result= check_choice(choices["Player"],choices["computer"])
print(result)

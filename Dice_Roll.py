import random 
def roll_dice(side = 6):
      return random.randint (1, sides)
rounds = int (input("How many round ? "))
target = int(input("Target score to reach: "))
total = 0 
history = []
round_num = 0
while total < target and round_num < rounds:
      roll = roll_dice
      total += roll

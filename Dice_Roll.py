import random 
def roll_dice(side = 6):
      return random.randint (1, sides)
rounds = int (input("How many round ? "))
target = int(input("Target score to reach: "))
total = 0 
history = []
round_num = 0
while total < target and round_num < rounds:
      roll = roll_dice()
      total += roll
      round_num += 1
      history.append(roll)
      print(f"Round {round_num }: rolled {roll} , total = {total}")
if total >= target:
      print(f"\nYou reached {total} in {round_num} rounds!")
else:
      print(f"\nOut of Rounds! Final Score : {total}")
print(f"Rolls :{history}")

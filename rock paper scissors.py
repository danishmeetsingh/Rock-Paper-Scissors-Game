import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input = input("What do you choose?0 for Rock, 1 for paper, 2 for Scissors ")
if user_input == "0":
  print(rock)
elif user_input == "1":
  print(paper)
elif user_input == "2":
  print(scissors)
print("Your Choice")
computer_choice = [rock,paper,scissors]
comp_output = random.choice(computer_choice)
print(comp_output)
print("Computer's Choice")

if user_input == "0" and comp_output == scissors or user_input == "1" and comp_output == rock or user_input == "2" and comp_output == paper:
  print("Congratulations, You won.")
elif user_input == "0" and comp_output == rock or user_input == "1" and comp_output == paper or user_input == "2" and comp_output == scissors:
  print("Match Drawn")
else:
  print("Computer Won")
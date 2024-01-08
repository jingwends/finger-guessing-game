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

#Let users pick what they want to put
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

if user_input==0:
  print(rock)
  user_graph=rock 
elif user_input==1:
  print(paper)
  user_graph=paper
elif user_input==2:
  print(scissors)
  user_graph=scissors



#Let coumputer chooce what it is going to have
import random 
choice=[rock,paper,scissors]
for i in range(1):
  computer=(random.choice(choice))
  print(computer)

#Run the game
if user_graph==computer:
  print("It's a draw")
elif user_graph==rock and computer==paper:
  print("Computer wins!")
elif user_graph==rock and computer==scissors:
  print("You win!")
elif user_graph==scissors and computer==paper:
  print("You win!")  
elif user_graph==scissors and computer==rock:
  print("Computer wins!")  
elif user_graph==paper and computer==scissors:
  print("Computer wins!")  
elif user_graph==paper and computer==rock:
  print("You win!")  

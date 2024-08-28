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
list_of_hand = [rock,paper,scissors]

# print(random.choice(list_of_hand))
computer_choice = random.randint(0,3)

your_choice = int(input("What do you choose? Type 0 for Rock,"
                        " 1 for paper or 2 for Scissors \n"))
print(list_of_hand[your_choice])
print(f"Computer Choice :{list_of_hand[computer_choice]}")

if your_choice >=3 or your_choice < 0 :
    print("It's invalid input , please provide valid input")
elif your_choice == 0 and computer_choice == 1:
    print("You Loose")
elif your_choice == 1 and computer_choice == 2:
    print("You Loose")
elif your_choice == 2 and computer_choice == 0 :
    print("You Loose")
elif your_choice == computer_choice:
    print("It's a Draw")
elif your_choice == 0 and computer_choice == 2 :
    print("You win")
elif your_choice == 1 and computer_choice == 0 :
    print("You win")

elif your_choice ==2 and computer_choice == 1:
    print("you win")

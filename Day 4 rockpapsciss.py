import random
n=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("You Chose")
if n==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

     ''')
elif n==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


          ''')
elif n==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          ''')
print("Computer chose")
p=random.randint(0,3)
if p==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

     ''')
elif p==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


          ''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          ''')
if n==0 and p==0:
    print("Draw")
elif n==0 and p==1:
    print("You Lose")
elif n==0 and p==2:
    print("You win")
elif n==1 and p==1:
    print("Draw")
elif n==1 and p==2:
    print("You Lose")
elif n==1 and p==0:
    print("You win")
elif n==2 and p==2:
    print("Draw")
elif n==2 and p==0:
    print("You Lose")
elif n==2 and p==1:
    print("You win")
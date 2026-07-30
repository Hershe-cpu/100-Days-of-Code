import random
from blackjack import num
print(num)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")
correct_number=(random.randint(1,100))
#print(correct_number)

def comparison(user_number,actual_number):
    if user_number < actual_number:
            print("Too low")
            
    elif user_number>actual_number:
            print("Too high")
    elif user_number==actual_number:
            print(f"You got it! The answer was {actual_number}")
            

diff=input("Choose a difficulty. Type 'easy' or 'hard': ")
guess_number=0
i=0
if diff.lower()=="hard":
    while i<=4 and guess_number!=correct_number:
        print(f"You have {5-i} attempts remaining to guess the number.")
        guess_number=int(input("Make a guess: "))
        comparison(guess_number,correct_number)
        if guess_number==correct_number or i==4:
            break
        print("Guess again")
        i+=1
    if i==4 and guess_number!=correct_number:
        print(f"Attempts finished. The correct number was {correct_number}")
elif diff.lower()=="easy":
    while i<=9 and guess_number!=correct_number:
        print(f"You have {10-i} attempts remaining to guess the number.")
        guess_number=int(input("Make a guess: "))
        comparison(guess_number,correct_number)
        if guess_number==correct_number or i==9:
            break
        print("Guess again")
        i+=1
    if i==9 and guess_number!=correct_number:    
        print(f"Attempts finished. The correct number was {correct_number}")




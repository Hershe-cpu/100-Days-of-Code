from blackjack import higher
from blackjack import vs
from record import data
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def stat():
    d=random.choice(data)
    return d


def assign(p):
    px= f"{p['name']}, a {p['description']}, from {p['country']}."
    return px


game_on = input("Type 'run' to play the game. ")
if game_on != "run":
    print("Game Exited.")

while game_on=="run":
    clear()
    dictA=stat()
    dictB=stat()
    score=0
    print(higher)
    still_guessing=True
    while still_guessing:

        if score>0:
            dictA=dictB
            dictB=stat()
            while dictA == dictB:
                dictB = stat()
        
        statementA = assign(dictA)
        
        statementB = assign(dictB)
        print(f"Compare A : {statementA}")
        print(vs)
        print(f"Against B : {statementB}")


        if dictA['follower_count']>dictB['follower_count']:
            correct_ans='A'
        else:
            correct_ans='B'

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess==correct_ans:
            clear()
            score+=1
            print(f"You're right! Current score: {score}")
        else:
            clear()
            still_guessing=False

        
    print(f"Sorry that's wrong. Final score. {score}")
    play_again = input("Want to Play Again? (y/n): ").lower()
        
    if play_again=='y':
        continue
    
    else:
        clear()
        print("Game Exited Successfully")
        break
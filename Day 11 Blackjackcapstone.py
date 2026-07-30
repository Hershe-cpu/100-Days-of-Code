import random 
from blackjack import logos
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_categories for card in cards_list]

random.shuffle(deck)



def scores(cardsh):
    score=0
    for card in cardsh:
        if card[0] in ['Jack', 'Queen', 'King']:
            score +=10
            
        elif card[0] in ['Ace']:
            if score+11>21:
                score+=1
            else:
                score +=11
            
        else:
            score +=int(card[0])
    return  score

# def computer_scores():
#     computer_score=0
#     for card in computer_cards:
#         if card[0] in ['Jack', 'Queen', 'King']:
#             computer_score +=10
            
#         elif card[0] in ['Ace']:
#             if computer_score+11>21:
#                 computer_score+=1
#             else:
#                 computer_score +=11
            
#         else:
#             computer_score +=int(card[0])
#     return computer_score

q=input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ")

if q=="y":
    game_start=True
    
    while game_start is True:
        print(logos)
        player_cards=[deck.pop(),deck.pop()]
        computer_cards=[deck.pop(),deck.pop()]
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        yn=input(f"Type 'y' to get another card, type 'n' to pass: ")
        if yn=="y":
            while yn=="y":
                player_cards.append(deck.pop())
                print(f"Your cards: {player_cards}")
                yn=input(f"Type 'y' to get another card, type 'n' to pass: ")

        score_of_computer=scores(computer_cards)
        while score_of_computer<17:
            computer_cards.append(deck.pop())
            score_of_computer=scores(computer_cards)

        print(f"Your final cards: {player_cards}")
        print(f"Computer's cards: {computer_cards}")

        score_of_player=scores(player_cards)
    

        if score_of_player>21:
            print("You busted! Dealer wins.")
        elif score_of_computer > 21 or (score_of_player <= 21 and score_of_player > score_of_computer):
            print("Player wins!")
        elif score_of_player == score_of_computer:
            print("It's a tie!")
        else:
            print("Computer Wins")
        
        q=input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ")
        if q=="n":
            game_start=False
        else:
            clear()
else:   
    print("OK")















































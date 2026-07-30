logo='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\

'''


# import random
# # Initialize deck of cards
# card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# deck = [(card, category) for category in card_categories for card in cards_list]
# # Function to assign card values
# def card_value(card):
#    if card[0] in ['Jack', 'Queen', 'King']:
#        return 10
#    elif card[0] == 'Ace':
#        return 11
#    else:
#        return int(card[0])
# # Shuffle the deck and deal initial cards
# random.shuffle(deck)
# player_cards = [deck.pop(), deck.pop()]
# dealer_cards = [deck.pop(), deck.pop()]
# # Game logic
# while True:
#    player_score = sum(card_value(card) for card in player_cards)
#    dealer_score = sum(card_value(card) for card in dealer_cards)
#    print(f"Player's Cards: {player_cards}, Score: {player_score}")
#    print(f"Dealer's Visible Card: {dealer_cards[0]}")
#    # Player's turn
#    choice = input("Do you want to [hit] or [stand]? ").lower()
#    if choice == "hit":
#        player_cards.append(deck.pop())
#        player_score = sum(card_value(card) for card in player_cards)
#        if player_score > 21:
#            print(f"Player's Cards: {player_cards}, Score: {player_score}")
#            print("You busted! Dealer wins.")
#            break
#    elif choice == "stand":
#        break
#    else:
#        print("Invalid choice. Please choose [hit] or [stand].")
# # Dealer's turn
# while dealer_score < 17:
#    dealer_cards.append(deck.pop())
#    dealer_score = sum(card_value(card) for card in dealer_cards)
# print(f"Dealer's Cards: {dealer_cards}, Score: {dealer_score}")
# # Determine the winner
# if dealer_score > 21 or (player_score <= 21 and player_score > dealer_score):
#    print("Player wins!")
# elif player_score == dealer_score:
#    print("It's a tie!")
# else:
#    print("Dealer wins!")
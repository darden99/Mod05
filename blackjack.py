# README
# This is my black jack table code, there are 4 decks being used, it is
# probaly busted in some way, I will try to fix it. Default balance is set to 500.
# Max bet is 500, Min is 25, side bets and insurance added later date.
# Recomended 4 players, otherwise gets somewhat crowded, wait for text to show up,
# there is a set delay time for some info to be displayed.
# If any Issues or recomendation, let me know somehow.
#
#   Hand      Payout
# Blackjack     3:2 (1.5x)
# Regular       1:1 (1x)
#
# Notes
# maybe add insurance or side bets
# add option to double down or split bets
# Add some custom stuff if dealt blackajck
# Possibly add visuals somehow

import random
import time

# set variables needed
LIST_CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
LIST_SUITS = ['♤', '♡', '♧', '♢']

def card_machine(cards_dealing):
    # Card machine will take all possible cards and suits, check if it has been dealt or not a
    # card that has not been dealt yet, list of cards has been set for 2 decks as of now 

    all_cards = []

    while len(all_cards) < cards_dealing:
        current_card = random.choice(LIST_CARDS) + random.choice(LIST_SUITS)
        all_cards.append(current_card)

    return all_cards

def calculate_total(hand):
    # Calculate total, it will take the cards that are strings, then change them to the correct
    # numerical value, it will acount for ace being 1 or 11 if needed

    card_value = 0
    num_aces = 0

    for card in hand:
        rank = card[:-1]  # Extract the rank of the card (excluding the suit)
        if rank in ['J', 'Q', 'K']:
            card_value += 10
        elif rank == 'A':
            num_aces += 1
            card_value += 11
        else:
            card_value += int(rank)

    # Adjust the value for Aces if necessary
    while card_value > 21 and num_aces > 0:
        card_value -= 10
        num_aces -= 1
    
    return card_value
    pass

def display_hands(players_hands, dealer_hand, player_totals):
    # Display hands will take the amount of player, generate hands for them, then diplay them.
    # It also generates the dealers hand and diplays one card

    players = len(players_hands)
    print('~'*30)
    time.sleep(1)
    print('| Initial Hand(s)')

    #Display the dealer hand
    print(f'| Dealers hand: {dealer_hand[0]} , hidden')

    # Display player hand(s) and total(s)
    for i in range(0,players):
        print(f'| Player {i+1} hand: {players_hands[i][0]}, {players_hands[i][1]}')
    for i in range(0,players):
        print(f'| Player {i+1} total: {player_totals[i]}')
    print('~'*30)
    time.sleep(1)

    pass

def player_turn(player_hand,player):
    # Player turn will ask each player if they want to hit or stand

    while True:
        user_input = input(f'| Player {player+1} do you want to Hit (H) or Stand (S)? ')
        if user_input[0].lower() == 'h':
            return True  # Player wants to hit, continue the turn
        elif user_input[0].lower() == 's':
            return False  # Player wants to stand, end the turn
        else:
            print("Invalid input. Please enter 'H' for Hit or 'S' for Stand.")

    pass

def dealer_turn(dealer_hand):
    # Dealer turn will go though and hit under 17 and display the cards pulled

    while calculate_total(dealer_hand) < 17:
        new_card = card_machine(1)[0]
        dealer_hand.append(new_card)
        print(f'| Dealer draws: {new_card}')

    dealer_total = calculate_total(dealer_hand)

    # Display the dealer's hand2
    print('| Dealer hand:', end=' ')
    for card in dealer_hand:
        print(card, end=' ')

    print(f'\n| Dealer total: {dealer_total}.')
    print('~' * 30)
    time.sleep(1)

    return dealer_total


def end_of_round(player_totals, dealer_total,players_hands):
    # Display outcomes of game based on betting on or off

        for i in range(len(player_totals)):
            if player_totals[i] > 21 or (dealer_total <= 21 and player_totals[i] < dealer_total):
                print(f"| Player {i+1} loses.")

            elif player_totals[i] == dealer_total:
                print(f"| Player {i+1} pushes.")

            elif player_totals[i] == 21 and len(players_hands[i]) == 2:  # Blackjack
                print(f"| Player {i+1} has a Blackjack!")

            else:
                print(f"| Player {i+1} wins.")
    
def main():

    # Inro message and basic info for game to start
    print('~' * 30)
    print("| Welcome to Blackjack!")
    num_players = int(input("| Enter the number of players: "))

    # Initialize player balances
    starting_balance = 500  # Set your desired initial balance
    balances = [starting_balance] * num_players
    
    # Starts the game
    while True:

        # Deal hands for each player and dealer then display
        dealer_hand = card_machine(2)
        players_hands = [card_machine(2) for _ in range(num_players)]
        player_totals = [calculate_total(hand) for hand in players_hands]
        display_hands(players_hands, dealer_hand, player_totals)
        
        # Go though each player and hit or stand
        for i in range(num_players):
            player_hand = players_hands[i] # Currnet player hand

            # Run though the player turn function to ask if hit or stand
            while player_turn(player_hand,i):
                new_card = card_machine(1)[0]
                player_hand.append(new_card) # add new card
                print(f'| You draw: {new_card}')
                player_totals[i] = calculate_total(player_hand)
                print(f'| Player {i+1} total: {player_totals[i]}')

            #Find out if bust or not for current player
                if player_totals[i] > 21:
                    print(f"| Player {i + 1} Bust.")
                    break

            print('~' * 30)
            time.sleep(1)
        
        
        # Run the dealer turn function to hit or stand for the dealer hand
        dealer_total = dealer_turn(dealer_hand)

        for i in range(0,num_players):
            print(f'| Player {i+1} total: {player_totals[i]}')  
        print('~' * 30)
        time.sleep(1)
        
        
        # End of round

        end_of_round(player_totals, dealer_total, players_hands)

        print('~' * 30)
        time.sleep(1)

        play_again = input("| Do you want to play again? (yes/no): ")
        time.sleep(1)
        if play_again[0].lower() != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

import random


def deal_card():

    cards = [11, 2,  10]
    ncard = random.choice(cards)
    return ncard

start_game = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

dealer_cards = []
player_cards = []

if start_game == 'y':

#first cards code
    for n in range(2):
        player_cards.append(deal_card())
    dealer_cards.append(deal_card())

    # we define the score of the player and the dealer. We also print
    # in the terminal the  cards and the score in each side
    player_score = 0
    dealer_score = 0
    for card in player_cards:
        player_score += card
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    # If the player have a blckjack they automatically win, so let's
    # code a proper response to that.
    keep_hitting = True

    if player_score == 21:
        print("BlackJack! You Win!")
        keep_hitting = False

    # In the cases that the player doesn't have a BlackJack



    while keep_hitting:
        choice = input("Do you wanna hit 'h' or stand 's' ")
        if choice == 'h':
            player_cards.append(deal_card())
            player_score = 0
            for card in player_cards:
                player_score += card
            if 11 in player_cards and player_score > 21:
                player_cards.remove(11)
                player_cards.append(1)
                player_score = 0
                for card in player_cards:
                    player_score += card


            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")
        if player_score > 21:
            print(r"""//////////////////////////////////////////////////////////""")
            print(f"Your final cards: {player_cards}, current score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")
            print("You went over. You lose")
            break
        elif choice == 's':

            while dealer_score < 17:

                dealer_cards.append(deal_card())
                dealer_score = 0
                for card in dealer_cards:
                    dealer_score += card
                print(f"Dealer cards: {dealer_cards}, current score: {dealer_score}")
                if dealer_score < 17:
                    print("Dealer hits")
            print(f"Your final cards: {player_cards}, final score: {player_score}")
            print(f"Dealer's final cards: {dealer_cards}, final score: {dealer_score}")
            if dealer_score > player_score:
                print("You Lose :/")
                break
            elif dealer_score < player_score:
                print("You Win! :D")
                break
            elif dealer_score == player_score:
                print("Tie 0_0")
                break


        else:
            pass
else:
    pass
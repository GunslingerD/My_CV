import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_game = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

dealer_cards = []
player_cards = []

if start_game == 'y':

#first cards code

    dealer_cards.append(cards[random.randint(0, len(cards)-1)])
    player_cards.append(cards[random.randint(0, len(cards)-1)])
    player_cards.append(cards[random.randint(0, len(cards)-1)])
    player_score = 0
    dealer_score = 0
    for card in player_cards:
        player_score += card
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    keep_hitting = True

    while keep_hitting:
        choice = input("Do you wanna hit 'h' or stand 's' ")
        if choice == 'h':
            player_cards.append(cards[random.randint(0, len(cards) - 1)])
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

                dealer_cards.append(cards[random.randint(0, len(cards) - 1)])
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
import os
import cards_util_module as utils

print( utils.blackjack_title )

while True:
    play_choice = input("Do you want to play a game of blackjack? Type 'y' to Play, or 'n' to quit:  " ).lower()
    if play_choice != 'y':
        break

    user_cards = [utils.get_random_card() for i in range(2)]
    computer_cards = [utils.get_random_card() for i in range(2)]

    print(f"Your cards:  {user_cards}")
    print(f"Computer's first card:  {computer_cards[0]}")

    user_move = input("Type 'y' to GET ANOTHER CARD, or type 'n' to PASS:  ").lower()
    if user_move not in ('y', 'n'):
        print("Invalid Move!", end="\n\n\n")
        continue

    if user_move == 'y':
        received_card = utils.get_random_card()
        user_cards.append( received_card )

        print(f"You got: {received_card}")
    
    print(f"Your final hand:  {user_cards}")
    print(f"Computer's final hand:  {computer_cards}")

    user_sum = utils.get_total_value( user_cards )
    computer_sum = utils.get_total_value( computer_cards )

    if user_sum > 21:
        # After first move, when user's total exceeds 21.
        utils.declare_bust(whose_bust="user")
    elif computer_sum <= 17:
        # After first move, when user's total is less than 21, and computer's total is less than 18
        while computer_sum <= 17:
            print("Computer total less than 18, so computer gets a card.")
            received_card = utils.get_random_card()
            computer_cards.append( received_card )

            print(f"Computer got: {received_card}")
            computer_sum = utils.get_total_value( computer_cards )

            print(f"Your final hand:  {user_cards}")
            print(f"Computer's final hand:  {computer_cards}")
        if computer_sum > 21:
            utils.declare_bust(whose_bust="computer")
        else:
            utils.declare_winner(user_sum=user_sum, computer_sum=computer_sum)

    else:
        # Case when User's total is less than equal to 21 and computer total is greater than 17 after User's first move.
        utils.declare_winner(user_sum=user_sum, computer_sum=computer_sum)
    
    print("______________________________________________________________________________________________")

    